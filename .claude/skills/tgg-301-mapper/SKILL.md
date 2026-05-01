---
name: tgg-301-mapper
description: >
  301 redirect mapper for The Good Guys. Processes a raw URL mapping CSV
  (source -> destination + confidence) using Simon's redirect rules, the live
  sitemap audit index, and an optional hybrid merge against another AI's output.
  Produces a Shopify-ready import file and a structured review queue.
  Trigger when Simon mentions "301s", "redirects", "URL mapping", "Seb's mapping",
  "process redirects", or shares a url_mappings CSV.
---

# TGG 301 Redirect Mapper Skill

Maps old/dead TGG URLs to valid Shopify redirect destinations using Simon's rules.
Primary breadcrumb source is `data/sitemap_audit_latest.csv` (refreshed weekly by
`sitemap-audit-weekly.yml`). Falls back to Products.csv if provided.

---

## Inputs Required

| Input | Where to find it |
|-------|-----------------|
| `url_mappings.csv` | From Seb, or a previous AI run. Columns: `Redirect from`, `Redirect to`, `confidence` |
| `data/sitemap_audit_latest.csv` | Auto-generated weekly. If missing, run the sitemap audit first |
| `Products.csv` (optional) | Shopify product export — only needed as fallback if sitemap is stale |
| Other AI's ready/review CSVs (optional) | For hybrid merge — improves coverage for unknown handles |

---

## Simon's Redirect Rules (non-negotiable)

**Rule 1 — No product-to-product redirects.**
If the destination is a product handle, redirect to its L3 category instead.
Avoids redirect chains when product stock changes.

**Rule 2 — Malformed source URLs → clean target.**
Malformed = has `?`, `--`, `/product/` prefix, garbage chars `{}[])`, or garbled text.
- Strip params + fix dashes → get clean URL
- If clean version is live in sitemap → redirect to clean product URL
- Otherwise → redirect to category (Rule 1)

**Rule 3 — Confidence threshold.**
Flag any row with `confidence < 0.92` for manual review.

**Rule 4 — Brand/category pages are correct.**
Single-segment, no digits, < 25 chars = brand/category page. Keep as-is.

---

## How to Run Locally

```bash
python tools/tgg_301_mapper.py \
  --mappings  data/redirects/url_mappings_latest.csv \
  --sitemap   data/sitemap_audit_latest.csv \
  --output-dir seo/outputs/redirects

# With hybrid merge against another AI's output:
python tools/tgg_301_mapper.py \
  --mappings  data/redirects/url_mappings_latest.csv \
  --sitemap   data/sitemap_audit_latest.csv \
  --existing-ready  path/to/other_ready.csv \
  --existing-review path/to/other_review.csv \
  --output-dir seo/outputs/redirects
```

## How to Run in GitHub Actions

1. **Commit your URL mappings CSV** to `data/redirects/url_mappings_latest.csv`
2. Go to **Actions → TGG 301 Redirect Mapper → Run workflow**
3. Enter the file path (default: `data/redirects/url_mappings_latest.csv`)
4. Set `commit_outputs: yes` to save results back to the repo
5. Download the `301-redirect-output-<run_id>` artifact for the CSVs

The workflow uses `data/sitemap_audit_latest.csv` automatically — no extra input needed.

---

## How to Refresh the Sitemap Index

The sitemap audit runs automatically every Sunday at 12:00 UTC. To trigger manually:

**Actions → TGG Sitemap Audit (Weekly) → Run workflow**

For a quick test run, set `max_urls: 5` to process only 5 URLs per sitemap.

---

## Outputs

| File | Description |
|------|-------------|
| `final_shopify_import_ready.csv` | `Redirect from, Redirect to` — Shopify-native, ready to import |
| `final_shopify_import_review.csv` | `Redirect from, Redirect to, Notes, Classification` — manual review queue |
| `my_shopify_import_ready.csv` | My raw output before merge (includes rule audit trail) |
| `my_shopify_import_review.csv` | My raw review before merge |
| `my_comparison_report.csv` | Full diff vs other AI (if provided) |

---

## Review File Classifications

| Classification | Meaning | Action |
|---------------|---------|--------|
| `product->review-no-breadcrumb` | Destination is a product, no category found in sitemap or Products.csv | Find category manually |
| `malformed->product-no-breadcrumb` | Malformed source, destination looks like product but no category | Assign category |
| `malformed->review` | Malformed URL that couldn't be resolved at all | Delete or assign manually |
| `category-low-conf` | Good destination but confidence < 0.92 | Verify destination is correct |
| `product->category-low-conf` | Remapped to category but low confidence | Verify category |
| `external-source` | URL not in url_mappings; from other AI's source | Verify it should be included |
| `unknown` | Couldn't classify | Manual review |

---

## Sitemap Audit Coverage

The sitemap audit (`tools/tgg_sitemap_audit.py`) scrapes TGG's product, brand,
category, content, and article sitemaps. For each URL it records:
- HTTP status
- Canonical URL
- Previous breadcrumb URL (from JSON-LD BreadcrumbList)
- Category path (extracted from breadcrumb URL)

This gives the 301 mapper a live, full-catalogue lookup — far more complete than
the ~127-product subset in a Shopify Products.csv export.

The sitemap audit is committed weekly to `data/sitemap_audit_latest.csv` via
`sitemap-audit-weekly.yml`. The 301 mapper always reads from this file, so the
more recent the sitemap run, the better the category coverage.
