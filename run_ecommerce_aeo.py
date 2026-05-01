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
# Note: faq_block is now detected via BS4 in check_ai_signals to avoid backtracking
AI_SIGNAL_PATTERNS = {
    "direct_answer_paragraph": re.compile(
        r"<p[^>]*>[^<]{80,}(?:is|are|means|refers to|defined as)[^<]{20,}</p>",
        re.IGNORECASE,
    ),
    "numbered_list": re.compile(r"<ol[^>]*>.*?</ol>", re.IGNORECASE | re.DOTALL),
    "comparison_table": re.compile(
        r"<table[^>]*>(?:(?!<table).){0,2000}?(?:vs\.?|versus|compare|difference)[^<]*?</table>",
        re.IGNORECASE | re.DOTALL,
    ),
    "definition_heading": re.compile(
        r"<h[23][^>]*>(?:What is|What are|How to|Why)[^<]{5,50}</h[23]>",
        re.IGNORECASE,
    ),
}

GRADE_EMOJI = {"A": "🟢", "B": "🟢", "C": "🟡", "D": "🟠", "F": "🔴"}


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
    if any(k in name for k in ("--", "product", "sku", "/p/")):
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
        pct_accessible = round(ratio * 100)
        diff_words = rendered_words - raw_words

        # Score: 20pts if >80% accessible, partial for 50-80%, 0 for <50%
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
            "hidden_words": max(diff_words, 0),
            "score": page_score,
            "maxScore": 20,
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

        blocked = [k for k, v in ua_results.items() if not v.get("allowed")]
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
            classes = " ".join(el.get("class", []))

            is_hidden = (
                "display:none" in style.replace(" ", "")
                or "display: none" in style
                or "visibility:hidden" in style.replace(" ", "")
                or aria_hidden == "true"
                or hidden_attr
                or any(c in classes for c in ["hidden", "d-none", "hide", "collapsed", "is-hidden"])
            )

            if is_hidden:
                hidden_el_set.add(id(el))
                text = el.get_text(separator=" ", strip=True)
                words = len(text.split())
                if words > 20:
                    hidden_words += words
                    hidden_elements.append({
                        "tag": el.name,
                        "class": classes[:60],
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

        # FAQ block detection via BS4 (replaces catastrophic-backtracking regex)
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
        "schema":        ("Schema / Structured Data", 30),
        "render_diff":   ("Render Diff (JS dependency)", 20),
        "user_agents":   ("User Agent Behaviour", 20),
        "hidden_content":("Hidden Content", 20),
        "ai_signals":    ("AI Content Signals", 10),
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
    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=hdrs)
    sha = existing.json().get("sha") if existing.status_code == 200 else None
    payload = {"message": f"Ecommerce AEO audit ({label}) run #{run_number}", "content": b64, "branch": ref}
    if sha:
        payload["sha"] = sha
    resp = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=hdrs, json=payload)
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
        # Default: use first 3 snapshots for live checks (keeps runtime short)
        domain_hint = snapshot_dir.name  # e.g. "thegoodguys.com.au"
        default_live = [
            f"https://www.{domain_hint}",
            f"https://www.{domain_hint}/televisions",
            f"https://www.{domain_hint}/air-conditioners",
        ]
        live_urls = default_live

    checks_to_run = (os.getenv("AEO_CHECKS") or "schema,render_diff,user_agents,hidden_content,ai_signals").split(",")
    checks_to_run = [c.strip() for c in checks_to_run]

    checks = {}

    if "schema" in checks_to_run:
        print("  [1/5] Schema / structured data...")
        checks["schema"] = check_schema(snapshot_dir)
        c = checks["schema"]
        print(f"        {GRADE_EMOJI.get(c.get('grade','?'),'?')} {c.get('grade','?')} ({c.get('percentage',0)}%) — {c.get('summary','')}")

    if "render_diff" in checks_to_run:
        print("  [2/5] Render diff (httpx vs Playwright snapshot)...")
        checks["render_diff"] = check_render_diff(snapshot_dir, live_urls[:5])
        c = checks["render_diff"]
        print(f"        {GRADE_EMOJI.get(c.get('grade','?'),'?')} {c.get('grade','?')} ({c.get('percentage',0)}%) — {c.get('summary','')}")

    if "user_agents" in checks_to_run:
        print("  [3/5] User agent behaviour...")
        checks["user_agents"] = check_user_agents(live_urls[:3])
        c = checks["user_agents"]
        print(f"        {GRADE_EMOJI.get(c.get('grade','?'),'?')} {c.get('grade','?')} ({c.get('percentage',0)}%) — {c.get('summary','')}")

    if "hidden_content" in checks_to_run:
        print("  [4/5] Hidden content analysis...")
        checks["hidden_content"] = check_hidden_content(snapshot_dir)
        c = checks["hidden_content"]
        print(f"        {GRADE_EMOJI.get(c.get('grade','?'),'?')} {c.get('grade','?')} ({c.get('percentage',0)}%) — {c.get('summary','')}")

    if "ai_signals" in checks_to_run:
        print("  [5/5] AI content signals...")
        checks["ai_signals"] = check_ai_signals(snapshot_dir)
        c = checks["ai_signals"]
        print(f"        {GRADE_EMOJI.get(c.get('grade','?'),'?')} {c.get('grade','?')} ({c.get('percentage',0)}%) — {c.get('summary','')}")

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
