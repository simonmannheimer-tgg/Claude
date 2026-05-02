"""
AEO Crawl — Ecommerce AI Discoverability Audit.

Screaming Frog-style per-URL signal audit for AI search engine visibility.
No external CLI tools — pure Python crawl using httpx + BeautifulSoup.

Checks per URL
──────────────
Domain-level (fetched once per hostname, score applied to every page):
  robots_ai   30 pts  Which AI bots are explicitly allowed in robots.txt?
                      GPTBot, ClaudeBot, PerplexityBot, Google-Extended,
                      Amazonbot, Bingbot — 5 pts each if allowed/unblocked
  llms_txt    20 pts  /llms.txt exists (10) + has sections (5) + ≥100 words (5)

Page-level (per URL):
  http_access 10 pts  HTTP 200 for normal UA (5) + GPTBot UA (5)
  meta_tags   20 pts  title 30-70 chars (5), description 100-160 chars (5),
                      og:type present (5), canonical self-referential (5)
  headings    20 pts  H1 present (5), single H1 (5), H2 present (5),
                      no H3-without-H2 skip (5)
  schema_type 20 pts  JSON-LD block exists (5), expected type for page type (10),
                      multiple types (5)
  content     20 pts  ≥300 words (5), FAQ/Q&A patterns (5), spec/list signals (5),
                      number/spec density (5)
  js_depend   20 pts  % of content accessible without JS — uses Playwright snapshot
                      if present: ≥80% (20), 50–79% (10), <50% (0)

Max per URL: 160 pts → letter grade A–F.

Usage:
    python run_aeo_crawl.py
    python run_aeo_crawl.py --snapshot-dir site-snapshots/thegoodguys.com.au
    AEO_URLS='[{"url":"...","label":"..."}]' python run_aeo_crawl.py
"""

import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import httpx
from bs4 import BeautifulSoup

CF_CHALLENGE_MARKERS = (
    "<title>Just a moment...</title>",
    "cf-browser-verification",
    "challenge-running",
    "Checking if the site connection is secure",
)

def _is_cf_blocked(html: str) -> bool:
    return any(m in html for m in CF_CHALLENGE_MARKERS)

def _find_snapshot(url: str, snapshot_dir) -> "Path | None":
    if not snapshot_dir:
        return None
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    fname = ("index" if not path else re.sub(r"[^a-zA-Z0-9_-]", "-", path.replace("/", "--"))) + ".html"
    candidate = snapshot_dir / fname
    return candidate if candidate.exists() else None

# ── Default URL set ────────────────────────────────────────────────────────────
# Home URLs run both domain-level + page-level checks.
# All other page types run page-level only (domain results are shared).
_PAGE = "content"   # shorthand used in run loop

_PAGE_CHECKS = "content-structure,token-budget,meta-tags"

DEFAULT_URLS = [
    # ── TGG — one URL per core page type ────────────────────────────────────────
    {"url": "https://www.thegoodguys.com.au",                                                                          "label": "TGG · Home",         "scope": "domain+page"},
    {"url": "https://www.thegoodguys.com.au/televisions",                                                              "label": "TGG · Category",     "scope": "page"},
    {"url": "https://www.thegoodguys.com.au/televisions/smart-tvs",                                                    "label": "TGG · Sub-category", "scope": "page"},
    {"url": "https://www.thegoodguys.com.au/samsung-65-inches-qn85f-neo-qled-4k-mini-led-smart-ai-tv-2025-qa65qn85fawxxy", "label": "TGG · Product",      "scope": "page"},
    {"url": "https://www.thegoodguys.com.au/buying-guide/television-buying-guide",                                     "label": "TGG · Buying Guide", "scope": "page"},
    {"url": "https://www.thegoodguys.com.au/samsung",                                                                  "label": "TGG · Brand Hub",    "scope": "page"},
    {"url": "https://www.thegoodguys.com.au/whats-new/unboxing-the-lg-tv-range-2025",                                  "label": "TGG · Blog Article", "scope": "page"},
    # ── JB Hi-Fi ────────────────────────────────────────────────────────────────
    {"url": "https://www.jbhifi.com.au",                                                    "label": "JB Hi-Fi · Home",          "scope": "domain+page"},
    {"url": "https://www.jbhifi.com.au/collections/tvs",                                    "label": "JB Hi-Fi · Category",      "scope": "page"},
    {"url": "https://www.jbhifi.com.au/products/samsung-65-qn90d-neo-qled-4k-smart-tv-2024", "label": "JB Hi-Fi · Product",      "scope": "page"},
    {"url": "https://www.jbhifi.com.au/pages/samsung",                                      "label": "JB Hi-Fi · Brand Hub",     "scope": "page"},
    {"url": "https://www.jbhifi.com.au/pages/tv-buying-guide",                              "label": "JB Hi-Fi · Buying Guide",  "scope": "page"},
    # ── Harvey Norman ───────────────────────────────────────────────────────────
    {"url": "https://www.harveynorman.com.au",                                                                "label": "Harvey Norman · Home",          "scope": "domain+page"},
    {"url": "https://www.harveynorman.com.au/tv-blu-ray-home-theatre/tvs-by-screen-size/all-tvs",             "label": "Harvey Norman · Category",      "scope": "page"},
    {"url": "https://www.harveynorman.com.au/hisense-65-inch-q6nau-4k-qled-smart-tv.html",                    "label": "Harvey Norman · Product",       "scope": "page"},
    {"url": "https://www.harveynorman.com.au/tv-blu-ray-home-theatre/tvs-by-brand/samsung-tvs",               "label": "Harvey Norman · Brand Page",    "scope": "page"},
    {"url": "https://www.harveynorman.com.au/buying-guides/television-buying-guide",                          "label": "Harvey Norman · Buying Guide",  "scope": "page"},
    # ── Appliances Online ───────────────────────────────────────────────────────
    {"url": "https://www.appliancesonline.com.au",                                                                               "label": "Appliances Online · Home",      "scope": "domain+page"},
    {"url": "https://www.appliancesonline.com.au/category/refrigeration/fridges/",                                                "label": "Appliances Online · Category",  "scope": "page"},
    {"url": "https://www.appliancesonline.com.au/product/westinghouse-easycare-9kg-front-load-washing-machine-wwf9024m5sa/",     "label": "Appliances Online · Product",   "scope": "page"},
    {"url": "https://www.appliancesonline.com.au/brand/samsung/",                                                                 "label": "Appliances Online · Brand Hub", "scope": "page"},
    {"url": "https://www.appliancesonline.com.au/article/refrigerator-size-guide/",                                              "label": "Appliances Online · Guide",     "scope": "page"},
]

# ── AI bots to check in robots.txt ────────────────────────────────────────────
AI_BOTS = [
    ("GPTBot",          "GPTBot/1.2"),
    ("ClaudeBot",       "ClaudeBot/1.0"),
    ("PerplexityBot",   "PerplexityBot/1.0"),
    ("Google-Extended", "Googlebot/2.1"),
    ("Amazonbot",       "Amazonbot/0.1"),
    ("Bingbot",         "bingbot/2.0"),
]
TIER1_BOTS = {"GPTBot", "ClaudeBot", "PerplexityBot"}

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)
GPGBOT_UA = "Mozilla/5.0 AppleWebKit/537.36 (compatible; GPTBot/1.2; +https://openai.com/gptbot)"

# ── Schema type expected per page type ────────────────────────────────────────
EXPECTED_SCHEMA = {
    "home":        ["WebSite", "Organization", "SiteLinksSearchBox"],
    "category":    ["ItemList", "BreadcrumbList"],
    "subcategory": ["ItemList", "BreadcrumbList"],
    "product":     ["Product", "Offer", "BreadcrumbList"],
    "guide":       ["Article", "FAQPage", "BreadcrumbList"],
    "brand":       ["ItemList", "BreadcrumbList"],
    "editorial":   ["Article", "BreadcrumbList"],
    "hub":         ["CollectionPage", "ItemList"],
}

# ── Page type inference ────────────────────────────────────────────────────────
def infer_page_type(url: str, label: str = "") -> str:
    lbl = label.lower()
    if "product" in lbl:     return "product"
    if "buying guide" in lbl or "guide" in lbl: return "guide"
    if "brand" in lbl:       return "brand"
    if "news hub" in lbl or "editorial" in lbl: return "hub"
    if "sub-category" in lbl: return "subcategory"
    if "category" in lbl:    return "category"
    if "home" in lbl:        return "home"
    # URL pattern fallback
    path = urlparse(url).path.strip("/")
    if not path:             return "home"
    if re.search(r"\.(html|htm)$", url): return "product"
    if "/buying-guide" in url or "/buying-guides" in url: return "guide"
    if "/blogs/" in url:     return "guide"
    if "/brand/" in url or "/pages/" in url: return "brand"
    return "category"


# ── Grade helper ───────────────────────────────────────────────────────────────
def grade(pct: int) -> str:
    if pct >= 80: return "A"
    if pct >= 65: return "B"
    if pct >= 50: return "C"
    if pct >= 35: return "D"
    return "F"


# ── HTTP client ────────────────────────────────────────────────────────────────
def _client(ua: str = BROWSER_UA) -> httpx.Client:
    return httpx.Client(
        headers={"User-Agent": ua},
        follow_redirects=True,
        timeout=12,
    )


# ── Domain-level checks ────────────────────────────────────────────────────────

def check_robots(domain: str) -> dict:
    """
    Parse robots.txt and score AI bot access.
    5 pts per bot that is allowed (or not explicitly blocked).
    Blocked tier-1 bot = critical flag.
    """
    url = f"https://www.{domain}/robots.txt"
    try:
        resp = httpx.get(url, timeout=10, headers={"User-Agent": BROWSER_UA}, follow_redirects=True)
        raw = resp.text
        status = resp.status_code
    except Exception as e:
        return {"score": 0, "max": 30, "error": str(e)[:80], "bots": {}, "status": None}

    if status != 200:
        return {"score": 0, "max": 30, "error": f"HTTP {status}", "bots": {}, "status": status}

    # Use stdlib RobotFileParser for accuracy
    parser = RobotFileParser()
    parser.set_url(url)
    try:
        parser.read()
    except Exception:
        pass

    bot_results = {}
    score = 0
    for bot_name, bot_ua in AI_BOTS:
        # Check if this UA is mentioned explicitly by scanning raw text (RobotFileParser
        # only checks can_fetch which defaults to allow-all when UA not mentioned)
        ua_pattern = re.compile(r"User-agent:\s*" + re.escape(bot_name.split("/")[0]), re.I)
        mentioned = bool(ua_pattern.search(raw))

        can_fetch = parser.can_fetch(bot_ua, f"https://www.{domain}/")
        if not mentioned:
            status_str = "not-mentioned"
            pts = 3  # ambiguous — not explicitly allowed or blocked
        elif can_fetch:
            status_str = "allowed"
            pts = 5
        else:
            status_str = "blocked"
            pts = 0

        bot_results[bot_name] = {"status": status_str, "mentioned": mentioned, "pts": pts}
        score += pts

    tier1_blocked = [b for b in TIER1_BOTS if bot_results.get(b, {}).get("status") == "blocked"]

    return {
        "score": score,
        "max": 30,
        "percentage": round(score / 30 * 100),
        "bots": bot_results,
        "tier1_blocked": tier1_blocked,
        "http_status": resp.status_code,
        "issue": f"Tier-1 AI bots blocked: {', '.join(tier1_blocked)}" if tier1_blocked else None,
    }


def check_llms_txt(domain: str) -> dict:
    """
    Fetch /llms.txt. Score on presence, section structure, and content density.
    """
    url = f"https://www.{domain}/llms.txt"
    try:
        resp = httpx.get(url, timeout=10, headers={"User-Agent": BROWSER_UA}, follow_redirects=True)
    except Exception as e:
        return {"score": 0, "max": 20, "exists": False, "error": str(e)[:80]}

    if resp.status_code != 200:
        return {"score": 0, "max": 20, "exists": False, "http_status": resp.status_code}

    text = resp.text.strip()
    word_count = len(text.split())
    sections = len(re.findall(r"^#{1,3} .+", text, re.MULTILINE))
    has_products = bool(re.search(r"product|categor|buy|shop|price|offer", text, re.I))

    score = 10  # exists
    if sections >= 2:  score += 5
    if word_count >= 100: score += 3
    if word_count >= 300: score += 2
    # No section deduction — llms.txt is still very new; existence alone is signal

    return {
        "score": score,
        "max": 20,
        "percentage": round(score / 20 * 100),
        "exists": True,
        "word_count": word_count,
        "sections": sections,
        "has_products": has_products,
        "issue": "llms.txt exists but has no sections — add ## headings for each content type" if sections < 2 else None,
    }


# ── Page-level checks ─────────────────────────────────────────────────────────

def check_http_access(url: str) -> dict:
    """
    Confirm page returns 200 for normal UA, then test GPTBot UA.
    """
    results = {}
    score = 0
    for label, ua in [("browser", BROWSER_UA), ("GPTBot", GPGBOT_UA)]:
        try:
            r = httpx.get(url, headers={"User-Agent": ua}, follow_redirects=True, timeout=10)
            results[label] = r.status_code
            if r.status_code == 200:
                score += 5
        except Exception as e:
            results[label] = f"error: {e}"

    return {
        "score": score,
        "max": 10,
        "percentage": round(score / 10 * 100),
        "statuses": results,
        "issue": "GPTBot receives non-200 response" if results.get("GPTBot") != 200 else None,
    }


def check_meta_tags(soup: BeautifulSoup, url: str, page_type: str) -> dict:
    """
    Check title, meta description, og:type, and canonical.
    """
    score = 0
    issues = []
    details = {}

    # Title
    title_el = soup.find("title")
    title = title_el.get_text(strip=True) if title_el else ""
    t_len = len(title)
    if title and 20 <= t_len <= 80:
        score += 5
    elif title:
        score += 2
        issues.append(f"Title length {t_len} — target 30-70 chars")
    else:
        issues.append("Missing title tag")
    details["title"] = {"text": title[:80], "length": t_len}

    # Meta description
    desc_el = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    desc = desc_el.get("content", "").strip() if desc_el else ""
    d_len = len(desc)
    if desc and 100 <= d_len <= 165:
        score += 5
    elif desc:
        score += 2
        issues.append(f"Description length {d_len} — target 100-160 chars")
    else:
        issues.append("Missing meta description")
    details["description"] = {"length": d_len}

    # og:type
    og_type_el = soup.find("meta", property="og:type")
    og_type = og_type_el.get("content", "").strip() if og_type_el else ""
    expected_og = {
        "product": "og:product", "guide": "article", "home": "website",
    }.get(page_type, "website")
    if og_type:
        score += 5
    else:
        issues.append("Missing og:type")
    details["og_type"] = og_type

    # Canonical
    canon_el = soup.find("link", rel="canonical")
    canon = canon_el.get("href", "").strip() if canon_el else ""
    parsed_url = urlparse(url)
    parsed_canon = urlparse(canon) if canon else None
    is_self = parsed_canon and parsed_canon.path == parsed_url.path if parsed_canon else False
    if canon and is_self:
        score += 5
    elif canon:
        score += 2
        issues.append("Canonical points to different URL")
    else:
        issues.append("Missing canonical")
    details["canonical"] = canon[:80] if canon else None

    return {
        "score": score,
        "max": 20,
        "percentage": round(score / 20 * 100),
        "details": details,
        "issues": issues,
        "issue": issues[0] if issues else None,
    }


def check_headings(soup: BeautifulSoup) -> dict:
    """
    H1 presence, single H1, H2 presence, no hierarchy skip (H3 without H2).
    """
    score = 0
    issues = []

    h1s = soup.find_all("h1")
    h2s = soup.find_all("h2")
    h3s = soup.find_all("h3")

    if h1s:
        score += 5
    else:
        issues.append("No H1 found")

    if len(h1s) == 1:
        score += 5
    elif len(h1s) > 1:
        issues.append(f"Multiple H1 tags ({len(h1s)})")
    else:
        pass  # already flagged above

    if h2s:
        score += 5
    else:
        issues.append("No H2 found")

    # H3 without H2 = hierarchy skip
    if h3s and not h2s:
        issues.append("H3 present but no H2 — heading hierarchy skip")
    else:
        score += 5

    return {
        "score": score,
        "max": 20,
        "percentage": round(score / 20 * 100),
        "h1_count": len(h1s),
        "h1_text": h1s[0].get_text(strip=True)[:80] if h1s else None,
        "h2_count": len(h2s),
        "h3_count": len(h3s),
        "issues": issues,
        "issue": issues[0] if issues else None,
    }


def check_schema_type(raw_html: str, page_type: str) -> dict:
    """
    Scan raw (non-JS) HTML for JSON-LD blocks and check expected schema types.
    Raw HTML = what AI bots see without executing JavaScript.
    """
    score = 0
    issues = []

    ld_blocks = re.findall(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        raw_html, re.DOTALL | re.IGNORECASE
    )

    if ld_blocks:
        score += 5
    else:
        issues.append("No JSON-LD found in raw HTML — schema may be JS-injected (invisible to AI bots)")
        return {"score": 0, "max": 20, "percentage": 0, "found_types": [], "issues": issues, "issue": issues[0]}

    found_types = []
    for block in ld_blocks:
        try:
            data = json.loads(block.strip())
            items = data if isinstance(data, list) else [data]
            for item in items:
                t = item.get("@type", "")
                if isinstance(t, list):
                    found_types.extend(t)
                elif t:
                    found_types.append(t)
        except (json.JSONDecodeError, TypeError):
            pass

    expected = EXPECTED_SCHEMA.get(page_type, [])
    matched = [t for t in expected if any(t.lower() in f.lower() for f in found_types)]

    if matched:
        score += min(10, len(matched) * 5)
    else:
        issues.append(f"Expected schema for {page_type}: {', '.join(expected[:2])} — none found in raw HTML")

    if len(found_types) >= 2:
        score += 5

    missing = [t for t in expected[:2] if t not in found_types]
    if missing:
        issues.append(f"Missing expected schema: {', '.join(missing)}")

    return {
        "score": min(score, 20),
        "max": 20,
        "percentage": round(min(score, 20) / 20 * 100),
        "found_types": found_types,
        "expected_types": expected,
        "missing_types": missing,
        "issues": issues,
        "issue": issues[0] if issues else None,
    }


def check_content(soup: BeautifulSoup) -> dict:
    """
    Word count, FAQ/Q&A signals, spec lists, number/spec density.
    Strips nav/header/footer before counting.
    """
    for tag in soup.find_all(["nav", "header", "footer", "script", "style", "noscript"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body
    text = (main or soup).get_text(separator=" ", strip=True) if main else ""
    words = text.split()
    word_count = len(words)

    score = 0
    issues = []

    # Word count
    if word_count >= 500:
        score += 5
    elif word_count >= 300:
        score += 3
    else:
        issues.append(f"Low word count ({word_count}) — AI needs content to cite")

    # FAQ / Q&A signals
    faq_patterns = (
        bool(re.search(r"\b(faq|frequently asked|common questions?)\b", text, re.I)) or
        bool(re.search(r"^\s*(what|how|why|when|which|can|does|is|are)\b[^?]{8,80}\?", text, re.I | re.MULTILINE))
    )
    if faq_patterns:
        score += 5
    else:
        issues.append("No FAQ/Q&A patterns — add question-based headings or an FAQ section")

    # Spec/feature lists (numbers + units, bullet lists)
    spec_pattern = re.search(
        r"\b\d+(?:[.,]\d+)?\s*(?:cm|mm|m|kg|g|inch|hz|w|kw|kwh|l|ml|gb|tb|mb|°|%)\b",
        text, re.I
    )
    list_elements = (soup.find_all("ul") or []) + (soup.find_all("ol") or [])
    if spec_pattern or len(list_elements) >= 2:
        score += 5
    else:
        issues.append("No spec/list signals — add product specifications or feature lists")

    # Number/spec density
    nums = re.findall(r"\b\d+(?:[.,]\d+)?\b", text)
    num_density = len(nums) / max(word_count, 1) * 1000
    if num_density >= 15:
        score += 5
    elif num_density >= 8:
        score += 3
    else:
        issues.append(f"Low spec density ({num_density:.0f}/1000 words) — add prices, measurements, specs")

    return {
        "score": score,
        "max": 20,
        "percentage": round(score / 20 * 100),
        "word_count": word_count,
        "has_faq": faq_patterns,
        "has_specs": bool(spec_pattern),
        "num_density": round(num_density, 1),
        "list_count": len(list_elements),
        "issues": issues,
        "issue": issues[0] if issues else None,
    }


def check_js_dependency(url: str, raw_html: str, snapshot_dir: Path | None) -> dict:
    """
    Compare content accessible in raw HTML (what AI bots see via httpx)
    vs Playwright-rendered snapshot (full DOM).
    Looks for an existing snapshot matching the URL path.
    """
    raw_soup = BeautifulSoup(raw_html, "html.parser")
    for tag in raw_soup.find_all(["nav", "header", "footer", "script", "style", "noscript"]):
        tag.decompose()
    main = raw_soup.find("main") or raw_soup.find("article") or raw_soup.body
    raw_words = len((main or raw_soup).get_text(separator=" ", strip=True).split())

    snapshot_path = None
    if snapshot_dir:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        fname = ("index" if not path else re.sub(r"[^a-zA-Z0-9_-]", "-", path.replace("/", "--"))) + ".html"
        candidate = snapshot_dir / fname
        if candidate.exists():
            snapshot_path = candidate

    if not snapshot_path:
        # No snapshot — use raw word count only, score as unknown
        return {
            "score": None,
            "max": 20,
            "raw_words": raw_words,
            "rendered_words": None,
            "pct_accessible": None,
            "note": "No Playwright snapshot — run Phase 2 crawl to get JS-rendered comparison",
        }

    rend_soup = BeautifulSoup(snapshot_path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    for tag in rend_soup.find_all(["nav", "header", "footer", "script", "style", "noscript"]):
        tag.decompose()
    main_r = rend_soup.find("main") or rend_soup.find("article") or rend_soup.body
    rendered_words = len((main_r or rend_soup).get_text(separator=" ", strip=True).split())

    ratio = raw_words / rendered_words if rendered_words else 0
    pct = min(round(ratio * 100), 100)
    ssr = raw_words > rendered_words

    if pct >= 80:
        score = 20
        issue = None
    elif pct >= 50:
        score = 10
        issue = f"Only {pct}% of content accessible without JS — bots miss {rendered_words - raw_words:,} words"
    else:
        score = 0
        issue = f"Critical JS dependency — only {pct}% accessible without JS ({raw_words:,} raw vs {rendered_words:,} rendered)"

    return {
        "score": score,
        "max": 20,
        "percentage": round(score / 20 * 100),
        "raw_words": raw_words,
        "rendered_words": rendered_words,
        "pct_accessible": pct,
        "ssr_detected": ssr,
        "issue": issue,
    }


# ── Per-URL audit ──────────────────────────────────────────────────────────────

def audit_url(entry: dict, domain_cache: dict, snapshot_dir: Path | None) -> dict:
    url    = entry["url"]
    label  = entry.get("label", url)
    scope  = entry.get("scope", "page")
    domain = urlparse(url).hostname or ""
    domain_key = re.sub(r"^www\.", "", domain)
    page_type = infer_page_type(url, label)

    print(f"  [{label}] {url}")

    # Fetch raw HTML once (used by multiple checks)
    raw_html = ""
    raw_soup = None
    cf_blocked = False
    try:
        resp = httpx.get(url, headers={"User-Agent": BROWSER_UA}, follow_redirects=True, timeout=12)
        raw_html = resp.text
        raw_soup = BeautifulSoup(raw_html, "html.parser")
        cf_blocked = _is_cf_blocked(raw_html)
    except Exception as e:
        print(f"    ✗ fetch error: {e}")

    # If CF-blocked, fall back to Playwright snapshot for content analysis.
    # http_access check still uses httpx (correct — reflects real bot experience).
    analysis_html = raw_html
    analysis_soup = raw_soup
    if cf_blocked:
        snap = _find_snapshot(url, snapshot_dir)
        if snap:
            analysis_html = snap.read_text(encoding="utf-8", errors="ignore")
            analysis_soup = BeautifulSoup(analysis_html, "html.parser")
            print(f"    CF blocked — using Playwright snapshot for content analysis")
        else:
            print(f"    CF blocked — no snapshot available (run crawl_site_snapshot.py first)")

    checks = {}
    total_score = 0
    max_score = 0

    # Domain-level checks (run once per domain, cached)
    if domain_key not in domain_cache:
        domain_cache[domain_key] = {
            "robots_ai":  check_robots(domain_key),
            "llms_txt":   check_llms_txt(domain_key),
        }

    # Apply domain scores to this URL
    for key in ("robots_ai", "llms_txt"):
        c = domain_cache[domain_key][key]
        checks[key] = c
        if c.get("score") is not None:
            total_score += c["score"]
            max_score   += c["max"]

    # Page-level checks
    # http_access always uses raw httpx (intentional — tests real bot access).
    # All content checks use analysis_html/soup which falls back to Playwright snapshot if CF-blocked.
    if raw_soup or analysis_soup:
        for key, fn in [
            ("http_access",  lambda: check_http_access(url)),
            ("meta_tags",    lambda: check_meta_tags(analysis_soup, url, page_type)),
            ("headings",     lambda: check_headings(analysis_soup)),
            ("schema_type",  lambda: check_schema_type(analysis_html, page_type)),
            ("content",      lambda: check_content(BeautifulSoup(analysis_html, "html.parser"))),
            ("js_depend",    lambda: check_js_dependency(url, raw_html, snapshot_dir)),
        ]:
            result = fn()
            checks[key] = result
            s = result.get("score")
            if s is not None:
                total_score += s
                max_score   += result["max"]
    else:
        checks["fetch_error"] = {"error": "Could not fetch URL", "score": 0, "max": 0}

    pct = round(total_score / max_score * 100) if max_score else 0
    g   = grade(pct)

    issues = [
        {"check": k, "issue": v["issue"]}
        for k, v in checks.items()
        if v.get("issue")
    ]

    print(f"    {'🟢' if g in 'AB' else '🟡' if g == 'C' else '🟠' if g == 'D' else '🔴'} "
          f"Grade {g} ({pct}%) — {len(issues)} issue(s)")

    return {
        "url":        url,
        "label":      label,
        "domain":     domain_key,
        "page_type":  page_type,
        "scope":      scope,
        "score":      total_score,
        "max_score":  max_score,
        "percentage": pct,
        "grade":      g,
        "checks":     checks,
        "issues":     issues,
        "cf_blocked": cf_blocked,
    }


# ── Main ───────────────────────────────────────────────────────────────────────

def push_to_repo(data: list[dict] | str, path_or_label: str, text: bool = False) -> None:
    """
    Push data to the repo via GitHub Contents API.
    text=False (default): data is a list[dict] → serialised as JSON, path derived from label.
    text=True: data is a string (e.g. Markdown), path_or_label is the full repo path.
    """
    import base64
    token = os.getenv("GITHUB_TOKEN")
    repo  = os.getenv("GITHUB_REPOSITORY")
    ref   = os.getenv("GITHUB_REF_NAME")
    run_n = os.getenv("GITHUB_RUN_NUMBER", "?")
    if not (token and repo and ref):
        return

    if text:
        path = path_or_label
        content_bytes = data.encode() if isinstance(data, str) else data
        msg = f"AEO run log run #{run_n}"
    else:
        slug = re.sub(r"[^a-z0-9-]", "-", path_or_label.lower())
        path = f"seo/outputs/aeo/crawl-latest-{slug}.json"
        content_bytes = json.dumps(data, indent=2).encode()
        msg = f"AEO crawl ({path_or_label}) run #{run_n}"

    b64  = base64.b64encode(content_bytes).decode()
    hdrs = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    api = "https://api.github.com"
    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=hdrs, timeout=20)
    sha = existing.json().get("sha") if existing.status_code == 200 else None
    payload = {"message": msg, "content": b64, "branch": ref}
    if sha:
        payload["sha"] = sha
    r = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=hdrs, json=payload, timeout=20)
    if r.status_code in (200, 201):
        print(f"Committed to repo: {path}")
    else:
        print(f"Warning: could not commit {path} ({r.status_code})", file=sys.stderr)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="AEO Crawl — Ecommerce AI discoverability audit")
    parser.add_argument("--snapshot-dir", default="", help="Path to Playwright HTML snapshots for JS dependency check")
    parser.add_argument("--label", default="tgg", help="Label for output files")
    args = parser.parse_args()

    snapshot_dir = Path(args.snapshot_dir) if args.snapshot_dir else None
    if not snapshot_dir:
        # Auto-detect default snapshot dir
        default = Path("site-snapshots/thegoodguys.com.au")
        if default.exists():
            snapshot_dir = default

    urls_raw = os.getenv("AEO_URLS", "").strip()
    if urls_raw:
        try:
            raw = json.loads(urls_raw)
            entries = [{"url": u, "label": u, "scope": "page"} if isinstance(u, str) else u for u in raw]
        except json.JSONDecodeError:
            entries = [{"url": u.strip(), "label": u.strip(), "scope": "page"} for u in urls_raw.splitlines() if u.strip()]
    else:
        entries = DEFAULT_URLS

    label = os.getenv("AEO_LABEL", args.label)
    print(f"AEO Crawl: {len(entries)} URL(s) | label={label}")
    if snapshot_dir:
        print(f"  Snapshot dir: {snapshot_dir}")

    domain_cache: dict = {}
    results = []

    # Run sequentially (httpx is sync; parallelising doesn't help much with network I/O here
    # because Cloudflare rate-limits rapid parallel requests per domain)
    for entry in entries:
        result = audit_url(entry, domain_cache, snapshot_dir)
        results.append(result)

    # Summary
    print(f"\nAEO Crawl complete — {len(results)} URLs")
    by_domain: dict[str, list] = {}
    for r in results:
        by_domain.setdefault(r["domain"], []).append(r)

    for domain, pages in by_domain.items():
        avg = round(sum(p["percentage"] for p in pages) / len(pages))
        g   = grade(avg)
        emoji = "🟢" if g in "AB" else "🟡" if g == "C" else "🟠" if g == "D" else "🔴"
        print(f"  {emoji} {domain:<40} avg {avg}% (Grade {g})  [{len(pages)} pages]")

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    slug = re.sub(r"[^a-z0-9-]", "-", label.lower())
    out_file = out_dir / f"crawl-{slug}-{ts}.json"
    out_file.write_text(json.dumps(results, indent=2))
    print(f"\nSaved {out_file}")

    # Run log (comprehensive Markdown) — written and pushed to repo
    log_file = write_run_log(results, label, out_dir, snapshot_dir)
    push_to_repo(log_file.read_text(), f"seo/outputs/aeo/{log_file.name}", text=True)

    # GitHub Actions step summary
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        _write_summary(results, summary_path, label)

    push_to_repo(results, label)  # JSON crawl data → crawl-latest-{label}.json


def write_run_log(results: list[dict], label: str, out_dir: Path, snapshot_dir: Path | None) -> Path:
    """
    Write a comprehensive Markdown run log to seo/outputs/aeo/run-log-{slug}-{ts}.md.

    Captures: run metadata, tool config, per-URL check detail with scores and issues,
    robots.txt bot access table per domain, and self-review instructions for future
    Claude Code sessions working on this tool.
    """
    ts_utc     = datetime.now(timezone.utc)
    ts_str     = ts_utc.strftime("%Y-%m-%d %H:%M UTC")
    ts_file    = ts_utc.strftime("%Y%m%d-%H%M")
    slug       = re.sub(r"[^a-z0-9-]", "-", label.lower())
    run_number = os.getenv("GITHUB_RUN_NUMBER", "local")
    run_id     = os.getenv("GITHUB_RUN_ID", "local")
    branch     = os.getenv("GITHUB_REF_NAME", "local")
    repo       = os.getenv("GITHUB_REPOSITORY", "simonmannheimer-tgg/Claude")

    by_domain: dict[str, list] = {}
    for r in results:
        by_domain.setdefault(r["domain"], []).append(r)

    check_keys = [
        ("robots_ai", 30), ("llms_txt", 20), ("http_access", 10),
        ("meta_tags", 20), ("headings", 20), ("schema_type", 20),
        ("content", 20), ("js_depend", 20),
    ]

    L = []

    # ── Header ───────────────────────────────────────────────────────────────
    L += [
        f"# AEO Crawl Run Log — {label}\n\n",
        f"**Generated:** {ts_str}  \n",
        f"**Run:** #{run_number} (ID: {run_id})  \n",
        f"**Branch:** `{branch}`  \n",
        f"**Repo:** `{repo}`  \n",
        f"**URLs audited:** {len(results)}  \n",
        f"**Snapshot dir:** `{snapshot_dir or 'none — js_depend unscored'}`  \n\n",
    ]

    # ── Tool config ──────────────────────────────────────────────────────────
    L += [
        "## Tool Config\n\n",
        "| Setting | Value |\n|---|---|\n",
        "| Script | `run_aeo_crawl.py` |\n",
        "| Max score per URL | 160 pts (A≥80%, B≥65%, C≥50%, D≥35%, F<35%) |\n",
        "| Domain checks | `robots_ai` 30 pts, `llms_txt` 20 pts — cached once per hostname |\n",
        "| Page checks | `http_access` 10, `meta_tags` 20, `headings` 20, `schema_type` 20, `content` 20, `js_depend` 20 |\n",
        "| AI bots tested | GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Amazonbot, Bingbot |\n",
        f"| js_depend | {'Playwright snapshots present — scored' if snapshot_dir else 'No snapshots — unscored'} |\n\n",
    ]

    # ── Domain summary ───────────────────────────────────────────────────────
    L += ["## Domain Summary\n\n", "| Domain | Grade | Avg % | Pages | Top failing check |\n", "|---|---|---|---|---|\n"]
    for domain, pages in sorted(by_domain.items()):
        avg = round(sum(p["percentage"] for p in pages) / len(pages))
        g   = grade(avg)
        issue_counts: dict[str, int] = {}
        for p in pages:
            for iss in p.get("issues", []):
                issue_counts[iss["check"]] = issue_counts.get(iss["check"], 0) + 1
        top = max(issue_counts, key=issue_counts.__getitem__) if issue_counts else "—"
        L.append(f"| `{domain}` | **{g}** | {avg}% | {len(pages)} | `{top}` |\n")
    L.append("\n")

    # ── Per-URL check detail ─────────────────────────────────────────────────
    L.append("## Per-URL Check Detail\n\n")
    for r in results:
        g   = r.get("grade", "?")
        pct = r.get("percentage", 0)
        ch  = r.get("checks", {})
        L += [
            f"### {r['label']}\n\n",
            f"`{r['url']}`  \n",
            f"**Grade {g} · {pct}%** &nbsp;·&nbsp; type: `{r['page_type']}` &nbsp;·&nbsp; domain: `{r['domain']}`\n\n",
            "| Check | Score | Max | % | Status | Issue |\n",
            "|---|---|---|---|---|---|\n",
        ]
        for key, mx in check_keys:
            c   = ch.get(key, {})
            s   = c.get("score")
            p   = c.get("percentage", round(s / mx * 100) if s is not None and mx else 0)
            iss = (c.get("issue") or "").replace("|", "\\|")[:90]
            if s is None:
                icon = "–"
            elif s >= mx * 0.8:
                icon = "✅"
            elif s >= mx * 0.5:
                icon = "⚠️"
            else:
                icon = "❌"
            L.append(f"| `{key}` | {s if s is not None else '–'} | {mx} | {p}% | {icon} | {iss} |\n")

        # Extra detail rows
        sc = ch.get("schema_type", {})
        if sc.get("found_types"):
            L.append(f"\n- **Schema found:** `{'`, `'.join(sc['found_types'][:6])}`\n")
        if sc.get("missing_types"):
            L.append(f"- **Schema missing:** `{'`, `'.join(sc['missing_types'])}`\n")
        co = ch.get("content", {})
        if co:
            L.append(
                f"- **Content:** {co.get('word_count', 0):,} words · "
                f"FAQ {'✅' if co.get('has_faq') else '❌'} · "
                f"Specs {'✅' if co.get('has_specs') else '❌'} · "
                f"num density {co.get('num_density', 0)}/1000\n"
            )
        jd = ch.get("js_depend", {})
        if jd.get("rendered_words"):
            L.append(
                f"- **JS dependency:** {jd.get('raw_words', 0):,} raw → "
                f"{jd.get('rendered_words', 0):,} rendered · "
                f"{jd.get('pct_accessible', 0)}% accessible without JS\n"
            )
        L.append("\n")

    # ── TGG issues list ──────────────────────────────────────────────────────
    tgg_issues = [
        (r["label"], i["check"], i["issue"])
        for r in results if "thegoodguys" in r.get("domain", "")
        for i in r.get("issues", [])
    ]
    if tgg_issues:
        L += ["## TGG Issues\n\n", "| Page | Check | Issue |\n", "|---|---|---|\n"]
        for lbl, chk, iss in tgg_issues:
            L.append(f"| {lbl} | `{chk}` | {iss.replace('|', chr(92)+'|')} |\n")
        L.append("\n")

    # ── Robots detail per domain ─────────────────────────────────────────────
    L.append("## robots.txt — AI Bot Access by Domain\n\n")
    seen: set[str] = set()
    for r in results:
        dom = r["domain"]
        if dom in seen:
            continue
        seen.add(dom)
        rb = r.get("checks", {}).get("robots_ai", {})
        if not rb or "bots" not in rb:
            continue
        L += [f"### `{dom}` — {rb.get('score', 0)}/{rb.get('max', 30)} pts\n\n",
              "| Bot | Status | Pts |\n|---|---|---|\n"]
        for bot, info in rb.get("bots", {}).items():
            st  = info.get("status", "?")
            pts = info.get("pts", 0)
            ic  = "✅" if st == "allowed" else "⚠️" if st == "not-mentioned" else "❌"
            L.append(f"| {bot} | {ic} {st} | {pts} |\n")
        if rb.get("tier1_blocked"):
            L.append(f"\n> ⚠️ **Tier-1 bots blocked:** {', '.join(rb['tier1_blocked'])}\n")
        L.append("\n")

    # ── Self-review instructions ──────────────────────────────────────────────
    L += [
        "---\n\n",
        "## Self-Review Instructions\n\n",
        "> This section is for Claude Code. When working on `run_aeo_crawl.py`, "
        "or when Simon asks for a run review, follow these steps:\n\n",
        "1. **Find the latest log** — `glob('seo/outputs/aeo/run-log-*.md')`, sort descending, read the most recent.\n",
        "2. **Domain summary first** — flag any domain with avg < 50% (D/F). That's the priority conversation.\n",
        "3. **robots_ai** — if `tier1_blocked` appears for TGG, that's critical. Draft a robots.txt fix immediately.\n",
        "4. **schema_type = 0** on TGG category or product pages → JSON-LD is JS-injected (AI bots can't see it). "
        "Flag as high severity; recommend adding SSR schema to page templates.\n",
        "5. **js_depend < 50%** on TGG pages → heavily client-rendered. Flag to Simon as AI crawlability risk.\n",
        "6. **llms_txt = 0** → `/llms.txt` missing. Offer to generate it via `generate_recommendations.py`.\n",
        "7. **Competitor gaps** — note any competitor that outscores TGG on `schema_type` or `robots_ai`. Name the domain and delta.\n",
        "8. **Regression check** — if a second log exists, diff the domain averages. Report any drop ≥5 percentage points.\n",
        "9. **Summary format for Simon** — domain avg table + top 3 TGG issues + one concrete next action. Keep it under 200 words.\n\n",
        f"_Log written by `run_aeo_crawl.py` · run #{run_number} · {ts_str}_\n",
    ]

    out_file = out_dir / f"run-log-{slug}-{ts_file}.md"
    out_file.write_text("".join(L), encoding="utf-8")
    print(f"Run log saved: {out_file}")
    return out_file


def _write_summary(results: list[dict], path: str, label: str) -> None:
    g_emoji = {"A": "🟢", "B": "🟢", "C": "🟡", "D": "🟠", "F": "🔴"}
    lines = [f"# AEO Crawl — {label}\n",
             "| Site / Page | Type | Grade | % | robots_ai | llms_txt | meta | headings | schema | content | JS |\n",
             "|---|---|---|---|---|---|---|---|---|---|---|\n"]

    def _bar(c: dict | None) -> str:
        if not c or c.get("score") is None:
            return "–"
        p = c.get("percentage", 0)
        icon = "✅" if p >= 80 else "⚠️" if p >= 50 else "❌"
        return f"{icon} {p}%"

    for r in results:
        ch = r.get("checks", {})
        g  = r.get("grade", "?")
        lines.append(
            f"| [{r['label']}]({r['url']}) | {r['page_type']} "
            f"| {g_emoji.get(g, '?')} {g} | {r['percentage']}% "
            f"| {_bar(ch.get('robots_ai'))} | {_bar(ch.get('llms_txt'))} "
            f"| {_bar(ch.get('meta_tags'))} | {_bar(ch.get('headings'))} "
            f"| {_bar(ch.get('schema_type'))} | {_bar(ch.get('content'))} "
            f"| {_bar(ch.get('js_depend'))} |\n"
        )

    issues = [(r["label"], i["check"], i["issue"]) for r in results for i in r.get("issues", [])]
    if issues:
        lines += ["\n## Issues\n", "| Page | Check | Issue |\n", "|---|---|---|\n"]
        for lbl, chk, issue in issues[:30]:
            lines.append(f"| {lbl} | `{chk}` | {issue} |\n")

    with open(path, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
