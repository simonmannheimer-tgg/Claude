#!/usr/bin/env python3
"""
Google Organic Shopping Scraper

Navigates to the Google Shopping tab for each keyword, skips sponsored
listings, and extracts organic product data:
  - Position, title, price, rating, review count, store, product URL
Saves results to results/organic_<keyword>.csv and results/organic_all.csv
"""

import asyncio
import csv
import re
import sys
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright, Page, BrowserContext

KEYWORDS = [
    "fridge",
    "vacuum",
    "television",
    "tv",
    "washer",
    "washing machine",
]

RESULTS_DIR = Path("results")
SCREENSHOTS_DIR = Path("screenshots")

HEADERS = [
    "keyword",
    "position",
    "title",
    "price",
    "rating",
    "reviews",
    "store",
    "url",
    "scraped_at",
]


def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def clean_reviews(s: str) -> str:
    match = re.search(r"[\d,]+", s)
    return match.group(0) if match else clean_text(s)


async def dismiss_consent(page: Page) -> None:
    selectors = [
        "button#L2AGLb",
        "button:has-text('Accept all')",
        "button:has-text('I agree')",
        "button:has-text('Agree')",
    ]
    for sel in selectors:
        try:
            btn = page.locator(sel)
            if await btn.count() > 0:
                await btn.first.click()
                await page.wait_for_timeout(800)
                return
        except Exception:
            pass


async def extract_organic_items(page: Page, keyword: str) -> list[dict]:
    """
    Extract organic (non-sponsored) product listings from the Shopping tab.
    Sponsored items have a visible 'Sponsored' label — we detect and skip them.
    """
    raw = await page.evaluate(r"""
        () => {
            const results = [];
            const priceRe = /[\$£€][\d,]+(?:\.\d{2})?/;

            // Google Shopping tab product cards
            const cards = Array.from(document.querySelectorAll(
                '.sh-dgr__content, .sh-pr__product-results-grid .KZmu8e, ' +
                '.sh-dlr__list-result, [data-docid]'
            ));

            // Fallback: any <li> or block that looks like a product
            const candidates = cards.length ? cards : Array.from(
                document.querySelectorAll('li.sh-osd__offer-row, .sh-np__click-target')
            );

            const seen = new Set();
            let pos = 0;

            for (const el of candidates) {
                if (seen.has(el)) continue;
                seen.add(el);

                // ── skip sponsored / paid items ──────────────────────────────
                const elText = el.innerText || el.textContent || '';
                const isSponsored =
                    el.querySelector('[aria-label*="Sponsored"], .nNzjpf-cS4Vcb-PvZLI-S, ' +
                                     '.Krfl3e, [data-dtld]') !== null ||
                    /^sponsored$/im.test(elText.split('\n')[0] || '');
                if (isSponsored) continue;

                // must contain a price
                if (!priceRe.test(elText)) continue;

                // ── title ────────────────────────────────────────────────────
                const titleEl = el.querySelector(
                    'h3, h4, [role="heading"], .Xjkr3b, .translate_noresize, ' +
                    '.sh-np__click-target, .BvQan'
                );
                const title = (titleEl?.innerText || titleEl?.textContent || '').trim();
                if (!title) continue;

                // ── price ────────────────────────────────────────────────────
                const priceEl = el.querySelector(
                    '.a8Pemb, .HRLxBb, .T14wmb, [data-price], ' +
                    '[aria-label*="$"], [aria-label*="£"], [aria-label*="€"]'
                );
                const priceRaw = priceEl?.getAttribute('aria-label') || priceEl?.innerText || '';
                const priceMatch = (priceRaw + elText).match(/[\$£€][\d,]+(?:\.\d{2})?/);
                const price = priceMatch ? priceMatch[0] : '';

                // ── rating ───────────────────────────────────────────────────
                const ratingEl = el.querySelector(
                    '[aria-label*="star"], [aria-label*="rating"], .Rsc7Yb, ' +
                    '.yi40Hd, [role="img"][aria-label]'
                );
                const ratingRaw = ratingEl?.getAttribute('aria-label') || ratingEl?.innerText || '';
                const ratingMatch = ratingRaw.match(/[\d.]+/);
                const rating = ratingMatch ? ratingMatch[0] : '';

                // ── review count ─────────────────────────────────────────────
                const reviewEl = el.querySelector(
                    '[aria-label*="review"], .HiT7Id, .NzHeef, .rGl5ye, .QIrs8'
                );
                const reviewRaw = reviewEl?.getAttribute('aria-label') || reviewEl?.innerText || '';
                const reviewMatch = reviewRaw.match(/[\d,]+/);
                const reviews = reviewMatch ? reviewMatch[0] : '';

                // ── store ────────────────────────────────────────────────────
                const storeEl = el.querySelector(
                    '.aULzUe, .E5ocAb, .LbUacb, .IuHnof, .zPEcBd, ' +
                    '[data-merchant-name], .NJMzre'
                );
                const store = (storeEl?.innerText || storeEl?.textContent || '').trim();

                // ── product URL ──────────────────────────────────────────────
                const linkEl = el.querySelector('a[href*="/shopping/product/"], a.shntl, a[href]');
                const href = linkEl?.getAttribute('href') || '';
                const url = href.startsWith('http') ? href
                          : href ? 'https://www.google.com' + href
                          : '';

                pos++;
                results.push({ pos, title, price, rating, reviews, store, url });
            }

            return results;
        }
    """)

    now = datetime.now().isoformat(timespec="seconds")
    items = []
    for r in raw:
        items.append({
            "keyword": keyword,
            "position": r["pos"],
            "title": clean_text(r.get("title", "")),
            "price": clean_text(r.get("price", "")),
            "rating": clean_text(r.get("rating", "")),
            "reviews": clean_reviews(r.get("reviews", "")),
            "store": clean_text(r.get("store", "")),
            "url": r.get("url", ""),
            "scraped_at": now,
        })
    return items


async def scrape_keyword(keyword: str, context: BrowserContext) -> list[dict]:
    page = await context.new_page()
    slug = keyword.replace(" ", "_")
    try:
        # tbm=shop → Google Shopping tab; tbs=p_ord:rv → sort by relevance (organic order)
        url = (
            f"https://www.google.com/search"
            f"?q={keyword.replace(' ', '+')}&tbm=shop&gl=us&hl=en&num=40"
        )
        print(f"  → Scraping organic: {keyword!r}")
        await page.goto(url, wait_until="domcontentloaded", timeout=30_000)
        await dismiss_consent(page)
        await page.wait_for_timeout(2000)

        SCREENSHOTS_DIR.mkdir(exist_ok=True)
        await page.screenshot(
            path=str(SCREENSHOTS_DIR / f"organic_{slug}.png"), full_page=False
        )

        items = await extract_organic_items(page, keyword)

        if not items:
            print(f"  ⚠  No organic items found for {keyword!r} — check screenshots/organic_{slug}.png")
        else:
            print(f"  ✓  {len(items)} organic products found for {keyword!r}")

        return items
    except Exception as e:
        print(f"  ✗  Error scraping {keyword!r}: {e}")
        return []
    finally:
        await page.close()


def save_csv(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)


async def main() -> None:
    keywords = sys.argv[1:] if len(sys.argv) > 1 else KEYWORDS

    print("Google Organic Shopping Scraper")
    print(f"Keywords: {keywords}")
    print(f"Output: {RESULTS_DIR}/\n")

    all_rows: list[dict] = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"],
        )
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
            locale="en-US",
        )
        await context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        for keyword in keywords:
            rows = await scrape_keyword(keyword, context)
            all_rows.extend(rows)

            slug = keyword.replace(" ", "_")
            save_csv(rows, RESULTS_DIR / f"organic_{slug}.csv")
            await asyncio.sleep(2)

        await browser.close()

    save_csv(all_rows, RESULTS_DIR / "organic_all.csv")

    print(f"\nDone. {len(all_rows)} total organic products across {len(keywords)} keywords.")
    print(f"Results saved to {RESULTS_DIR}/")

    if all_rows:
        print("\n── Summary ──────────────────────────────────────────────")
        print(f"{'Keyword':<20} {'Organic products':>18}")
        print("-" * 40)
        for kw in keywords:
            count = sum(1 for r in all_rows if r["keyword"] == kw)
            print(f"{kw:<20} {count:>18}")


if __name__ == "__main__":
    asyncio.run(main())
