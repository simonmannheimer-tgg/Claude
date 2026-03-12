#!/usr/bin/env python3
"""
Google Shopping Carousel Scraper

Searches Google for each keyword, extracts organic shopping carousel data:
  - Position, title, price, rating, review count, store/brand
Saves results to results/<keyword>.csv and results/all_results.csv
"""

import asyncio
import csv
import json
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
    "scraped_at",
]


def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def clean_price(s: str) -> str:
    match = re.search(r"[\$£€][\d,]+(?:\.\d{2})?", s)
    return match.group(0) if match else clean_text(s)


def clean_rating(s: str) -> str:
    match = re.search(r"[\d.]+(?:\s*(?:out of|\/)\s*5)?", s)
    return match.group(0).strip() if match else clean_text(s)


def clean_reviews(s: str) -> str:
    match = re.search(r"[\d,]+", s)
    return match.group(0) if match else clean_text(s)


async def dismiss_consent(page: Page) -> None:
    """Click through cookie/consent dialogs if present."""
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


async def extract_carousel_items(page: Page, keyword: str) -> list[dict]:
    """
    Extract items from the Google Shopping carousel using a JS evaluation
    that tries multiple selector strategies in priority order.
    """
    raw = await page.evaluate(r"""
        () => {
            const results = [];

            // ── Strategy 1: dedicated shopping list result containers ──────────
            const strategy1 = document.querySelectorAll(
                '.sh-dlr__list-result, [data-docid].sh-dlr__list-result, .mnr-c'
            );

            // ── Strategy 2: product cards inside inline shopping units ─────────
            const strategy2 = document.querySelectorAll(
                '.g .kp-wholepage .sg-product, .comercial-unit .sg-product'
            );

            // ── Strategy 3: aria-based – look for list/grid inside a section
            //    whose heading contains "Popular products" or similar  ──────────
            let strategy3 = [];
            for (const heading of document.querySelectorAll('h3, h2, [role="heading"]')) {
                const txt = heading.textContent || '';
                if (/popular products|shopping results/i.test(txt)) {
                    const section = heading.closest('div[data-hveid], div[jsname], section');
                    if (section) {
                        strategy3 = Array.from(section.querySelectorAll(
                            '[data-hveid], [jsname], li, .sh-dlr__list-result'
                        ));
                    }
                    break;
                }
            }

            // ── Strategy 4: any block with a price near a title ───────────────
            const strategy4 = [];
            const priceRe = /[\$£€][\d,]+(?:\.\d{2})?/;
            document.querySelectorAll('div[data-hveid]').forEach(block => {
                const text = block.innerText || '';
                if (priceRe.test(text) && text.length < 600) {
                    strategy4.push(block);
                }
            });

            const candidates = strategy1.length  ? strategy1
                             : strategy2.length  ? strategy2
                             : strategy3.length  ? strategy3
                             : strategy4;

            const seen = new Set();
            let pos = 0;

            for (const el of candidates) {
                // deduplicate by element reference
                if (seen.has(el)) continue;
                seen.add(el);

                const innerText = el.innerText || el.textContent || '';

                // must contain a price to be a product card
                if (!priceRe.test(innerText)) continue;

                // ── title ────────────────────────────────────────────────────
                const titleEl = el.querySelector(
                    'h3, [role="heading"], .translate_noresize, .Xjkr3b, ' +
                    '.sh-np__click-target, [data-sh-gr] h3'
                );
                const title = (titleEl?.innerText || titleEl?.textContent || '').trim();

                // ── price ────────────────────────────────────────────────────
                const priceEl = el.querySelector(
                    '[aria-label*="$"], [aria-label*="£"], .a8Pemb, .OFFNJ, ' +
                    '[data-price], .T14wmb, .HRLxBb'
                );
                const priceRaw = priceEl?.getAttribute('aria-label')
                               || priceEl?.innerText
                               || '';
                const priceMatch = (priceRaw + innerText).match(/[\$£€][\d,]+(?:\.\d{2})?/);
                const price = priceMatch ? priceMatch[0] : '';

                // ── rating ───────────────────────────────────────────────────
                const ratingEl = el.querySelector(
                    '[aria-label*="star"], [aria-label*="rating"], .Rsc7Yb, ' +
                    '.yi40Hd, [role="img"][aria-label]'
                );
                const ratingRaw = ratingEl?.getAttribute('aria-label')
                                || ratingEl?.innerText
                                || '';
                const ratingMatch = ratingRaw.match(/[\d.]+/);
                const rating = ratingMatch ? ratingMatch[0] : '';

                // ── review count ─────────────────────────────────────────────
                const reviewEl = el.querySelector(
                    '[aria-label*="review"], .HiT7Id, .NzHeef, .rGl5ye'
                );
                const reviewRaw = reviewEl?.getAttribute('aria-label')
                                || reviewEl?.innerText
                                || '';
                const reviewMatch = reviewRaw.match(/[\d,]+/);
                const reviews = reviewMatch ? reviewMatch[0] : '';

                // ── store / brand ────────────────────────────────────────────
                const storeEl = el.querySelector(
                    '.aULzUe, .E5ocAb, .LbUacb, [data-merchant-name], ' +
                    '.IuHnof, .zPEcBd'
                );
                const store = (storeEl?.innerText || storeEl?.textContent || '').trim();

                pos++;
                results.push({ pos, title, price, rating, reviews, store });
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
            "scraped_at": now,
        })
    return items


async def scrape_keyword(keyword: str, context: BrowserContext) -> list[dict]:
    page = await context.new_page()
    slug = keyword.replace(" ", "_")
    try:
        url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}&gl=us&hl=en&num=10"
        print(f"  → Searching: {keyword!r}")
        await page.goto(url, wait_until="domcontentloaded", timeout=30_000)
        await dismiss_consent(page)
        await page.wait_for_timeout(2000)  # let JS render carousel

        SCREENSHOTS_DIR.mkdir(exist_ok=True)
        await page.screenshot(
            path=str(SCREENSHOTS_DIR / f"{slug}.png"), full_page=False
        )

        items = await extract_carousel_items(page, keyword)

        if not items:
            print(f"  ⚠  No carousel items found for {keyword!r} — check screenshots/{slug}.png")
        else:
            print(f"  ✓  {len(items)} products found for {keyword!r}")

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
    keywords = KEYWORDS

    print(f"Google Shopping Carousel Scraper")
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
        # hide webdriver flag
        await context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        for keyword in keywords:
            rows = await scrape_keyword(keyword, context)
            all_rows.extend(rows)

            slug = keyword.replace(" ", "_")
            save_csv(rows, RESULTS_DIR / f"{slug}.csv")
            await asyncio.sleep(2)  # polite delay between searches

        await browser.close()

    # combined file
    save_csv(all_rows, RESULTS_DIR / "all_results.csv")

    print(f"\nDone. {len(all_rows)} total products across {len(keywords)} keywords.")
    print(f"Results saved to {RESULTS_DIR}/")

    # quick summary table
    if all_rows:
        print("\n── Summary ──────────────────────────────────────────────")
        print(f"{'Keyword':<20} {'Products found':>15}")
        print("-" * 37)
        for kw in keywords:
            count = sum(1 for r in all_rows if r["keyword"] == kw)
            print(f"{kw:<20} {count:>15}")


if __name__ == "__main__":
    asyncio.run(main())
