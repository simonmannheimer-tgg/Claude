---
name: tgg-ce-outline
description: Content engineering pipeline stage — outline. Generates and validates the article outline from brief.md. Delegates structure creation to tgg-content-strategist, then validates H2 count against the numeric target for the content type. Blocks progression if H2 count is outside target. Use only within the content pipeline.
---

# CE Outline — Stage 5

Produces `runs/<run-id>/outline.md`. Owns the numeric H2 validation. Does not own structural editing reasoning — that lives in `tgg-content-strategist`.

## Inputs required

- `runs/<run-id>/brief.md` (must have passed the Stage 4 gate)

## Step 1: Generate outline

Hand `brief.md` to `tgg-content-strategist` with this exact request:

> Produce a markdown outline for this article brief. Each H2 must have:
> - A heading (the exact text to use in the article)
> - An estimated word budget (how many words that section should contain)
> - A one-sentence note on what the section must cover
>
> Include a "Frequently asked questions" H2 as the penultimate section.
> Include a brief introduction note (not an H2 — intro has no heading).
> Do not write any body copy. Headings and notes only.
> Return markdown only. No commentary.

## Step 2: Validate H2 count

Count the H2 headings. Compare against the target for the content type:

| Content type | H2 min | H2 max | Action if outside |
|---|---|---|---|
| buying-guide | 6 | 9 | Reject and request revision |
| how-to | 4 | 7 | Reject and request revision |
| comparison | 4 | 6 | Reject and request revision |
| eav-explainer | 4 | 7 | Reject and request revision |

Also check:
- FAQ H2 is present
- buying-guide: "Australian retail considerations" or equivalent section is present
- comparison: a comparison table H2 and a recommendation H2 are present
- eav-explainer: an EAV attributes H2 or similar is present
- how-to: H2 steps are numbered or clearly sequential

If the outline fails any of these checks: return it to `tgg-content-strategist` with specific revision instructions. Do not pass to Stage 6 with a failing outline. Maximum 2 revision cycles before escalating to human.

## Step 3: Word budget check

Sum all section word budgets. Compare to the content type word count range from `references/numeric-constraints.md`:

- buying-guide: 1,800–2,500
- how-to: 800–1,400
- comparison: 1,200–2,000
- eav-explainer: 1,000–1,800

If the sum is outside the range, ask `tgg-content-strategist` to adjust section budgets. The sum does not need to match exactly — within ±10% of the range is acceptable.

## Step 4: Save

State the final H2 count and word budget total before saving:

```
Outline validated:
- H2 count: <n> (target: <min>–<max>) ✓
- Word budget total: <n> (target: <min>–<max>) ✓
- FAQ section: present ✓
- Required sections: all present ✓
```

Save to `runs/<run-id>/outline.md`.

## What this skill does NOT do

- Does not write the outline — `tgg-content-strategist` does
- Does not validate copy constraints (char counts, banned phrases) — that is Stage 7
- Does not select or verify internal links — that is Stage 9
