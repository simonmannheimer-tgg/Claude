# Batch Output Schema

Defines the shape of every output file produced by `tgg-ce-batch` runs.

---

## Input CSV schema

Required columns (must all be present or `csv_validator.py` rejects the file):

| Column | Type | Values | Notes |
|---|---|---|---|
| `keyword` | string | any | Target keyword or topic |
| `slug` | string | starts with `/` | Proposed URL slug |
| `content_type` | enum | `buying-guide`, `how-to`, `comparison`, `eav-explainer`, `plp-intro`, `faq-block` | Drives pipeline path |
| `angle` | string | any, or `none` | Free-text angle; `none` to skip |
| `byline` | enum | `simon`, `editorial`, `uncredited` | Drives `simon-voice` invocation |

Optional columns (ignored if absent):

| Column | Type | Notes |
|---|---|---|
| `priority` | integer 1–5 | Processing order within batch (1 = highest) |
| `must_cover` | string | Semicolon-separated list of must-cover sub-topics |
| `existing_url` | string | Existing TGG URL to reference or refresh |

---

## Per-row artefact structure

Each row produces a run folder at `runs/<run-id>/` containing the artefacts from the relevant pipeline path:

**Full 9-stage (long-form types):**
```
runs/<run-id>/
├── intake.md
├── seo-data.md
├── competitive-extract.md
├── existing-content.md
├── brief.md
├── outline.md
├── draft.md
├── qa-report.md
├── humanised-draft.md
├── final.md
├── metadata.md
├── faq.json
├── internal-links.md
└── pipeline-status.md
```

**Micro 3-stage (plp-intro, faq-block):**
```
runs/<run-id>/
├── intake.md
├── draft.md
├── qa-report.md
├── humanised-draft.md
├── final.md
└── pipeline-status.md
```

---

## Aggregate report schema

`runs/batch-<batch-id>/aggregate.csv` columns:

| Column | Description |
|---|---|
| `run_id` | Stable run identifier |
| `slug` | URL slug |
| `content_type` | Content type |
| `status` | `COMPLETE`, `FAILED`, `BLOCKED`, `ALREADY_COMPLETE` |
| `word_count` | Final word count (blank if failed) |
| `faq_count` | FAQ question count (blank if failed or not applicable) |
| `internal_link_count` | Resolved internal links (blank if failed) |
| `unresolved_links` | Count of `[LINK: /slug]` not resolved by tgg-contentful-linker |
| `qa_result` | `PASS` or `FAIL` |
| `qa_fail_reasons` | Semicolon-separated list of failing constraints |
| `time_seconds` | Approximate wall-clock time for this row |

---

## API quota reference

| API | Limit | Notes |
|---|---|---|
| Semrush | 10 req/sec, ~10,000 req/day (standard) | Per API key |
| GSC Data API | 1 req/sec, 25,000 req/day | Per project credential |
| GA4 Data API | 10 concurrent, 100,000 tokens/day | Tokens scale with row complexity |
| Anthropic API | Per-tier rate limits | Check console.anthropic.com for current limits |

`batch_runner.py` implements exponential backoff (2s, 4s, 8s, 16s, then FAIL) on HTTP 429 responses from all APIs.

---

## Idempotency key

Run-id format: `YYYY-MM-DD-<slug-sanitised>-<sha1-6char>`

Example: `2026-05-01-buying-guides-heat-pump-dryer-a3f9c2`

The slug-hash component ensures stable run-ids even if the keyword changes between runs. To force a re-run from scratch for a specific row, delete the `runs/<run-id>/` folder.
