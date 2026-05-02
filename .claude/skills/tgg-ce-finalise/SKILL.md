---
name: tgg-ce-finalise
description: Content engineering pipeline stage — finalise. Assembles the production-ready package from humanised-draft.md: resolves internal link placeholders via tgg-contentful-linker, generates metadata via tgg-seo (production mode), writes JSON-LD FAQPage schema, and optionally runs simon-voice if byline is simon. Returns final.md, metadata.md, faq.json, and internal-links.md. Use only within the content pipeline.
---

# CE Finalise — Stage 9

Produces `runs/<run-id>/final.md`, `runs/<run-id>/metadata.md`, `runs/<run-id>/faq.json`, `runs/<run-id>/internal-links.md`. Assembles four artefacts from the humanised draft. Delegates all resolution and copy logic to existing skills.

## Inputs required

- `runs/<run-id>/humanised-draft.md`
- `runs/<run-id>/intake.md` (for byline, slug, content_type)
- `runs/<run-id>/qa-report.md` (confirm it shows PASS or no block_delivery items)

Do not begin if `qa-report.md` is missing or shows Block delivery: YES.

## Step 1: Voice pass (conditional)

Read `byline` field from `intake.md`.

If `byline: simon` → hand `humanised-draft.md` to `simon-voice`. Use the voice-passed output as the base for all subsequent steps.

If `byline: editorial` or `byline: uncredited` → skip. Use `humanised-draft.md` directly.

## Step 2: Resolve internal links

Extract all `[LINK: /slug]` placeholders from the draft. Compile as a list.

Hand the list to `tgg-contentful-linker` with this request:

> Resolve each of these TGG slugs to its Contentful entry ID. Return a markdown table:
> | Slug | Contentful entry ID | Page title |
> For any slug you cannot resolve, mark it as "unresolved — manual check needed".

Replace each `[LINK: /slug]` placeholder in the draft with a proper markdown link: `[Page title](/slug)`. Do not use Contentful entry IDs in the rendered article — use slugs. The entry IDs go to `internal-links.md` for the CMS team.

Save to `runs/<run-id>/internal-links.md`:
```markdown
# Internal Links
Run: <run-id>

| Anchor text | Slug | Contentful entry ID | Status |
|---|---|---|---|
...
```

## Step 3: Generate metadata

Hand the finalised article body (first 300 words) plus the intake keyword and slug to `tgg-seo (production mode)` with this request:

> Write metadata for this article:
> - Meta title: ≤60 characters, includes primary keyword, no clickbait
> - Meta description: ≤155 characters, includes primary keyword, natural call to action
> - Slug: confirm or improve on <slug from intake>
> - OG title: can differ from meta title, ≤65 characters
>
> Return as a markdown table. Australian English.

Save to `runs/<run-id>/metadata.md`.

## Step 4: Build FAQ JSON

Extract the FAQ block from the article. The FAQ section begins at `## Frequently asked questions` and ends at the next H2 or end of document.

Write `runs/<run-id>/faq.json` in JSON-LD FAQPage format:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "<question text — exact match to article heading>",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<answer text — plain prose only, no markdown>"
      }
    }
  ]
}
```

Strip any remaining markdown from answer text (**, ##, -, etc.) before writing to JSON. Verify the JSON is valid before saving.

## Step 5: Assemble final.md

```markdown
---
slug: <slug>
content_type: <content_type>
keyword: <keyword>
byline: <byline>
run_id: <run_id>
date: <date>
word_count: <final count>
status: ready-for-review
---

<full article body with resolved links and FAQ>
```

Count final words (body only, not YAML front matter or FAQ). Record in front matter.

## Step 6: Stop and confirm

State:
```
Stage 9 complete. Run <run-id> is ready for review.

Artefacts:
- runs/<run-id>/final.md (<word count> words)
- runs/<run-id>/metadata.md
- runs/<run-id>/faq.json (<n> FAQ entries)
- runs/<run-id>/internal-links.md (<n> links, <n unresolved> need manual check)

Confirm to commit via tgg-repo-manager.
```

Wait for explicit confirmation before calling `tgg-repo-manager`.

## What this skill does NOT do

- Does not humanise the draft — that is Stage 8 (`tgg-humanizer`)
- Does not validate constraints — that is Stage 7 (`tgg-ce-qa`)
- Does not apply voice rules directly — delegates to `simon-voice` only if `byline: simon`
- Does not write the metadata copy itself — `tgg-seo (production mode)` does
