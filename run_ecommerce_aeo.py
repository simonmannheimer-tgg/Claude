"""
Phase 3 — Ecommerce AEO Audit

Ecommerce-specific checks that agentic-seo misses:
  1. Schema/structured data  — Product, FAQ, BreadcrumbList, AggregateRating, Offer
  2. Render diff             — httpx raw response vs Playwright snapshot (bot vs browser)
  3. User agent behaviour    — ClaudeBot, GPTBot, PerplexityBot vs real browser UA
  4. Hidden content          — display:none / aria-hidden / collapsed details/accordions
  5. AI content signals      — FAQ blocks, comparison tables, direct answers, definition §

Usage:
    SNAPSHOT_DIR=site-snapshots/thegoodguys.com.au python run_ecommerce_aeo.py
    SNAPSHOT_DIR=site-snapshots/thegoodguys.com.au LIVE_URLS='["https://..."]' python run_ecommerce_aeo.py

Requires:
    pip install httpx beautifulsoup4
    (Playwright snapshots should already exist from Phase 2)

Writes:
    $GITHUB_STEP_SUMMARY              — appended after Phase 1 + 2 summaries
    seo/outputs/aeo/ecommerce-aeo-<label>-YYYYMMDD-HHMM.json
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urljoin

import httpx
from bs4 import BeautifulSoup

# ── Constants ─────────────────────────────────────────────────────────────────

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

# Primary AI bots — blocking any of these is scored as a failure
AI_BOT_UAS = {
    "ClaudeBot":       "ClaudeBot/1.0 (+https://www.anthropic.com/claude-bot)",
    "GPTBot":          "GPTBot/1.1 (+https://openai.com/gptbot)",
    "PerplexityBot":   "PerplexityBot/1.0 (+https://docs.perplexity.ai/docs/perplexitybot)",
    "Google-Extended": "Mozilla/5.0 (compatible; Google-Extended)",
}
# Informational only — not scored (blocking Googlebot is a separate SEO issue, not AEO)
GOOGLEBOT_UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

# Schema types that matter for ecommerce AI visibility
REQUIRED_SCHEMA_TYPES = {
    "home":     ["WebSite", "Organization", "SiteLinksSearchBox"],
    "category": ["ItemList", "BreadcrumbList", "CollectionPage"],
    "product":  ["Product", "Offer", "AggregateRating", "BreadcrumbList"],
    "guide":    ["Article", "FAQPage", "BreadcrumbList", "VideoObject"],
    "default":  ["BreadcrumbList", "WebPage"],
}

# AI Overview content signals — patterns that increase citation probability
# comparison_table is detected via BS4 in check_ai_signals (avoids re.DOTALL risk on large HTML)
AI_SIGNAL_PATTERNS = {
    "direct_answer_paragraph": re.compile(
        r"<p[^>]*>[^<]{80,}(?:is|are|means|refers to|defined as)[^<]{20,}</p>",
        re.IGNORECASE,
    ),
    "numbered_list": re.compile(r"<ol[^>]*>.*?</ol>", re.IGNORECASE | re.DOTALL),
    "definition_heading": re.compile(
        r"<h[23][^>]*>(?:What is|What are|How to|Why)[^<]{5,50}</h[23]>",
        re.IGNORECASE,
    ),
}

GRADE_EMOJI = {"A": "🟢", "B": "🟢", "C": "🟡", "D": "🟠", "F": "🔴"}

# Required fields per schema @type for validity checks
SCHEMA_REQUIRED_FIELDS: dict[str, set[str]] = {
    "Product":          {"name", "offers"},
    "Offer":            {"price", "priceCurrency"},
    "AggregateRating":  {"ratingValue", "reviewCount"},
    "FAQPage":          {"mainEntity"},
    "Question":         {"name", "acceptedAnswer"},
    "BreadcrumbList":   {"itemListElement"},
    "Article":          {"headline", "author"},
    "WebSite":          {"url"},
    "Organization":     {"name"},
    "ItemList":         {"itemListElement"},
    "LocalBusiness":    {"name", "address"},
}

DEFAULT_COMPETITORS = [
    {"label": "JB Hi-Fi",         "url": "https://www.jbhifi.com.au"},
    {"label": "Harvey Norman",     "url": "https://www.harveynorman.com.au"},
    {"label": "Appliances Online", "url": "https://www.appliancesonline.com.au"},
]


# ── Helpers ────────────────────────────────────────────────────────────────────

def grade(pct: int) -> str:
    if pct >= 90: return "A"
    if pct >= 75: return "B"
    if pct >= 60: return "C"
    if pct >= 40: return "D"
    return "F"


def parse_html(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")


def infer_page_type(filename: str) -> str:
    name = filename.lower()
    if name == "index.html":
        return "home"
    if any(k in name for k in ("buying-guide", "best-", "guide")):
        return "guide"
    # Products have SKU numbers, /p/ path segment, or "product" in name.
    # Sub-categories use -- to join path segments (televisions--smart-tvs.html)
    # and should NOT be classified as products.
    if any(k in name for k in ("product", "sku")) or re.search(r"\bp\b", name):
        return "product"
    return "category"


def extract_jsonld(soup: BeautifulSoup) -> list[dict]:
    schemas = []
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.get_text() or "")
            if isinstance(data, list):
                schemas.extend(data)
            else:
                schemas.append(data)
        except (json.JSONDecodeError, TypeError):
            pass
    return schemas


def flatten_schema_types(schemas: list[dict]) -> set[str]:
    types = set()
    for s in schemas:
        t = s.get("@type", "")
        if isinstance(t, list):
            types.update(t)
        elif t:
            types.add(t)
        # Recurse into @graph
        for item in s.get("@graph", []):
            types.update(flatten_schema_types([item]))
    return types


# ── Check 1: Schema / Structured Data ─────────────────────────────────────────

def check_schema(snapshot_dir: Path) -> dict:
    results = []
    total_score = 0
    max_score = 0

    html_files = sorted(snapshot_dir.glob("*.html"))
    if not html_files:
        return {"error": "No HTML snapshots found", "score": 0, "maxScore": 0}

    for html_file in html_files:
        page_type = infer_page_type(html_file.name)
        required = REQUIRED_SCHEMA_TYPES.get(page_type, REQUIRED_SCHEMA_TYPES["default"])
        soup = parse_html(html_file)
        schemas = extract_jsonld(soup)
        found_types = flatten_schema_types(schemas)

        present = [t for t in required if t in found_types]
        missing = [t for t in required if t not in found_types]
        extra = [t for t in found_types if t not in required]
        bonus = [t for t in ["FAQPage", "VideoObject", "HowTo"] if t in found_types and t not in required]

        page_max = len(required) * 10
        page_score = len(present) * 10 + len(bonus) * 5
        page_score = min(page_score, page_max)

        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "page_type": page_type,
            "found_types": sorted(found_types),
            "required": required,
            "present": present,
            "missing": missing,
            "bonus": bonus,
            "score": page_score,
            "maxScore": page_max,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r["missing"]]
    return {
        "score": total_score,
        "maxScore": max_score,
        "percentage": pct,
        "grade": grade(pct),
        "pages": results,
        "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have all required schema",
    }


# ── Check 2: Render Diff (bot-accessible vs JS-rendered content) ───────────────

def check_render_diff(snapshot_dir: Path, urls: list[str]) -> dict:
    results = []
    total_score = 0
    max_score = len(urls) * 20 if urls else 0

    client = httpx.Client(
        headers={"User-Agent": BROWSER_UA},
        follow_redirects=True,
        timeout=15,
    )

    for url in urls:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        filename = ("index" if not path else re.sub(r"[^a-zA-Z0-9_-]", "-", path.replace("/", "--"))) + ".html"
        snapshot_path = snapshot_dir / filename

        if not snapshot_path.exists():
            results.append({"url": url, "error": "No snapshot found"})
            continue

        # Rendered word count from Playwright snapshot
        rendered_soup = parse_html(snapshot_path)
        rendered_text = rendered_soup.get_text(separator=" ", strip=True)
        rendered_words = len(rendered_text.split())

        # Raw server response (what a headless bot without JS sees)
        try:
            resp = client.get(url, timeout=15)
            raw_soup = BeautifulSoup(resp.text, "html.parser")
            raw_text = raw_soup.get_text(separator=" ", strip=True)
            raw_words = len(raw_text.split())
            status = resp.status_code
        except Exception as e:
            results.append({"url": url, "error": str(e)[:100]})
            continue

        if rendered_words == 0:
            results.append({"url": url, "error": "Empty rendered snapshot"})
            continue

        ratio = raw_words / rendered_words if rendered_words else 0
        # For SSR pages raw > rendered is expected (server sends full DOM before JS runs).
        # Cap display at 100% — anything >=80% scores full marks.
        pct_accessible = min(round(ratio * 100), 100)
        ssr_detected = raw_words > rendered_words
        diff_words = rendered_words - raw_words  # negative when SSR (no JS-gated content)

        # Score: 20pts if >=80% content accessible without JS, partial 50-79%, 0 <50%
        if pct_accessible >= 80:
            page_score = 20
        elif pct_accessible >= 50:
            page_score = 10
        else:
            page_score = 0

        total_score += page_score

        results.append({
            "url": url,
            "status_code": status,
            "raw_words": raw_words,
            "rendered_words": rendered_words,
            "pct_accessible": pct_accessible,
            "ssr_detected": ssr_detected,
            "js_only_words": max(diff_words, 0),
            "score": page_score,
            "maxScore": 20,
            "note": "SSR detected — raw HTML contains full content" if ssr_detected else None,
            "issue": "High JS dependency — bots without JS miss significant content" if pct_accessible < 80 else None,
        })

    client.close()
    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("pct_accessible", 100) < 80 and "error" not in r]
    return {
        "score": total_score,
        "maxScore": max_score,
        "percentage": pct,
        "grade": grade(pct),
        "pages": results,
        "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages ≥80% content accessible without JS",
    }


# ── Check 3: User Agent Behaviour ─────────────────────────────────────────────

def check_user_agents(test_urls: list[str]) -> dict:
    results = []
    total_score = 0
    max_score = len(test_urls) * len(AI_BOT_UAS) * 5 if test_urls else 0

    for url in test_urls:
        ua_results = {}
        for bot_name, ua_string in AI_BOT_UAS.items():
            try:
                resp = httpx.get(
                    url,
                    headers={"User-Agent": ua_string},
                    follow_redirects=True,
                    timeout=10,
                )
                allowed = resp.status_code == 200
                ua_results[bot_name] = {
                    "status": resp.status_code,
                    "allowed": allowed,
                    "score": 5 if allowed else 0,
                }
                if allowed:
                    total_score += 5
            except Exception as e:
                ua_results[bot_name] = {"status": "error", "allowed": False, "error": str(e)[:80], "score": 0}

        # Googlebot: informational only, not scored (blocking is an SEO issue not AEO)
        try:
            resp_gb = httpx.get(
                url,
                headers={"User-Agent": GOOGLEBOT_UA},
                follow_redirects=True,
                timeout=10,
            )
            ua_results["Googlebot (info)"] = {
                "status": resp_gb.status_code,
                "allowed": resp_gb.status_code == 200,
                "score": None,
                "note": "informational — not scored",
            }
        except Exception as e:
            ua_results["Googlebot (info)"] = {"status": "error", "note": str(e)[:80], "score": None}

        blocked = [k for k, v in ua_results.items() if k != "Googlebot (info)" and not v.get("allowed")]
        results.append({
            "url": url,
            "bots": ua_results,
            "blocked": blocked,
            "issue": f"Blocked for: {', '.join(blocked)}" if blocked else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("blocked")]
    return {
        "score": total_score,
        "maxScore": max_score,
        "percentage": pct,
        "grade": grade(pct),
        "pages": results,
        "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages accessible to all AI bots",
    }


# ── Check 4: Hidden Content ────────────────────────────────────────────────────

def check_hidden_content(snapshot_dir: Path) -> dict:
    results = []
    total_score = 0
    max_score = 0

    html_files = sorted(snapshot_dir.glob("*.html"))
    if not html_files:
        return {"error": "No HTML snapshots found", "score": 0, "maxScore": 0}

    for html_file in html_files:
        soup = parse_html(html_file)
        all_text = soup.get_text(separator=" ", strip=True)
        all_words = len(all_text.split())
        if all_words == 0:
            continue

        # Find elements that conceal content — skip descendants of already-counted hidden elements
        # to avoid double-counting nested structures.
        hidden_words = 0
        hidden_elements = []
        hidden_el_set: set = set()  # ids of elements already counted as hidden

        for el in soup.find_all(True):
            # Skip if any ancestor is already marked hidden
            if any(id(a) in hidden_el_set for a in el.parents):
                continue

            style = el.get("style", "")
            aria_hidden = el.get("aria-hidden", "")
            hidden_attr = el.has_attr("hidden")
            el_classes = el.get("class", [])
            classes_str = " ".join(el_classes)

            # Viewport-specific responsive classes (hide at certain breakpoints only,
            # not from all agents) — exclude these from AI-hidden detection.
            VIEWPORT_HIDE_PATTERN = re.compile(
                r"\bhide-(?:xxs|xs|sm|md|lg|xl)\b"
                r"|\bd-(?:sm|md|lg|xl|xxl)-none\b"
                r"|\bvisible-(?:xs|sm|md|lg|xl)\b",
                re.IGNORECASE,
            )
            has_only_viewport_hide = (
                any(VIEWPORT_HIDE_PATTERN.search(c) for c in el_classes)
                and not any(c in ("hidden", "d-none", "is-hidden", "collapsed") for c in el_classes)
            )

            is_hidden = (
                not has_only_viewport_hide
                and (
                    "display:none" in style.replace(" ", "")
                    or "display: none" in style
                    or "visibility:hidden" in style.replace(" ", "")
                    or aria_hidden == "true"
                    or hidden_attr
                    or any(c in el_classes for c in ("hidden", "d-none", "is-hidden", "collapsed"))
                )
            )

            if is_hidden:
                hidden_el_set.add(id(el))
                text = el.get_text(separator=" ", strip=True)
                words = len(text.split())
                if words > 20:
                    hidden_words += words
                    hidden_elements.append({
                        "tag": el.name,
                        "class": classes_str[:60],
                        "words": words,
                        "reason": (
                            "display:none" if "display" in style else
                            "aria-hidden" if aria_hidden == "true" else
                            "hidden attr" if hidden_attr else
                            "CSS class"
                        ),
                    })

        # Check for details/summary (collapsed by default in browsers)
        details_text_words = 0
        for details in soup.find_all("details"):
            if not details.has_attr("open"):
                text = details.get_text(separator=" ", strip=True)
                details_text_words += len(text.split())

        hidden_ratio = hidden_words / all_words if all_words else 0
        details_ratio = details_text_words / all_words if all_words else 0

        # Score: 20pts if <10% hidden, 10pts if 10-30%, 0 if >30%
        page_max = 20
        if hidden_ratio < 0.10:
            page_score = 20
        elif hidden_ratio < 0.30:
            page_score = 10
        else:
            page_score = 0

        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "total_words": all_words,
            "hidden_words": hidden_words,
            "hidden_ratio_pct": round(hidden_ratio * 100),
            "details_collapsed_words": details_text_words,
            "hidden_elements_count": len(hidden_elements),
            "top_hidden": hidden_elements[:5],
            "score": page_score,
            "maxScore": page_max,
            "issue": f"{round(hidden_ratio*100)}% of content hidden from AI crawlers" if hidden_ratio >= 0.10 else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score,
        "maxScore": max_score,
        "percentage": pct,
        "grade": grade(pct),
        "pages": results,
        "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have <10% content hidden",
    }


# ── Check 5: AI Content Signals ────────────────────────────────────────────────

def check_ai_signals(snapshot_dir: Path) -> dict:
    results = []
    total_score = 0
    max_score = 0

    html_files = sorted(snapshot_dir.glob("*.html"))
    if not html_files:
        return {"error": "No HTML snapshots found", "score": 0, "maxScore": 0}

    for html_file in html_files:
        raw_html = html_file.read_text(encoding="utf-8", errors="ignore")
        soup = BeautifulSoup(raw_html, "html.parser")
        page_type = infer_page_type(html_file.name)

        signals_found = []
        signals_missing = []

        # Check regex-based signal patterns (safe patterns only — no backtracking risk)
        for signal_name, pattern in AI_SIGNAL_PATTERNS.items():
            if pattern.search(raw_html):
                signals_found.append(signal_name)
            else:
                signals_missing.append(signal_name)

        # FAQ block detection via BS4 (avoids catastrophic-backtracking regex)
        faq_keywords = {"faq", "frequently asked", "question", "q&a", "q & a"}
        faq_found = False
        for tag in soup.find_all(["details", "section", "div"], limit=200):
            tag_text = tag.get_text(" ", strip=True).lower()[:200]
            classes = " ".join(tag.get("class", [])).lower()
            if any(kw in tag_text or kw in classes for kw in faq_keywords):
                faq_found = True
                break
        if faq_found:
            signals_found.append("faq_block")

        # Comparison table via BS4 (avoids re.DOTALL on large HTML)
        COMPARE_WORDS = {"vs", "versus", "compare", "comparison", "difference"}
        for table in soup.find_all("table", limit=20):
            tbl_text = table.get_text(" ", strip=True).lower()[:500]
            if any(w in tbl_text for w in COMPARE_WORDS):
                signals_found.append("comparison_table")
                break

        # Additional structural checks
        h1_tags = soup.find_all("h1")
        h2_tags = soup.find_all("h2")
        tables = soup.find_all("table")
        ols = soup.find_all("ol")
        uls = [ul for ul in soup.find_all("ul") if len(ul.find_all("li")) >= 3]
        details_open = soup.find_all("details")

        if h1_tags:
            signals_found.append("h1_present")
        if len(h2_tags) >= 3:
            signals_found.append("structured_headings")
        if tables:
            signals_found.append("data_tables")
        if ols:
            signals_found.append("ordered_lists")
        if uls:
            signals_found.append("structured_lists")
        if details_open:
            signals_found.append("expandable_faq")

        # Word count in first 200 words — direct answer check
        all_text = soup.get_text(separator=" ", strip=True)
        first_200 = " ".join(all_text.split()[:200])
        has_intro_answer = len(first_200) > 150 and any(
            kw in first_200.lower()
            for kw in ["shop", "find", "buy", "choose", "best", "range", "available"]
        )
        if has_intro_answer:
            signals_found.append("intro_answer_present")

        # Score: 5pts per signal, max 25
        page_max = 25
        page_score = min(len(signals_found) * 3, page_max)
        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "page_type": page_type,
            "signals_found": signals_found,
            "signals_missing": signals_missing,
            "h1_count": len(h1_tags),
            "h2_count": len(h2_tags),
            "table_count": len(tables),
            "score": page_score,
            "maxScore": page_max,
            "issue": "Low AI content signals — few patterns AI models cite" if page_score < 10 else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score,
        "maxScore": max_score,
        "percentage": pct,
        "grade": grade(pct),
        "pages": results,
        "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have strong AI content signals",
    }


# ── Check 6: Schema Validity ──────────────────────────────────────────────────

def _validate_schema_block(block: dict) -> list[str]:
    t = block.get("@type", "")
    if isinstance(t, list):
        t = t[0] if t else ""
    required = SCHEMA_REQUIRED_FIELDS.get(t, set())
    return [f for f in required if not block.get(f)]


def check_schema_validity(snapshot_dir: Path) -> dict:
    """Validates required fields in found JSON-LD blocks — presence alone isn't enough."""
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        schemas = extract_jsonld(soup)
        page_max = 15

        if not schemas:
            max_score += page_max
            results.append({"file": html_file.name, "schema_count": 0, "valid": 0,
                            "invalid": 0, "score": 0, "maxScore": page_max,
                            "issues": [], "issue": "No JSON-LD found"})
            continue

        issues = []
        valid_count = 0

        def _validate(item: dict) -> None:
            nonlocal valid_count
            missing = _validate_schema_block(item)
            t = item.get("@type", "unknown")
            if isinstance(t, list): t = t[0]
            if missing:
                issues.append(f"{t}: missing {', '.join(missing)}")
            else:
                valid_count += 1
            for sub in item.get("@graph", []):
                _validate(sub)

        for s in schemas:
            _validate(s)

        total_blocks = len(schemas)
        page_score = round(valid_count / total_blocks * page_max) if total_blocks else 0
        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "schema_count": total_blocks,
            "valid": valid_count,
            "invalid": total_blocks - valid_count,
            "score": page_score,
            "maxScore": page_max,
            "issues": issues[:5],
            "issue": "; ".join(issues[:2]) if issues else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have fully valid schema",
    }


# ── Check 7: DOM Structure & Rendering ────────────────────────────────────────

_HEADING_RE = re.compile(r'<h([1-6])', re.IGNORECASE)


def check_dom_structure(snapshot_dir: Path) -> dict:
    """
    Semantic HTML landmarks let AI parsers identify primary content without executing JS.
    Heading hierarchy gaps break document outline extraction.
    High external JS counts signal render-blocking complexity for non-JS bots.
    """
    results = []
    total_score = 0
    max_score = 0

    for html_file in sorted(snapshot_dir.glob("*.html")):
        soup = parse_html(html_file)
        raw_html = html_file.read_text(encoding="utf-8", errors="ignore")

        signals = []
        issues = []

        has_main    = bool(soup.find("main"))
        has_article = bool(soup.find("article"))
        has_header  = bool(soup.find("header"))
        has_nav     = bool(soup.find("nav"))
        has_footer  = bool(soup.find("footer"))
        landmark_count = sum([has_main, has_article, has_header, has_nav, has_footer])

        if has_main:    signals.append("<main>")
        else:           issues.append("missing <main> — AI cannot identify primary content area")
        if has_article: signals.append("<article>")
        if landmark_count >= 3: signals.append(f"{landmark_count} semantic landmarks")
        elif landmark_count < 2: issues.append("fewer than 2 semantic landmarks")

        # Heading hierarchy
        heading_levels = [int(m.group(1)) for m in _HEADING_RE.finditer(raw_html)]
        hierarchy_ok = True
        prev = 0
        for level in heading_levels:
            if level > prev + 1 and prev > 0:
                hierarchy_ok = False
                break
            prev = level
        if hierarchy_ok: signals.append("clean heading hierarchy")
        else:            issues.append("heading level skipped (e.g. H1→H3) — breaks AI doc outline")

        # External JS (signals render complexity for no-JS bots)
        ext_scripts = len([s for s in soup.find_all("script", src=True)
                           if s["src"].startswith(("http", "//"))])
        if ext_scripts <= 5:   signals.append(f"low JS ({ext_scripts} external scripts)")
        elif ext_scripts > 20: issues.append(f"high external JS ({ext_scripts} scripts)")

        # DOM element count
        dom_size = len(soup.find_all(True))
        if dom_size <= 1500:  signals.append(f"lean DOM ({dom_size} elements)")
        elif dom_size > 4000: issues.append(f"very large DOM ({dom_size} elements)")

        # ARIA usage (accessibility = AI parsability)
        aria_labels = len(soup.find_all(attrs={"aria-label": True}))
        if aria_labels >= 5: signals.append(f"good ARIA ({aria_labels} labels)")

        page_max = 25
        page_score = min(len(signals) * 5, page_max)
        total_score += page_score
        max_score += page_max

        results.append({
            "file": html_file.name,
            "has_main": has_main,
            "has_article": has_article,
            "landmark_count": landmark_count,
            "heading_hierarchy_ok": hierarchy_ok,
            "external_scripts": ext_scripts,
            "dom_elements": dom_size,
            "aria_labels": aria_labels,
            "signals": signals,
            "score": page_score,
            "maxScore": page_max,
            "issue": "; ".join(issues[:2]) if issues else None,
        })

    pct = round(total_score / max_score * 100) if max_score else 0
    errors = [r for r in results if r.get("issue")]
    return {
        "score": total_score, "maxScore": max_score, "percentage": pct, "grade": grade(pct),
        "pages": results, "errors": errors,
        "summary": f"{len(results) - len(errors)}/{len(results)} pages have strong DOM structure",
    }


# ── Check 8: Robots.txt & llms.txt Content ────────────────────────────────────

def _parse_robots(content: str) -> dict[str, dict]:
    """Return {agent: {allow: [...], disallow: [...]}}."""
    agents: dict[str, dict] = {}
    current: list[str] = []
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            if current and not any(agents.get(a, {}).get("disallow") or agents.get(a, {}).get("allow") for a in current):
                current = current + [value]
            else:
                current = [value]
            if value not in agents:
                agents[value] = {"allow": [], "disallow": []}
        elif key in ("allow", "disallow") and current:
            for a in current:
                agents.setdefault(a, {"allow": [], "disallow": []})[key].append(value)
    return agents


def check_robots_content(base_url: str) -> dict:
    """
    Parses actual robots.txt rules per AI bot — not just existence.
    A site that blocks GPTBot but allows ClaudeBot needs a different fix than
    one that uses a wildcard disallow. llms.txt quality also assessed.
    """
    bot_map = {
        "ClaudeBot":       ["claudebot"],
        "GPTBot":          ["gptbot"],
        "PerplexityBot":   ["perplexitybot"],
        "Google-Extended": ["google-extended"],
        "Googlebot":       ["googlebot"],
    }
    result: dict = {
        "robots": {}, "llms_txt": {},
        "score": 0, "maxScore": 50,
        "issues": [], "signals": [],
    }

    try:
        resp = httpx.get(f"{base_url}/robots.txt", timeout=15, follow_redirects=True,
                         headers={"User-Agent": BROWSER_UA})
        if resp.status_code == 200:
            parsed = _parse_robots(resp.text)
            wildcard = parsed.get("*", {})
            for bot_name, patterns in bot_map.items():
                bot_rules: dict = {"allow": [], "disallow": []}
                for pat in patterns:
                    for agent, rules in parsed.items():
                        if pat in agent.lower():
                            bot_rules["allow"].extend(rules.get("allow", []))
                            bot_rules["disallow"].extend(rules.get("disallow", []))

                blocked = "/" in bot_rules["disallow"] or (
                    "/" in wildcard.get("disallow", [])
                    and not bot_rules["allow"]
                    and not wildcard.get("allow", [])
                )
                bot_rules["blocked"] = blocked
                result["robots"][bot_name] = bot_rules
                if blocked and bot_name != "Googlebot":
                    result["issues"].append(f"{bot_name} is blocked in robots.txt")
                elif not blocked and bot_name != "Googlebot":
                    result["signals"].append(f"{bot_name} accessible via robots.txt")
        else:
            result["issues"].append(f"robots.txt returned HTTP {resp.status_code}")
    except Exception as e:
        result["issues"].append(f"robots.txt error: {str(e)[:60]}")

    try:
        resp = httpx.get(f"{base_url}/llms.txt", timeout=15, follow_redirects=True,
                         headers={"User-Agent": BROWSER_UA})
        if resp.status_code == 200:
            sections = re.findall(r'^##\s+.+', resp.text, re.MULTILINE)
            word_count = len(resp.text.split())
            result["llms_txt"] = {"exists": True, "sections": len(sections),
                                   "section_names": [s.strip("# ") for s in sections[:8]],
                                   "word_count": word_count}
            result["signals"].append(f"llms.txt: {len(sections)} sections, {word_count} words")
        else:
            result["llms_txt"] = {"exists": False}
            result["issues"].append("No llms.txt — AI agents cannot get a structured site overview")
    except Exception as e:
        result["llms_txt"] = {"exists": False, "error": str(e)[:60]}

    # Scoring
    ai_bots = [b for b in bot_map if b != "Googlebot"]
    accessible = sum(1 for b in ai_bots if not result["robots"].get(b, {}).get("blocked", False))
    score = accessible * 6  # max 24 (4 bots × 6pts)
    if result["llms_txt"].get("exists"):
        score += 16
        if result["llms_txt"].get("sections", 0) >= 3:
            score += 10

    result["score"] = min(score, 50)
    result["percentage"] = round(result["score"] / 50 * 100)
    result["grade"] = grade(result["percentage"])
    result["errors"] = [{"issue": i} for i in result["issues"]]
    result["summary"] = f"{accessible}/{len(ai_bots)} AI bots accessible | llms.txt: {'yes' if result['llms_txt'].get('exists') else 'no'}"
    return result


# ── Check 9: Sitemap Coverage ──────────────────────────────────────────────────

def _fetch_sitemap_urls(url: str, depth: int = 0) -> list[str]:
    if depth > 2:
        return []
    try:
        resp = httpx.get(url, timeout=20, follow_redirects=True, headers={"User-Agent": BROWSER_UA})
        if resp.status_code != 200:
            return []
        content = resp.text
        if "<sitemapindex" in content:
            sub_locs = re.findall(r'<loc>([^<]+)</loc>', content)
            urls: list[str] = []
            for sub in sub_locs[:8]:
                urls.extend(_fetch_sitemap_urls(sub.strip(), depth + 1))
            return urls
        return re.findall(r'<loc>([^<]+)</loc>', content)
    except Exception:
        return []


def check_sitemap_coverage(base_url: str) -> dict:
    """
    AI crawlers discover content via sitemaps. Missing content types = uncrawled pages.
    Checks for homepage, categories, products, and buying guides in sitemap index.
    """
    result: dict = {"score": 0, "maxScore": 40, "issues": [], "signals": [],
                    "url_count": 0, "coverage": {}}

    sitemap_urls: list[str] = []
    for path in ["/sitemap.xml", "/sitemap_index.xml", "/sitemap-index.xml"]:
        urls = _fetch_sitemap_urls(f"{base_url}{path}")
        if urls:
            sitemap_urls = urls
            result["signals"].append(f"sitemap found ({path}): {len(urls)} URLs")
            break

    if not sitemap_urls:
        result.update({"issues": ["No sitemap.xml found"], "percentage": 0,
                        "grade": "F", "summary": "No sitemap found",
                        "errors": [{"issue": "No sitemap.xml — AI crawlers may miss content"}]})
        return result

    result["url_count"] = len(sitemap_urls)
    sample = "\n".join(sitemap_urls[:6000])

    coverage = {
        "category_pages":  bool(re.search(r'/(televisions|air-conditioners|washing-machines|refrigerators|laptops)', sample)),
        "buying_guides":   bool(re.search(r'/buying-guide/', sample)),
        "product_pages":   bool(re.search(r'(-\d{5,}|/products?/|/p/)', sample)),
        "content_pages":   bool(re.search(r'/(whats-new|blog|news|advice)/', sample)),
    }
    result["coverage"] = coverage
    covered = sum(coverage.values())

    for ct, present in coverage.items():
        if present: result["signals"].append(f"{ct} in sitemap")
        else:       result["issues"].append(f"{ct} not found in sitemap")

    score = round(covered / len(coverage) * 40)
    result.update({
        "score": score,
        "percentage": round(score / 40 * 100),
        "grade": grade(round(score / 40 * 100)),
        "errors": [{"issue": i} for i in result["issues"]],
        "summary": f"{covered}/{len(coverage)} content types in sitemap | {len(sitemap_urls)} total URLs",
    })
    return result


# ── Check 10: Competitor Schema Comparison ────────────────────────────────────

def check_competitor_schema(snapshot_dir: Path, competitors: list[dict] | None = None) -> dict:
    """
    Compares TGG schema breadth against competitors fetched via httpx.
    Schema types TGG has that competitors lack = competitive advantage.
    Schema types competitors have that TGG lacks = priority gap to close.
    """
    competitors = competitors or DEFAULT_COMPETITORS

    # TGG schema from snapshots (already crawled — no HTTP needed)
    tgg_all: set[str] = set()
    for html_file in sorted(snapshot_dir.glob("*.html")):
        tgg_all.update(flatten_schema_types(extract_jsonld(parse_html(html_file))))

    # Competitor schema via httpx (homepage + category attempt)
    comp_results = []
    all_comp_schema: set[str] = set()

    for comp in competitors[:3]:
        comp_schema: set[str] = set()
        for path in ["", "/televisions", "/tv"]:
            url = comp["url"].rstrip("/") + path
            try:
                resp = httpx.get(url, timeout=15, follow_redirects=True,
                                 headers={"User-Agent": BROWSER_UA})
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "html.parser")
                    comp_schema.update(flatten_schema_types(extract_jsonld(soup)))
            except Exception:
                pass
            if comp_schema:
                break  # got schema, move on
        all_comp_schema.update(comp_schema)
        comp_results.append({"label": comp["label"], "url": comp["url"],
                              "schema_types": sorted(comp_schema), "count": len(comp_schema)})

    advantages = sorted(tgg_all - all_comp_schema)
    gaps = sorted(all_comp_schema - tgg_all)
    avg_comp = sum(r["count"] for r in comp_results) / max(len(comp_results), 1)

    issues = []
    signals = []
    score = 0

    if len(tgg_all) >= avg_comp * 1.2:
        score += 20
        signals.append(f"TGG leads on schema breadth ({len(tgg_all)} vs avg {avg_comp:.0f})")
    elif len(tgg_all) >= avg_comp:
        score += 12
    else:
        issues.append(f"TGG has fewer schema types than avg competitor ({len(tgg_all)} vs {avg_comp:.0f})")

    score += max(0, 15 - len(gaps) * 3)
    for g_item in gaps[:3]:
        issues.append(f"Competitors have {g_item} schema — TGG doesn't")

    if advantages:
        score += min(len(advantages) * 2, 10)
        signals.append(f"TGG-unique schema: {', '.join(advantages[:4])}")

    pct = round(min(score, 45) / 45 * 100)
    return {
        "score": min(score, 45), "maxScore": 45, "percentage": pct, "grade": grade(pct),
        "tgg_schema_types": sorted(tgg_all),
        "tgg_schema_count": len(tgg_all),
        "competitors": comp_results,
        "tgg_advantages": advantages,
        "tgg_gaps": gaps,
        "signals": signals,
        "errors": [{"issue": i} for i in issues],
        "summary": f"TGG: {len(tgg_all)} schema types | {len(gaps)} gaps vs competitors",
    }


# ── Report builder ─────────────────────────────────────────────────────────────

def build_summary(checks: dict, label: str, snapshot_dir: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total_score = sum(c.get("score", 0) for c in checks.values() if isinstance(c, dict))
    total_max = sum(c.get("maxScore", 0) for c in checks.values() if isinstance(c, dict))
    pct = round(total_score / total_max * 100) if total_max else 0
    g = grade(pct)

    lines = [
        f"# AEO Ecommerce Audit — {label}\n",
        f"**Snapshot directory:** `{snapshot_dir}` | {ts}\n",
        f"## {GRADE_EMOJI.get(g, '❓')} Grade {g} &nbsp; {total_score}/{total_max} ({pct}%)\n",
        "## Check Results\n",
        "| | Check | Score | % | Summary |",
        "|--|-------|------:|--:|---------|",
    ]

    check_labels = {
        "schema":            ("Schema / Structured Data",      30),
        "schema_validity":   ("Schema Validity",               15),
        "render_diff":       ("Render Diff (JS dependency)",   20),
        "user_agents":       ("User Agent Behaviour",          20),
        "hidden_content":    ("Hidden Content",                20),
        "ai_signals":        ("AI Content Signals",            10),
        "dom_structure":     ("DOM Structure & Rendering",     25),
        "robots_content":    ("Robots.txt & llms.txt Rules",   50),
        "sitemap_coverage":  ("Sitemap Coverage",              40),
        "competitor_schema": ("Competitor Schema Comparison",  45),
    }

    for key, (name, weight) in check_labels.items():
        c = checks.get(key, {})
        if "error" in c:
            lines.append(f"| ✗ | {name} | — | — | {c['error'][:60]} |")
            continue
        c_pct = c.get("percentage", 0)
        icon = "✓" if c_pct >= 75 else "◑" if c_pct >= 50 else "✗"
        lines.append(
            f"| {icon} | {name} | {c.get('score', 0)}/{c.get('maxScore', 0)} "
            f"| {c_pct}% | {c.get('summary', '')} |"
        )

    # Errors section
    all_errors = []
    for key, (name, _) in check_labels.items():
        for e in checks.get(key, {}).get("errors", []):
            issue = e.get("issue") or e.get("error") or ""
            identifier = e.get("url") or e.get("file") or ""
            if issue:
                all_errors.append((name, identifier, issue))

    if all_errors:
        lines.append("\n## Issues Found\n")
        for check_name, identifier, issue in all_errors[:20]:
            lines.append(f"- **[{check_name}]** `{identifier}` — {issue}")

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
    path = f"seo/outputs/aeo/ecommerce-latest-{slug}.json"
    b64 = base64.b64encode(json.dumps(data, indent=2).encode()).decode()
    api = "https://api.github.com"
    hdrs = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=hdrs, timeout=30)
    sha = existing.json().get("sha") if existing.status_code == 200 else None
    payload = {"message": f"Ecommerce AEO audit ({label}) run #{run_number}", "content": b64, "branch": ref}
    if sha:
        payload["sha"] = sha
    resp = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=hdrs, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"Committed to repo: {path}")
    else:
        print(f"Warning: could not commit ({resp.status_code})", file=sys.stderr)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    snapshot_dir_str = os.getenv("SNAPSHOT_DIR", "").strip()
    if not snapshot_dir_str:
        print(
            "ERROR: SNAPSHOT_DIR not set.\n"
            "Example: SNAPSHOT_DIR=site-snapshots/thegoodguys.com.au python run_ecommerce_aeo.py",
            file=sys.stderr,
        )
        sys.exit(1)

    snapshot_dir = Path(snapshot_dir_str)
    if not snapshot_dir.exists():
        print(f"ERROR: Snapshot directory not found: {snapshot_dir}", file=sys.stderr)
        sys.exit(1)

    label = os.getenv("AEO_LABEL", snapshot_dir.name)
    html_files = sorted(snapshot_dir.glob("*.html"))
    print(f"Ecommerce AEO audit: {snapshot_dir} ({len(html_files)} snapshots)")

    # Derive live URLs from snapshot filenames for checks that need HTTP
    live_urls_raw = os.getenv("LIVE_URLS", "").strip()
    if live_urls_raw:
        try:
            live_urls = json.loads(live_urls_raw)
        except json.JSONDecodeError:
            live_urls = [u.strip() for u in live_urls_raw.splitlines() if u.strip()]
    else:
        # Default: diverse page types — home, category, sub-category, buying guide
        # Buying guides are on a stricter Cloudflare policy; include them to surface blocks.
        domain_hint = snapshot_dir.name  # e.g. "thegoodguys.com.au"
        default_live = [
            f"https://www.{domain_hint}",
            f"https://www.{domain_hint}/televisions",
            f"https://www.{domain_hint}/televisions/smart-tvs",
            f"https://www.{domain_hint}/buying-guide/best-tvs",
        ]
        live_urls = default_live

    # Derive base URL and competitor list from env
    base_url = os.getenv("BASE_URL", f"https://www.{snapshot_dir.name}")
    competitor_urls_raw = os.getenv("COMPETITOR_URLS", "").strip()
    competitor_urls = json.loads(competitor_urls_raw) if competitor_urls_raw else None

    default_checks = "schema,schema_validity,render_diff,user_agents,hidden_content,ai_signals,dom_structure,robots_content,sitemap_coverage,competitor_schema"
    checks_to_run = set((os.getenv("AEO_CHECKS") or default_checks).split(","))
    checks_to_run = {c.strip() for c in checks_to_run}

    checks = {}
    total_checks = len(checks_to_run)
    step = 0

    def run_check(key: str, label: str, fn):
        nonlocal step
        step += 1
        if key not in checks_to_run:
            return
        print(f"  [{step}/{total_checks}] {label}...")
        checks[key] = fn()
        c = checks[key]
        print(f"        {GRADE_EMOJI.get(c.get('grade','?'),'?')} {c.get('grade','?')} ({c.get('percentage',0)}%) — {c.get('summary','')}")

    run_check("schema",           "Schema / structured data",           lambda: check_schema(snapshot_dir))
    run_check("schema_validity",  "Schema validity",                    lambda: check_schema_validity(snapshot_dir))
    run_check("render_diff",      "Render diff (httpx vs Playwright)",  lambda: check_render_diff(snapshot_dir, live_urls[:5]))
    run_check("user_agents",      "User agent behaviour",               lambda: check_user_agents(live_urls))
    run_check("hidden_content",   "Hidden content",                     lambda: check_hidden_content(snapshot_dir))
    run_check("ai_signals",       "AI content signals",                 lambda: check_ai_signals(snapshot_dir))
    run_check("dom_structure",    "DOM structure & rendering",          lambda: check_dom_structure(snapshot_dir))
    run_check("robots_content",   "Robots.txt & llms.txt rules",        lambda: check_robots_content(base_url))
    run_check("sitemap_coverage", "Sitemap coverage",                   lambda: check_sitemap_coverage(base_url))
    run_check("competitor_schema","Competitor schema comparison",       lambda: check_competitor_schema(snapshot_dir, competitor_urls))

    # Totals
    total_score = sum(c.get("score", 0) for c in checks.values() if isinstance(c, dict))
    total_max = sum(c.get("maxScore", 0) for c in checks.values() if isinstance(c, dict))
    pct = round(total_score / total_max * 100) if total_max else 0
    g = grade(pct)
    print(f"\nEcommerce AEO: {GRADE_EMOJI.get(g,'?')} Grade {g} ({pct}%) — {total_score}/{total_max}")

    # Save outputs
    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    slug = re.sub(r"[^a-z0-9-]", "-", label.lower())
    out_file = out_dir / f"ecommerce-aeo-{slug}-{ts}.json"
    payload = {
        "label": label,
        "dir": str(snapshot_dir),
        "grade": g,
        "score": total_score,
        "maxScore": total_max,
        "percentage": pct,
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
