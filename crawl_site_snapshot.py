"""
Download fully-rendered HTML snapshots for local agentic-seo analysis.
Uses Playwright (Chromium) to bypass Cloudflare and JS-rendering requirements.

Usage:
    python crawl_site_snapshot.py                            # TGG defaults
    python crawl_site_snapshot.py --urls '["https://..."]'  # custom URLs
    python crawl_site_snapshot.py --out site-snapshots/custom/

Install:
    pip install playwright
    playwright install chromium --with-deps

Output: site-snapshots/<domain>/*.html, ready for:
    node .claude/optional/agentic-seo/repo/bin/aeo.js site-snapshots/<domain>/
    python run_aeo_local.py  (AEO_DIR=site-snapshots/<domain>)
"""

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from playwright.async_api import async_playwright

DEFAULT_URLS = [
    # Home
    "https://www.thegoodguys.com.au",
    # Category pages
    "https://www.thegoodguys.com.au/televisions",
    "https://www.thegoodguys.com.au/air-conditioners",
    "https://www.thegoodguys.com.au/washing-machines",
    "https://www.thegoodguys.com.au/refrigerators",
    # Sub-category
    "https://www.thegoodguys.com.au/televisions/smart-tvs",
    # Buying guides (protected paths — crawler uses longer wait)
    "https://www.thegoodguys.com.au/buying-guide/best-tvs",
    "https://www.thegoodguys.com.au/buying-guide/best-air-conditioners",
    "https://www.thegoodguys.com.au/buying-guide/best-washing-machines",
    # Editorial / blog
    "https://www.thegoodguys.com.au/whats-new",
    # Product detail page — tests Product + Offer + AggregateRating schema
    "https://www.thegoodguys.com.au/samsung-65-4k-qled-smart-tv-qa65qn90dauxsa",
]

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)
VP = {"width": 1280, "height": 900}


def url_to_filename(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index.html"
    safe = re.sub(r"[^a-zA-Z0-9_-]", "-", path.replace("/", "--"))
    return f"{safe}.html"


CF_CHALLENGE_MARKERS = (
    "<title>Just a moment...</title>",
    "cf-browser-verification",
    "challenge-running",
    "Checking if the site connection is secure",
)

# Domains that serve Cloudflare bot challenges.
# We pre-warm these by visiting the homepage first so that CF issues a
# cf_clearance session cookie before we crawl any subpages.
CF_SESSION_DOMAINS = {"harveynorman.com.au"}
CF_DOMAIN_DELAY = 3.5  # seconds between requests for CF-protected domains


async def _warmup_cf_domain(page, domain: str) -> None:
    """Visit homepage to establish CF clearance cookie before crawling subpages."""
    print(f"  [CF warmup] https://www.{domain}/ — establishing session cookie")
    try:
        await page.goto(f"https://www.{domain}/", wait_until="networkidle", timeout=45_000)
        await page.wait_for_timeout(4_500)
        print(f"  [CF warmup] Done")
    except Exception as e:
        print(f"  [CF warmup] Warning: {e}")


def _is_protected_path(url: str) -> bool:
    """Buying guides and editorial pages sit behind stricter Cloudflare rules."""
    path = urlparse(url).path.lower()
    return any(seg in path for seg in ("/buying-guide/", "/whats-new", "/blog/", "/news/"))


async def fetch_page(page, url: str, retries: int = 3) -> tuple[str | None, str | None]:
    protected = _is_protected_path(url)
    for attempt in range(retries + 1):
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=40_000)
            # Protected paths (buying guides) need longer to clear the CF interstitial.
            if protected:
                initial_wait = 8_000 if attempt == 0 else 12_000
            else:
                initial_wait = 3_000 if attempt == 0 else 5_000
            await page.wait_for_timeout(initial_wait)
            await page.evaluate("window.scrollTo(0, Math.floor(document.body.scrollHeight * 0.4))")
            await page.wait_for_timeout(1_000)
            html = await page.content()
            # Detect Cloudflare challenge page — retry with longer wait
            if any(marker in html for marker in CF_CHALLENGE_MARKERS):
                if attempt < retries:
                    extra = 8_000 if protected else 4_000
                    await page.wait_for_timeout(extra)
                    continue
                return None, "Cloudflare challenge not resolved after retries"
            return html, None
        except Exception as e:
            if attempt < retries:
                await page.wait_for_timeout(3_000)
                continue
            return None, str(e)
    return None, "Max retries exceeded"


async def crawl(urls: list[str], out_dir: Path, delay: float = 1.5) -> list[dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    warmed_domains: set[str] = set()

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        ctx = await browser.new_context(user_agent=UA, viewport=VP)
        page = await ctx.new_page()

        for i, url in enumerate(urls):
            domain = urlparse(url).netloc.replace("www.", "")

            # Pre-warm CF session for blocked domains before their first subpage.
            # Skip warmup if this URL IS the homepage (avoid double-visiting).
            if domain in CF_SESSION_DOMAINS and domain not in warmed_domains:
                is_homepage = urlparse(url).path.strip("/") == ""
                if not is_homepage:
                    await _warmup_cf_domain(page, domain)
                    await asyncio.sleep(CF_DOMAIN_DELAY)
                warmed_domains.add(domain)

            print(f"[{i+1}/{len(urls)}] {url}")
            html, error = await fetch_page(page, url)

            if error:
                print(f"  ✗ {error}", file=sys.stderr)
                results.append({"url": url, "error": error})
            else:
                filename = url_to_filename(url)
                filepath = out_dir / filename
                filepath.write_text(html, encoding="utf-8")
                size_kb = len(html) / 1024
                # Sanity check: suspiciously small pages are likely CF block pages
                # that slipped through the marker check (e.g. custom CF templates).
                word_count = len(html.split())
                if word_count < 600:
                    print(f"  ⚠ {filename} ({size_kb:.0f} KB, {word_count} words — may be blocked)", file=sys.stderr)
                else:
                    print(f"  ✓ {filename} ({size_kb:.0f} KB, {word_count} words)")
                results.append({"url": url, "file": str(filepath), "size_bytes": len(html), "word_count": word_count, "suspected_block": word_count < 600})

            if i < len(urls) - 1:
                # Slow down for CF-protected domains (helps avoid re-triggering challenge)
                next_domain = urlparse(urls[i + 1]).netloc.replace("www.", "")
                effective_delay = CF_DOMAIN_DELAY if domain in CF_SESSION_DOMAINS or next_domain in CF_SESSION_DOMAINS else delay
                await asyncio.sleep(effective_delay)

        await browser.close()

    return results


def main():
    parser = argparse.ArgumentParser(description="Crawl HTML snapshots for AEO analysis")
    parser.add_argument("--urls", type=str, help="JSON array of URLs")
    parser.add_argument("--out", type=str, help="Output directory")
    parser.add_argument("--delay", type=float, default=1.5, help="Seconds between requests")
    args = parser.parse_args()

    if args.urls:
        try:
            urls = json.loads(args.urls)
        except json.JSONDecodeError:
            urls = [u.strip() for u in args.urls.splitlines() if u.strip()]
    else:
        urls = DEFAULT_URLS

    if not urls:
        print("No URLs to crawl", file=sys.stderr)
        sys.exit(1)

    if args.out:
        out_dir = Path(args.out)
    else:
        domain = urlparse(urls[0]).netloc.replace("www.", "")
        out_dir = Path("site-snapshots") / domain

    print(f"\nCrawling {len(urls)} URL(s) → {out_dir}/\n")
    results = asyncio.run(crawl(urls, out_dir, args.delay))

    saved = [r for r in results if "file" in r]
    failed = [r for r in results if "error" in r]

    print(f"\nDone: {len(saved)} saved, {len(failed)} failed")
    print(f"\nNext step — run local AEO audit:")
    print(f"  AEO_DIR={out_dir} AEO_LABEL='TGG' python run_aeo_local.py")

    if failed:
        for r in failed:
            print(f"  Failed: {r['url']} — {r['error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
