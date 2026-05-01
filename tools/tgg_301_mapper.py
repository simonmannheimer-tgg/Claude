#!/usr/bin/env python3
"""
TGG 301 Redirect Mapper
Applies Simon's redirect rules to a raw URL mapping CSV and produces
a Shopify-ready import file plus a structured manual-review file.

Primary breadcrumb source: sitemap audit CSV (data/sitemap_audit_latest.csv)
Fallback: Shopify Products.csv export

Usage:
    python tools/tgg_301_mapper.py \\
        --mappings  data/redirects/url_mappings_latest.csv \\
        --sitemap   data/sitemap_audit_latest.csv \\
        [--products data/products.csv] \\
        [--existing-ready  path/to/other_ai_ready.csv] \\
        [--existing-review path/to/other_ai_review.csv] \\
        [--output-dir seo/outputs/redirects]

Outputs (written to --output-dir):
    final_shopify_import_ready.csv   — 2-col Shopify import, rule-compliant
    final_shopify_import_review.csv  — manual review queue with notes
    my_shopify_import_ready.csv      — my raw ready (pre-merge)
    my_shopify_import_review.csv     — my raw review (pre-merge)
    my_comparison_report.csv         — diff vs other AI (if provided)
"""

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

CONF_THRESHOLD = 0.92


# ── 1. Load sitemap audit (primary breadcrumb source) ─────────────────────────

def load_sitemap_index(path: Path) -> dict:
    """
    Returns: handle (lower) -> {category_path, http_status, url}
    Reads 'Handle', 'Category Path', 'HTTP Status', 'URL' columns.
    Prefers 200-status entries when there are duplicates.
    """
    index = {}
    if not path or not path.exists():
        return index

    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            handle = (row.get("Handle") or "").strip().lower()
            cat_path = (row.get("Category Path") or "").strip()
            status = (row.get("HTTP Status") or "").strip()
            url = (row.get("URL") or "").strip()
            if not handle:
                continue
            # Prefer 200 entries; don't overwrite a 200 with a non-200
            existing = index.get(handle)
            if existing and existing.get("http_status") == "200" and status != "200":
                continue
            index[handle] = {
                "category_path": cat_path,
                "http_status": status,
                "url": url,
            }
    return index


# ── 2. Load Products.csv fallback ─────────────────────────────────────────────

def load_products(path: Path) -> dict:
    """Returns: handle (lower) -> {breadcrumb, status}"""
    products = {}
    if not path or not path.exists():
        return products

    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            handle = (row.get("Handle") or "").strip().lower()
            breadcrumb = (
                row.get("Metafield: tgg.breadcrumb [single_line_text_field]") or ""
            ).strip()
            status = (row.get("Status") or "").strip()
            if handle:
                if handle not in products or status == "Active":
                    products[handle] = {"breadcrumb": breadcrumb, "status": status}
    return products


def breadcrumb_to_path(breadcrumb: str) -> str:
    """'l1_l2_l3' -> '/l1/l2/l3'"""
    if not breadcrumb:
        return ""
    return "/" + breadcrumb.replace("_", "/")


# ── 3. Category path lookup (sitemap first, Products.csv fallback) ─────────────

def get_category_path(handle: str, sitemap: dict, products: dict) -> str:
    """Return the best available category path for a product handle."""
    h = handle.lower()
    # Sitemap: prefer 200 entries with a category path
    sm = sitemap.get(h)
    if sm and sm["category_path"]:
        return sm["category_path"]
    # Products.csv fallback
    prod = products.get(h)
    if prod and prod["breadcrumb"]:
        return breadcrumb_to_path(prod["breadcrumb"])
    return ""


def handle_is_live(handle: str, sitemap: dict) -> bool:
    """True if the handle appears in the sitemap with a 200 status."""
    entry = sitemap.get(handle.lower())
    return bool(entry and entry.get("http_status") == "200")


# ── 4. URL helpers ────────────────────────────────────────────────────────────

def strip_query(url: str) -> str:
    return url.split("?")[0] if "?" in url else url


def fix_double_dash(url: str) -> str:
    return re.sub(r"-{2,}", "-", url)


def is_malformed(url: str) -> tuple[bool, list[str]]:
    reasons = []
    if "?" in url:
        reasons.append("query-string")
    if re.search(r"-{2,}", url):
        reasons.append("double-dash")
    if url.startswith("/product/"):
        reasons.append("legacy-product-prefix")
    if re.search(r"[{}\[\])]", url):
        reasons.append("garbage-chars")
    if re.search(r"[bcdfghjklmnpqrstvwxyz]{6,}", url, re.IGNORECASE):
        reasons.append("garbled-text")
    return bool(reasons), reasons


def path_segments(url: str) -> list[str]:
    return [p for p in url.strip("/").split("/") if p]


def is_product_handle(url: str, sitemap: dict, products: dict) -> bool:
    segs = path_segments(url)
    if len(segs) != 1:
        return False
    handle = segs[0].lower()
    if handle in sitemap or handle in products:
        return True
    # Heuristic: long handle with digits = product
    if len(handle) >= 25 and re.search(r"\d", handle):
        return True
    if re.search(r"-\d{6,8}$", handle):
        return True
    return False


def is_likely_brand_category(url: str, sitemap: dict, products: dict) -> bool:
    segs = path_segments(url)
    if len(segs) != 1:
        return False
    handle = segs[0].lower()
    if handle in sitemap or handle in products:
        return False
    return len(handle) < 25 and not re.search(r"\d", handle)


def is_category_path(url: str, sitemap: dict, products: dict) -> bool:
    segs = path_segments(url)
    if len(segs) > 1:
        return True
    return is_likely_brand_category(url, sitemap, products)


def is_valid_category_dest(url: str) -> bool:
    return len(path_segments(url)) >= 2


# ── 5. Core decision logic ────────────────────────────────────────────────────

NO_BREADCRUMB_CLASSES = {
    "product->review-no-breadcrumb",
    "malformed->product-no-breadcrumb",
    "malformed->review",
    "unknown",
}
REVIEW_ONLY_CLASSES = {
    "category-low-conf",
    "product->category-low-conf",
}


def remap(source: str, destination: str, confidence: float,
          sitemap: dict, products: dict) -> dict:
    malformed, mal_reasons = is_malformed(source)

    # ── Rule 2: malformed source ──────────────────────────────────────────────
    if malformed:
        clean = fix_double_dash(strip_query(source))
        clean_handle = clean.lstrip("/").lower()

        # 2a: clean version is a live product → redirect to it
        if handle_is_live(clean_handle, sitemap):
            return dict(
                final_dest=clean, needs_review=False, review_reason=None,
                classification="malformed->clean-product",
                rule_applied="Rule 2: malformed; clean version is live",
            )

        # 2b: destination already a multi-segment category
        if is_category_path(destination, sitemap, products):
            return dict(
                final_dest=destination, needs_review=False, review_reason=None,
                classification="malformed->category",
                rule_applied="Rule 2: malformed; destination already category",
            )

        # 2c: destination is a known product → look up category
        dest_handle = destination.lstrip("/").lower()
        cat = get_category_path(dest_handle, sitemap, products)
        if cat and dest_handle in sitemap or dest_handle in products:
            return dict(
                final_dest=cat, needs_review=False, review_reason=None,
                classification="malformed->category-via-lookup",
                rule_applied="Rule 2+1: malformed; dest product -> category",
            )

        # 2c-heuristic: looks like product, no category data
        if is_product_handle(destination, sitemap, products):
            return dict(
                final_dest=destination, needs_review=True,
                review_reason="malformed source; dest looks like product, no category — assign manually",
                classification="malformed->product-no-breadcrumb",
                rule_applied="Rule 2: malformed; dest likely product, no category",
            )

        # 2d: unresolvable
        return dict(
            final_dest=destination, needs_review=True,
            review_reason=f"malformed ({', '.join(mal_reasons)}); destination unresolvable",
            classification="malformed->review",
            rule_applied="Rule 2: malformed; unresolvable",
        )

    # ── Rule 1: product -> category ───────────────────────────────────────────
    dest_handle = destination.lstrip("/").lower()
    if is_product_handle(destination, sitemap, products):
        cat = get_category_path(dest_handle, sitemap, products)
        if cat:
            if confidence < CONF_THRESHOLD:
                return dict(
                    final_dest=cat, needs_review=True,
                    review_reason=f"product->category (conf={confidence:.2f} < {CONF_THRESHOLD}); verify",
                    classification="product->category-low-conf",
                    rule_applied="Rule 1 + low conf: product -> category",
                )
            return dict(
                final_dest=cat, needs_review=False, review_reason=None,
                classification="product->category",
                rule_applied="Rule 1: product -> category",
            )
        return dict(
            final_dest=destination, needs_review=True,
            review_reason="product destination; no category found — assign manually",
            classification="product->review-no-breadcrumb",
            rule_applied="Rule 1: product; no category available",
        )

    # ── Category / brand already correct ─────────────────────────────────────
    if is_category_path(destination, sitemap, products):
        if confidence < CONF_THRESHOLD:
            return dict(
                final_dest=destination, needs_review=True,
                review_reason=f"category dest (conf={confidence:.2f} < {CONF_THRESHOLD}); verify",
                classification="category-low-conf",
                rule_applied="Category dest; low confidence",
            )
        return dict(
            final_dest=destination, needs_review=False, review_reason=None,
            classification="category",
            rule_applied="Category/brand dest already correct",
        )

    return dict(
        final_dest=destination, needs_review=True,
        review_reason="unclassified destination",
        classification="unknown",
        rule_applied="Unclassified",
    )


# ── 6. Process mappings ───────────────────────────────────────────────────────

def process_mappings(mapping_path: Path, sitemap: dict, products: dict):
    ready, review = [], []
    with open(mapping_path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            source = (row.get("Redirect from") or "").strip()
            destination = (row.get("Redirect to") or "").strip()
            try:
                confidence = float((row.get("confidence") or "1").strip())
            except ValueError:
                confidence = 1.0
            if not source:
                continue

            result = remap(source, destination, confidence, sitemap, products)
            base = dict(
                source=source, original_dest=destination,
                confidence=confidence, classification=result["classification"],
                rule=result["rule_applied"],
            )
            if result["needs_review"]:
                review.append({**base, "suggested": result["final_dest"],
                                "notes": result["review_reason"]})
            else:
                ready.append({**base, "final_dest": result["final_dest"]})
    return ready, review


# ── 7. Load other AI output ───────────────────────────────────────────────────

def load_other_ai(ready_path: Path, review_path: Path):
    other_ready = {}
    if ready_path and ready_path.exists():
        with open(ready_path, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                src = (row.get("Redirect from") or "").strip()
                dst = (row.get("Redirect to") or "").strip()
                if src:
                    other_ready[src] = dst

    other_review = {}
    if review_path and review_path.exists():
        with open(review_path, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                src = (row.get("Redirect from") or "").strip()
                if src:
                    other_review[src] = {
                        "suggested": (row.get("Suggested redirect to") or "").strip(),
                        "notes": (row.get("Notes") or "").strip(),
                    }
    return other_ready, other_review


# ── 8. Hybrid merge ───────────────────────────────────────────────────────────

def produce_final(my_ready, my_review, other_ready, other_review, comparison):
    my_ready_map = {r["source"]: r for r in my_ready}
    my_review_map = {r["source"]: r for r in my_review}

    final_ready, final_review = [], []
    seen = set()

    for row in comparison:
        src = row["source"]
        if src in seen:
            continue
        seen.add(src)

        my_r = my_ready_map.get(src)
        my_rv = my_review_map.get(src)
        my_class = row["my_class"]
        other_dest = row["other_dest"]
        other_status = row["other_status"]

        # Confident, rule-compliant ready row
        if my_r and my_class not in NO_BREADCRUMB_CLASSES | REVIEW_ONLY_CLASSES:
            final_ready.append(
                {"Redirect from": src, "Redirect to": my_r["final_dest"]}
            )
            continue

        # No breadcrumb — use other AI's category if it's valid
        if my_class in NO_BREADCRUMB_CLASSES:
            if other_status == "ready" and is_valid_category_dest(other_dest):
                final_ready.append({"Redirect from": src, "Redirect to": other_dest})
            else:
                suggested = (
                    my_rv["suggested"] if my_rv else (other_dest if other_dest != "-" else "-")
                )
                final_review.append({
                    "Redirect from": src,
                    "Redirect to": suggested,
                    "Notes": my_rv["notes"] if my_rv else "no category available",
                    "Classification": my_class,
                })
            continue

        # Low confidence — always review
        if my_class in REVIEW_ONLY_CLASSES:
            my_dest = my_r["final_dest"] if my_r else (my_rv["suggested"] if my_rv else "-")
            note = my_rv["notes"] if my_rv else "low confidence; verify destination"
            extra = (
                f" | other-AI: {other_dest}"
                if other_dest != "-" and is_valid_category_dest(other_dest)
                else ""
            )
            final_review.append({
                "Redirect from": src, "Redirect to": my_dest,
                "Notes": note + extra, "Classification": my_class,
            })
            continue

        # External source (not in url_mappings)
        if row["agreement"] == "ONLY-IN-OTHER":
            final_review.append({
                "Redirect from": src,
                "Redirect to": other_dest if other_dest != "-" else "-",
                "Notes": "not in url_mappings; from other AI source — verify",
                "Classification": "external-source",
            })
            continue

        # Fallback
        if my_r:
            final_ready.append({"Redirect from": src, "Redirect to": my_r["final_dest"]})
        elif my_rv:
            final_review.append({
                "Redirect from": src, "Redirect to": my_rv["suggested"],
                "Notes": my_rv["notes"], "Classification": my_rv["classification"],
            })

    return final_ready, final_review


# ── 9. Comparison ─────────────────────────────────────────────────────────────

def compare(my_ready, my_review, other_ready, other_review):
    my_ready_map = {r["source"]: r for r in my_ready}
    my_review_map = {r["source"]: r for r in my_review}
    all_sources = (
        set(my_ready_map) | set(my_review_map) | set(other_ready) | set(other_review)
    )
    comparison = []

    for src in sorted(all_sources):
        my_r = my_ready_map.get(src)
        my_rv = my_review_map.get(src)
        o_r = other_ready.get(src)
        o_rv = other_review.get(src)

        my_dest = (
            my_r["final_dest"] if my_r else (my_rv["suggested"] if my_rv else "-")
        )
        my_status = "ready" if my_r else ("review" if my_rv else "missing")
        other_dest = o_r if o_r else (o_rv["suggested"] if o_rv else "-")
        other_status = "ready" if o_r else ("review" if o_rv else "missing")

        dests_match = (
            my_dest.rstrip("/") == other_dest.rstrip("/")
            if my_dest != "-" and other_dest != "-"
            else False
        )
        if dests_match and my_status == other_status:
            agreement = "AGREE"
        elif dests_match:
            agreement = "DEST-AGREE STATUS-DIFF"
        elif my_status == "missing":
            agreement = "ONLY-IN-OTHER"
        elif other_status == "missing":
            agreement = "ONLY-IN-MINE"
        else:
            agreement = "DISAGREE"

        my_class = my_r["classification"] if my_r else (my_rv["classification"] if my_rv else "-")
        comparison.append(dict(
            source=src, my_dest=my_dest, my_status=my_status, my_class=my_class,
            other_dest=other_dest, other_status=other_status, agreement=agreement,
        ))
    return comparison


# ── 10. Write CSV ─────────────────────────────────────────────────────────────

def write_csv(path: Path, rows: list, fieldnames: list):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"  {path.name}: {len(rows)} rows")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="TGG 301 Redirect Mapper")
    parser.add_argument("--mappings", required=True,
                        help="URL mappings CSV (Redirect from / Redirect to / confidence)")
    parser.add_argument("--sitemap", default="data/sitemap_audit_latest.csv",
                        help="Sitemap audit CSV (default: data/sitemap_audit_latest.csv)")
    parser.add_argument("--products", default=None,
                        help="Shopify Products.csv (optional fallback)")
    parser.add_argument("--existing-ready", default=None,
                        help="Other AI's ready CSV for hybrid merge")
    parser.add_argument("--existing-review", default=None,
                        help="Other AI's review CSV for hybrid merge")
    parser.add_argument("--output-dir", default="seo/outputs/redirects",
                        help="Output directory (default: seo/outputs/redirects)")
    args = parser.parse_args()

    out = Path(args.output_dir)
    mappings_path = Path(args.mappings)
    sitemap_path = Path(args.sitemap)
    products_path = Path(args.products) if args.products else None
    existing_ready_path = Path(args.existing_ready) if args.existing_ready else None
    existing_review_path = Path(args.existing_review) if args.existing_review else None

    print("\n=== TGG 301 Mapper ===\n")

    # Load lookup tables
    print("Loading sitemap index...")
    sitemap = load_sitemap_index(sitemap_path)
    print(f"  {len(sitemap)} handles from sitemap audit")

    print("Loading Products.csv fallback...")
    products = load_products(products_path) if products_path else {}
    print(f"  {len(products)} handles from Products.csv")

    # Process mappings
    print("\nProcessing URL mappings...")
    my_ready, my_review = process_mappings(mappings_path, sitemap, products)
    print(f"  My ready:  {len(my_ready)}")
    print(f"  My review: {len(my_review)}")

    cls_counts = Counter(r["classification"] for r in my_ready + my_review)
    print("\n  Classification breakdown:")
    for cls, n in cls_counts.most_common():
        print(f"    {cls}: {n}")

    # Write my raw outputs
    print("\nWriting my outputs...")
    write_csv(out / "my_shopify_import_ready.csv", my_ready,
              ["source", "final_dest", "confidence", "classification", "rule"])
    write_csv(out / "my_shopify_import_review.csv", my_review,
              ["source", "original_dest", "suggested", "confidence", "notes",
               "classification", "rule"])

    # Hybrid merge (if other AI files provided)
    other_ready, other_review = load_other_ai(existing_ready_path, existing_review_path)
    if other_ready or other_review:
        print(f"\nLoaded other AI: {len(other_ready)} ready, {len(other_review)} review")
    comparison = compare(my_ready, my_review, other_ready, other_review)

    agree_counts = Counter(r["agreement"] for r in comparison)
    print("\nAgreement breakdown:")
    for status, n in agree_counts.most_common():
        print(f"  {status}: {n}")

    write_csv(out / "my_comparison_report.csv", comparison,
              ["source", "my_dest", "my_status", "my_class",
               "other_dest", "other_status", "agreement"])

    final_ready, final_review = produce_final(
        my_ready, my_review, other_ready, other_review, comparison
    )

    # ── Validation gates ────────────────────────────────────────────────────
    print("\nValidation:")
    # No product handles in ready destinations
    product_leaks = [
        r for r in final_ready
        if is_product_handle(r["Redirect to"], sitemap, products)
    ]
    print(f"  Product handles in ready: {len(product_leaks)}"
          + (" ✓" if not product_leaks else " ✗ FAIL"))

    # No duplicate sources
    sources = [r["Redirect from"] for r in final_ready]
    dupes = len(sources) - len(set(sources))
    print(f"  Duplicate sources: {dupes}" + (" ✓" if not dupes else " ✗ FAIL"))

    # Destination depth breakdown
    depths = Counter(len(path_segments(r["Redirect to"])) for r in final_ready)
    print(f"  Dest depth: "
          + " | ".join(f"{d}-seg: {n}" for d, n in sorted(depths.items())))

    # Write final outputs
    print("\nWriting final outputs...")
    write_csv(out / "final_shopify_import_ready.csv", final_ready,
              ["Redirect from", "Redirect to"])
    write_csv(out / "final_shopify_import_review.csv", final_review,
              ["Redirect from", "Redirect to", "Notes", "Classification"])

    print(f"\nFinal ready:  {len(final_ready)} rows")
    print(f"Final review: {len(final_review)} rows")

    # GitHub Actions step summary
    import os
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY", "")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write("## TGG 301 Mapper Results\n\n")
            f.write(f"| File | Rows |\n|------|------|\n")
            f.write(f"| `final_shopify_import_ready.csv` | {len(final_ready)} |\n")
            f.write(f"| `final_shopify_import_review.csv` | {len(final_review)} |\n\n")
            f.write("### Classification Breakdown\n\n")
            for cls, n in cls_counts.most_common():
                f.write(f"- `{cls}`: {n}\n")

    print("\n=== Done ===\n")


if __name__ == "__main__":
    main()
