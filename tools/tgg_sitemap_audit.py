#!/usr/bin/env python3
"""
TGG Sitemap Audit
Fetches all TGG sitemaps, checks each URL's HTTP status, canonical, and
breadcrumb, and writes results to a CSV.

Usage:
    python tools/tgg_sitemap_audit.py [--output data/sitemap_audit_latest.csv]
                                      [--workers 10]
                                      [--timeout 12]
                                      [--max-urls 0]    # 0 = no limit

Output columns:
    Sitemap | URL | Handle | Last Modified | HTTP Status | Error
    Canonical URL | Previous Breadcrumb URL | Category Path
"""

import argparse
import csv
import json
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

SITEMAPS = [
    "https://sitemap.thegoodguys.com.au/product_sitemap_1.xml",
    "https://sitemap.thegoodguys.com.au/product_sitemap_2.xml",
    "https://sitemap.thegoodguys.com.au/product_sitemap_3.xml",
    "https://sitemap.thegoodguys.com.au/product_sitemap_4.xml",
    "https://sitemap.thegoodguys.com.au/brand_sitemap_1.xml",
    "https://sitemap.thegoodguys.com.au/category_sitemap_1.xml",
    "https://sitemap.thegoodguys.com.au/content_sitemap_1.xml",
    "https://sitemap.thegoodguys.com.au/article_sitemap_1.xml",
    "https://sitemap.thegoodguys.com.au/storelocation_sitemap_1.xml",
]

COLUMNS = [
    "Sitemap", "URL", "Handle", "Last Modified",
    "HTTP Status", "Error", "Canonical URL",
    "Previous Breadcrumb URL", "Category Path",
]

USER_AGENT = "Mozilla/5.0 (compatible; TGG-SEO-Audit/1.0)"


def handle_from_url(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    # Shopify products: /products/<handle>
    if "/products/" in path:
        return path.split("/products/")[-1]
    # Fallback: last path segment
    return path.split("/")[-1]


def category_path_from_breadcrumb_url(breadcrumb_url: str) -> str:
    if not breadcrumb_url or breadcrumb_url == "N/A":
        return ""
    parsed = urlparse(breadcrumb_url)
    return parsed.path.rstrip("/") or "/"


def parse_sitemap(sitemap_url: str, timeout: int) -> list[tuple]:
    sitemap_name = sitemap_url.split("/")[-1]
    try:
        r = requests.get(
            sitemap_url, timeout=timeout,
            headers={"User-Agent": USER_AGENT}
        )
        r.raise_for_status()
    except Exception as e:
        print(f"  [WARN] Could not fetch {sitemap_name}: {e}", flush=True)
        return []

    root = ET.fromstring(r.content)
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    entries = []
    for url_tag in root.findall(f"{ns}url"):
        loc_tag = url_tag.find(f"{ns}loc")
        if loc_tag is None:
            continue
        loc = loc_tag.text.strip()
        lastmod_tag = url_tag.find(f"{ns}lastmod")
        lastmod = lastmod_tag.text if lastmod_tag is not None else "N/A"
        entries.append((sitemap_name, loc, lastmod))
    return entries


def scrape_url(entry: tuple, timeout: int, session: requests.Session) -> dict:
    sitemap_name, loc, lastmod = entry
    handle = handle_from_url(loc)
    result = {
        "Sitemap": sitemap_name,
        "URL": loc,
        "Handle": handle,
        "Last Modified": lastmod,
        "HTTP Status": "Error",
        "Error": "",
        "Canonical URL": "N/A",
        "Previous Breadcrumb URL": "N/A",
        "Category Path": "",
    }

    try:
        r = session.get(loc, timeout=timeout, allow_redirects=True)
        result["HTTP Status"] = r.status_code

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            # Canonical
            canonical_tag = soup.find("link", rel="canonical")
            if canonical_tag and canonical_tag.get("href"):
                result["Canonical URL"] = canonical_tag["href"]

            # Breadcrumb from JSON-LD
            for script_tag in soup.find_all("script", type="application/ld+json"):
                try:
                    data = json.loads(script_tag.string or "")
                    if data.get("@type") == "BreadcrumbList":
                        items = data.get("itemListElement", [])
                        if len(items) >= 2:
                            bc_url = items[-2]["item"]["@id"]
                            result["Previous Breadcrumb URL"] = bc_url
                            result["Category Path"] = category_path_from_breadcrumb_url(bc_url)
                        break
                except Exception:
                    continue

    except requests.exceptions.Timeout:
        result["Error"] = "Timeout"
    except requests.exceptions.ConnectionError:
        result["Error"] = "Connection error"
    except Exception as e:
        result["Error"] = str(e)[:120]

    return result


def main():
    parser = argparse.ArgumentParser(description="TGG Sitemap Audit")
    parser.add_argument(
        "--output", default="data/sitemap_audit_latest.csv",
        help="Output CSV path (default: data/sitemap_audit_latest.csv)"
    )
    parser.add_argument(
        "--workers", type=int, default=10,
        help="Concurrent HTTP workers (default: 10)"
    )
    parser.add_argument(
        "--timeout", type=int, default=12,
        help="Request timeout in seconds (default: 12)"
    )
    parser.add_argument(
        "--max-urls", type=int, default=0,
        help="Max URLs to process per sitemap (0 = no limit, for testing)"
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n=== TGG Sitemap Audit — {datetime.now().strftime('%Y-%m-%d %H:%M')} ===\n")

    # ── Step 1: Parse all sitemaps ──────────────────────────────────────────
    print("Fetching sitemaps...", flush=True)
    all_entries = []
    for sm in SITEMAPS:
        entries = parse_sitemap(sm, args.timeout)
        if args.max_urls > 0:
            entries = entries[: args.max_urls]
        print(f"  {sm.split('/')[-1]}: {len(entries)} URLs", flush=True)
        all_entries.extend(entries)

    # Deduplicate — last-seen sitemap wins per URL
    unique: dict = {}
    for sitemap_name, loc, lastmod in all_entries:
        unique[loc] = (sitemap_name, lastmod)
    all_entries = [(v[0], k, v[1]) for k, v in unique.items()]
    print(f"\nTotal unique URLs to process: {len(all_entries)}", flush=True)

    # ── Step 2: Scrape concurrently ─────────────────────────────────────────
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    results = []
    start_time = time.time()
    completed = 0

    print(f"Scraping with {args.workers} workers...\n", flush=True)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(scrape_url, entry, args.timeout, session): entry
            for entry in all_entries
        }
        for future in as_completed(futures):
            results.append(future.result())
            completed += 1
            if completed % 100 == 0 or completed == len(all_entries):
                elapsed = time.time() - start_time
                rate = completed / elapsed if elapsed > 0 else 0
                eta = (len(all_entries) - completed) / rate if rate > 0 else 0
                print(
                    f"  {completed}/{len(all_entries)} URLs "
                    f"({elapsed:.0f}s elapsed, ~{eta:.0f}s remaining)",
                    flush=True,
                )

    elapsed = time.time() - start_time
    print(f"\nCompleted {len(results)} URLs in {elapsed:.1f}s", flush=True)

    # ── Step 3: Write output ────────────────────────────────────────────────
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    print(f"\nOutput: {output_path} ({len(results)} rows)")

    # Status summary
    from collections import Counter
    statuses = Counter(str(r["HTTP Status"]) for r in results)
    print("\nHTTP status breakdown:")
    for status, count in statuses.most_common():
        print(f"  {status}: {count}")

    # Category path coverage
    with_breadcrumb = sum(1 for r in results if r["Category Path"])
    print(f"\nBreadcrumb coverage: {with_breadcrumb}/{len(results)} "
          f"({with_breadcrumb/len(results)*100:.1f}%)")

    # GitHub Actions step summary
    summary_path = Path(
        __import__("os").environ.get("GITHUB_STEP_SUMMARY", "/dev/null")
    )
    if summary_path.name != "null":
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(f"## TGG Sitemap Audit\n\n")
            f.write(f"- **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}\n")
            f.write(f"- **Total URLs:** {len(results)}\n")
            f.write(f"- **Breadcrumb coverage:** {with_breadcrumb} URLs "
                    f"({with_breadcrumb/len(results)*100:.1f}%)\n")
            f.write(f"- **Output:** `{output_path}`\n\n")
            f.write("### HTTP Status Breakdown\n\n")
            for status, count in statuses.most_common():
                f.write(f"- `{status}`: {count}\n")


if __name__ == "__main__":
    main()
