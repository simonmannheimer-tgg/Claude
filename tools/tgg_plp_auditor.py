#!/usr/bin/env python3
"""TGG PLP Intro Auditor — self-installing, double-click to run."""

import subprocess, sys, importlib

def _ensure(pkg, import_as=None):
    try:
        importlib.import_module(import_as or pkg)
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "--quiet"])

_ensure("playwright")
_ensure("beautifulsoup4", "bs4")
_ensure("lxml")

# Ensure Chromium browser binary is present
try:
    from playwright.sync_api import sync_playwright as _sp
    with _sp() as _p:
        _p.chromium.launch().close()
except Exception:
    print("Installing Chromium browser (one-time, ~150MB)...")
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])

import re
import json
import csv
import asyncio
from urllib.parse import urlparse
from dataclasses import dataclass, field
from typing import Optional

from playwright.async_api import async_playwright, Page, Browser
from bs4 import BeautifulSoup


# ── CONFIG ────────────────────────────────────────────────────────────────────

CHAR_MIN       = 220
CHAR_MAX       = 250
CHAR_IDEAL_MIN = 225
CHAR_IDEAL_MAX = 235

# Viewports to test — order matters for report readability
VIEWPORTS = [
    {"name": "360px Android",  "width": 360,  "height": 800},
    {"name": "390px iPhone 14","width": 390,  "height": 844},
    {"name": "414px iPhone Plus","width": 414, "height": 896},
    {"name": "768px Tablet",   "width": 768,  "height": 1024},
    {"name": "1280px Desktop", "width": 1280, "height": 800},
]

# Brands recognised as brand slugs in URL path position 0
KNOWN_BRANDS = {
    'lg', 'samsung', 'sony', 'haier', 'hisense', 'tcl', 'bosch', 'miele',
    'fisher-paykel', 'electrolux', 'westinghouse', 'beko', 'breville',
    'delonghi', 'dyson', 'panasonic', 'philips', 'smeg', 'apple', 'google',
    'jbl', 'bose', 'sonos', 'garmin', 'fitbit', 'nespresso', 'gorenje',
    'kelvinator', 'sharp', 'toshiba', 'asus', 'hp', 'lenovo', 'acer',
    'microsoft', 'dell', 'epson', 'brother', 'canon', 'fujifilm', 'nikon',
}

# Hard-banned patterns. Tuples of (regex, note).
# 'save/saving' handled separately (price-context only).
HARD_BANS = [
    (r'\bsale\b',                    "SEM compliance"),
    (r'\bsales\b',                   "SEM compliance"),
    (r'\bdiscount\b',                "SEM compliance"),
    (r'\bexclusive\b',               "legal risk"),
    (r"australia['']s trusted choice", "SEM compliance"),
    (r'\bquality brands\b',          "SEM compliance"),
    (r'get great value\b',           "SEM compliance"),
    (r'perfect for all needs\b',     "too vague"),
    (r'chat to our staff\b',         "SEM compliance"),
    (r'chat to our team\b',          "SEM compliance"),
    (r'\bamazing\b',                 "oversold/generic"),
    (r'\bstunning\b',                "oversold/generic"),
    (r'\bwonderful\b',               "oversold/generic"),
    (r'\bbusy homes\b',              "cliché/AI-sounding"),
    (r'\bhearty meals\b',            "cliché/AI-sounding"),
    (r'\bsleek design\b',            "cliché/AI-sounding"),
]

# Price-framing context for save/saving
SAVE_PRICE_PATTERN = re.compile(
    r'\bsav(?:e|ing|ings)\b.{0,40}(?:money|on\s|with\s|with price beat|price|deal|cost)',
    re.IGNORECASE
)

# Banned on Type B and C pages only
BRAND_PAGE_BANS = [
    (r'\btrusted\b',   "makes brand page feel generic"),
    (r'\breliable\b',  "makes brand page feel generic"),
    (r'\benjoy\b',     "makes brand page feel generic"),
    (r'\bfeatures\b',  "too vague — name the actual feature"),
]

# S1 openers that are banned
S1_BANNED_OPENERS = {'discover', 'explore', 'shop'}

# Overuse warnings (appear >1x in one piece)
OVERUSE_WORDS = ['premium', 'high-quality', 'best-in-class', 'cutting-edge', 'upgrade']

# Encoding artifacts
ENCODING_ARTIFACTS = ['â€™', 'â€\x99', 'â€œ', 'â€', 'â€¢', '\ufffd', '&amp;', '&nbsp;']


# ── DATA CLASSES ──────────────────────────────────────────────────────────────

@dataclass
class ViewportResult:
    viewport_name: str
    width: int
    readmore_button_present: bool = False
    readmore_content_hidden: bool = False
    copy_truncated: bool = False
    approx_lines: Optional[int] = None
    css_clamp: str = "none"
    css_max_height: str = "none"
    visible_text_preview: str = ""


@dataclass
class AuditResult:
    url: str
    page_type: str = "?"
    raw_html: str = ""
    text: str = ""
    char_count: int = 0
    sentence_count: int = 0
    s1: str = ""
    s2: str = ""
    s1_len: int = 0
    s2_len: int = 0
    inlinks: list = field(default_factory=list)
    fails: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    viewport_results: list = field(default_factory=list)
    load_error: str = ""
    passed: bool = False


# ── PAGE TYPE ─────────────────────────────────────────────────────────────────

def classify_page_type(url: str) -> str:
    """Classify URL into A (generic category), B (brand hub), C (brand+category), D (deals)."""
    path = urlparse(url).path.strip('/')
    segs = [s.lower() for s in path.split('/') if s]

    if not segs:
        return 'A'
    if 'deals' in segs:
        return 'D'

    is_brand = segs[0] in KNOWN_BRANDS
    if is_brand and len(segs) == 1:
        return 'B'
    if is_brand and len(segs) >= 2:
        return 'C'
    return 'A'


# ── FETCH & EXTRACT ───────────────────────────────────────────────────────────

async def load_page(url: str, browser: Browser, viewport: dict) -> Page:
    ctx = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": viewport["width"], "height": viewport["height"]},
    )
    page = await ctx.new_page()
    await page.goto(url, wait_until="networkidle", timeout=45000)
    await page.wait_for_timeout(2500)  # SPA settle time
    return page


async def extract_intro(page: Page) -> tuple[str, str]:
    """
    Returns (full_div_html, paragraph_text).

    Selector priority:
      1. [data-testid='contentful-richtext'] p          — most reliable, both classes present
      2. div[class*='_richText_'][class*='_rte_'] p     — combined class guard, avoids promo blobs
      3. div[class*='_richText_'] p                     — broadest fallback, length-gated

    For selectors 2 and 3, picks the LONGEST paragraph >= 100 chars to skip
    short promo elements (StoreCash banners etc.) that share the _richText_ class.
    """

    # ── Priority 1: data-testid (stable, specific) ─────────────────────────
    try:
        parent_sel = "[data-testid='contentful-richtext']"
        para_sel   = "[data-testid='contentful-richtext'] p"
        para = page.locator(para_sel).first
        await para.wait_for(timeout=6000)
        text = (await para.inner_text()).strip()
        if len(text) >= 100:
            parent = page.locator(parent_sel).first
            html = (await parent.inner_html()).strip()
            return html, text
    except Exception:
        pass

    # ── Priority 2 & 3: class-based, pick longest paragraph >= 100 chars ──
    candidate_selectors = [
        ("div[class*='_richText_'][class*='_rte_']", "div[class*='_richText_'][class*='_rte_'] p"),
        ("div[class*='_richText_']",                  "div[class*='_richText_'] p"),
    ]

    for parent_sel, para_sel in candidate_selectors:
        try:
            count = await page.locator(para_sel).count()
            if count == 0:
                continue

            best_text = ""
            best_html = ""
            for i in range(min(count, 10)):
                para = page.locator(para_sel).nth(i)
                t = (await para.inner_text()).strip()
                if len(t) >= 100 and len(t) > len(best_text):
                    # Walk up to the parent div for the HTML
                    parent_el = page.locator(parent_sel).nth(i)
                    h = (await parent_el.inner_html()).strip()
                    best_text = t
                    best_html = h

            if best_text:
                return best_html, best_text
        except Exception:
            continue

    return "", ""


def extract_inlinks(html: str) -> list[dict]:
    """Extract all <a href> links from the richtext div HTML."""
    if not html:
        return []
    soup = BeautifulSoup(html, 'lxml')
    return [
        {"text": a.get_text(strip=True), "href": a.get("href", "")}
        for a in soup.find_all("a", href=True)
    ]


# ── SENTENCE SPLITTING ────────────────────────────────────────────────────────

def split_sentences(text: str) -> list[str]:
    """
    Split into sentences on '. ' / '! ' / '? ' followed by uppercase.
    Handles common abbreviations by requiring uppercase after the split.
    """
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text.strip())
    return [p.strip() for p in parts if p.strip()]


# ── COPY AUDIT ────────────────────────────────────────────────────────────────

def audit_copy(result: AuditResult) -> AuditResult:
    text = result.text
    page_type = result.page_type

    if not text:
        result.fails.append("FAIL: No PLP intro copy found — check selector or page content")
        return result

    result.char_count = len(text)
    sents = split_sentences(text)
    result.sentence_count = len(sents)

    # Assign S1/S2
    if len(sents) >= 1:
        result.s1 = sents[0]
        result.s1_len = len(sents[0])
    if len(sents) >= 2:
        result.s2 = sents[1]
        result.s2_len = len(sents[1])

    # ── 1. Character count ──────────────────────────────────────────────────
    if result.char_count < CHAR_MIN:
        result.fails.append(
            f"FAIL [char-count]: {result.char_count} chars — below minimum {CHAR_MIN}"
        )
    elif result.char_count > CHAR_MAX:
        result.fails.append(
            f"FAIL [char-count]: {result.char_count} chars — exceeds maximum {CHAR_MAX}"
        )
    elif not (CHAR_IDEAL_MIN <= result.char_count <= CHAR_IDEAL_MAX):
        result.warnings.append(
            f"WARN [char-count]: {result.char_count} chars — valid but outside ideal 225–235 range"
        )

    # ── 2. Exactly 2 sentences ─────────────────────────────────────────────
    if result.sentence_count != 2:
        result.fails.append(
            f"FAIL [sentence-count]: detected {result.sentence_count} sentences (must be exactly 2)"
        )

    # ── 3. S2 shorter than S1 ──────────────────────────────────────────────
    if result.sentence_count == 2:
        if result.s2_len >= result.s1_len:
            result.fails.append(
                f"FAIL [s2-length]: S2 ({result.s2_len} chars) is not shorter than S1 ({result.s1_len} chars)"
            )

    # ── 4. "The Good Guys" exactly once ────────────────────────────────────
    tgg_count = text.count("The Good Guys")
    if tgg_count == 0:
        result.fails.append("FAIL [tgg-mention]: 'The Good Guys' not found in copy")
    elif tgg_count > 1:
        result.fails.append(
            f"FAIL [tgg-mention]: 'The Good Guys' appears {tgg_count}× (must be exactly 1)"
        )

    # ── 5. Hard-banned words ───────────────────────────────────────────────
    for pattern, reason in HARD_BANS:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            result.fails.append(
                f"FAIL [hard-ban]: '{m.group()}' — {reason}"
            )

    # Price-framing save/saving check (separate from blanket save ban)
    m = SAVE_PRICE_PATTERN.search(text)
    if m:
        result.fails.append(f"FAIL [hard-ban]: price-framing 'save' found — '{m.group()}'")

    # ── 6. Brand-page banned words (Type B/C) ──────────────────────────────
    if page_type in ('B', 'C'):
        for pattern, reason in BRAND_PAGE_BANS:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                result.fails.append(
                    f"FAIL [brand-ban] (Type {page_type}): '{m.group()}' — {reason}"
                )

    # ── 7. S1 opener ───────────────────────────────────────────────────────
    if result.s1:
        opener = result.s1.split()[0].lower().rstrip('.,!?')
        if opener in S1_BANNED_OPENERS:
            result.fails.append(
                f"FAIL [s1-opener]: S1 opens with '{opener.capitalize()}' — banned for S1"
            )

    # ── 8. Sentence case ───────────────────────────────────────────────────
    for i, sent in enumerate(sents[:2], 1):
        if sent and sent[0] != sent[0].upper():
            result.fails.append(
                f"FAIL [sentence-case]: S{i} does not start with uppercase character"
            )

    # ── 9. Encoding artifacts ──────────────────────────────────────────────
    for artifact in ENCODING_ARTIFACTS:
        if artifact in text:
            result.fails.append(f"FAIL [encoding]: artifact found — '{artifact}'")

    # ── 10. No raw HTML/markdown in text ──────────────────────────────────
    if re.search(r'<[a-zA-Z][^>]*>', text):
        result.fails.append("FAIL [format]: HTML tags found in copy text")
    if re.search(r'\[.+?\]\(.+?\)', text):
        result.fails.append("FAIL [format]: Markdown link syntax found in copy text")

    # ── 11. "across the range" ─────────────────────────────────────────────
    if re.search(r'\bacross the range\b', text, re.IGNORECASE):
        result.warnings.append(
            "WARN [phrasing]: 'across the range' found — use 'across a range' instead"
        )

    # ── 12. Overuse warnings ───────────────────────────────────────────────
    for word in OVERUSE_WORDS:
        count = len(re.findall(rf'\b{re.escape(word)}\b', text, re.IGNORECASE))
        if count > 1:
            result.warnings.append(
                f"WARN [overuse]: '{word}' appears {count}× in one piece"
            )

    # ── 13. Inlinks (info, not pass/fail) ─────────────────────────────────
    result.inlinks = extract_inlinks(result.raw_html)

    result.passed = len(result.fails) == 0
    return result


# ── VIEWPORT / READMORE ───────────────────────────────────────────────────────

async def check_viewport(page: Page, vp: dict, reload: bool = False) -> ViewportResult:
    """
    Resize viewport then probe readmore state and copy truncation.

    By default (reload=False): resize only — fast, accurate for CSS-based readmore/
    truncation. JS-driven readmore components that re-evaluate on page load may not
    reflect correctly; the report notes this.

    With reload=True (--reload-viewports flag): full reload at each size — slow but
    accurate for JS-driven readmore triggers.
    """
    vr = ViewportResult(viewport_name=vp["name"], width=vp["width"])

    await page.set_viewport_size({"width": vp["width"], "height": vp["height"]})
    if reload:
        await page.reload(wait_until="networkidle", timeout=35000)
        await page.wait_for_timeout(1000)
    else:
        await page.wait_for_timeout(600)  # allow CSS reflow

    # ── Readmore detection ────────────────────────────────────────────────
    # TGG uses data-testid="readmore-content" on the collapsible block.
    # A visible element = expanded; hidden = content is behind the trigger.
    # Class-based selectors (.readMore etc.) are intentionally excluded —
    # they cause false positives by matching unrelated page elements.
    try:
        rm_sel = '[data-testid="readmore-content"]'
        count  = await page.locator(rm_sel).count()
        if count > 0:
            vr.readmore_button_present = True
            is_vis = await page.locator(rm_sel).first.is_visible()
            vr.readmore_content_hidden = not is_vis
    except Exception:
        pass

    # ── Copy truncation probe ─────────────────────────────────────────────
    try:
        metrics = await page.evaluate("""() => {
            const selectors = [
                "div[class*='_richText_'] p",
                "[data-testid='contentful-richtext'] p"
            ];
            let el = null;
            for (const sel of selectors) {
                el = document.querySelector(sel);
                if (el) break;
            }
            if (!el) return null;
            const style = window.getComputedStyle(el);
            const lh = parseFloat(style.lineHeight) || parseFloat(style.fontSize) * 1.4 || 20;
            const rect = el.getBoundingClientRect();
            const clamp = style.webkitLineClamp || style.lineClamp || "none";
            const maxH = style.maxHeight;
            return {
                height: rect.height,
                lineHeight: lh,
                approxLines: Math.round(rect.height / lh),
                webkitLineClamp: String(clamp),
                maxHeight: String(maxH),
                overflow: style.overflow,
                text: el.textContent ? el.textContent.substring(0, 140) : ""
            };
        }""")

        if metrics:
            vr.approx_lines = metrics.get("approxLines")
            vr.css_clamp = metrics.get("webkitLineClamp", "none")
            vr.css_max_height = metrics.get("maxHeight", "none")
            vr.visible_text_preview = (metrics.get("text") or "").replace("\n", " ").strip()

            clamp_val = vr.css_clamp
            max_h_val = vr.css_max_height
            is_clamped = clamp_val not in ("none", "", "0", "unset", "normal")
            is_height_capped = (
                max_h_val not in ("none", "", "unset")
                and re.match(r'[\d.]+px', max_h_val)
                and float(re.match(r'([\d.]+)', max_h_val).group(1)) < 150
            )
            vr.copy_truncated = is_clamped or is_height_capped

    except Exception:
        pass

    return vr


async def check_all_viewports(url: str, browser: Browser, reload: bool = False) -> list[ViewportResult]:
    """
    Single page load, then resize (or optionally reload) for each viewport.
    Default: resize only — ~6x faster. Pass reload=True for accurate JS readmore state.
    """
    results = []

    ctx = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
    )
    page = await ctx.new_page()

    try:
        await page.goto(url, wait_until="networkidle", timeout=35000)
        await page.wait_for_timeout(1500)

        for vp in VIEWPORTS:
            vr = await check_viewport(page, vp, reload=reload)
            results.append(vr)
    except Exception as e:
        results.append(ViewportResult(
            viewport_name="ERROR", width=0,
            visible_text_preview=f"viewport check failed: {str(e)[:120]}"
        ))
    finally:
        await ctx.close()

    return results


# ── FULL URL AUDIT ────────────────────────────────────────────────────────────

async def audit_url(url: str, browser: Browser, reload_viewports: bool = False) -> AuditResult:
    result = AuditResult(url=url, page_type=classify_page_type(url))

    # ── Copy extraction (desktop viewport) ────────────────────────────────
    ctx = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
    )
    page = await ctx.new_page()
    try:
        await page.goto(url, wait_until="networkidle", timeout=40000)
        await page.wait_for_timeout(1500)
        html, text = await extract_intro(page)
        result.raw_html = html
        result.text = text
    except Exception as e:
        result.load_error = str(e)
        result.fails.append(f"FAIL [page-load]: {e}")
        await ctx.close()
        return result
    finally:
        await ctx.close()

    # ── Audit copy rules ──────────────────────────────────────────────────
    result = audit_copy(result)

    # ── Viewport / readmore checks ────────────────────────────────────────
    result.viewport_results = await check_all_viewports(url, browser, reload=reload_viewports)

    return result


# ── REPORTING ─────────────────────────────────────────────────────────────────

def print_report(results: list[AuditResult]) -> None:
    W = 82
    print("\n" + "=" * W)
    print("  TGG PLP INTRO AUDIT REPORT")
    print("=" * W)

    for r in results:
        status = "✅ PASS" if r.passed else "❌ FAIL"
        print(f"\n{'─' * W}")
        print(f"{status}  {r.url}")
        print(f"Page Type: {r.page_type}  |  Chars: {r.char_count}  |  Sentences: {r.sentence_count}")

        if r.text:
            # Wrap at 78 chars for readability
            wrapped = "\n    ".join(
                r.text[i:i+76] for i in range(0, len(r.text), 76)
            )
            print(f"\nCopy:\n    {wrapped}")

        if r.s1:
            print(f"\n  S1 [{r.s1_len} chars]: {r.s1}")
        if r.s2:
            print(f"  S2 [{r.s2_len} chars]: {r.s2}")

        if r.fails:
            print(f"\n  FAILURES ({len(r.fails)}):")
            for f in r.fails:
                print(f"    {f}")

        if r.warnings:
            print(f"\n  WARNINGS ({len(r.warnings)}):")
            for w in r.warnings:
                print(f"    {w}")

        if r.inlinks:
            print(f"\n  INLINKS ({len(r.inlinks)} found in richtext div):")
            for link in r.inlinks:
                print(f"    [{link['text']}] → {link['href']}")
        else:
            print("\n  INLINKS: none detected in richtext HTML")

        # Viewport table
        if r.viewport_results:
            print(f"\n  {'VIEWPORT':<22} {'LINES':>5}  {'READMORE':>8}  {'TRUNCATED':>9}  NOTES")
            print(f"  {'─'*22}  {'─'*5}  {'─'*8}  {'─'*9}  {'─'*20}")
            for vp in r.viewport_results:
                lines_str = str(vp.approx_lines) if vp.approx_lines else "?"
                rm_str    = "YES" if vp.readmore_button_present else "no"
                trunc_str = "YES" if vp.copy_truncated else "no"
                notes = []
                if vp.readmore_content_hidden:
                    notes.append("content hidden")
                if vp.css_clamp not in ("none", "", "0", "unset"):
                    notes.append(f"line-clamp:{vp.css_clamp}")
                note_str = ", ".join(notes) if notes else ""
                print(f"  {vp.viewport_name:<22} {lines_str:>5}  {rm_str:>8}  {trunc_str:>9}  {note_str}")

    print(f"\n{'=' * W}")
    passed_count = sum(1 for r in results if r.passed)
    total = len(results)
    print(f"  SUMMARY: {passed_count}/{total} passed")
    if any(r.fails for r in results):
        print(f"\n  FAILURES ACROSS ALL URLS:")
        for r in results:
            if r.fails:
                short = urlparse(r.url).path
                for f in r.fails:
                    print(f"    {short}: {f}")
    print("=" * W + "\n")


def export_json(results: list[AuditResult], path: str = "plp_audit_results.json") -> None:
    out = []
    for r in results:
        out.append({
            "url": r.url,
            "page_type": r.page_type,
            "passed": r.passed,
            "text": r.text,
            "char_count": r.char_count,
            "sentence_count": r.sentence_count,
            "s1": r.s1,
            "s2": r.s2,
            "s1_len": r.s1_len,
            "s2_len": r.s2_len,
            "inlinks": r.inlinks,
            "fails": r.fails,
            "warnings": r.warnings,
            "raw_html": r.raw_html,
            "viewport_results": [
                {
                    "viewport": vp.viewport_name,
                    "width": vp.width,
                    "readmore_button_present": vp.readmore_button_present,
                    "readmore_content_hidden": vp.readmore_content_hidden,
                    "copy_truncated": vp.copy_truncated,
                    "approx_lines": vp.approx_lines,
                    "css_clamp": vp.css_clamp,
                    "css_max_height": vp.css_max_height,
                    "visible_text_preview": vp.visible_text_preview,
                }
                for vp in r.viewport_results
            ],
        })
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"JSON export → {path}")


def export_csv(results: list[AuditResult], path: str = "plp_audit_results.csv") -> None:
    rows = []
    for r in results:
        base = {
            "url": r.url,
            "page_type": r.page_type,
            "passed": r.passed,
            "char_count": r.char_count,
            "sentence_count": r.sentence_count,
            "s1_len": r.s1_len,
            "s2_len": r.s2_len,
            "tgg_count": r.text.count("The Good Guys") if r.text else 0,
            "inlink_count": len(r.inlinks),
            "fail_count": len(r.fails),
            "warning_count": len(r.warnings),
            "fails": " | ".join(r.fails),
            "warnings": " | ".join(r.warnings),
            "inlinks": " | ".join(f"{l['text']} -> {l['href']}" for l in r.inlinks),
            "text": r.text,
        }
        # Viewport columns
        for vp in r.viewport_results:
            col = vp.viewport_name.replace(" ", "_")
            base[f"vp_{col}_readmore"] = vp.readmore_button_present
            base[f"vp_{col}_truncated"] = vp.copy_truncated
            base[f"vp_{col}_lines"] = vp.approx_lines
        rows.append(base)

    if rows:
        keys = list(rows[0].keys())
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(rows)
        print(f"CSV export  → {path}")


# ── URL INGESTION ─────────────────────────────────────────────────────────────

def load_urls_from_csv(path: str) -> list[str]:
    """
    Read URLs from a CSV file. Accepts any of these column names (case-insensitive):
    url, urls, address, loc, location, page, page_url, full_address
    Falls back to the first column if none match.
    """
    path = path.strip().strip('"').strip("'")
    urls = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        col = None
        if reader.fieldnames:
            candidates = ["url", "urls", "address", "loc", "location",
                          "page", "page_url", "full_address"]
            for c in candidates:
                match = next((h for h in reader.fieldnames if h.strip().lower() == c), None)
                if match:
                    col = match
                    break
            if not col:
                col = reader.fieldnames[0]
        for row in reader:
            val = row.get(col, "").strip()
            if val.startswith("http"):
                urls.append(val)
    return urls


def load_urls_from_sitemap(url: str) -> list[str]:
    """Fetch an XML sitemap (or sitemap index) and extract all <loc> URLs."""
    import urllib.request
    urls = []
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            content = resp.read().decode("utf-8", errors="replace")
        # Sitemap index — recurse into child sitemaps
        child_maps = re.findall(r'<loc>\s*(https?://[^\s<]+\.xml[^<]*)\s*</loc>', content)
        if child_maps:
            print(f"  Sitemap index detected — {len(child_maps)} child sitemaps found.")
            for sm in child_maps:
                urls.extend(load_urls_from_sitemap(sm.strip()))
        else:
            locs = re.findall(r'<loc>\s*(https?://[^\s<]+)\s*</loc>', content)
            urls.extend(locs)
    except Exception as e:
        print(f"  Warning: could not fetch sitemap {url} — {e}")
    return urls


def prompt_for_urls() -> tuple[list[str], bool, bool]:
    """
    Interactive prompt. Returns (urls, do_csv, reload_viewports).
    Accepts: one or more CSV file paths, sitemap URLs, or plain page URLs — mixed.
    """
    print("\n" + "=" * 62)
    print("  TGG PLP Intro Auditor")
    print("=" * 62)
    print("""
Enter one or more sources, separated by commas or newlines.
Accepted inputs:
  - Path to a CSV file     e.g. C:\\Users\\...\\urls.csv
  - Sitemap URL            e.g. https://www.thegoodguys.com.au/sitemap.xml
  - Direct page URL        e.g. https://www.thegoodguys.com.au/lg/televisions

You can mix all three types in one run.
""")

    raw = []
    print("Source(s) — paste and press Enter twice when done:")
    while True:
        line = input().strip()
        if not line:
            if raw:
                break
            continue
        # Allow comma-separated on one line
        raw.extend([x.strip() for x in line.split(",") if x.strip()])

    all_urls: list[str] = []
    for item in raw:
        if item.startswith("http") and ".xml" in item:
            # Sitemap URL
            found = load_urls_from_sitemap(item)
            print(f"  Sitemap: {len(found)} URLs loaded from {item}")
            all_urls.extend(found)
        elif item.startswith("http"):
            # Direct page URL
            all_urls.append(item)
        else:
            # File path — try as CSV
            try:
                found = load_urls_from_csv(item)
                print(f"  CSV: {len(found)} URLs loaded from {item}")
                all_urls.extend(found)
            except Exception as e:
                print(f"  Could not read file {item}: {e}")

    # Deduplicate, preserve order
    seen: set[str] = set()
    deduped = []
    for u in all_urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)

    if not deduped:
        print("\nNo URLs found. Exiting.")
        sys.exit(0)

    print(f"\n{len(deduped)} unique URL(s) queued.")

    # Options
    print("\nExport CSV as well? (y/n, default n): ", end="")
    do_csv = input().strip().lower() == "y"

    print("Reload page at each viewport for accurate JS readmore state?")
    print("(Slower — ~5× — but needed if readmore is JS-driven. y/n, default n): ", end="")
    reload_vp = input().strip().lower() == "y"

    return deduped, do_csv, reload_vp


# ── ENTRY POINT ───────────────────────────────────────────────────────────────

async def main() -> None:
    # CLI mode: URLs / flags passed as arguments — non-interactive
    cli_args = [a for a in sys.argv[1:] if not a.startswith("--")]
    do_csv           = "--csv" in sys.argv
    reload_viewports = "--reload-viewports" in sys.argv

    if cli_args:
        urls = cli_args
        print(f"\nCLI mode — {len(urls)} URL(s) queued.")
    else:
        urls, do_csv, reload_viewports = prompt_for_urls()

    mode = "reload per viewport (slow, accurate)" if reload_viewports else "resize only (fast)"
    print(f"\nStarting audit — {len(urls)} URL(s), viewport mode: {mode}\n")

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        results = []
        for i, url in enumerate(urls, 1):
            print(f"  [{i}/{len(urls)}] {url}")
            r = await audit_url(url, browser, reload_viewports=reload_viewports)
            results.append(r)
        await browser.close()

    print_report(results)
    export_json(results)
    if do_csv:
        export_csv(results)

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    asyncio.run(main())