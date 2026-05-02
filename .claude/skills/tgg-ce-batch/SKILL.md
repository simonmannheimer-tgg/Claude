---
name: tgg-ce-batch
description: Content engineering pipeline stage — batch runner. Processes a CSV of content jobs in parallel using subagents, aggregates results, and writes a batch report. Use with /batch command. Supports full 9-stage pipeline for long-form content and a 3-stage micro-pipeline for high-volume short-form (plp-intro, faq-block). Concurrency cap: 10 parallel subagents by default. Idempotent — re-running an existing run-id resumes from last successful stage.
disable-model-invocation: false
---

# CE Batch — Multi-Row Content Runner

Runs the content engineering pipeline across a CSV of jobs. Delegates each row to a subagent. Aggregates results. Does not do any writing itself.

## Input CSV format

Required columns: `keyword`, `slug`, `content_type`, `angle`, `byline`

```csv
keyword,slug,content_type,angle,byline
heat pump dryer,/buying-guides/heat-pump-dryer,buying-guide,"emphasise running cost vs vented; mention 6-star energy rating; mention finance",editorial
how to clean a dishwasher filter,/how-to/clean-dishwasher-filter,how-to,none,editorial
```

Validate the CSV first using `scripts/csv_validator.py` before dispatching any subagents.

`content_type` must be one of: `buying-guide`, `how-to`, `comparison`, `eav-explainer`, `plp-intro`, `faq-block`

For `plp-intro` and `faq-block`, the micro-pipeline runs (see Pipeline path selection below).

## Pipeline path selection

| content_type | Pipeline path | Stages run |
|---|---|---|
| buying-guide | Full 9-stage | 1–9 |
| how-to | Full 9-stage | 1–9 |
| comparison | Full 9-stage | 1–9 |
| eav-explainer | Full 9-stage | 1–9 |
| plp-intro | Micro 3-stage | Intake → Draft (tgg-seo (production mode) only) → QA+Humanise |
| faq-block | Micro 3-stage | Intake → Draft (tgg-seo (production mode) only) → QA+Humanise |

The micro-pipeline skips research, competitor extract, brief, and outline. It feeds `keyword`, `slug`, and `angle` directly into `tgg-seo (production mode)` then validates with `verification-gate-protocol --type <type>` and humanises with `tgg-humanizer`.

## Idempotency

Each row gets a stable `run-id` from `scripts/batch_runner.py` (format: `<date>-<slug-hash>`). If a `runs/<run-id>/` folder already exists:
- Check `runs/<run-id>/pipeline-status.md` for last completed stage
- Resume from the next stage rather than restarting
- If `final.md` already exists and is non-empty: skip row entirely and mark as ALREADY_COMPLETE

## Concurrency

Default: 10 parallel subagents. Override with `--concurrency N` flag.

Cap at 20. Higher concurrency risks:
- Semrush API rate limits (10 req/sec on standard plans)
- GSC/GA4 quota exhaustion
- Token burn without proportional output improvement

## Usage

```
/batch input=batches/plp-intros-2026-q2.csv type=plp-intro
/batch input=batches/buying-guides-q2.csv concurrency=5
```

## Execution sequence

1. Validate CSV via `scripts/csv_validator.py` → fail fast if required columns missing
2. Assign stable run-ids via `scripts/batch_runner.py` → skip ALREADY_COMPLETE rows
3. Dispatch subagents in batches of `concurrency` (default 10):
   - Long-form rows → `tgg-ce-researcher` subagent (research) then `tgg-ce-drafter` subagent (draft + QA + humanise + finalise)
   - Short-form rows → `tgg-ce-drafter` subagent only (micro-pipeline)
4. Collect results — each subagent returns its run-id and status (COMPLETE / FAILED / BLOCKED)
5. Checkpoint after every 10 rows: report pass/fail distribution, flag any systematic failures
6. Run aggregate QA after all rows: `scripts/aggregate_report.py`
7. Write `runs/batch-<batch-id>/aggregate.md` and `runs/batch-<batch-id>/aggregate.csv`

## Systematic failure detection

After every 10 rows, check for patterns in FAIL items:
- Same constraint failing across 3+ rows → systematic issue, pause and report
- Same banned phrase appearing in 5+ outputs → `tgg-humanizer` not catching it, escalate
- All rows from a specific category type failing → content-type template issue, escalate

Do not continue past 30% failure rate without pausing and reporting to the human.

## Batch report format

`runs/batch-<batch-id>/aggregate.md`:
```markdown
# Batch Report
Batch ID: <batch-id>
Date: <YYYY-MM-DD>
Input: <csv filename>
Total rows: <n>

## Summary
- Complete: <n>
- Failed: <n>
- Blocked (QA gate): <n>
- Skipped (already complete): <n>

## Per-row results
| Slug | Type | Status | Word count | FAQ count | Int. links | QA result |
|---|---|---|---|---|---|---|
...

## Systematic issues
<Any patterns detected across rows>

## Next steps
<What needs manual review>
```

`runs/batch-<batch-id>/aggregate.csv` — same data, CSV format for import into Sheets or Excel.

## Quota guidance

Document in `references/batch-output-schema.md`. Key limits:
- Semrush: 10 requests/sec, 10,000 requests/day (standard plan)
- GSC: 25,000 requests/day, 1 req/sec per project
- GA4 Data API: 10 concurrent requests, 100,000 tokens/day

If 429 rate-limit errors occur: `scripts/batch_runner.py` backs off exponentially (2s, 4s, 8s, 16s) then retries up to 4 times before marking row as FAILED.

## What this skill does NOT do

- Does not write any content directly — delegates to subagents which call existing skills
- Does not bypass QA gates — every row passes through `verification-gate-protocol`
- Does not commit outputs — call `tgg-repo-manager` explicitly after reviewing the aggregate report
