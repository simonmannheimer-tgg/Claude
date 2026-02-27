# Process 01: PLP Intro Copy (2-Sentence)

> **Version:** 2.0 — Reworked per Simon's feedback: guardrails not templates  
> **Last updated:** 2026-02-27  
> **Depends on:** `00-tov-language-reference.md` (read first)

## Purpose

Write two-sentence intro paragraphs for Product Listing Pages (PLPs) on The Good Guys website. Copy must be viewport-safe (≤5 lines on ~360px mobile), SEO-correct, intent-aligned, and sound like a human wrote it.

## Page Types

Classify every URL before writing:

| Type | URL Pattern | Examples |
|------|-------------|---------|
| A — Generic Category | No brand slug | /audio, /coffee-machines |
| B — Brand Hub | Brand slug only | /samsung, /lg |
| C — Brand + Category | Brand slug + category | /samsung/fridges, /dyson/vacuums |
| D — Promo/Deals | /deals/ path | /deals/black-friday-fridges |

---

## Character Count

- **Range:** 230–260 characters (every letter, space, punctuation mark)
- **Sweet spot:** Aim for ~250. Don't pad to hit 250, don't awkwardly truncate to stay under 260.
- **If it reads naturally at 235 or 258, that's fine.** The range exists to keep copy viewport-safe, not to create a rigid target.

---

## Writing Approach

### What good PLP intro copy does:
- Opens with a clear benefit or outcome for the customer
- Includes enough entities (brands, features, product types) to be useful to search engines and AI
- Reads naturally — like the first line of a helpful buying guide, not an ad
- Includes "The Good Guys" once, placed wherever it reads most naturally (doesn't have to be the last words of S2)

### What it avoids:
- Repetitive patterns across a batch. If you're writing 20 intros and they all follow the same skeleton, vary them.
- Keyword stuffing. The primary keyword should appear, but it shouldn't feel forced.
- Sounding like every other retailer. Be specific — name features, name brands, name use cases.
- Any words/phrases on the hard ban list (see `00-tov-language-reference.md`)

---

## Page Type Guidance

### Type A — Generic Category
- S1 should anchor the category and a key benefit
- S2 should add breadth — brands, formats, or use cases
- Mention 2–3 brand names somewhere in the copy

### Type B — Brand Hub
- Must feel specific to THIS brand — not interchangeable with any other
- Use actual brand technologies, product names, or outcomes — not generic benefit language
- No competitor brands. No comparison language (compare, versus, choose between)
- No discovery-stage language (options to suit everyone, find the right fit, explore the range) — this page has brand-navigational intent
- Brand name must appear in S1

### Type C — Brand + Category
- Combine brand identity with category-specific benefits
- Name actual variants, capacities, series, or tech — not vague "range of options"
- Brand name in S1, no competitors

### Type D — Promo / Deals
- S1 must contain ONE of: `{Category} Black Friday sale {year}` / `deals {year}` / `offers {year}`
- Include year immediately after the intent phrase
- Do not stack multiple intent phrases
- Use features/entities to carry commercial intent — not price language
- **Year rule:** Currently 2026. Update annually.

---

## Overuse Watch (Brand PLPs Specifically)

On brand PLPs (Type B and C), these words are banned because they make brand-specific copy feel generic:
- trusted, reliable, enjoy, features

On all other page types, these are fine in moderation.

"Upgrade" — only use for aspirational products (cooking appliances, phones, TVs). Don't use for small products (scales, kettles, accessories).

See full overuse list in `00-tov-language-reference.md`.

---

## Sentence Structure

**Exactly 2 sentences.** No run-ons disguised with commas. No extra clauses added to pad length.

S2 should be shorter than S1. This keeps the visual weight balanced on mobile — a long S2 creates an awkward orphaned block.

**Don't open S1 with Discover, Explore, or Shop** — these work better as S2 openers. But this isn't a rigid template — if S2 genuinely reads better without one of these, that's fine too.

---

## Formatting
- Sentence case only (capitalise first word + proper nouns)
- Capitalise: brand names, The Good Guys, seasonal events
- If the H1 includes a seasonal phrase, rephrase naturally — don't copy the H1 verbatim
- Plain text only — no links, HTML, markdown
- No exclamation marks
- No hard-sell language

---

## Character Hygiene
- No encoding artifacts: â€', â€™, â€œ, â€¢, replacement glyphs (�)
- Use standard punctuation: hyphen (-), straight apostrophe (')
- Avoid en/em dashes unless confirmed to render correctly in CMS
- Correct brand capitalisation: Samsung, LG, Sony, TCL, TP-Link, Fisher & Paykel

---

## QA Checklist

### Mechanical
- [ ] Exactly 2 sentences
- [ ] 230–260 characters (aiming ~250)
- [ ] S2 shorter than S1
- [ ] "The Good Guys" appears exactly once
- [ ] No hard-banned words (check `00-tov-language-reference.md`)
- [ ] Sentence case throughout
- [ ] No encoding artifacts
- [ ] No links, HTML, or markdown
- [ ] Australian English

### Intent & Quality
- [ ] Page type classification matches URL
- [ ] S1 matches page intent (correct category, brand, or promo framing)
- [ ] Entities match page — no stray brands, no wrong product types
- [ ] Brand PLPs: no competitor mentions, spec-based not generic, no brand-banned words
- [ ] Copy reads naturally — not templated, not keyword-stuffed
- [ ] If part of a batch: check for pattern repetition across the set

### Staging
- [ ] Renders ≤5 lines on ~360px viewport
- [ ] No "Read more" trigger
- [ ] No awkward orphaned last line

---

## Rewrite Guidance

**If too long (>260):** Remove redundant adjectives → reduce list items → compress phrases → shorten S2 first (protect S1 clarity)

**If too short (<230):** Add one meaningful feature, variant, or use case. Don't pad with fluff.

**If S2 longer than S1:** Move detail into S1 or trim S2.

**If it sounds like every other intro in the batch:** Rewrite with a different angle — lead with use case instead of benefit, or lead with the product type instead of the outcome.
