"""
Heuristic content quality judge for AEO scoring.

Replaces an LLM judge with deterministic, measurable heuristics.
No model download, no API call — runs on github-hosted Ubuntu in milliseconds.

Scores ecommerce page content on four dimensions (0-10 each):
  - clarity            Flesch reading ease + sentence length variance
  - specificity        Entity density + numerical/spec density + brand mention count
  - schema_alignment   Visible-text-to-schema entity overlap (set similarity)
  - query_answerability  Direct-answer patterns + intro answer + FAQ density

Why heuristics over an LLM judge:
  - Deterministic and reproducible across runs
  - Sub-second per page (vs 30-60s on a CPU-only LLM)
  - No model download, no API key, no self-hosted runner needed
  - Uses signals already extracted in Phase 3 (schema) and Phase 4 (entities)

Usage:
    python llm_judge.py --text "Samsung 65-inch 4K TV..." --type product
    python llm_judge.py --file site-snapshots/thegoodguys.com.au/televisions.html --type category
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
    _BS4 = True
except ImportError:
    _BS4 = False


# ── Reading ease (simplified Flesch) ──────────────────────────────────────────

def _count_syllables(word: str) -> int:
    """Approximate syllable count for an English word."""
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)
    if not word:
        return 0
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)


def _flesch_reading_ease(text: str) -> float:
    """Higher = easier. 60-70 = plain English, <30 = academic."""
    sentences = re.split(r"[.!?]+\s", text)
    sentences = [s for s in sentences if s.strip()]
    words = re.findall(r"\b[a-zA-Z]+\b", text)
    if not sentences or not words:
        return 0.0
    syllables = sum(_count_syllables(w) for w in words)
    asl = len(words) / len(sentences)
    asw = syllables / len(words)
    return 206.835 - 1.015 * asl - 84.6 * asw


# ── Helpers ────────────────────────────────────────────────────────────────────

_NUM_PATTERN = re.compile(r"\b\d+(?:[.,]\d+)?(?:\s*(?:cm|mm|m|kg|g|inch|in|hz|w|kw|kwh|l|ml|gb|tb|mb|°c|°|%|\$|\bAUD|\bA\$|stars?|years?|months?|weeks?|days?))?\b", re.I)
_PRICE_PATTERN = re.compile(r"\$\s*\d{1,3}(?:[,]\d{3})*(?:\.\d{2})?\b|\bAUD\s*\d|\bA\$\s*\d", re.I)
_QUESTION_PATTERN = re.compile(r"\b(?:what|how|why|when|where|which|can|does|is|are|should|do|will)\b[^.?!]{8,80}\?", re.I)
_DEFINITION_PATTERN = re.compile(r"\b(?:is|are|means|refers to|consists of)\s+(?:a|an|the|one of)\b", re.I)


def _extract_entities(text: str) -> set[str]:
    """Heuristic entity extraction: capitalised multi-word phrases + known brand patterns."""
    # Multi-word capitalised phrases (e.g. "Samsung Galaxy", "Smart TV", "Bosch Series 6")
    phrases = re.findall(r"\b(?:[A-Z][a-z0-9]+(?:\s+[A-Z][a-z0-9]+){1,3})\b", text)
    # Single-word brand-like tokens (capitalised, often followed by model number)
    brand_tokens = re.findall(r"\b[A-Z][a-zA-Z]{2,15}(?=\s+(?:[A-Z0-9]|\d))", text)
    return set(phrases + brand_tokens)


def _extract_schema_entities(html: str) -> set[str]:
    """Pull entity names from JSON-LD blocks: Product.name, Brand.name, ItemList items, etc."""
    if not _BS4:
        return set()
    entities = set()
    soup = BeautifulSoup(html, "html.parser")
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "{}")
        except (json.JSONDecodeError, TypeError):
            continue
        for block in data if isinstance(data, list) else [data]:
            _walk_schema(block, entities)
    return entities


def _walk_schema(node, entities: set[str]):
    if isinstance(node, dict):
        for key in ("name", "headline", "brand", "itemListElement"):
            v = node.get(key)
            if isinstance(v, str) and len(v) > 2:
                entities.add(v.strip())
            elif isinstance(v, dict):
                _walk_schema(v, entities)
            elif isinstance(v, list):
                for item in v:
                    _walk_schema(item, entities)
        for v in node.values():
            if isinstance(v, (dict, list)):
                _walk_schema(v, entities)
    elif isinstance(node, list):
        for item in node:
            _walk_schema(item, entities)


# ── Scoring dimensions ────────────────────────────────────────────────────────

def _score_clarity(text: str) -> tuple[int, str]:
    """Reading ease + sentence variance. 0-10."""
    flesch = _flesch_reading_ease(text)
    # Map Flesch 30-80 → 0-10. Below 30 = academic, above 80 = too simple.
    if flesch >= 60:
        flesch_score = 10
    elif flesch >= 50:
        flesch_score = 8
    elif flesch >= 40:
        flesch_score = 6
    elif flesch >= 30:
        flesch_score = 4
    else:
        flesch_score = 2

    # Sentence length variance (penalise wall-of-text or all-fragments)
    sentences = [s for s in re.split(r"[.!?]+\s", text) if s.strip()]
    if len(sentences) < 3:
        return max(0, flesch_score - 4), f"Flesch {flesch:.0f}, only {len(sentences)} sentences"
    lengths = [len(s.split()) for s in sentences]
    avg = sum(lengths) / len(lengths)
    if avg > 30 or avg < 5:  # too long or too fragmented
        flesch_score = max(0, flesch_score - 2)

    return min(10, flesch_score), f"Flesch reading ease {flesch:.0f}, avg sentence {avg:.0f} words"


def _score_specificity(text: str, entities: set[str]) -> tuple[int, str]:
    """Entity density + numerical/spec density + brand-like tokens. 0-10."""
    word_count = len(text.split())
    if word_count < 50:
        return 0, f"Only {word_count} words — too thin to score"

    nums = len(_NUM_PATTERN.findall(text))
    prices = len(_PRICE_PATTERN.findall(text))
    entity_count = len(entities)

    # Densities per 1000 words
    num_density = nums / word_count * 1000
    entity_density = entity_count / word_count * 1000

    # Heuristic targets for retail content:
    #  - num_density: ~30-60 strong (lots of specs/measurements)
    #  - entity_density: ~20-40 strong
    num_score = min(5, round(num_density / 12))
    entity_score = min(5, round(entity_density / 8))
    base = num_score + entity_score

    # Bonus for prices visible in text (signals a real product/category page)
    if prices > 0:
        base = min(10, base + 1)

    return base, f"{nums} numbers, {entity_count} entities, {prices} prices in {word_count} words"


def _score_schema_alignment(text: str, schema_entities: set[str]) -> tuple[int, str]:
    """Overlap between schema-claimed entities and visible text. 0-10."""
    if not schema_entities:
        return 0, "No schema entities found — cannot align"

    visible_lower = text.lower()
    matched = sum(1 for e in schema_entities if e.lower() in visible_lower and len(e) > 2)
    coverage = matched / len(schema_entities)

    score = round(coverage * 10)
    return score, f"{matched}/{len(schema_entities)} schema entities visible in text"


def _score_query_answerability(text: str) -> tuple[int, str]:
    """Question-answer patterns + intro definition + FAQ-like blocks. 0-10."""
    word_count = len(text.split())
    if word_count < 50:
        return 0, "Content too thin for question-answering"

    questions = len(_QUESTION_PATTERN.findall(text))
    definitions = len(_DEFINITION_PATTERN.findall(text))

    # Intro answer: first 300 chars contain a definition pattern
    intro = text[:400]
    has_intro_def = bool(_DEFINITION_PATTERN.search(intro))

    # Q&A density per 1000 words
    qa_density = (questions + definitions) / word_count * 1000

    score = 0
    if has_intro_def:
        score += 4  # strong signal — intro defines/answers the topic
    score += min(4, round(qa_density / 1.5))
    if questions >= 3:  # FAQ-style block
        score += 2

    return min(10, score), f"{questions} questions, {definitions} definitions, intro_answer={has_intro_def}"


# ── Main scoring entry point ──────────────────────────────────────────────────

def judge_content(text: str, page_type: str = "page", html: str = "", **_) -> dict:
    """
    Score content using deterministic heuristics. Always 'available'.

    Args:
        text: visible text content (extracted from HTML body)
        page_type: product/category/guide/home — used for context only
        html: optional raw HTML (enables schema_alignment scoring)
    """
    if not text or len(text) < 30:
        return {
            "available": True,
            "method": "heuristic",
            "clarity": 0, "specificity": 0,
            "schema_alignment": 0, "query_answerability": 0,
            "llm_overall": 0,
            "reasoning": "Content too short to evaluate",
        }

    entities = _extract_entities(text)
    schema_entities = _extract_schema_entities(html) if html else set()

    clarity, c_note   = _score_clarity(text)
    specif, s_note    = _score_specificity(text, entities)
    schema, sa_note   = _score_schema_alignment(text, schema_entities)
    query,  qa_note   = _score_query_answerability(text)

    overall = round((clarity + specif + schema + query) / 4, 1)

    return {
        "available": True,
        "method": "heuristic",
        "page_type": page_type,
        "clarity": clarity,
        "specificity": specif,
        "schema_alignment": schema,
        "query_answerability": query,
        "llm_overall": overall,
        "reasoning": f"clarity: {c_note}; specificity: {s_note}; schema: {sa_note}; query: {qa_note}",
    }


def judge_html_file(path: str, page_type: str = "page") -> dict:
    if not _BS4:
        return {"available": False, "reason": "beautifulsoup4 not installed"}
    html = Path(path).read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    # Strip navigation/footer/script noise before scoring
    for tag in soup.find_all(["nav", "header", "footer", "script", "style", "noscript"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body
    text = (main or soup).get_text(separator=" ", strip=True)
    return judge_content(text, page_type, html=html)


# ── Back-compat shim for existing callers ─────────────────────────────────────

def _is_ollama_available() -> bool:
    """Always returns True — heuristic judge has no external dep. Kept for back-compat."""
    return True


def main():
    parser = argparse.ArgumentParser(description="Heuristic content quality judge for AEO scoring")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Content text to score")
    group.add_argument("--file", help="HTML file to score")
    parser.add_argument("--type", default="page", help="Page type (product/category/guide/home)")
    args = parser.parse_args()

    if args.file:
        result = judge_html_file(args.file, args.type)
    else:
        result = judge_content(args.text, args.type)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
