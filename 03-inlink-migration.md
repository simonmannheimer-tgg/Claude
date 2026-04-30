# Process 03: Inlink Migration (Top Copy → Bottom Copy)

> **Version:** 1.0  
> **Last updated:** 2026-02-27

## Purpose

Rewrite ecommerce HTML copy so it can move from the top of a page to the bottom, while preserving all internal links and avoiding duplication of the top copy's intent.

## Inputs

- `{HTML_CODE}` — Current HTML code including all internal links (`<a>` tags)
- `{TOP_COPY}` — Top copy text whose intent, angle, and primary elements must NOT be duplicated

---

## Core Rules

### 1. Avoid Duplicating Top Copy Intent
- Do not replicate the combination of: primary use case + features + brands + opening benefit phrasing from `{TOP_COPY}`
- Use secondary/alternative angles: design, layout, aesthetics, ease of use, versatility, efficiency, convenience, complementary sub-benefits

### 2. Preserve Internal Links
- All `<a>` tags must remain exactly as in `{HTML_CODE}`
- `href` must not change
- Anchor text may adapt naturally
- Anchor tags must contain only anchor text — no punctuation, spaces, or `&nbsp;` inside
- Punctuation sits outside the `<a>` tag
- Do not nest anchor tags or place them directly adjacent

### 3. Slate/CSS Formatting (CMS-Specific)

| Element | Required Format |
|---------|----------------|
| Paragraphs | `<div class="css-9daywu" data-slate-node="element">` |
| Text spans | `<span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">…</span></span></span>` |
| Lists (ul) | `<ul class="css-bjaxj3" data-slate-node="element">` |
| List items | `<li class="css-165b468" data-slate-node="element">` |

- Each `<li>` must wrap a `<div class="css-9daywu">` with Slate spans
- Anchor tags in lists must retain CMS classes and nested spans exactly
- No new CSS classes, inline styles, or plain HTML elements
- All output must be paste-safe in React/Slate-based editors

### 4. Structure & Formatting
- Use multiple paragraphs for general content
- Use bullet points (`<ul>`/`<li>`) for lists or multiple sub-benefits
- Every sub-benefit must be a bullet when multiple points exist
- Avoid mirroring the top copy's single-paragraph style

### 5. Tone & SEO
- Engaging, benefit-driven, ecommerce-appropriate
- Australian English (optimise, favourable, organisation)
- Include relevant product-category keywords naturally
- Highlight credible brands when relevant

---

## QA Checklist

- [ ] All original `<a>` tags preserved with unchanged `href`
- [ ] No punctuation inside anchor tags
- [ ] Slate formatting classes correct on all elements
- [ ] Intent/angle is distinct from top copy
- [ ] Australian English used throughout
- [ ] Bullets used for multi-point content
- [ ] No new CSS classes or inline styles
- [ ] Paste-safe for React/Slate CMS

---

## Notes

- The Slate CSS class names (`css-9daywu`, `css-bjaxj3`, `css-165b468`) are specific to the current CMS build. If CMS changes, these will need updating.
- Consider using Process 06 (Internal Linking — Hierarchy Validation) rules when evaluating which links to emphasise in the rewrite.
