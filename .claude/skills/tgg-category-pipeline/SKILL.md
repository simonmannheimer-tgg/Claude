---
name: tgg-category-pipeline
description: >
  Master content engineering pipeline for The Good Guys category pages. Chains all
  production steps — EAV mapping, keyword research, PLP intro, FAQ copy, metadata,
  internal links — in sequence with one command. Each step saves its own output file.
  Use when building or rebuilding a category page from scratch, or running a full
  content refresh. Equivalent to a blog-pipeline for TGG category SEO.
---

# TGG Category Pipeline

Runs all content production steps for a TGG category page in sequence. Each step
saves its output file before passing to the next stage. Simon can stop at any checkpoint
and resume from the last good output.

---

## How to trigger

```
/tgg-category-pipeline [URL or category slug]
```

Optional context parameter — add anything that should shape the output:
```
/tgg-category-pipeline /air-fryers context: "focus on compact models for small kitchens, Ninja is the #1 brand this season, avoid mentioning Philips"
```

The context is saved to `seo/outputs/briefs/context-[slug]-[date].md` and referenced
by every downstream step. Front-load everything you know — angles, brand priorities,
sub-topics to cover, things to avoid.

---

## Pipeline steps

### Step 0 — Save context
If context was provided, write it to:
`seo/outputs/briefs/context-[slug]-[YYYY-MM-DD].md`

If no context: create a minimal file with URL and date only. This file is referenced
by all downstream steps so they stay aligned.

---

### Step 1 — EAV mapping
Delegate to **eav-researcher**.

Goal: map the product entity landscape for this category.
- Entities (product types, brands stocked, key technologies)
- Attributes (capacity, power, size, connectivity, special features)
- Values (the specific variants/ranges that appear in the category)

Output: `seo/outputs/eav/eav-[slug]-[YYYY-MM-DD].json`

**Checkpoint.** Pause here if Simon wants to review or correct entity mapping before
keywords and copy are generated.

---

### Step 2 — Keyword research
Delegate to **seo-keyword-researcher**.

Input: EAV output + category URL.
Goal: primary keyword, 3–5 supporting keywords, search volumes, intent classification.
Use Semrush AU database.

Output: `seo/outputs/keywords/keywords-[slug]-[YYYY-MM-DD].json`

---

### Step 3 — Content brief (query fanout)
Delegate to **content-analyst**.

Input: EAV output + keyword data + context file.
Goal: identify primary query, related queries, FAQ candidate questions (from "People Also Ask"
and question patterns), and internal link candidates.

Output: `seo/outputs/briefs/brief-[slug]-[YYYY-MM-DD].md`

---

### Step 4 — PLP intro copy
Delegate to **plp-copywriter**.

Input: EAV output + keyword data + context file.
Rules: Process 01 (220–250 chars, 2 sentences, TOV reference).

Output: `seo/outputs/plp/plp-[slug]-[YYYY-MM-DD].md`

Deliver 2 variations. Include: full copy, char count, page type, primary KW check,
TGG language check, entities included.

**Checkpoint.** The intro copy is the most visible output. Review before continuing.

---

### Step 5 — FAQ + category copy
Delegate to **faq-writer**.

Input: content brief + EAV output + keyword data + context file.
Rules: Process 05 (5–7 Q&A pairs + 150–250 word brand+category section with internal links).

Output: `seo/outputs/faqs/faqs-[slug]-[YYYY-MM-DD].md`

---

### Step 6 — Metadata
Delegate to **metadata-writer**.

Input: content brief + PLP copy (as page context) + keyword data.
Rules: Process 02 (title ≤60 chars, description ≤155 chars, intent-aligned).

Output: `seo/outputs/metadata/metadata-[slug]-[YYYY-MM-DD].md`

---

### Step 7 — Internal links
Delegate to **internal-linking-agent**.

Input: PLP copy + FAQ copy + content brief.
Run: 6A (find candidates) → 6B (validate by hierarchy) → 6C (categorise) → 6D (insert).
Rules: Process 06.

Output: `seo/outputs/links/links-[slug]-[YYYY-MM-DD].md`

---

### Step 8 — Final assembly
Combine all step outputs into one delivery file:
`seo/outputs/[slug]-build-[YYYY-MM-DD].md`

Structure:
```
# [Category Name] — Full Page Build [YYYY-MM-DD]

## Context & angles
[from context file]

## EAV summary
[key entities/attributes from step 1]

## Keyword targets
[primary + supporting from step 2]

## PLP intro copy
[preferred variation from step 4]

## FAQ section
[from step 5]

## Metadata
[title + description from step 6]

## Internal links inserted
[from step 7]
```

---

## Partial runs

Skip to any step by specifying it:

```
/tgg-category-pipeline /air-fryers start-at: step-4
```

If starting mid-pipeline, list which earlier output files exist so the pipeline can
load them rather than regenerate.

---

## Recursive improvement (end-of-build)

After every full build, do a brief review pass:
- Did any step produce output that needed manual correction?
- Was any agent missing key context?
- Did any rule in a process file seem to conflict with another?

If yes: note the issue at the end of the assembly file under `## Pipeline notes`.
These notes feed the CONNECTIONS TASK and the ONBOARDING TASK (see CLAUDE.md).

---

## Output file map

| Step | Output path |
|------|------------|
| Context | `seo/outputs/briefs/context-[slug]-[date].md` |
| EAV | `seo/outputs/eav/eav-[slug]-[date].json` |
| Keywords | `seo/outputs/keywords/keywords-[slug]-[date].json` |
| Brief | `seo/outputs/briefs/brief-[slug]-[date].md` |
| PLP copy | `seo/outputs/plp/plp-[slug]-[date].md` |
| FAQ copy | `seo/outputs/faqs/faqs-[slug]-[date].md` |
| Metadata | `seo/outputs/metadata/metadata-[slug]-[date].md` |
| Links | `seo/outputs/links/links-[slug]-[date].md` |
| Full build | `seo/outputs/[slug]-build-[date].md` |
