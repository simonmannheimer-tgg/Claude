"""
Phase 4 — Content Intelligence AEO Audit

Content-level checks for AI discoverability, entity prominence, and LLM retrieval quality.
Operates entirely on HTML snapshots — no network required after Phase 2 crawl.

Checks:
  1. boilerplate_ratio      — nav/header/footer words vs substantive main content
  2. content_chunking       — paragraph/section length distribution for LLM retrieval
  3. entity_signals         — brand/category/spec entity frequency, placement, density
  4. knowledge_graph        — sameAs links, authority references, external entity signals
  5. semantic_structure     — Q&A, definitions, comparisons, how-to patterns, lexical richness
  6. anchor_quality         — internal link anchor text specificity vs generic terms
  7. content_similarity     — semantic embedding similarity against ideal AI-citable passages

Similarity implementation:
  Check 7 uses sentence-transformers (all-MiniLM-L6-v2 from HuggingFace) to embed both
  page content chunks and a reference corpus of ~20 ideal ecommerce AI-citation passages,
  then scores via cosine similarity. Falls back to TF-IDF bag-of-words if the model
  is not installed (pip install sentence-transformers).

  TODO — upgrade options when API access is available:
    Option A (OpenAI):    text-embedding-3-small via OPENAI_API_KEY env var (best accuracy)
    Option B (Cohere):    embed-english-v3.0 via COHERE_API_KEY env var
    Option C (Anthropic): no embeddings API yet — use Claude to score passage quality instead

Usage:
    SNAPSHOT_DIR=site-snapshots/thegoodguys.com.au python run_content_aeo.py
    SNAPSHOT_DIR=site-snapshots/thegoodguys.com.au AEO_LABEL="TGG" python run_content_aeo.py
"""

import json
import math
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

# sentence-transformers for semantic similarity (Check 7).
# Falls back to TF-IDF cosine if not installed.
try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    _ST_MODEL: SentenceTransformer | None = None
    _ST_AVAILABLE = True
except ImportError:
    _ST_AVAILABLE = False

GRADE_EMOJI = {"A": "🟢", "B": "🟢", "C": "🟡", "D": "🟠", "F": "🔴"}

# ── Entity lexicons (TGG ecommerce context) ────────────────────────────────────

BRAND_ENTITIES = {
    "samsung", "lg", "sony", "hisense", "tcl", "panasonic", "philips",
    "beko", "bosch", "fisher & paykel", "haier", "westinghouse", "electrolux",
    "aeg", "miele", "dyson", "irobot", "shark", "bissell", "hoover",
    "apple", "microsoft", "dell", "lenovo", "hp", "asus", "acer",
    "ninja", "tefal", "breville", "sunbeam", "kenwood", "kitchenaid",
    "smeg", "liebherr", "neff", "siemens", "daikin", "mitsubishi", "fujitsu",
    "kelvinator", "toshiba", "sharp", "jvc", "grundig", "baumatic",
}

CATEGORY_ENTITIES = {
    "television", "tv", "air conditioner", "air con", "washing machine",
    "washer", "dryer", "refrigerator", "fridge", "freezer", "dishwasher",
    "microwave", "oven", "cooktop", "rangehood", "vacuum", "coffee machine",
    "espresso", "blender", "mixer", "toaster", "laptop", "tablet",
    "headphones", "earbuds", "speaker", "soundbar", "projector", "monitor",
    "robot vacuum", "steam mop", "pressure cooker", "air fryer",
    "split system", "portable air conditioner", "evaporative cooler",
    "heat pump", "ducted air conditioning", "reverse cycle",
}

SPEC_ENTITIES = {
    "4k", "8k", "uhd", "oled", "qled", "led", "mini led", "hdr",
    "dolby vision", "dolby atmos", "hdmi", "bluetooth", "wi-fi", "wifi",
    "inverter", "capacity", "litres", "watts", "energy star", "energy rating",
    "star rating", "front loader", "top loader", "spin speed", "rpm",
    "noise level", "cubic metre", "smart home", "alexa", "google home",
    "voice control", "app control", "5g", "intel", "amd", "ssd", "ram",
}

COMMERCE_ENTITIES = {
    "price", "deal", "discount", "save", "sale", "warranty", "guarantee",
    "delivery", "pickup", "afterpay", "zip pay", "interest free",
    "layby", "installation", "compare", "review", "clearance",
    "price match", "concierge", "best price",
}

ALL_ENTITIES = BRAND_ENTITIES | CATEGORY_ENTITIES | SPEC_ENTITIES | COMMERCE_ENTITIES

GENERIC_ANCHORS = {
    "click here", "here", "read more", "learn more", "find out more",
    "more", "more info", "more information", "see more", "view more",
    "see all", "view all", "shop now", "buy now", "get started",
    "contact us", "this", "link", "page", "website",
}

AUTHORITY_DOMAINS = {
    "wikipedia.org", "energy.gov.au", "choice.com.au", "productreview.com.au",
    "schema.org", "wikidata.org", "abs.gov.au", "accc.gov.au",
    "energyrating.gov.au", "google.com/shopping",
}


# ── Helpers ────────────────────────────────────────────────────────────────────

def grade(pct: int) -> str:
    if pct >= 90: return "A"
    if pct >= 75: return "B"
    if pct >= 60: return "C"
    if pct >= 40: return "D"
    return "F"


def parse_html(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")


def get_main_content(soup: BeautifulSoup) -> BeautifulSoup | None:
    return (
        soup.find("main")
        or soup.find("article")
        or soup.find(id=re.compile(r"content|main|body", re.I))
    )


# ── Similarity: reference corpus & embedding/TF-IDF cosine ────────────────────
#
# These passages represent the kind of content AI Answer Engines (Google AI Overviews,
# ChatGPT, Perplexity) preferentially cite. They are direct, factual, entity-rich,
# and structured as standalone answers — not marketing copy.
#
# Similarity is computed with sentence-transformers (all-MiniLM-L6-v2) when available,
# falling back to TF-IDF bag-of-words cosine otherwise.
# TODO: swap to OpenAI/Cohere embeddings API for higher accuracy — see module docstring.

REFERENCE_CORPUS = [
    # Buying guide — direct answer format
    "A 4K OLED television offers exceptional contrast by turning off individual pixels to produce true blacks. OLED is ideal for dark home theatre rooms and delivers the best picture quality currently available in consumer televisions.",
    "To choose the right air conditioner, measure the room size in cubic metres and match it to the unit's cooling capacity in kilowatts. A 2.5kW split system suits rooms up to 20 square metres, while larger living areas need 5-7kW.",
    "Front-load washing machines are more energy and water efficient than top-loaders and typically achieve better wash results at lower temperatures. Top-loaders are faster and gentler on clothes that require hand-wash care.",
    "An inverter air conditioner varies its compressor speed to maintain a set temperature, using up to 30% less energy than a fixed-speed unit. All reverse-cycle models can both heat and cool, making them suitable for Australian climates year-round.",
    "When choosing a refrigerator, allow 15-20cm clearance on all sides for ventilation. French door models offer the largest usable capacity for families, while bottom-mount designs put the main fridge compartment at eye level for easier access.",
    # Product comparison — spec-driven
    "The Samsung QN90D features a 65-inch Neo QLED panel with a 144Hz refresh rate and AMD FreeSync Premium Pro, making it one of the best gaming televisions available in 2024. Quantum Mini LEDs improve local dimming precision over standard QLED.",
    "LG's C-series OLED and Samsung's QN90 QLED target different buyers: OLED delivers perfect blacks and wider viewing angles, while QLED offers higher peak brightness for HDR content in bright rooms and a longer lifespan.",
    "Dyson V15 Detect uses a laser to reveal microscopic dust invisible to the naked eye and automatically adjusts suction power based on detected debris. Its HEPA filtration captures 99.97% of particles as small as 0.3 microns.",
    "Bosch Series 8 washing machines use ActiveOxygen technology to remove bacteria and allergens at 20°C, achieving a 60°C wash result with less energy. The i-DOS system automatically dispenses the exact amount of detergent required.",
    # How-to / educational
    "To set up a split-system air conditioner, the indoor unit must be installed on an interior wall with access to an exterior wall for the refrigerant pipe and drain hose. Minimum recommended installation height is 2.1 metres from the floor.",
    "To clean a dishwasher filter, remove the cylindrical filter from the base, rinse under warm running water, and use a soft brush to clear any debris. Clean the filter monthly to maintain washing performance and prevent odours.",
    "OLED burn-in occurs when static elements display for extended periods at high brightness. Modern OLED panels include pixel-shift and screen-saver features that significantly reduce this risk in normal home viewing conditions.",
    "Energy star ratings in Australia use a red-orange label with stars and annual electricity consumption in kWh. Each additional star represents approximately 10% lower energy use. A 5-star refrigerator uses roughly half the energy of a 2-star equivalent.",
    # FAQ-style direct answers
    "What is the difference between ducted and split-system air conditioning? Ducted air conditioning conditions the entire home through concealed ductwork from a central unit, while split systems heat or cool individual rooms with a visible wall unit. Ducted systems cost more to install but offer whole-home climate control.",
    "How long does a washing machine last? Most washing machines last 10-14 years with regular maintenance. Front-loaders tend to have longer lifespans than top-loaders but require door seal cleaning to prevent mould build-up.",
    "Can I run a portable air conditioner without a window? Portable air conditioners require a vent to exhaust hot air — typically through a window or sliding door using the included kit. Without venting, the unit recirculates hot air and provides no cooling.",
    # Commerce / trust signals
    "The Good Guys price match guarantee covers identical products sold by Australian retailers including online stores. Customers can claim the price match in-store by presenting proof of the lower price before or within 30 days of purchase.",
    "Interest-free finance options through Latitude allow customers to spread payments over 6, 12, or 24 months with no interest charges when minimum monthly payments are made. Standard Latitude fees and charges apply.",
    # Specification definitions
    "IP44 rating on a portable speaker means the device is protected against solid objects greater than 1mm and against water splashing from any direction. IP67 means dust-tight and waterproof when submerged up to 1 metre for 30 minutes.",
    "Refresh rate measures how many times per second a television updates its image, expressed in Hz. 60Hz is sufficient for standard viewing, while 120Hz or higher reduces motion blur for fast-paced gaming and sports content.",
]


# ── TF-IDF fallback (used when sentence-transformers not installed) ─────────────

def _tokenize(text: str) -> list[str]:
    return re.findall(r'\b[a-z]{3,}\b', text.lower())


def _tfidf_vector(tokens: list[str], idf: dict[str, float]) -> dict[str, float]:
    tf = Counter(tokens)
    total = sum(tf.values())
    return {w: (tf[w] / total) * idf.get(w, 1.0) for w in tf}


def _cosine_dict(va: dict[str, float], vb: dict[str, float]) -> float:
    common = set(va) & set(vb)
    num = sum(va[w] * vb[w] for w in common)
    denom = math.sqrt(sum(v**2 for v in va.values())) * math.sqrt(sum(v**2 for v in vb.values()))
    return num / denom if denom else 0.0


def _build_idf(corpus: list[str]) -> dict[str, float]:
    n = len(corpus)
    df: Counter = Counter()
    for doc in corpus:
        for w in set(_tokenize(doc)):
            df[w] += 1
    return {w: math.log((n + 1) / (c + 1)) + 1 for w, c in df.items()}


_REF_IDF = _build_idf(REFERENCE_CORPUS)
_REF_VECS_TFIDF = [_tfidf_vector(_tokenize(p), _REF_IDF) for p in REFERENCE_CORPUS]


def _tfidf_similarity(text: str) -> tuple[float, float, str]:
    tokens = _tokenize(text)
    if not tokens:
        return 0.0, 0.0, ""
    vec = _tfidf_vector(tokens, _REF_IDF)
    scored = sorted(
        [(_cosine_dict(vec, rv), REFERENCE_CORPUS[i]) for i, rv in enumerate(_REF_VECS_TFIDF)],
        key=lambda x: x[0], reverse=True,
    )
    return scored[0][0], sum(s for s, _ in scored[:3]) / 3, scored[0][1][:100]


# ── sentence-transformers implementation ───────────────────────────────────────

_REF_EMBEDDINGS = None  # lazy-initialised on first call


def _get_st_model() -> "SentenceTransformer":
    global _ST_MODEL
    if _ST_MODEL is None:
        # all-MiniLM-L6-v2: 80MB, fast, good semantic quality for English
        _ST_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return _ST_MODEL


def _st_similarity(text: str) -> tuple[float, float, str]:
    global _REF_EMBEDDINGS
    model = _get_st_model()
    if _REF_EMBEDDINGS is None:
        _REF_EMBEDDINGS = model.encode(REFERENCE_CORPUS, normalize_embeddings=True)
    vec = model.encode([text], normalize_embeddings=True)[0]
    sims = _REF_EMBEDDINGS @ vec  # cosine similarity (normalized dot product)
    top_idx = int(np.argmax(sims))
    top3_avg = float(np.mean(np.sort(sims)[-3:]))
    return float(sims[top_idx]), top3_avg, REFERENCE_CORPUS[top_idx][:100]


# ── Unified entry point ────────────────────────────────────────────────────────

def similarity_to_corpus(text: str) -> tuple[float, float, str]:
    """
    Returns (max_similarity, avg_top3_similarity, best_matching_reference_snippet).

    Uses sentence-transformers (semantic) when available, else TF-IDF (lexical).
    Sentence-transformers scores: strong ecommerce content ~0.60-0.80, marketing copy ~0.30-0.45.
    TF-IDF scores: strong content ~0.25-0.45, marketing copy <0.15 (different scale).
    """
    if _ST_AVAILABLE:
        return _st_similarity(text)
    return _tfidf_similarity(text)


def extract_entities(text: str) -> dict[str, int]:
    text_lower = text.lower()
    found = {}
    for entity in ALL_ENTITIES:
        count = len(re.findall(r'\b' + re.escape(entity) + r'\b', text_lower))
        if count > 0:
            found[entity] = count
    return found


# ── Check 1: Boilerplate Ratio ─────────────────────────────────────────────────

def check_boilerplate_ratio(snapshot_dir: Path) -> dict:
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        all_words = len(soup.get_text(" ", strip=True).split())
        if all_words < 50:
            continue

        boilerplate_words = sum(
            len(el.get_text(" ", strip=True).split())
            for el in soup.find_all(["nav", "header", "footer", "aside"])
        )
        boilerplate_ratio = boilerplate_words / all_words

        main = get_main_content(soup)
        main_words = len(main.get_text(" ", strip=True).split()) if main else 0
        main_ratio = main_words / all_words if all_words else 0

        page_max = 20
        if main_ratio >= 0.60 or boilerplate_ratio <= 0.25:
            page_score = 20
        elif main_ratio >= 0.40 or boilerplate_ratio <= 0.40:
            page_score = 12
        elif main_ratio >= 0.25:
            page_score = 6
        else:
            page_score = 0

        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "total_words": all_words,
            "main_words": main_words,
            "main_ratio_pct": round(main_ratio * 100),
            "boilerplate_ratio_pct": round(boilerplate_ratio * 100),
            "score": page_score,
            "maxScore": page_max,
            "issue": f"High boilerplate ({round(boilerplate_ratio*100)}%) — AI reads mostly nav/footer" if boilerplate_ratio > 0.40 else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have <40% boilerplate",
    }


# ── Check 2: Content Chunking ──────────────────────────────────────────────────

def check_content_chunking(snapshot_dir: Path) -> dict:
    """
    LLMs retrieve content in chunks. Ideal paragraph size for RAG is 50-400 words.
    Very long paragraphs (>500 words) exceed a single retrieval unit.
    Very short paragraphs (<20 words) are too fragmented to carry semantic meaning.
    """
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        paragraphs = [
            p.get_text(" ", strip=True)
            for p in soup.find_all("p")
            if len(p.get_text(" ", strip=True).split()) >= 15
        ]
        if not paragraphs:
            continue

        para_lengths = [len(p.split()) for p in paragraphs]
        avg_para = sum(para_lengths) / len(para_lengths)
        long_paras = sum(1 for l in para_lengths if l > 500)
        good_paras = sum(1 for l in para_lengths if 50 <= l <= 400)
        good_ratio = good_paras / len(para_lengths) if para_lengths else 0

        # Approximate token count (1 word ≈ 1.3 tokens)
        total_words = len(soup.get_text(" ", strip=True).split())
        approx_tokens = round(total_words * 1.3)

        page_max = 25
        if good_ratio >= 0.70:
            page_score = 25
        elif good_ratio >= 0.50:
            page_score = 15
        elif good_ratio >= 0.30:
            page_score = 8
        else:
            page_score = 0

        total_score += page_score
        max_score += page_max

        issue = None
        if long_paras > 2:
            issue = f"{long_paras} paragraphs >500 words — too large for single LLM retrieval chunk"
        elif good_ratio < 0.50:
            issue = f"Only {round(good_ratio*100)}% of paragraphs in the ideal 50-400 word range"

        results.append({
            "file": html_file.name,
            "paragraph_count": len(paragraphs),
            "avg_paragraph_words": round(avg_para),
            "good_chunk_pct": round(good_ratio * 100),
            "long_paragraphs": long_paras,
            "approx_total_tokens": approx_tokens,
            "score": page_score,
            "maxScore": page_max,
            "issue": issue,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have well-chunked content",
    }


# ── Check 3: Entity Signals ────────────────────────────────────────────────────

def check_entity_signals(snapshot_dir: Path) -> dict:
    """
    Entity density and placement indicate how well a page signals its topic to AI.
    AI models use entity frequency + position to determine page relevance for queries.
    Entities in headings and the first 200 words carry extra weight.
    """
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        full_text = soup.get_text(" ", strip=True)
        word_count = len(full_text.split())
        if word_count < 50:
            continue

        entities = extract_entities(full_text)
        entity_count = len(entities)
        total_mentions = sum(entities.values())
        entity_density = total_mentions / word_count

        heading_text = " ".join(h.get_text(" ", strip=True) for h in soup.find_all(["h1", "h2", "h3"]))
        heading_entities = extract_entities(heading_text)

        first_200 = " ".join(full_text.split()[:200])
        intro_entities = extract_entities(first_200)

        brand_count = sum(1 for e in entities if e in BRAND_ENTITIES)
        category_count = sum(1 for e in entities if e in CATEGORY_ENTITIES)
        spec_count = sum(1 for e in entities if e in SPEC_ENTITIES)

        page_max = 25
        score = 0
        if entity_count >= 10: score += 8
        elif entity_count >= 5: score += 5
        elif entity_count >= 2: score += 2
        if heading_entities: score += 7
        if intro_entities: score += 5
        if brand_count >= 3: score += 5
        elif brand_count >= 1: score += 3

        page_score = min(score, page_max)
        total_score += page_score
        max_score += page_max

        top_entities = sorted(entities.items(), key=lambda x: x[1], reverse=True)[:8]
        results.append({
            "file": html_file.name,
            "entity_count": entity_count,
            "total_mentions": total_mentions,
            "entity_density_pct": round(entity_density * 100, 1),
            "brand_entities": brand_count,
            "category_entities": category_count,
            "spec_entities": spec_count,
            "heading_entities": list(heading_entities.keys())[:5],
            "intro_entities": list(intro_entities.keys())[:5],
            "top_entities": [{"entity": e, "count": c} for e, c in top_entities],
            "score": page_score,
            "maxScore": page_max,
            "issue": "Low entity density — page may be too generic for AI topic matching" if entity_count < 5 else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have strong entity signals",
    }


# ── Check 4: Knowledge Graph Signals ──────────────────────────────────────────

def check_knowledge_graph(snapshot_dir: Path) -> dict:
    """
    sameAs in JSON-LD links brand/org to Wikipedia/Wikidata, increasing entity confidence.
    Authority links (energyrating.gov.au, Choice, Wikipedia) increase trust signals.
    Organization schema with address/phone confirms physical entity identity.
    """
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        signals = []
        missing = []

        # sameAs links in JSON-LD
        same_as_urls = []
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.get_text() or "")
                items = data if isinstance(data, list) else [data]
                for item in items:
                    for sub in [item] + item.get("@graph", []):
                        sa = sub.get("sameAs", [])
                        if isinstance(sa, str):
                            sa = [sa]
                        same_as_urls.extend(sa)
            except (json.JSONDecodeError, TypeError):
                pass

        if same_as_urls:
            signals.append(f"sameAs ({len(same_as_urls)} links)")
        else:
            missing.append("sameAs links in JSON-LD (connect brand to Wikipedia/Wikidata)")

        # External authority links
        authority_links = [
            a["href"] for a in soup.find_all("a", href=True)
            if any(d in a["href"] for d in AUTHORITY_DOMAINS)
        ]
        if authority_links:
            signals.append(f"authority links ({len(authority_links)})")
        else:
            missing.append("external authority links (energy ratings, Choice, Wikipedia)")

        # Organization schema with contact details
        has_org = False
        has_contact = False
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.get_text() or "")
                items = data if isinstance(data, list) else [data]
                for item in items:
                    for sub in [item] + item.get("@graph", []):
                        if sub.get("@type") in ("Organization", "LocalBusiness", "Store"):
                            has_org = True
                            if sub.get("address") or sub.get("telephone"):
                                has_contact = True
            except (json.JSONDecodeError, TypeError):
                pass

        if has_org:
            signals.append("Organization schema")
        if has_contact:
            signals.append("contact details in schema")
        if not has_org:
            missing.append("Organization schema with address/phone")

        page_max = 20
        page_score = min(len(signals) * 5, page_max)
        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "signals_found": signals,
            "signals_missing": missing[:3],
            "same_as_count": len(same_as_urls),
            "authority_link_count": len(authority_links),
            "score": page_score,
            "maxScore": page_max,
            "issue": "No knowledge graph signals — AI cannot confirm entity identity" if not signals else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have knowledge graph signals",
    }


# ── Check 5: Semantic Structure ────────────────────────────────────────────────

DEFINITION_RE = re.compile(r'\b(?:is a|is an|are|means|refers to|defined as|known as)\b', re.IGNORECASE)
COMPARISON_RE = re.compile(r'\b(?:vs\.?|versus|compared to|difference between|better than|unlike)\b', re.IGNORECASE)
HOW_TO_RE = re.compile(r'<h[234][^>]*>(?:how to|steps to|guide to|tips for|ways to)[^<]{3,60}</h[234]>', re.IGNORECASE)
QUESTION_HEAD_RE = re.compile(r'<h[2-4][^>]*>(?:what|why|how|when|which|can|do|does|is|are)[^<]{5,80}[?]?\s*</h[2-4]>', re.IGNORECASE)


def check_semantic_structure(snapshot_dir: Path) -> dict:
    """
    Semantic patterns increase AI citation probability. Google AI Overviews and ChatGPT
    preferentially extract pages with explicit definitions, comparisons, Q&A, and how-to
    content. Type-token ratio is a proxy for lexical richness / content uniqueness.
    """
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        raw_html = html_file.read_text(encoding="utf-8", errors="ignore")
        full_text = soup.get_text(" ", strip=True)
        if len(full_text.split()) < 50:
            continue

        patterns_found = []
        patterns_missing = []

        def_count = len(DEFINITION_RE.findall(full_text))
        if def_count >= 3:
            patterns_found.append(f"definitions ({def_count})")
        else:
            patterns_missing.append("definition sentences ('X is a...', 'X means...')")

        comp_count = len(COMPARISON_RE.findall(full_text))
        if comp_count >= 2:
            patterns_found.append(f"comparisons ({comp_count})")
        else:
            patterns_missing.append("comparison language (vs, compared to, unlike)")

        q_heads = len(QUESTION_HEAD_RE.findall(raw_html))
        if q_heads >= 2:
            patterns_found.append(f"question headings ({q_heads})")
        else:
            patterns_missing.append("question-format headings (What is...?, How to...?)")

        howto = len(HOW_TO_RE.findall(raw_html))
        if howto >= 1:
            patterns_found.append(f"how-to headings ({howto})")

        ols = len(soup.find_all("ol"))
        if ols >= 1:
            patterns_found.append(f"ordered lists ({ols})")
        else:
            patterns_missing.append("ordered lists (step-by-step instructions)")

        details = len(soup.find_all("details"))
        if details >= 2:
            patterns_found.append(f"expandable sections ({details})")

        # Type-token ratio — proxy for content uniqueness vs repetition
        words = re.findall(r'\b[a-z]{4,}\b', full_text.lower())
        ttr = len(set(words)) / len(words) if words else 0
        if ttr >= 0.40:
            patterns_found.append(f"high lexical diversity (TTR {round(ttr, 2)})")
        elif ttr < 0.25:
            patterns_missing.append("lexical diversity — content appears repetitive")

        page_max = 30
        page_score = min(len(patterns_found) * 5, page_max)
        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "patterns_found": patterns_found,
            "patterns_missing": patterns_missing[:3],
            "definition_count": def_count,
            "comparison_count": comp_count,
            "question_headings": q_heads,
            "ordered_lists": ols,
            "type_token_ratio": round(ttr, 3),
            "score": page_score,
            "maxScore": page_max,
            "issue": "Few semantic patterns — low AI citation probability" if len(patterns_found) < 2 else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have strong semantic structure",
    }


# ── Check 6: Anchor Text Quality ──────────────────────────────────────────────

def check_anchor_quality(snapshot_dir: Path) -> dict:
    """
    AI models use anchor text to understand what a linked page is about.
    Generic anchors ('click here', 'read more') provide zero semantic signal.
    Specific anchors ('best 65-inch TVs', 'Samsung air conditioner range') help both
    AI discovery and traditional SEO link equity.
    """
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        all_links = soup.find_all("a", href=True)

        internal_links = [
            a for a in all_links
            if not a["href"].startswith(("mailto:", "tel:", "javascript:"))
            and (not a["href"].startswith("http") or "thegoodguys.com.au" in a["href"])
        ]
        if not internal_links:
            continue

        generic = []
        specific = []
        empty = []

        for a in internal_links:
            text = a.get_text(" ", strip=True).lower().strip()
            if not text or len(text) < 2:
                empty.append(a.get("href", "")[:60])
            elif text in GENERIC_ANCHORS or (len(text.split()) == 1 and text in {"here", "more", "link", "page"}):
                generic.append(text)
            else:
                specific.append(text[:60])

        total = len(internal_links)
        specific_ratio = len(specific) / total if total else 0
        generic_ratio = len(generic) / total if total else 0

        page_max = 20
        if specific_ratio >= 0.85:
            page_score = 20
        elif specific_ratio >= 0.70:
            page_score = 14
        elif specific_ratio >= 0.50:
            page_score = 8
        else:
            page_score = 0

        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "total_internal_links": total,
            "specific_anchors": len(specific),
            "generic_anchors": len(generic),
            "empty_anchors": len(empty),
            "specific_ratio_pct": round(specific_ratio * 100),
            "top_generic": generic[:5],
            "score": page_score,
            "maxScore": page_max,
            "issue": f"{round(generic_ratio*100)}% generic anchors — zero semantic signal for AI" if generic_ratio > 0.20 else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have >85% specific anchor text",
    }


# ── Check 7: Content Similarity ───────────────────────────────────────────────

def check_content_similarity(snapshot_dir: Path) -> dict:
    """
    TF-IDF cosine similarity between page content and a reference corpus of ideal
    AI-citable ecommerce passages. Measures whether page content resembles the kind
    of direct, factual, entity-rich content AI Answer Engines prefer to cite.

    Scoring thresholds (sentence-transformers / TF-IDF fallback):
      ST  ≥0.65 | TFIDF ≥0.35 — strong: direct, factual, entity-rich content
      ST  ≥0.55 | TFIDF ≥0.28 — moderate: good passages among marketing copy
      ST  ≥0.45 | TFIDF ≥0.20 — weak: mostly promotional, few citable facts
      ST  <0.45 | TFIDF <0.20 — very weak: almost no AI-citable patterns

    TODO: swap similarity_to_corpus() to OpenAI/Cohere embeddings API for higher
    accuracy — see module docstring for options.
    """
    # Thresholds differ between semantic (ST) and lexical (TF-IDF) backends
    if _ST_AVAILABLE:
        thresholds = (0.65, 0.55, 0.45, 0.38)
        method = "sentence-transformers all-MiniLM-L6-v2"
    else:
        thresholds = (0.35, 0.28, 0.20, 0.12)
        method = "TF-IDF cosine (bag-of-words) — install sentence-transformers for semantic similarity"

    t_strong, t_good, t_weak, t_poor = thresholds

    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        full_text = soup.get_text(" ", strip=True)
        if len(full_text.split()) < 80:
            continue

        # Use main content if available — strips nav/footer noise
        main = get_main_content(soup)
        content_text = main.get_text(" ", strip=True) if main else full_text

        # Full-page similarity
        best_score, avg_top3, best_ref = similarity_to_corpus(full_text)

        # Passage-level: split into ~200-word chunks, find best citable passage
        words = content_text.split()
        chunks = [
            " ".join(words[i:i + 200])
            for i in range(0, len(words), 200)
            if len(words[i:i + 200]) >= 50
        ]
        best_passage_score = 0.0
        best_passage_text = ""
        for chunk in chunks:
            s, _, _ = similarity_to_corpus(chunk)
            if s > best_passage_score:
                best_passage_score = s
                best_passage_text = chunk[:150]

        page_max = 25
        if best_passage_score >= t_strong:
            page_score = 25
        elif best_passage_score >= t_good:
            page_score = 18
        elif best_passage_score >= t_weak:
            page_score = 10
        elif best_passage_score >= t_poor:
            page_score = 5
        else:
            page_score = 0

        total_score += page_score
        max_score += page_max

        issue = None
        if best_passage_score < t_poor:
            issue = f"Very low similarity ({best_passage_score:.2f}) — content reads as promotional, not citable"
        elif best_passage_score < t_weak:
            issue = f"Low similarity ({best_passage_score:.2f}) — few factual/educational passages for AI to cite"

        results.append({
            "file": html_file.name,
            "full_page_similarity": round(best_score, 3),
            "avg_top3_similarity": round(avg_top3, 3),
            "best_passage_similarity": round(best_passage_score, 3),
            "best_passage_preview": best_passage_text,
            "best_reference_match": best_ref,
            "score": page_score,
            "maxScore": page_max,
            "issue": issue,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    all_scores = [r["best_passage_similarity"] for r in results]
    avg_sim = round(sum(all_scores) / len(all_scores), 3) if all_scores else 0

    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "avg_similarity": avg_sim,
        "similarity_method": method,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have strong AI-citable content (avg: {avg_sim}, method: {'ST' if _ST_AVAILABLE else 'TF-IDF'})",
    }


# ── Summary & output ───────────────────────────────────────────────────────────

def build_summary(checks: dict, label: str, snapshot_dir: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total_score = sum(c.get("score", 0) for c in checks.values() if isinstance(c, dict))
    total_max = sum(c.get("maxScore", 0) for c in checks.values() if isinstance(c, dict))
    pct = round(total_score / total_max * 100) if total_max else 0
    g = grade(pct)

    lines = [
        f"# AEO Content Intelligence — {label}\n",
        f"**Snapshot directory:** `{snapshot_dir}` | {ts}\n",
        f"## {GRADE_EMOJI.get(g, '❓')} Grade {g} &nbsp; {total_score}/{total_max} ({pct}%)\n",
        "## Check Results\n",
        "| | Check | Score | % | Summary |",
        "|--|-------|------:|--:|---------|",
    ]

    check_labels = {
        "boilerplate_ratio":  "Boilerplate Ratio",
        "content_chunking":   "Content Chunking (LLM retrieval)",
        "entity_signals":     "Entity Signals",
        "knowledge_graph":    "Knowledge Graph",
        "semantic_structure": "Semantic Structure",
        "anchor_quality":     "Anchor Text Quality",
        "content_similarity": "Content Similarity (TF-IDF)",
    }
    for key, name in check_labels.items():
        c = checks.get(key, {})
        if "error" in c:
            lines.append(f"| ✗ | {name} | — | — | {c['error'][:60]} |")
            continue
        c_pct = c.get("percentage", 0)
        icon = "✓" if c_pct >= 75 else "◑" if c_pct >= 50 else "✗"
        lines.append(f"| {icon} | {name} | {c.get('score', 0)}/{c.get('maxScore', 0)} | {c_pct}% | {c.get('summary', '')} |")

    all_issues = []
    for key, name in check_labels.items():
        for e in checks.get(key, {}).get("errors", []):
            issue = e.get("issue") or e.get("error") or ""
            ident = e.get("file") or e.get("url") or ""
            if issue:
                all_issues.append((name, ident, issue))

    if all_issues:
        lines.append("\n## Issues Found\n")
        for check_name, ident, issue in all_issues[:20]:
            lines.append(f"- **[{check_name}]** `{ident}` — {issue}")

    return "\n".join(lines)


def push_to_repo(data: dict, label: str) -> None:
    import base64
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    ref = os.getenv("GITHUB_REF_NAME")
    run_number = os.getenv("GITHUB_RUN_NUMBER", "?")
    if not (token and repo and ref):
        return
    slug = re.sub(r"[^a-z0-9-]", "-", label.lower())
    path = f"seo/outputs/aeo/content-latest-{slug}.json"
    b64 = base64.b64encode(json.dumps(data, indent=2).encode()).decode()
    api = "https://api.github.com"
    hdrs = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=hdrs, timeout=30)
    sha = existing.json().get("sha") if existing.status_code == 200 else None
    payload = {"message": f"Content AEO audit ({label}) run #{run_number}", "content": b64, "branch": ref}
    if sha:
        payload["sha"] = sha
    resp = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=hdrs, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"Committed to repo: {path}")
    else:
        print(f"Warning: could not commit ({resp.status_code})", file=sys.stderr)


def main():
    snapshot_dir_str = os.getenv("SNAPSHOT_DIR", "").strip()
    if not snapshot_dir_str:
        print("ERROR: SNAPSHOT_DIR not set. Example: SNAPSHOT_DIR=site-snapshots/thegoodguys.com.au python run_content_aeo.py", file=sys.stderr)
        sys.exit(1)

    snapshot_dir = Path(snapshot_dir_str)
    if not snapshot_dir.exists():
        print(f"ERROR: Snapshot directory not found: {snapshot_dir}", file=sys.stderr)
        sys.exit(1)

    label = os.getenv("AEO_LABEL", snapshot_dir.name)
    html_files = sorted(snapshot_dir.glob("*.html"))
    print(f"Content AEO audit: {snapshot_dir} ({len(html_files)} snapshots)")

    checks = {}
    all_checks = [
        ("boilerplate_ratio",  "Boilerplate ratio",           lambda: check_boilerplate_ratio(snapshot_dir)),
        ("content_chunking",   "Content chunking",            lambda: check_content_chunking(snapshot_dir)),
        ("entity_signals",     "Entity signals",              lambda: check_entity_signals(snapshot_dir)),
        ("knowledge_graph",    "Knowledge graph",             lambda: check_knowledge_graph(snapshot_dir)),
        ("semantic_structure", "Semantic structure",          lambda: check_semantic_structure(snapshot_dir)),
        ("anchor_quality",     "Anchor text quality",         lambda: check_anchor_quality(snapshot_dir)),
        ("content_similarity", "Content similarity (TF-IDF)", lambda: check_content_similarity(snapshot_dir)),
    ]
    for i, (key, name, fn) in enumerate(all_checks, 1):
        print(f"  [{i}/{len(all_checks)}] {name}...")
        checks[key] = fn()
        c = checks[key]
        print(f"        {GRADE_EMOJI.get(c.get('grade','?'), '?')} {c.get('grade','?')} ({c.get('percentage',0)}%) — {c.get('summary','')}")

    total_score = sum(c.get("score", 0) for c in checks.values())
    total_max = sum(c.get("maxScore", 0) for c in checks.values())
    pct = round(total_score / total_max * 100) if total_max else 0
    g = grade(pct)
    print(f"\nContent AEO: {GRADE_EMOJI.get(g, '?')} Grade {g} ({pct}%) — {total_score}/{total_max}")

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    slug = re.sub(r"[^a-z0-9-]", "-", label.lower())
    out_file = out_dir / f"content-aeo-{slug}-{ts}.json"
    payload = {
        "label": label, "dir": str(snapshot_dir),
        "grade": g, "score": total_score, "maxScore": total_max, "percentage": pct,
        "checks": checks,
    }
    out_file.write_text(json.dumps(payload, indent=2))
    print(f"Saved {out_file}")

    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as f:
            f.write("\n\n---\n\n")
            f.write(build_summary(checks, label, str(snapshot_dir)))

    push_to_repo(payload, label)


if __name__ == "__main__":
    main()
