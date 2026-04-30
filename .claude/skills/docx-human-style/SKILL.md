---
name: docx-human-style
description: Apply when creating any Word document (.docx). Enforces plain, human-looking document defaults. Prevents AI-generated document aesthetics — no custom brand colours, no styled heading colours, no shaded table headers, no decorative elements. Use whenever the user asks for a Word doc, report, brief, or any .docx output.
---

# DOCX Human Style

Word documents should look like a person made them in Word. Not like a design tool, a slide deck, or an AI trying to impress. The default Word aesthetic is correct. Do not override it.

---

## The problem to avoid

AI-generated .docx files default to:
- Custom heading colours (navy, blue, teal, branded hex values)
- Shaded table header rows in dark colours with white text
- Alternating row shading across table bodies
- Decorative horizontal rules, title banners, or divider lines
- Non-standard fonts chosen for visual effect
- Over-formatted title pages with multiple font sizes and colour accents
- Subtitle lines listing the document sections ("Section A | Section B | Section C")
- Skipping an intro paragraph and jumping straight into content
- Page breaks that produce blank pages

These patterns immediately mark a document as AI-generated. Do not produce them unless explicitly asked.

---

## Defaults to always use

**Font:** Arial, 11pt (22 in DXA half-points) for body text throughout.

**Headings:**
- H1: Arial, 14pt (28), bold, black. Spacing before 360, after 120.
- H2: Arial, 12pt (24), bold, black. Spacing before 240, after 80.
- No colour values on any heading. No underlines on headings or subtitle lines.
- CRITICAL: docx-js HeadingLevel styles inherit Word's built-in blue colour by default. You MUST override them in the document `styles` block or headings will render blue regardless of what you set on the TextRun. Always include this in every document:

```javascript
styles: {
  paragraphStyles: [
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: "Arial", size: 28, bold: true, color: "000000" },
      paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 0 } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: "Arial", size: 24, bold: true, color: "000000" },
      paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 1 } },
  ]
}
```

**Body text:** Arial, 11pt, black, spacing before/after 80.

**Tables:**
- Simple single-line black borders: BorderStyle.SINGLE, size 4, color "000000"
- Header row: bold text only. No fill, no shading, no white text on dark background.
- Body rows: white background. No alternating shading.
- Cell padding: top 80, bottom 80, left 120, right 120.
- Always set both columnWidths on the table AND width on each cell in DXA.

**Code blocks and prompt text:** Courier New, 9pt (18), with light grey paragraph shading (fill: "F5F5F5", type: ShadingType.CLEAR). Always use this for any code, prompt, or template content — never render it as plain body text.

**Colours:** Black text (000000) on white background throughout. No hex colour values unless the user specifies them.

**Page layout:** 1 inch margins (1440 DXA) all sides.

**Page breaks:** Use only where a new section genuinely needs a new page. Never add a page break after the last content block — this creates a blank final page.

**Footer:** Page number, right-aligned, 9pt. Only on multi-page documents.

**No decorative elements:** No coloured rules, no banner paragraphs, no styled divider lines.

---

## Document opening — what to always include

Every document must open with:
1. A plain bold title (one line, black, no colour)
2. A brief intro paragraph (2-4 sentences) explaining what the document is and how to use it
3. Then section content

Do not add a subtitle line listing the sections. Do not add a decorative rule under the title.

AVOID:
  TGG Product Descriptions                              <- large coloured title
  Feedback Summary | Audit Checklist | Updated Prompt   <- section list subtitle
  ─────────────────────────────────────────────────     <- decorative rule

DO:
  TGG Product Descriptions                              <- plain bold title, black

  This document covers the feedback from the 38-product <- intro paragraph
  audit, a reusable audit checklist, the updated prompt,
  and a change log.

---

## Pre-generation checklist

Run through this before writing any docx-js code:

- [ ] Heading styles overridden in the document `styles` block with color "000000" — not just on the TextRun
- [ ] Table header rows: bold text only, no fill shading
- [ ] Table body rows: no alternating shading
- [ ] Font is Arial throughout
- [ ] Code and prompt content uses Courier New with F5F5F5 shading
- [ ] No subtitle line under the title
- [ ] Intro paragraph present after the title
- [ ] No PageBreak after the last content block
- [ ] No decorative coloured rules or dividers

---

## docx-js patterns

Header row — bold, no fill:
  new TableCell({
    borders,
    width: { size: 3000, type: WidthType.DXA },
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [new Paragraph({
      children: [new TextRun({ text: "Column", size: 20, bold: true })]
    })]
  })

Code block paragraph:
  new Paragraph({
    children: [new TextRun({ text: "content", font: "Courier New", size: 18 })],
    shading: { fill: "F5F5F5", type: ShadingType.CLEAR },
    spacing: { before: 0, after: 0 }
  })

Plain H1:
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: "Title", bold: true, size: 28 })],
    spacing: { before: 360, after: 120 }
  })

---

## When the user complains the doc looks AI-generated

This skill was not applied. Check the pre-generation checklist, identify what failed, fix it, rebuild. Do not apologise — just fix and resubmit.
