#!/usr/bin/env python3
"""
TGG Product Shopping Audit
===========================
Fetches the TGG sitemap, extracts product titles, then scrapes Google Shopping
organic results for each product to show where TGG ranks vs competitors.

Usage:
    python seo/scripts/product-shopping-audit.py                  # all products
    python seo/scripts/product-shopping-audit.py --limit 50       # first 50 products
    python seo/scripts/product-shopping-audit.py --sitemap-url https://... --limit 100
    python seo/scripts/product-shopping-audit.py --titles-csv titles.csv  # skip sitemap

Outputs:
    seo/outputs/shopping-audit/shopping-audit-YYYY-MM-DD.csv
    seo/outputs/shopping-audit/shopping-audit-YYYY-MM-DD-summary.csv

Requirements:
    pip install playwright requests
    playwright install chromium --with-deps
"""

import asyncio
import csv
import re
import sys
import time
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus, urlparse

try:
    import requests
except ImportError:
    sys.exit("requests not found — run: pip install requests")

try:
    from playwright.async_api import async_playwright
except ImportError:
    sys.exit("playwright not found — run: pip install playwright && playwright install chromium --with-deps")


# ── Config ────────────────────────────────────────────────────────────────────

TGG_DOMAIN = "thegoodguys.com.au"
TGG_SITEMAP = "https://www.thegoodguys.com.au/sitemap.xml"
RESULTS_DIR = Path("seo/outputs/shopping-audit")

ORGANIC_HEADERS = [
    "product_title", "tgg_sku", "position", "result_title", "price",
    "original_price", "rating", "reviews", "store", "store_domain",
    "sponsored", "tgg_visible", "tgg_position", "url", "mode", "scraped_at"
]
SUMMARY_HEADERS = [
    "product_title", "tgg_sku", "tgg_found", "tgg_position",
    "lowest_competitor_price", "tgg_price", "total_results", "scraped_at"
]

MOBILE_UA  = "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
DESKTOP_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
MOBILE_VP  = {"width": 390,  "height": 844}
DESKTOP_VP = {"width": 1280, "height": 900}

AU_RETAILERS = {
    "harvey norman": "harveynorman.com.au", "harvey norman australia": "harveynorman.com.au",
    "jb hi-fi": "jbhifi.com.au", "jb hifi": "jbhifi.com.au", "jb hi fi": "jbhifi.com.au",
    "the good guys": "thegoodguys.com.au", "good guys": "thegoodguys.com.au",
    "big w": "bigw.com.au", "kmart": "kmart.com.au", "target": "target.com.au",
    "amazon au": "amazon.com.au", "amazon": "amazon.com.au",
    "kogan": "kogan.com", "kogan.com": "kogan.com",
    "bing lee": "binglee.com.au", "appliances online": "appliancesonline.com.au",
    "catch": "catch.com.au", "ebay": "ebay.com.au", "ebay au": "ebay.com.au",
    "winning appliances": "winningappliances.com.au",
    "domayne": "domayne.com.au", "betta home living": "betta.com.au",
    "officeworks": "officeworks.com.au", "myer": "myer.com.au",
}


# ── Sitemap fetching ──────────────────────────────────────────────────────────

def fetch_sitemap_products(sitemap_url: str, limit: int | None = None) -> list[dict]:
    """Fetch product URLs and titles from TGG sitemap. Returns list of {url, title, sku}."""
    print(f"Fetching sitemap: {sitemap_url}")
    products = []

    try:
        resp = requests.get(sitemap_url, timeout=30, headers={"User-Agent": "TGG-SEO-Audit/1.0"})
        resp.raise_for_status()
    except Exception as e:
        sys.exit(f"Failed to fetch sitemap: {e}")

    root = ET.fromstring(resp.content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    # Check if this is a sitemap index (points to child sitemaps)
    child_sitemaps = root.findall("sm:sitemap/sm:loc", ns)
    if child_sitemaps:
        print(f"  Sitemap index found — {len(child_sitemaps)} child sitemaps")
        for child_loc in child_sitemaps:
            child_url = child_loc.text.strip()
            # Only process product sitemaps
            if "product" in child_url.lower() or "sitemap-product" in child_url.lower():
                products.extend(_parse_product_sitemap(child_url, ns))
                if limit and len(products) >= limit:
                    break
            if limit and len(products) >= limit:
                break
    else:
        # Single sitemap — parse directly
        products.extend(_parse_product_sitemap(sitemap_url, ns, already_fetched=resp.content))

    if limit:
        products = products[:limit]

    print(f"  Found {len(products)} product URLs")
    return products


def _parse_product_sitemap(url: str, ns: dict, already_fetched: bytes | None = None) -> list[dict]:
    """Parse a single product sitemap XML into product records."""
    if already_fetched:
        content = already_fetched
    else:
        try:
            resp = requests.get(url, timeout=30, headers={"User-Agent": "TGG-SEO-Audit/1.0"})
            resp.raise_for_status()
            content = resp.content
        except Exception as e:
            print(f"  Warning: could not fetch {url}: {e}")
            return []

    root = ET.fromstring(content)
    products = []
    for loc_el in root.findall("sm:url/sm:loc", ns):
        loc = loc_el.text.strip()
        parsed = urlparse(loc)
        path = parsed.path.rstrip("/")
        # Only include URLs that look like product pages (have a SKU or deep path)
        # TGG product URLs: /product-name-SKU or /brand/product-name-SKU
        slug = path.split("/")[-1]
        if not slug or len(path.split("/")) < 2:
            continue
        title = _slug_to_title(slug)
        sku = _extract_sku(slug)
        products.append({"url": loc, "title": title, "sku": sku})

    return products


def _slug_to_title(slug: str) -> str:
    """Convert a URL slug to a human-readable product title."""
    # Remove trailing SKU (numeric sequence at end)
    clean = re.sub(r"-?\d{5,}$", "", slug)
    clean = re.sub(r"-[A-Z0-9]{6,}$", "", clean)
    # Convert hyphens to spaces, title-case
    return clean.replace("-", " ").strip().title()


def _extract_sku(slug: str) -> str:
    """Extract SKU from slug if present (trailing numeric or alphanumeric code)."""
    m = re.search(r"[-/]([A-Z0-9]{5,})$", slug, re.IGNORECASE)
    return m.group(1).upper() if m else ""


def load_titles_from_csv(csv_path: str) -> list[dict]:
    """Load product titles from a CSV file with columns: title (required), sku (optional)."""
    products = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get("title") or row.get("Title") or row.get("product_title") or ""
            sku = row.get("sku") or row.get("SKU") or ""
            if title.strip():
                products.append({"title": title.strip(), "sku": sku.strip(), "url": ""})
    print(f"Loaded {len(products)} titles from {csv_path}")
    return products


# ── Scraper ───────────────────────────────────────────────────────────────────

def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def resolve_store_domain(store: str, el_html_hrefs: list[str]) -> str:
    # Tier 1: decode from Google redirect href
    for raw in el_html_hrefs:
        m = re.search(r"[?&](?:url|q|dest|adurl)=(https?[^&]+)", raw, re.IGNORECASE)
        if m:
            dm = re.search(r"https?://(?:www\.)?([^/?#]+)", re.sub(r"%2F", "/", m.group(1)))
            if dm:
                return dm.group(1)
        if raw.startswith("http") and "google." not in raw:
            dm = re.search(r"https?://(?:www\.)?([^/?#]+)", raw)
            if dm:
                return dm.group(1)
    # Tier 2: known AU retailer
    if store:
        key = store.lower().strip()
        if key in AU_RETAILERS:
            return AU_RETAILERS[key]
        for k, v in AU_RETAILERS.items():
            if key in k or k in key:
                return v
    # Tier 3: normalise store name
    if store and len(store) > 2:
        return re.sub(r"[^a-z0-9]", "", store.lower().replace(" australia", "").replace(" au", "")) + ".com.au"
    return ""


ORGANIC_JS = r"""
() => {
    const priceRe  = /A?\$[\d,]+(?:\.\d{2})?/g;
    const ratingRe = /^(\d\.\d)\b/;
    const googleHost = location.hostname;

    const cardSet = new Set();
    const root = document.getElementById('rso') || document.getElementById('search') || document.body;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
        if (!/A?\$[\d,]+/.test(node.nodeValue || '')) continue;
        let el = node.parentElement;
        for (let d = 0; d < 14; d++) {
            if (!el || el === document.body) break;
            const txt = el.innerText || '';
            const lines = txt.split('\n').filter(l => l.trim()).length;
            if (lines >= 2 && lines <= 20 && txt.length <= 900) { cardSet.add(el); break; }
            el = el.parentElement;
        }
    }
    const allCards = Array.from(cardSet);
    const leafCards = allCards.filter(el => !allCards.some(other => other !== el && el.contains(other)));

    const seenKey = new Set();
    const results  = [];
    let pos = 0;

    for (const el of leafCards) {
        const lines = (el.innerText || '').split('\n').map(l => l.trim()).filter(Boolean);
        if (lines.length < 2) continue;

        const fullText = el.innerText || '';
        const allPrices = [...new Set(fullText.match(/A?\$[\d,]+(?:\.\d{2})?/g) || [])];
        if (allPrices.length === 0) continue;

        const price = allPrices.sort((a, b) =>
            parseFloat(a.replace(/[A$,]/g,'')) - parseFloat(b.replace(/[A$,]/g,''))
        )[0];
        const originalPrice = allPrices.length > 1 ? allPrices[allPrices.length - 1] : '';

        const priceIdx = lines.findIndex(l => /A?\$[\d,]/.test(l));
        const titleCandidates = lines
            .slice(0, priceIdx < 0 ? lines.length : priceIdx)
            .filter(l => !/A?\$[\d,]/.test(l) && l.length > 3 && !/^\d+[%$]/.test(l));
        const title = titleCandidates.sort((a, b) => b.length - a.length)[0] || '';
        if (!title) continue;

        const key = title + '||' + price;
        if (seenKey.has(key)) continue;
        seenKey.add(key);

        const isSponsored = !!el.querySelector('[aria-label*="Sponsored"],.Krfl3e,[data-dtld],.mnKHRc')
            || /^sponsored$/im.test(lines[0]);

        let rating = '', reviews = '';
        const ratingEl = el.querySelector('[aria-label*="out of 5"],[aria-label*="Rated"],[aria-label*="stars"]');
        if (ratingEl) { const m = (ratingEl.getAttribute('aria-label')||'').match(/(\d\.\d)/); if (m) rating = m[1]; }
        if (!rating) { for (const l of lines) { if (ratingRe.test(l)) { rating = l.match(ratingRe)[1]; break; } } }
        for (const l of lines) {
            const m = l.match(/^\(?([\d,]+)\)?\s*(?:reviews?|ratings?)?$/i);
            if (m && l !== price && l !== originalPrice) {
                const n = parseInt(m[1].replace(/,/g,''), 10);
                if (n > 0 && n < 2000000) { reviews = String(n); break; }
            }
        }

        const storeEl = el.querySelector('[data-merchant-name],.aULzUe,.E5ocAb,.LbUacb,.IuHnof,.NJMzre,.zPEcBd,.Lq5OHe');
        let store = (storeEl?.getAttribute('data-merchant-name') || storeEl?.innerText || '').replace(/^from\s+/i,'').trim();
        if (!store) {
            const afterLines = lines.slice(priceIdx + 1);
            store = afterLines.find(l =>
                !/A?\$[\d,]/.test(l) && !/^[\d.,()%]+$/.test(l) &&
                !/^\d+%\s*(off|save)/i.test(l) && !/^free\s*(delivery|shipping)/i.test(l) && l.length > 1
            ) || '';
        }
        if (/^\d+%|^free\s*(delivery|ship)/i.test(store)) store = '';

        const hrefs = Array.from(el.querySelectorAll('a[href]')).map(a => a.getAttribute('href') || '');

        let productUrl = '';
        for (const a of el.querySelectorAll('a[href]')) {
            const h = a.getAttribute('href') || '';
            if (h.includes('/shopping/product/') || h.startsWith('/shopping/')) {
                productUrl = 'https://' + googleHost + h; break;
            }
        }
        if (productUrl.includes('support.google.com')) productUrl = '';

        pos++;
        results.push({ pos, title, price,
            originalPrice: originalPrice === price ? '' : originalPrice,
            rating, reviews, store, hrefs, sponsored: isSponsored, productUrl });
    }
    return results;
}
"""


async def scrape_shopping(page, keyword: str, page_offset: int = 0) -> list[dict]:
    raw = await page.evaluate(ORGANIC_JS)
    now = datetime.now().isoformat(timespec="seconds")
    rows = []
    for r in raw:
        store = clean(r.get("store", ""))
        hrefs = r.get("hrefs", [])
        store_domain = resolve_store_domain(store, hrefs)
        rows.append({
            "keyword":        keyword,
            "position":       r["pos"] + page_offset,
            "result_title":   clean(r["title"]),
            "price":          clean(r["price"]),
            "original_price": clean(r.get("originalPrice", "")),
            "rating":         r["rating"],
            "reviews":        r["reviews"],
            "store":          store or store_domain,
            "store_domain":   store_domain,
            "sponsored":      "yes" if r.get("sponsored") else "no",
            "tgg_visible":    "yes" if TGG_DOMAIN in store_domain else "no",
            "url":            r.get("productUrl", ""),
            "scraped_at":     now,
        })
    return rows


async def dismiss_consent(page):
    for sel in ["button#L2AGLb", "button:has-text('Accept all')", "button:has-text('I agree')"]:
        try:
            btn = page.locator(sel)
            if await btn.count() > 0:
                await btn.first.click()
                await page.wait_for_timeout(800)
                return
        except Exception:
            pass


async def slow_scroll(page):
    height = await page.evaluate("document.body.scrollHeight")
    for y in range(0, height + 1, 500):
        await page.evaluate(f"window.scrollTo(0,{y})")
        await page.wait_for_timeout(150)
    await page.evaluate("window.scrollTo(0,0)")
    await page.wait_for_timeout(500)


async def audit_products(products: list[dict], mode: str = "mobile", pages_per_kw: int = 2) -> tuple[list[dict], list[dict]]:
    """Run Google Shopping scrape for each product title. Returns (all_rows, summary_rows)."""
    is_mobile = mode == "mobile"
    all_rows = []
    summary_rows = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )
        ctx = await browser.new_context(
            viewport=MOBILE_VP if is_mobile else DESKTOP_VP,
            user_agent=MOBILE_UA if is_mobile else DESKTOP_UA,
            locale="en-AU",
            is_mobile=is_mobile,
            has_touch=is_mobile,
        )
        await ctx.add_init_script(
            "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"
        )

        first_page = True
        for i, product in enumerate(products, 1):
            title = product["title"]
            sku = product.get("sku", "")
            print(f"[{i}/{len(products)}] {title[:60]}")

            kw_rows = []
            for pg in range(pages_per_kw):
                start = pg * 40
                page = await ctx.new_page()
                try:
                    url = (
                        f"https://www.google.com.au/search"
                        f"?q={quote_plus(title)}&tbm=shop&gl=au&hl=en-AU&num=40&start={start}"
                    )
                    await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    if first_page:
                        await dismiss_consent(page)
                        first_page = False
                    await page.wait_for_timeout(2000)
                    await slow_scroll(page)
                    rows = await scrape_shopping(page, title, page_offset=start)
                    if not rows:
                        break
                    kw_rows.extend(rows)
                except Exception as e:
                    print(f"  Error page {pg+1}: {e}")
                finally:
                    await page.close()
                await asyncio.sleep(1.5)

            # Deduplicate by title+price across pages
            seen = set()
            deduped = []
            for r in kw_rows:
                k = r["result_title"] + "||" + r["price"]
                if k not in seen:
                    seen.add(k)
                    deduped.append(r)
            for idx, r in enumerate(deduped, 1):
                r["position"] = idx

            # Attach product metadata
            for r in deduped:
                r["product_title"] = title
                r["tgg_sku"] = sku

            # Find TGG position
            tgg_rows = [r for r in deduped if r["tgg_visible"] == "yes"]
            tgg_position = tgg_rows[0]["position"] if tgg_rows else ""
            tgg_price = tgg_rows[0]["price"] if tgg_rows else ""

            # Lowest competitor price (exclude TGG)
            competitor_prices = []
            for r in deduped:
                if r["tgg_visible"] != "yes" and r["price"]:
                    try:
                        competitor_prices.append(float(re.sub(r"[A$,]", "", r["price"])))
                    except ValueError:
                        pass
            low_comp = f"${min(competitor_prices):.2f}" if competitor_prices else ""

            summary_rows.append({
                "product_title": title,
                "tgg_sku": sku,
                "tgg_found": "yes" if tgg_rows else "no",
                "tgg_position": tgg_position,
                "lowest_competitor_price": low_comp,
                "tgg_price": tgg_price,
                "total_results": len(deduped),
                "scraped_at": datetime.now().isoformat(timespec="seconds"),
            })

            all_rows.extend(deduped)

            if tgg_rows:
                print(f"  TGG: position {tgg_position}, {tgg_price} | low comp: {low_comp} | {len(deduped)} total results")
            else:
                print(f"  TGG: NOT FOUND | low comp: {low_comp} | {len(deduped)} total results")

            await asyncio.sleep(2)

        await browser.close()

    return all_rows, summary_rows


# ── Output ────────────────────────────────────────────────────────────────────

def save_csv(rows: list[dict], path: Path, fieldnames: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved: {path} ({len(rows)} rows)")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="TGG Product Shopping Audit")
    parser.add_argument("--sitemap-url", default=TGG_SITEMAP, help="Sitemap URL to crawl")
    parser.add_argument("--titles-csv", help="CSV of product titles to skip sitemap fetch")
    parser.add_argument("--limit", type=int, default=None, help="Max products to audit")
    parser.add_argument("--mode", choices=["mobile", "desktop"], default="mobile")
    parser.add_argument("--pages", type=int, default=2, help="Google Shopping pages per product (40 results each)")
    args = parser.parse_args()

    if args.titles_csv:
        products = load_titles_from_csv(args.titles_csv)
    else:
        products = fetch_sitemap_products(args.sitemap_url, limit=args.limit)

    if not products:
        sys.exit("No products found — check sitemap URL or CSV.")

    if args.limit:
        products = products[:args.limit]

    print(f"\nAuditing {len(products)} products in {args.mode} mode ({args.pages} page(s) each)\n")

    date_str = datetime.now().strftime("%Y-%m-%d")
    detail_path  = RESULTS_DIR / f"shopping-audit-{date_str}.csv"
    summary_path = RESULTS_DIR / f"shopping-audit-{date_str}-summary.csv"

    all_rows, summary_rows = asyncio.run(audit_products(products, mode=args.mode, pages_per_kw=args.pages))

    save_csv(all_rows, detail_path, ORGANIC_HEADERS)
    save_csv(summary_rows, summary_path, SUMMARY_HEADERS)

    # Print quick summary
    found = sum(1 for r in summary_rows if r["tgg_found"] == "yes")
    not_found = len(summary_rows) - found
    print(f"\n{'='*60}")
    print(f"TGG visible:     {found}/{len(summary_rows)} products ({found/len(summary_rows)*100:.0f}%)")
    print(f"TGG not found:   {not_found} products")
    avg_pos = [int(r["tgg_position"]) for r in summary_rows if r["tgg_position"]]
    if avg_pos:
        print(f"Avg TGG position: {sum(avg_pos)/len(avg_pos):.1f}")
    print(f"{'='*60}")
    print(f"Detail:  {detail_path}")
    print(f"Summary: {summary_path}")


if __name__ == "__main__":
    main()
