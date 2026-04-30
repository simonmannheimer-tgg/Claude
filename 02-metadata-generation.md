# Process 02: Metadata Generation

> **Version:** 1.0 — Merged from API (batch) + Chat (single) prompts  
> **Last updated:** 2026-02-27

## Purpose

Generate meta titles and descriptions for The Good Guys website URLs. Supports two modes: batch processing (CSV output) and single URL (detailed output).

## Modes

**Batch mode:** Input = list of URLs → Output = CSV rows  
**Single mode:** Input = one URL → Output = structured block with keyword identification

---

## Page Type Classification

Identify before writing:

| Type | Pattern | Approach |
|------|---------|----------|
| Category/PLP | /air-fryers, /washing-machines | Include brands, product types, features |
| Content/Editorial | /whats-new/how-to-... | Focus on topic, user benefit, actionable advice |
| Brand | /samsung/tvs | Lead with brand, include product range |
| Utility | /terms-of-use, /scam-alerts | Informational, trust-focused |

---

## Meta Title Rules

| Rule | Requirement |
|------|-------------|
| Length | Maximum 60 characters |
| Structure | `[Primary Keyword] - [Feature/Benefit] [Modifier]` |
| Separators | Dashes (-) or colons (:) — no pipes for editorial content |
| Keyword placement | Primary keyword in first half |
| Do NOT include | "The Good Guys", "best", "top", "cheap", "deals", "sale", "save" |

### Good Examples
- `Air Fryers - Dual Zone & Compact Models for Every Kitchen`
- `How to Clean Your Oven - Quick Tips for Sparkling Results`
- `Samsung OLED TVs - 4K Picture with Dolby Atmos Sound`

---

## Meta Description Rules

| Rule | Requirement |
|------|-------------|
| Length | 140–155 characters (hard max: 155) |
| Structure | `[User Benefit]. [Details]. [The Good Guys]. [CTA].` |
| CTA | `Shop online or in-store today!` OR `Shop now at The Good Guys.` |
| TGG mention | Exactly once, mid-description (not at start) |
| Ending | Must end with `.` or `!` |

### Prohibited
- "peace of mind"
- "reliable" more than once
- "hassle-free" / "fuss-free" / "worry-free" in same description
- Delivery/shipping mentions
- Price mentions
- "expert advice"

### Trust Phrase Rotation
Instead of "peace of mind", rotate: with confidence, you can count on, built to last, trusted performance, backed by warranty

---

## Page Type Specifics

**Category/PLP:** Include 2–3 top brands, mention key product types or filters (dual zone, compact, large capacity)

**Content/Editorial:** Focus on topic and user benefit, no brand lists unless article is brand-specific

**Brand:** Lead description with brand name, include product range breadth

---

## Output Formats

### Batch Mode (CSV)
```
Address,New Title,Title Len,Description,Desc Len
```
No header row if appending to existing file.

### Single Mode
```
URL: [provided URL]
Keyword: [identified primary keyword]

Title: [your title]
Title Length: [character count]

Description: [your description]
Description Length: [character count]
```

---

## QA Checklist

- [ ] Title ≤60 characters
- [ ] Description 140–155 characters
- [ ] No "The Good Guys" in title
- [ ] "The Good Guys" appears once in description (not at start)
- [ ] No prohibited words
- [ ] Ends with correct CTA format
- [ ] Proper punctuation (. or !)
- [ ] Primary keyword in first half of title
