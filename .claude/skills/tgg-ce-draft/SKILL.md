---
name: tgg-ce-draft
description: Content engineering pipeline stage — draft. Produces the full article draft by delegating body copy to tgg-seo (strategy mode) and short-form blocks (FAQ, metadata) to tgg-seo (production mode). Provides TGG-specific Australian retail language and voice reference augmentations. Uses content-type templates from references/content-type-templates/ as additive guidance only — canonical templates live in tgg-template-generator. Use only within the content pipeline.
---

# CE Draft — Stage 6

Produces `runs/<run-id>/draft.md`. Delegates all writing to existing skills. Owns the augmentation layer specific to TGG ecommerce content.

## Inputs required

- `runs/<run-id>/brief.md`
- `runs/<run-id>/outline.md` (validated, H2 count confirmed)
- `runs/<run-id>/seo-data.md`
- `runs/<run-id>/competitive-extract.md`

## Step 1: Load augmentation references

Before delegating to `tgg-seo (strategy mode)`, read the following files and include their content as additional guidance in the delegation request:

- `references/australian-retail-language.md` — must-use phrases and AU retail context
- `references/content-type-templates/<content_type>.md` — TGG-specific augmentations for this content type (not the base template — that came from `tgg-template-generator` at Stage 4)

Do NOT read `references/voice-references.md` here — voice is handled at Stage 8 by `tgg-humanizer` and optionally Stage 9 by `simon-voice`.

## Step 2: Delegate body draft to tgg-seo (strategy mode)

Pass `brief.md`, `outline.md`, `seo-data.md`, and `competitive-extract.md` plus the augmentation content to `tgg-seo (strategy mode)` with this request:

> Write the full article body following the outline exactly. Section by section, match the heading text and word budget from the outline.
>
> Rules:
> - Use the angle from the brief verbatim — do not substitute a different angle
> - Use Australian English throughout (organise, colour, optimise)
> - No em dashes as sentence connectors (use a full stop and space instead)
> - For internal links, use placeholder format [LINK: /slug] — do not write anchor text differently
> - Every factual claim must be followed immediately by a source link or explicit attribution
> - Use the Australian retail language from the augmentation notes where applicable
> - Do not write the FAQ section — that comes separately
>
> Return the body copy only (introduction through last H2 before FAQ). No FAQ. No metadata.

## Step 3: Delegate FAQ block to tgg-seo (production mode)

Pass `brief.md` and `seo-data.md` related queries to `tgg-seo (production mode)` with this request:

> Write a FAQ block for this article. Rules:
> - 5–8 questions
> - Each answer: 50–120 words, plain prose only (no markdown, no bullet lists)
> - Questions must be natural-language queries (how a person would type them)
> - Answers must be schema-safe (JSON-LD FAQPage ready)
> - Use Australian English
> - Draw question topics from the related queries in seo-data.md and from the brief's must-cover list
> - No duplicate intent across questions

## Step 4: Assemble draft.md

Combine body + FAQ into `draft.md`:

```markdown
# <H1 — matches the primary keyword or a natural variant>

<intro paragraph — no heading>

## <H2 from outline>
<body copy>

...

## Frequently asked questions

**<Question 1>**
<Answer 1>

**<Question 2>**
<Answer 2>

...
```

All `[LINK: /slug]` placeholders must remain in place. Do not remove or modify them.

Count total words (excluding FAQ) and confirm it falls within the type range before saving.

Save to `runs/<run-id>/draft.md`.

## What this skill does NOT do

- Does not apply voice rules — `tgg-humanizer` (Stage 8) and `simon-voice` (Stage 9) handle that
- Does not validate constraints — that is Stage 7
- Does not resolve `[LINK: /slug]` placeholders to Contentful IDs — that is Stage 9
- Does not produce metadata (title, description, slug) — `tgg-seo (production mode)` at Stage 9 handles that
- Does not duplicate base templates from `tgg-template-generator` — augmentations only
