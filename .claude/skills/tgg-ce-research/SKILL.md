---
name: tgg-ce-research
description: Content engineering pipeline stage — research bundle. Assembles the SEO and analytics research package for a single content pipeline run. Called by tgg-content-pipeline at Stage 2. Delegates analytics to tgg-marketing-analyst and runs scripts/run_research.py for deterministic Semrush and keyword data. Returns a single structured seo-data.md artefact. Use only within the content pipeline, not standalone.
---

# CE Research — Stage 2

Produces `runs/<run-id>/seo-data.md`. All domain logic lives in `tgg-marketing-analyst`. This skill owns the bundle format and the script invocation.

## Step 1: Deterministic data fetch

Run the script first to get structured, reproducible keyword data:

```bash
python3 .claude/skills/tgg-ce-research/scripts/run_research.py \
  --keyword "<keyword from intake.md>" \
  --market au \
  --competitors jbhifi.com.au,harveynorman.com.au,appliancesonline.com.au \
  --output runs/<run-id>/seo-data-raw.json
```

If the script fails (missing API key, quota exceeded), log the failure and continue with analyst-only data. Do not block the pipeline on script failure.

## Step 2: Analyst research

Hand off to `tgg-marketing-analyst` with this exact request:

> Return a single structured markdown file (not a chat summary) covering:
> - GSC impressions and clicks for "<keyword>" and close variants over the last 90 days
> - GA4 engagement rate for existing TGG content in this category
> - Semrush KD, monthly volume (AU database), and parent topic for "<keyword>"
> - Top 5 ranking URLs for "<keyword>" in AU SERPs
> - Top 15 related queries by AU volume
> - SERP intent classification: informational / commercial / navigational

## Step 3: Merge into seo-data.md

Combine script output and analyst output into a single `seo-data.md` with this structure:

```markdown
# SEO Data — <keyword>
Run: <run-id> | Date: <YYYY-MM-DD>

## Keyword metrics
- Primary: <keyword>
- Semrush KD: <value>
- Monthly volume (AU): <value>
- Parent topic: <value>
- SERP intent: <intent>

## Related queries (top 15, AU volume)
| Query | Volume |
|---|---|
...

## Top-ranking competitors
| Rank | URL | Est. traffic |
|---|---|---|
...

## GSC performance (last 90 days)
- Impressions: <value>
- Clicks: <value>
- Avg. position: <value>
- CTR: <value>

## GA4 engagement (existing TGG category content)
- Avg. engagement rate: <value>
- Top performing page: <url>

## Content opportunities
<3–5 bullet points identifying gaps between current TGG content and ranking competitors>
```

Save to `runs/<run-id>/seo-data.md`. Delete the intermediate `seo-data-raw.json`.

## What this skill does NOT do

- Does not call GSC, GA4, or Semrush APIs directly — `tgg-marketing-analyst` and the script handle that
- Does not make editorial judgements about keyword selection
- Does not decide content angle or structure
