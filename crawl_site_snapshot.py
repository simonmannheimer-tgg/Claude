"""
Download HTML snapshots of a site for local agentic-seo analysis.

Usage:
    python crawl_site_snapshot.py                      # TGG defaults
    python crawl_site_snapshot.py --urls '["https://..."]' --out site-snapshots/custom

Outputs HTML files to site-snapshots/<domain>/ ready for:
    node .claude/optional/agentic-seo/repo/bin/aeo.js site-snapshots/<domain>/

Uses httpx (no curl/wget). Respects rate limits. Handles redirects and errors.
"""

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import httpx

DEFAULT_URLS = [
    "https://www.thegoodguys.com.au",
    "https://www.thegoodguys.com.au/televisions",
    "https://www.thegoodguys.com.au/air-conditioners",
    "https://www.thegoodguys.com.au/washing-machines",
    "https://www.thegoodguys.com.au/refrigerators",
    "https://www.thegoodguys.com.au/laptops-computers",
    "https://www.thegoodguys.com.au/vacuum-cleaners",
    "https://www.thegoodguys.com.au/buying-guide/best-tvs",
    "https://www.thegoodguys.com.au/buying-guide/best-air-conditioners",
    "https://www.thegoodguys.com.au/buying-guide/best-washing-machines",
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-AU,en;q=0.9",
}


def url_to_filename(url: str) -> str:
    """Convert a URL path to a safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index.html"
    # Replace slashes with dashes, strip unsafe chars
    safe = re.sub(r"[^a-zA-Z0-9_-]", "-", path.replace("/", "--"))
    return f"{safe}.html"


async def fetch_page(client: httpx.AsyncClient, url: str) -> tuple[str, str | None, str | None]:
    """Fetch a URL and return (url, html_content, error)."""
    try:
        resp = await client.get(url, follow_redirects=True, timeout=20)
        if resp.status_code == 200:
            return url, resp.text, None
        return url, None, f"HTTP {resp.status_code}"
    except httpx.TimeoutException:
        return url, None, "Timeout after 20s"
    except Exception as e:
        return url, None, str(e)


async def crawl(urls: list[str], out_dir: Path, delay: float = 1.0) -> list[dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []

    async with httpx.AsyncClient(headers=HEADERS) as client:
        for i, url in enumerate(urls):
            print(f"[{i+1}/{len(urls)}] {url}")
            _, html, error = await fetch_page(client, url)

            if error:
                print(f"  ✗ {error}", file=sys.stderr)
                results.append({"url": url, "error": error})
                continue

            filename = url_to_filename(url)
            filepath = out_dir / filename
            filepath.write_text(html, encoding="utf-8")
            size_kb = len(html) / 1024
            print(f"  ✓ {filename} ({size_kb:.0f} KB)")
            results.append({"url": url, "file": str(filepath), "size_bytes": len(html)})

            # Polite delay between requests
            if i < len(urls) - 1:
                await asyncio.sleep(delay)

    return results


def main():
    parser = argparse.ArgumentParser(description="Download HTML snapshots for AEO analysis")
    parser.add_argument("--urls", type=str, help="JSON array of URLs to crawl")
    parser.add_argument("--out", type=str, help="Output directory (default: site-snapshots/<domain>)")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests (default: 1.0)")
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

    # Derive output directory from first URL's domain
    if args.out:
        out_dir = Path(args.out)
    else:
        domain = urlparse(urls[0]).netloc.replace("www.", "")
        out_dir = Path("site-snapshots") / domain

    print(f"\nCrawling {len(urls)} URL(s) → {out_dir}/\n")
    results = asyncio.run(crawl(urls, out_dir, delay=args.delay))

    saved = [r for r in results if "file" in r]
    failed = [r for r in results if "error" in r]

    print(f"\nDone: {len(saved)} saved, {len(failed)} failed")
    print(f"\nRun AEO local audit:")
    print(f"  node .claude/optional/agentic-seo/repo/bin/aeo.js {out_dir}/")
    print(f"  node .claude/optional/agentic-seo/repo/bin/aeo.js --json {out_dir}/ > seo/outputs/aeo/local-audit.json")

    if failed:
        for r in failed:
            print(f"  Failed: {r['url']} — {r['error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
