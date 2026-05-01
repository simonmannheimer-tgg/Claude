"""
LLM-judge for AEO content quality scoring.

Uses a local Ollama instance to score ecommerce page content on four dimensions:
  - clarity           (0-10): Is the content clear and easy to understand?
  - specificity       (0-10): Does it name specific products, brands, specs?
  - schema_alignment  (0-10): Does visible content match what schema claims?
  - query_answerability (0-10): Could an AI answer a user question from this text?

Primary model:  phi4 (Phi-4 14B Q4_K_M) via Ollama
Fallback model: qwen2.5:7b-instruct via Ollama
Graceful skip:  if Ollama unreachable, returns {"available": false}

Usage:
    python llm_judge.py --text "Samsung 65-inch 4K TV..." --type product
    python llm_judge.py --file site-snapshots/thegoodguys.com.au/televisions.html --type category

Requires:
    Ollama running locally: ollama serve
    Model pulled: ollama pull phi4  (or: ollama pull qwen2.5:7b-instruct)
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import httpx
    _HTTPX = True
except ImportError:
    _HTTPX = False

OLLAMA_BASE = "http://localhost:11434"
PRIMARY_MODEL = "phi4"
FALLBACK_MODEL = "qwen2.5:7b-instruct"
MAX_TEXT_CHARS = 6000  # ~1500 tokens; keep prompt within context budget

JUDGE_PROMPT = """\
You are an AI content evaluator assessing ecommerce page content for AI discoverability.
Evaluate the following {page_type} page content on four criteria. Return ONLY valid JSON.

Content:
{text}

Rate each criterion from 0 to 10:
- clarity: Is the content clear, concise, and well-organised for AI parsing?
- specificity: Does it include specific product names, brands, specs, and prices?
- schema_alignment: Does the visible text match what structured data (schema.org) would claim?
- query_answerability: Could an AI agent directly answer a user question using only this content?

Respond with exactly this JSON structure (no other text):
{{"clarity": <int>, "specificity": <int>, "schema_alignment": <int>, "query_answerability": <int>, "reasoning": "<one sentence>"}}
"""


def _is_ollama_available() -> bool:
    if not _HTTPX:
        return False
    try:
        resp = httpx.get(f"{OLLAMA_BASE}/api/tags", timeout=5)
        return resp.status_code == 200
    except Exception:
        return False


def _available_models() -> list[str]:
    try:
        resp = httpx.get(f"{OLLAMA_BASE}/api/tags", timeout=5)
        if resp.status_code == 200:
            return [m["name"] for m in resp.json().get("models", [])]
    except Exception:
        pass
    return []


def _call_ollama(model: str, prompt: str, timeout: int = 120) -> str | None:
    try:
        resp = httpx.post(
            f"{OLLAMA_BASE}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=timeout,
        )
        if resp.status_code == 200:
            return resp.json().get("response", "")
    except Exception:
        pass
    return None


def _parse_scores(raw: str) -> dict | None:
    json_match = re.search(r'\{[^{}]+\}', raw, re.DOTALL)
    if not json_match:
        return None
    try:
        data = json.loads(json_match.group())
        required = {"clarity", "specificity", "schema_alignment", "query_answerability"}
        if not required.issubset(data):
            return None
        for k in required:
            data[k] = max(0, min(10, int(data[k])))
        return data
    except (json.JSONDecodeError, ValueError, TypeError):
        return None


def judge_content(text: str, page_type: str = "page", timeout: int = 120) -> dict:
    """
    Score content using local LLM. Returns scoring dict or {"available": false}.
    """
    if not _is_ollama_available():
        return {"available": False, "reason": "Ollama not running at localhost:11434"}

    # Truncate to token budget
    truncated = text[:MAX_TEXT_CHARS]
    if len(text) > MAX_TEXT_CHARS:
        truncated += "\n[...content truncated...]"

    prompt = JUDGE_PROMPT.format(page_type=page_type, text=truncated)

    # Try primary model, then fallback
    models = _available_models()
    for model in [PRIMARY_MODEL, FALLBACK_MODEL]:
        if not any(model in m for m in models):
            continue
        raw = _call_ollama(model, prompt, timeout=timeout)
        if raw:
            scores = _parse_scores(raw)
            if scores:
                overall = round(sum(scores[k] for k in ("clarity", "specificity", "schema_alignment", "query_answerability")) / 4, 1)
                return {
                    "available": True,
                    "model": model,
                    "clarity": scores["clarity"],
                    "specificity": scores["specificity"],
                    "schema_alignment": scores["schema_alignment"],
                    "query_answerability": scores["query_answerability"],
                    "llm_overall": overall,
                    "reasoning": scores.get("reasoning", ""),
                }

    return {"available": False, "reason": "No suitable model available (pull phi4 or qwen2.5:7b-instruct)"}


def judge_html_file(path: str, page_type: str = "page") -> dict:
    from bs4 import BeautifulSoup
    html = Path(path).read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    return judge_content(text, page_type)


def main():
    parser = argparse.ArgumentParser(description="LLM-judge for AEO content scoring")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Content text to score")
    group.add_argument("--file", help="HTML file to score")
    parser.add_argument("--type", default="page", help="Page type (product/category/guide/home)")
    parser.add_argument("--timeout", type=int, default=120, help="Ollama timeout (seconds)")
    args = parser.parse_args()

    if args.file:
        result = judge_html_file(args.file, args.type)
    else:
        result = judge_content(args.text, args.type, args.timeout)

    print(json.dumps(result, indent=2))
    if not result.get("available"):
        sys.exit(1)


if __name__ == "__main__":
    main()
