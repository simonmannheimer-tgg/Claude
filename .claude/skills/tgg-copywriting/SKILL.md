---
name: tgg-copywriting
description: >
  Write SEO-optimised ecommerce copy for The Good Guys (thegoodguys.com.au), an Australian electronics
  and appliances retailer. Covers PLP intro copy (2-sentence, 220–250 chars), meta titles/descriptions,
  FAQ and category copy, inlink migration (top-to-bottom HTML rewrites), and EAV mapping. Use this skill
  whenever asked to write, edit, QA, or batch-produce any on-site copy for The Good Guys — PLP intros,
  metadata, FAQ sections, brand+category copy, category introductions, bottom-of-page copy, or EAV
  descriptions. Also trigger for "write copy for these URLs", "batch intros", "metadata for these pages",
  "rewrite this HTML copy", or when context (Australian retailer, appliance/electronics categories) implies
  TGG copywriting even without explicit mention.
---

# TGG Copywriting Skill

Write production-ready ecommerce copy for The Good Guys. Every piece must balance five concerns:
user value, AI citability, SEO performance, legal compliance, and brand voice.

---

## Step 1 — Identify the Content Type

Before writing anything, classify what's being asked for. Read the request and match to one of these:

| Type | Trigger Phrases | Reference File |
|------|----------------|----------------|
| **PLP Intro** | "PLP intro", "2-sentence intro", "intro copy", copy for a category/brand URL | `references/01-plp-intros.md` |
| **Metadata** | "meta title", "meta description", "metadata", "title tag" | `references/02-metadata.md` |
| **Inlink Migration** | "rewrite HTML", "top to bottom copy", "inlink migration", "bottom copy" | `references/03-inlink-migration.md` |
| **FAQ / Category Copy** | "FAQ", "category copy", "brand+category copy", "extended intro" | `references/05-faq-category-copy.md` |
| **EAV Descriptions** | "EAV", "entity attribute value", "category entity mapping" | `references/08-eav-descriptions.md` |

If the request spans multiple types (e.g. "write PLP intros and metadata for these URLs"), load each relevant reference file and produce both outputs.

If the type is ambiguous, ask — don't guess.

---

## Step 2 — Load References

**Always load `references/00-tov.md` first.** It contains hard-banned words, overuse warnings, Australian English rules, and phrasing principles that apply to every content type. Then load the specific reference file for the content type identified in Step 1.

Read the reference files using the `view` tool before writing. Do not work from memory of what the rules might be — the reference files are the source of truth and contain nuances that matter.

---

## Step 3 — Classify the Page

Most content types require page-type classification before writing. Classify every URL:

| Type | URL Pattern | Examples |
|------|-------------|---------|
| A — Generic Category | No brand slug | /audio, /coffee-machines |
| B — Brand Hub | Brand slug only | /samsung, /lg |
| C — Brand + Category | Brand slug + category | /samsung/fridges, /dyson/vacuums |
| D — Promo / Deals | /deals/ path | /deals/black-friday-fridges |

Page type affects which rules apply — brand PLPs have additional banned words, promo pages have specific structural requirements, and so on. The reference files spell out the differences.

---

## Step 4 — Write the Copy

Follow the rules in the loaded reference file. Key cross-cutting principles:

1. **Sound human.** If it reads like a chatbot or a keyword list disguised as prose, rewrite it.
2. **Be specific.** Name brands, name features, name use cases. Specificity makes copy useful to humans and citable by AI.
3. **Vary everything.** Sentence openers, TGG placement, benefit angles, structure. No two pieces in a batch should follow the same skeleton.
4. **Australian English.** optimise, colour, organisation, centre, favourite, behaviour.
5. **Guardrails, not templates.** The banned-word list tells you what to avoid. There is no "allowed words" list — write naturally within the constraints.

---

## Step 5 — Batch Mode

When writing multiple pieces (3+ items), enforce these additional rules:

### Cross-Batch Variation Check
After writing the full batch, review all pieces together and check for:
- **Opener repetition:** Do 3+ pieces start with the same structure (e.g. "[Verb] [benefit] with [category]")? Rewrite the duplicates with different angles.
- **TGG placement repetition:** Is "The Good Guys" always in the same position (e.g. always the last 3 words of S2)? Vary it.
- **Benefit-angle repetition:** Do most pieces lead with the same angle (e.g. always "big brands")? Mix in use-case-first, product-first, or outcome-first angles.
- **Vocabulary clustering:** Are certain words appearing in 50%+ of pieces (e.g. "range", "perfect", "upgrade")? Diversify.

### Batch Output Format
For PLP intros, output as a table:

```
| URL | Page Type | Copy | Chars |
```

For metadata, output as CSV or structured blocks (see the metadata reference).

For FAQ/category copy, output each piece with a clear URL header.

### Batch Size Guidance
- Up to 20 items: write all, then run the variation check.
- 21–50 items: write in sub-batches of ~15, running variation checks per sub-batch AND across the full set.
- 50+ items: flag that this is a large batch and suggest breaking into thematic groups (by category, by brand, by page type).

---

## Step 6 — Self-QA

Before presenting output, run the QA checklist from the relevant reference file. Every reference file has a checklist at the bottom — use it. If any item fails, fix the copy before presenting it. Don't present a piece and then list the QA failures as caveats.

For batches, also run the cross-batch variation check from Step 5.

---

## Reference File Index

| File | Content |
|------|---------|
| `references/00-tov.md` | Hard bans, overuse warnings, phrasing principles, Australian English — **read first, always** |
| `references/01-plp-intros.md` | 2-sentence PLP intro rules: char limits, page types, sentence structure, formatting |
| `references/02-metadata.md` | Meta title (≤60 chars) and description (140–155 chars) rules |
| `references/03-inlink-migration.md` | HTML rewrite rules: Slate/CSS formatting, link preservation, intent differentiation |
| `references/05-faq-category-copy.md` | FAQ generation, brand+category FAQ (150–250 words), extended PLP intro (230–260 words) |
| `references/08-eav-descriptions.md` | Entity-attribute-value mapping for category research |

---

## What This Skill Does NOT Cover

- **Content analysis** (query fanout, entity extraction, summarisation) — these are research tasks, not copywriting. If the user needs analysis to inform the copy, do it as a preliminary step but don't conflate the two.
- **Internal linking strategy** (hierarchy validation, link status checking) — this is a technical SEO task. The copywriting skill uses validated links as inputs when provided, but doesn't run the validation itself.
- **AEO auditing** — content improvement suggestions are a separate analytical process.
- **AI visibility polling** — poll question generation is a research/strategy task.

If the user asks for something in this list, let them know it's outside this skill's scope and suggest they handle it separately.
