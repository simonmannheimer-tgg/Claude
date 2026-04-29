---
name: tgg-pptx-style
description: >
  Apply The Good Guys SEO deck visual style when creating or editing PowerPoint presentations
  for TGG — including the monthly SEO update, ad-hoc slides, or any deck Simon needs to match
  the established brand and layout system. Trigger when Simon asks to "build the deck", "add a
  slide", "update the presentation", "make slides from this data", or "match the TGG style".
  Also trigger when editing an existing TGG .pptx and content needs to be added or updated.
  This skill encodes the exact colour tokens, layout patterns, component specs, and XML
  conventions used across the Jan-26, Feb-26, and Mar-26 SEO update decks.
---

# TGG PPTX Style Skill

## Quick orientation

This skill sits on top of the base pptx skill. Always read `/mnt/skills/public/pptx/SKILL.md`
first for tooling (unpack, pack, QA workflow). This skill provides the TGG-specific design
system: colours, layouts, components, and slide-type recipes.

**For editing an existing TGG deck:** read `references/design-tokens.md` and `references/components.md`, then follow the base pptx editing workflow.

**For creating a new slide from scratch:** read all three reference files before writing any XML.

---

## Reference files

| File | When to read |
|---|---|
| `references/design-tokens.md` | Every time — colours, fonts, spacing |
| `references/components.md` | When building or editing KPI tiles, tables, factor slides, focus tables |
| `references/slide-recipes.md` | When adding a new slide type to match the existing deck |

---

## Workflow

### 1. If given an existing TGG .pptx

```bash
python scripts/thumbnail.py deck.pptx          # Visual layout map
extract-text deck.pptx                         # Content inventory
python scripts/office/unpack.py deck.pptx unpacked/
```

Read `references/design-tokens.md` to confirm the colour hex values match what's in the XML
(colours can drift between template versions). If they differ, note the actual values from the
XML — those take precedence.

### 2. If creating new slides to append

Use `add_slide.py` to duplicate the nearest matching existing slide. Do **not** create slides
from a blank layout — the TGG design carries specific shape groups, background elements, and
margins that a blank layout won't have.

```bash
python scripts/add_slide.py unpacked/ slide2.xml   # Duplicate closest match
```

### 3. Edit content

Follow base pptx editing.md rules. TGG-specific additions:
- Never remove the left red accent bar or bottom red corner block — they are part of every slide
- Never centre-align body text — TGG slides are fully left-aligned
- Bold all KPI tile metric names and all table header row text
- Maintain the title format exactly: `"Monthly SEO Overview - [subtitle]"` with the dash separating fixed prefix from variable subtitle

### 4. QA

Run the base pptx visual QA (soffice → pdftoppm → image inspection). Additionally check:
- Left red bar present on every content slide
- Bottom red block present on every slide
- KPI tile boxes are vertically aligned across the row
- Table header rows match the dark navy token exactly (not a lighter blue)
- No slide title is centre-aligned

---

## Core design principles

The TGG SEO deck is **data-dense and functional**, not decorative. Design decisions serve
readability of numbers and competitive comparisons, not aesthetics. When in doubt:

- More whitespace, not less
- Numbers bigger, labels smaller
- One strong visual (chart or table) per slide, not two competing ones
- The story goes in the title line — not buried in bullets
