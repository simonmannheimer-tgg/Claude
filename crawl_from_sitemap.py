"""
Sitemap-driven site crawler for AEO analysis.

Fetches a domain's sitemap index, categorises URLs by page type, samples N per
type, then crawls using Playwright. Output files land in site-snapshots/<domain>/
and are ready for run_ecommerce_aeo.py and run_content_aeo.py.

Usage:
    python crawl_from_sitemap.py --domain thegoodguys.com.au
    python crawl_from_sitemap.py --domain thegoodguys.com.au --sample 5 --types category,guide
    python crawl_from_sitemap.py --domain jbhifi.com.au --sample 3 --out site-snapshots/jbhifi/
    python crawl_from_sitemap.py --domain thegoodguys.com.au --list-only  # show URLs, no crawl

Requires:
    pip install playwright httpx beautifulsoup4
    playwright install chromium --with-deps
"""

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup

# Reuse Playwright crawl logic from crawl_site_snapshot
from crawl_site_snapshot import crawl, url_to_filename

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

ALL_TYPES = ["home", "category", "product", "guide", "blog", "other"]


# ── Sitemap fetching ──────────────────────────────────────────────────────────

def _fetch_xml(url: str) -> str | None:
    try:
        resp = httpx.get(url, timeout=20, follow_redirects=True,
                         headers={"User-Agent": BROWSER_UA})
        if resp.status_code == 200:
            return resp.text
        return None
    except Exception:
        return None


def fetch_sitemap_index(domain: str) -> list[str]:
    """
    Fetches sitemap index for domain. Returns list of child sitemap URLs.
    Tries /sitemap_index.xml, /sitemap.xml, /sitemap-index.xml in order.
    If a sitemap index is found, returns child sitemap URLs.
    If a regular sitemap is found, returns the sitemap URL itself.
    """
    base = f"https://www.{domain}" if not domain.startswith("http") else domain
    for path in ["/sitemap_index.xml", "/sitemap.xml", "/sitemap-index.xml"]:
        content = _fetch_xml(f"{base}{path}")
        if not content:
            continue
        if "<sitemapindex" in content:
            locs = re.findall(r'<loc>([^<]+)</loc>', content)
            return [l.strip() for l in locs]
        if "<urlset" in content:
            return [f"{base}{path}"]
    return []


def fetch_sitemap_urls(sitemap_url: str) -> list[str]:
    """Parses <loc> tags from a single sitemap XML."""
    content = _fetch_xml(sitemap_url)
    if not content:
        return []
    return [l.strip() for l in re.findall(r'<loc>([^<]+)</loc>', content)]


def fetch_all_urls(domain: str, max_sitemaps: int = 10) -> list[str]:
    """Fetches all URLs from the domain's sitemap hierarchy."""
    child_sitemaps = fetch_sitemap_index(domain)
    if not child_sitemaps:
        print(f"  ✗ No sitemap found for {domain}", file=sys.stderr)
        return []

    print(f"  Found {len(child_sitemaps)} child sitemap(s)")
    all_urls: list[str] = []
    for sitemap in child_sitemaps[:max_sitemaps]:
        urls = fetch_sitemap_urls(sitemap)
        all_urls.extend(urls)
        print(f"  {sitemap}: {len(urls)} URLs")

    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for u in all_urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)

    print(f"  Total unique URLs: {len(unique)}")
    return unique


# ── URL classification ────────────────────────────────────────────────────────

_GENERIC_PRODUCT_RE = re.compile(r'(?:/p/|-\d{6,}|/products?/|/sku/)', re.IGNORECASE)
_GENERIC_GUIDE_RE   = re.compile(r'/(?:buying-guide|guide|advice|how-to|reviews?)/', re.IGNORECASE)
_GENERIC_BLOG_RE    = re.compile(r'/(?:blog|news|whats-new|editorial|magazine|stories?)(?:/|$)', re.IGNORECASE)
_TGG_MODEL_RE       = re.compile(r'(?:/|-)(?=[^-/]*[a-z])(?=[^-/]*\d[^-/]*\d[^-/]*\d[^-/]*\d)[a-z0-9]+(?:-|$|/)', re.IGNORECASE)

_DOMAIN_PATTERNS: dict[str, list[tuple[str, re.Pattern]]] = {
    "jbhifi.com.au": [
        ("product",  re.compile(r'^/products/')),
        ("blog",     re.compile(r'^/blogs/')),
        ("guide",    re.compile(r'^/pages/.*(?:guide|advice|help)', re.I)),
        ("category", re.compile(r'^/collections/')),
    ],
    "harveynorman.com.au": [
        ("product",  re.compile(r'\.html$')),
        ("guide",    re.compile(r'^/buying-guides/')),
        ("brand",    re.compile(r'^/brands/')),
    ],
    "appliancesonline.com.au": [
        ("product",  re.compile(r'^/p/')),
        ("category", re.compile(r'^/(?:category|filter)/')),
        ("brand",    re.compile(r'^/brand/')),
        ("guide",    re.compile(r'^/article/')),
        ("blog",     re.compile(r'^/article/')),
    ],
}


def classify_url(url: str) -> str:
    """Returns: home | category | product | guide | blog | brand | other"""
    parsed = urlparse(url)
    path   = parsed.path.rstrip("/")
    domain = re.sub(r'^www\.', '', parsed.hostname or '')

    if not path or path == "/":
        return "home"

    domain_rules = _DOMAIN_PATTERNS.get(domain)
    if domain_rules:
        for page_type, pattern in domain_rules:
            if pattern.search(path):
                return page_type
        if domain == "harveynorman.com.au":
            segments = [s for s in path.split("/") if s]
            if len(segments) >= 2:
                return "category"
        return "other"

    # Generic / TGG
    if _GENERIC_GUIDE_RE.search(path):   return "guide"
    if _GENERIC_BLOG_RE.search(path):    return "blog"
    if _GENERIC_PRODUCT_RE.search(path): return "product"
    if _TGG_MODEL_RE.search(path):       return "product"
    segments = [s for s in path.split("/") if s]
    if 1 <= len(segments) <= 2 and not parsed.query:
        return "category"
    return "other"


def sample_by_type(urls: list[str], types: list[str], n: int) -> list[str]:
    """Returns up to n URLs per requested type, preserving sitemap order."""
    buckets: dict[str, list[str]] = {t: [] for t in types}

    for url in urls:
        page_type = classify_url(url)
        if page_type in buckets and len(buckets[page_type]) < n:
            buckets[page_type].append(url)

    selected: list[str] = []
    for t in types:
        selected.extend(buckets[t])

    return selected


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Crawl a site via its sitemap for AEO analysis"
    )
    parser.add_argument("--domain", required=True,
                        help="Domain to crawl (e.g. thegoodguys.com.au)")
    parser.add_argument("--sample", type=int, default=5,
                        help="URLs to sample per page type (default: 5)")
    parser.add_argument("--types", type=str, default="home,category,product,guide,blog",
                        help="Comma-separated page types to include (default: home,category,product,guide,blog)")
    parser.add_argument("--out", type=str, default="",
                        help="Output directory (default: site-snapshots/<domain>/)")
    parser.add_argument("--list-only", action="store_true",
                        help="List sampled URLs and exit without crawling")
    parser.add_argument("--delay", type=float, default=1.5,
                        help="Seconds between page requests (default: 1.5)")
    parser.add_argument("--max-sitemaps", type=int, default=10,
                        help="Max child sitemaps to fetch (default: 10)")
    args = parser.parse_args()

    types = [t.strip() for t in args.types.split(",") if t.strip()]
    invalid = [t for t in types if t not in ALL_TYPES]
    if invalid:
        print(f"Unknown page types: {invalid}. Valid: {ALL_TYPES}", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out) if args.out else Path(f"site-snapshots/{args.domain}")

    print(f"Fetching sitemap for {args.domain}...")
    all_urls = fetch_all_urls(args.domain, max_sitemaps=args.max_sitemaps)
    if not all_urls:
        sys.exit(1)

    sampled = sample_by_type(all_urls, types, args.sample)
    if not sampled:
        print(f"No URLs matched types {types}", file=sys.stderr)
        sys.exit(1)

    print(f"\nSampled {len(sampled)} URL(s) across types {types}:")
    by_type: dict[str, list[str]] = {}
    for url in sampled:
        t = classify_url(url)
        by_type.setdefault(t, []).append(url)
    for t, urls in by_type.items():
        for url in urls:
            print(f"  [{t}] {url}")

    if args.list_only:
        list_path = out_dir.parent / f"sitemap-sample-{args.domain}.json"
        list_path.parent.mkdir(parents=True, exist_ok=True)
        list_path.write_text(json.dumps({
            "domain": args.domain,
            "total_sitemap_urls": len(all_urls),
            "sampled": len(sampled),
            "by_type": by_type,
        }, indent=2))
        print(f"\nList saved to {list_path} (no crawl)")
        return

    print(f"\nCrawling {len(sampled)} URL(s) → {out_dir}/")
    results = asyncio.run(crawl(sampled, out_dir, delay=args.delay))

    ok = sum(1 for r in results if "error" not in r)
    print(f"\nDone: {ok}/{len(results)} pages saved to {out_dir}/")

    manifest = out_dir / "sitemap-crawl-manifest.json"
    manifest.write_text(json.dumps({
        "domain": args.domain,
        "types": types,
        "sample_per_type": args.sample,
        "total_sitemap_urls": len(all_urls),
        "crawled": len(results),
        "ok": ok,
        "results": results,
    }, indent=2))
    print(f"Manifest: {manifest}")


if __name__ == "__main__":
    main()
