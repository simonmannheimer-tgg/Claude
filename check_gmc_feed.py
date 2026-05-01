"""
GMC (Google Merchant Centre) feed completeness checker.

Fetches or reads a local GMC product feed (XML/TSV/CSV) and reports:
- Required field completeness %
- Optional field completeness %
- Missing field counts per field name
- Per-product issues (sample)

Usage:
    python check_gmc_feed.py --feed https://www.thegoodguys.com.au/feed.xml
    python check_gmc_feed.py --feed inbox/products.xml
    python check_gmc_feed.py --feed inbox/products.tsv --format tsv

Writes:
    seo/outputs/aeo/gmc-feed-<label>-YYYYMMDD-HHMM.json
"""

import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

import httpx

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

# Google Merchant Centre required fields
GMC_REQUIRED = [
    "id",
    "title",
    "description",
    "link",
    "image_link",
    "availability",
    "price",
    "brand",
    "condition",
]

# Fields that significantly boost AI/Shopping visibility
GMC_IMPORTANT = [
    "gtin",
    "mpn",
    "google_product_category",
    "product_type",
]

# Recommended optional fields
GMC_OPTIONAL = [
    "additional_image_link",
    "sale_price",
    "sale_price_effective_date",
    "product_detail",
    "product_highlight",
    "shipping",
    "tax",
    "size",
    "color",
    "age_group",
    "gender",
    "material",
    "pattern",
    "item_group_id",
    "custom_label_0",
    "custom_label_1",
    "loyalty_points",
    "installment",
]

# XML namespace for Google Shopping feed
GMC_NS = "http://base.google.com/ns/1.0"


def _extract_xml_products(content: str) -> list[dict]:
    """Parse RSS/Atom XML feed — handles Google Shopping and standard RSS formats."""
    products = []
    try:
        root = ET.fromstring(content)
        channel = root.find("channel")
        items = (channel or root).findall("item")
        if not items:
            items = root.findall(".//{http://www.w3.org/2005/Atom}entry")

        for item in items:
            product = {}
            # Try Google namespace fields first
            for field in GMC_REQUIRED + GMC_IMPORTANT + GMC_OPTIONAL:
                el = item.find(f"{{{GMC_NS}}}{field}")
                if el is None:
                    # Fall back to plain tag
                    el = item.find(field.replace("_", "-")) or item.find(field)
                if el is not None and el.text:
                    product[field] = el.text.strip()
            # Standard RSS fields
            for tag, field in [("title", "title"), ("description", "description"),
                                ("link", "link"), ("g:id", "id")]:
                if field not in product:
                    el = item.find(tag)
                    if el is not None and el.text:
                        product[field] = el.text.strip()
            if product:
                products.append(product)
    except ET.ParseError as e:
        print(f"XML parse error: {e}", file=sys.stderr)
    return products


def _extract_tsv_products(content: str, delimiter: str = "\t") -> list[dict]:
    """Parse TSV/CSV feed."""
    reader = csv.DictReader(io.StringIO(content), delimiter=delimiter)
    products = []
    for row in reader:
        # Normalise header names: spaces→underscores, strip BOM
        product = {k.strip().lstrip("﻿").replace(" ", "_").lower(): v.strip()
                   for k, v in row.items() if v and v.strip()}
        if product:
            products.append(product)
    return products


def _detect_format(content: str, filename: str) -> str:
    if filename.endswith(".tsv") or filename.endswith(".txt"):
        return "tsv"
    if filename.endswith(".csv"):
        return "csv"
    if content.strip().startswith("<"):
        return "xml"
    # Heuristic: if first line has many tabs it's TSV
    first_line = content.split("\n")[0]
    if first_line.count("\t") >= 5:
        return "tsv"
    return "xml"


def analyse_feed(products: list[dict]) -> dict:
    """Compute completeness stats across all products."""
    if not products:
        return {"error": "No products found in feed"}

    total = len(products)
    all_fields = GMC_REQUIRED + GMC_IMPORTANT + GMC_OPTIONAL

    # Count presence per field
    field_counts: dict[str, int] = {f: 0 for f in all_fields}
    for product in products:
        for field in all_fields:
            if product.get(field):
                field_counts[field] += 1

    # Required completeness
    required_pcts = {f: round(field_counts[f] / total * 100) for f in GMC_REQUIRED}
    important_pcts = {f: round(field_counts[f] / total * 100) for f in GMC_IMPORTANT}
    optional_pcts = {f: round(field_counts[f] / total * 100) for f in GMC_OPTIONAL}

    required_avg = round(sum(required_pcts.values()) / len(GMC_REQUIRED))
    important_avg = round(sum(important_pcts.values()) / len(GMC_IMPORTANT))
    optional_avg = round(sum(optional_pcts.values()) / len(GMC_OPTIONAL))

    # Missing field counts
    missing_required = {f: total - field_counts[f] for f in GMC_REQUIRED if field_counts[f] < total}
    missing_important = {f: total - field_counts[f] for f in GMC_IMPORTANT if field_counts[f] < total}

    # GTIN validation sample
    gtin_valid = 0
    gtin_invalid = 0
    gtin_missing = total - field_counts.get("gtin", 0)
    for product in products[:1000]:  # cap at 1000 for performance
        gtin = product.get("gtin", "")
        if gtin:
            digits = re.sub(r'\D', '', gtin)
            if len(digits) in (8, 12, 13, 14):
                total_check = 0
                for i, d in enumerate(reversed(digits[:-1])):
                    n = int(d)
                    total_check += n * 3 if i % 2 == 0 else n
                check = (10 - total_check % 10) % 10
                if check == int(digits[-1]):
                    gtin_valid += 1
                else:
                    gtin_invalid += 1

    # Sample issues
    issues = []
    for product in products[:5]:
        p_missing = [f for f in GMC_REQUIRED if not product.get(f)]
        if p_missing:
            pid = product.get("id", product.get("link", "unknown"))[:60]
            issues.append({"id": pid, "missing_required": p_missing})

    # Score (0-30 pts, used in Phase 3)
    score = round(required_avg * 0.15 + important_avg * 0.1 + optional_avg * 0.05)
    score = min(score, 30)
    pct = round(score / 30 * 100)

    def grade(p):
        if p >= 90: return "A"
        if p >= 75: return "B"
        if p >= 60: return "C"
        if p >= 40: return "D"
        return "F"

    return {
        "total_products": total,
        "required_completeness_pct": required_avg,
        "important_completeness_pct": important_avg,
        "optional_completeness_pct": optional_avg,
        "field_completeness": {**required_pcts, **important_pcts},
        "missing_required": missing_required,
        "missing_important": missing_important,
        "gtin_valid": gtin_valid,
        "gtin_invalid": gtin_invalid,
        "gtin_missing": gtin_missing,
        "sample_issues": issues,
        "score": score,
        "maxScore": 30,
        "percentage": pct,
        "grade": grade(pct),
        "summary": (
            f"{total} products | required: {required_avg}% | "
            f"GTIN: {field_counts.get('gtin',0)}/{total} present, {gtin_invalid} invalid"
        ),
    }


def fetch_or_read(source: str) -> tuple[str, str]:
    """Returns (content, filename)."""
    if source.startswith("http://") or source.startswith("https://"):
        resp = httpx.get(source, timeout=30, follow_redirects=True,
                         headers={"User-Agent": BROWSER_UA})
        resp.raise_for_status()
        filename = urlparse(source).path.split("/")[-1] or "feed.xml"
        return resp.text, filename
    path = Path(source)
    return path.read_text(encoding="utf-8", errors="ignore"), path.name


def main():
    parser = argparse.ArgumentParser(description="Check GMC feed completeness")
    parser.add_argument("--feed", required=True, help="Feed URL or local file path")
    parser.add_argument("--format", choices=["xml", "tsv", "csv", "auto"], default="auto",
                        help="Feed format (default: auto-detect)")
    parser.add_argument("--label", default="", help="Label for output filename")
    args = parser.parse_args()

    print(f"Fetching feed: {args.feed}")
    content, filename = fetch_or_read(args.feed)
    print(f"  {len(content):,} chars")

    fmt = args.format if args.format != "auto" else _detect_format(content, filename)
    print(f"  Format: {fmt}")

    if fmt == "xml":
        products = _extract_xml_products(content)
    elif fmt in ("tsv", "csv"):
        delim = "\t" if fmt == "tsv" else ","
        products = _extract_tsv_products(content, delim)
    else:
        print("Unknown format", file=sys.stderr)
        sys.exit(1)

    print(f"  {len(products)} products extracted")

    result = analyse_feed(products)

    print(f"\nGMC Feed: {result.get('grade','?')} ({result.get('percentage',0)}%)")
    print(f"  Required: {result.get('required_completeness_pct',0)}%")
    print(f"  Important (GTIN/MPN/category): {result.get('important_completeness_pct',0)}%")
    if result.get("missing_required"):
        print("  Missing required fields:")
        for f, n in sorted(result["missing_required"].items(), key=lambda x: -x[1]):
            print(f"    {f}: {n} products missing")

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    label = args.label or re.sub(r'[^a-z0-9-]', '-', filename.lower().replace('.', '-'))
    out_file = out_dir / f"gmc-feed-{label}-{ts}.json"
    out_file.write_text(json.dumps(result, indent=2))
    print(f"\nSaved {out_file}")


if __name__ == "__main__":
    main()
