---
name: tgg-ce-brief
description: Content engineering pipeline stage — brief. Consolidates intake, SEO data, competitor extracts, and existing content into a production brief for tgg-content-strategist. Adds TGG-specific requirements (Australian retail, EAV, schema) on top of the base brief template from tgg-template-generator. Calls verification-gate-protocol as a hard gate before passing the brief to Stage 5. Use only within the content pipeline.
---

# CE Brief — Stage 4

Produces `runs/<run-id>/brief.md`. Owns the TGG-specific brief augmentation layer. Does not own strategy reasoning — that lives in `tgg-content-strategist`.

## Inputs required (all must exist before starting)

- `runs/<run-id>/intake.md`
- `runs/<run-id>/seo-data.md`
- `runs/<run-id>/competitive-extract.md`
- `runs/<run-id>/existing-content.md`

If any input file is empty or missing, stop and report which stage failed to produce it.

## Step 1: Get base template

Call `tgg-template-generator` with `content_type=<content_type from intake.md>`. Request the brief scaffold only (not outline, not draft template). This returns the base section structure.

## Step 2: Add TGG-specific brief requirements

Append or expand the following sections in the template before passing to `tgg-content-strategist`. These are TGG augmentations — do not duplicate what the template already covers:

**Australian retail considerations (all types):**
- Relevant energy star ratings or efficiency labels for this product/topic (if applicable)
- Available finance options at TGG (interest-free, BPAY, etc.) — mention where relevant
- Click-and-collect availability — mention where relevant to the buying decision
- Australian Standards or safety regulations affecting this category (if applicable)

**EAV requirements (buying-guide and eav-explainer types only):**
- List of 5–10 key attributes for this product category that the article must define
- For each attribute: name, what range of values exists, and what a buyer should look for
- Source: use `seo-data.md` related queries and `competitive-extract.md` headings to infer attributes buyers care about

**Schema requirements (all types):**
- FAQ block: 5–8 questions, schema-ready (plain prose answers, no markdown)
- HowTo schema: required for how-to content type only
- Specify target schema type in brief so drafting skill produces schema-safe copy

**Internal link opportunities:**
- List slug-level opportunities from `existing-content.md`
- Do not yet resolve to Contentful entry IDs — that is Stage 9
- Format: `[LINK: /slug]`

## Step 3: Brief assembly

Pass all inputs plus the augmented template to `tgg-content-strategist` with this request:

> Produce a complete production brief using the attached template and inputs. Use the angle verbatim from intake.md — do not reinterpret it. Include every section in the template. For Australian retail considerations, EAV requirements, and schema requirements, use the augmentation notes I have appended.
>
> Return the brief as a single markdown document. No commentary.

Save output to `runs/<run-id>/brief.md`.

## Step 4: Hard gate

Run `verification-gate-protocol --type <content_type>` on `brief.md` in pre-draft mode.

The gate checks:
- All required sections present (from the constraint YAML file)
- Angle field is present and matches intake.md verbatim
- EAV attributes listed (buying-guide and eav-explainer only)
- Schema type specified
- Internal link opportunities listed (at least 3 slug-level candidates)

If gate returns FAIL: present the gap list to the human. Do not proceed to Stage 5 until PASS.

## What this skill does NOT do

- Does not write the brief itself — `tgg-content-strategist` does
- Does not generate the base template — `tgg-template-generator` does
- Does not apply the 29 banned AI phrases — that is `tgg-humanizer` at Stage 8
- Does not resolve Contentful entry IDs — that is Stage 9
