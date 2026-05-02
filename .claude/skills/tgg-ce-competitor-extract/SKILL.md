---
name: tgg-ce-competitor-extract
description: Content engineering pipeline stage — competitor extract. Fetches and parses the H1/H2/H3 structure, key claims, and content gaps from JB Hi-Fi, Harvey Norman, and Appliances Online pages matching the target keyword. Called by tgg-content-pipeline at Stage 3. Runs scripts/extract_competitors.py for deterministic fetching, then delegates SEO judgement to tgg-seo (technical mode). Returns competitive-extract.md. Use only within the content pipeline.
---

# CE Competitor Extract — Stage 3 (part 1)

Produces `runs/<run-id>/competitive-extract.md`. The script handles fetching and parsing. `tgg-seo (technical mode)` handles the editorial analysis of gaps and opportunities.

## Step 1: Deterministic page fetch

```bash
python3 .claude/skills/tgg-ce-competitor-extract/scripts/extract_competitors.py \
  --keyword "<keyword from intake.md>" \
  --competitors jbhifi.com.au,harveynorman.com.au,appliancesonline.com.au \
  --output runs/<run-id>/competitor-raw.json
```

If a competitor page cannot be fetched (404, timeout, bot block), log the failure in the output JSON and continue. Do not block on one competitor failing.

## Step 2: SEO analysis

Hand `competitor-raw.json` to `tgg-seo (technical mode)` with this exact request:

> For each competitor page in this file, identify:
> 1. The H1/H2/H3 structure (list of headings in order)
> 2. Three to five key claims or unique angles they use
> 3. Topics or attributes they cover that TGG's existing content does not
> 4. Topics or attributes that TGG could own better (thin coverage, outdated info, or missing)
>
> Return structured markdown only — no commentary.

## Step 3: Assemble competitive-extract.md

```markdown
# Competitive Extract — <keyword>
Run: <run-id> | Date: <YYYY-MM-DD>

## JB Hi-Fi
URL: <url>
Status: <fetched | failed — <reason>>

### Heading structure
- H1: <text>
- H2: <text>
...

### Key claims
- <claim 1>
- <claim 2>
...

### Content gaps (they miss, TGG could own)
- <gap 1>
...

---

## Harvey Norman
[same structure]

---

## Appliances Online
[same structure]

---

## Cross-competitor gap summary
<3–5 topics or angles no competitor covers well — highest opportunity for TGG>
```

Delete `competitor-raw.json` after assembly. Save final to `runs/<run-id>/competitive-extract.md`.

## What this skill does NOT do

- Does not scrape pages itself — the script handles fetching
- Does not make SEO strategy decisions — `tgg-seo (technical mode)` handles that
- Does not select internal links — that is Stage 3 part 2 (`tgg-contentful-linker`)
