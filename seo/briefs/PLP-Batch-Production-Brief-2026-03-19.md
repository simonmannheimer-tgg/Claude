# PLP Intro Copy — Batch Production Brief

**Project:** The Good Guys brand+category PLP intro copy
**Scope:** Batches 2–4, ~843 URLs, Status = Not Started
**Date issued:** 19 March 2026
**Owner:** Simon Mannheimer, SEO Strategist, The Good Guys

---

## 1. Objective

Produce production-ready 2-sentence PLP intro copy for all Not Started URLs across Batches 2–4 of the brand+category PLP migration. Output must be ready for direct Contentful upload with zero manual editing required.

---

## 2. Pre-flight — complete before opening the issue

### 2a. Update `.claude/agents/plp-copywriter.md`

Find:
```
Range: 230–260 characters total (every letter, space, punctuation)
Sweet spot: ~250. Don't pad or truncate awkwardly.
```

Replace with:
```
Range: 220–250 characters (every letter, space, punctuation).
Lower end preferred. Aim for 225–235 where copy reads naturally.
Floor: 220. Never below. Ceiling: 250. Hard stop.
If S1 runs long, shorten S2 first.
```

Also change any reference from `01-plp-intro-copy.md` to `01-plp-intros.md`.

---

### 2b. Sync `01-plp-intro-copy.md` with `01-plp-intros.md`

Copy the full contents of `01-plp-intros.md` into `01-plp-intro-copy.md`. Both filenames stay in the repo — bring them into sync so both reflect the 220–250 range.

---

### 2c. Update Claude.ai skills — char range and consistency

The `tgg-copywriting` skill was updated separately via Edit with Claude. The following three skills still carry the old 230–260 char range and need the same fix applied wherever they reference PLP intro character counts.

**`tgg-seo-specialist/SKILL.md`**

| Find | Replace with |
|------|-------------|
| `Length: 230–260 characters. Strict. Confirm count before every delivery.` | `Length: 220–250 characters. Lower end preferred (225–235 ideal). Floor 220, ceiling 250. Confirm count before every delivery.` |
| `- [ ] PLP intro: character count confirmed (230–260)` | `- [ ] PLP intro: character count confirmed (220–250, lower end preferred)` |
| `**Character count: [n] / 230–260**` | `**Character count: [n] / 220–250**` |

**`tgg-content-strategist/SKILL.md`**

| Find | Replace with |
|------|-------------|
| `**Length: 230–260 characters exactly. Confirm count before every delivery.**` | `**Length: 220–250 characters. Lower end preferred (225–235 ideal). Floor 220, ceiling 250. Confirm count before every delivery.**` |
| `- [ ] PLP intro: character count confirmed (230–260)` | `- [ ] PLP intro: character count confirmed (220–250, lower end preferred)` |
| `**Character count: [n] / 230–260** ✓ or ✗` | `**Character count: [n] / 220–250** ✓ or ✗` |

**`tgg-template-generator/SKILL.md`**

| Find | Replace with |
|------|-------------|
| `- [ ] PLP intro (230–260 chars)` | `- [ ] PLP intro (220–250 chars, lower end preferred)` |

`tgg-marketing-analyst` and `tgg-repo-manager` — no PLP char limits referenced. No changes needed.

---

### 2d. Commit all pre-flight repo changes

```bash
git add .claude/agents/plp-copywriter.md \
        01-plp-intro-copy.md \
        01-plp-intros.md

git commit -m "fix(agents,process): update plp-copywriter and process files — char range 220-250"
git push -u origin HEAD
```

Skills are updated via the Claude.ai UI (Edit with Claude) — no git commit required for those.

---

## 3. Source file

**Filename:** `TGG_-_SEO_WIP___SM_-_PLP_Intro__Brand_Cat_.csv`
**Location:** Confirm path in repo before running

**Parse rules:**
- Skip row 1 (blank)
- Header is row 2
- Filter: `BATCH` = "Batch 2" OR "Batch 3" OR "Batch 4"
- Filter: `Status` (rightmost column) = "Not Started"
- Expected row count: ~843

**Key columns:**

| Column | Use |
|--------|-----|
| `Address` | Page URL — primary input |
| `Type` | Page type hint (B1 = Brand Hub, B2 = Brand+Category, B3 = Brand+Category deeper) |
| `Non brand clicks (3mnt)` | Traffic threshold for Semrush decision |
| `Current Intro` | Existing copy — do not replicate angle or phrasing |
| `Status` | Filter to "Not Started" only |

---

## 4. Agent chain

Orchestrate via `seo-team-lead`. Run this sequence per URL:

```
1. eav-researcher         → map brand + category entity landscape
2. seo-keyword-researcher → pull Semrush url_organic (if traffic threshold met)
3. plp-copywriter         → write copy using both inputs
```

**Token efficiency rules:**
- Run `eav-researcher` and `seo-keyword-researcher` in parallel where inputs allow
- Pass only JSON summaries between agents — never raw API responses
- Use `ctx_index` / `ctx_search` for any result set over 100 lines
- Run `ctx_list()` at session start to reuse already-indexed category data

---

## 5. Semrush keyword pull — conditional

**Pull only if:** `Non brand clicks (3mnt)` > 200

**Parameters:**
```
report:          url_organic
database:        au
display_limit:   8
display_sort:    tr_desc
export_columns:  Ph, Po, Nq, Tr
```

**If below threshold:** use brand knowledge and `eav-researcher` output only. Do not make a Semrush call.

---

## 6. Page type classification

The CSV `Type` column is a hint only. Verify against URL pattern before writing:

| Type | URL pattern | Key rules |
|------|-------------|-----------|
| B — Brand Hub | `/[brand]` only (1 slug after root) | Brand in S1, proprietary tech, no competitors, no: trusted / reliable / enjoy / features |
| C — Brand + Category | `/[brand]/[category]` or deeper | Brand + category-specific tech in S1, sub-types in S2, no: trusted / reliable / enjoy / features |
| A — Generic Category | No brand slug | 2–3 brand names, category benefit, breadth in S2 |

CSV codes map as: B1 = Type B, B2 = Type C, B3 = Type C (deeper path).

---

## 7. Copy rules

### Character count
- Range: 220–250 characters (every letter, space, punctuation mark)
- Target: 225–235
- Floor: 220 — never below
- Ceiling: 250 — hard stop
- Do not pad to reach 220. Do not force truncation to stay under 250. If it reads well at 228 or 244 that is correct.

### Structure
- Exactly 2 sentences
- S2 must be shorter than S1
- S1: brand name + at least one specific technology, format, or differentiator
- S2: TGG anchor + 2–3 specific sub-types, series names, tech references, or capacity ranges

### S1 opener rotation — vary across the batch

Rotate through these angles. No single angle should exceed 30% of the batch:

| Angle | Description |
|-------|-------------|
| Outcome-first | What the product does for the user |
| Feature-first | Lead with a named proprietary technology |
| Format-first | Lead with product format range |
| Spec-first | Lead with a capacity or spec range |
| Problem-first | Lead with what the product solves |

Do **not** open S1 with: Discover, Explore, Shop.

### S2 opener rotation

Valid openers: Find, Shop, Discover, Explore, Choose. Rotate. Never open 3+ consecutive S2s the same way.

### TGG placement

"The Good Guys" appears exactly once per piece. Vary S2 position (early / mid / late) across the batch — do not default to end of S2 on every piece.

### Hard bans — never use

| Banned | Reason |
|--------|--------|
| sale / sales | SEM compliance |
| save / saving as price framing ("save money", "save on", "save with Price Beat") | SEM compliance |
| discount | SEM compliance |
| exclusive (re: deals) | Legal |
| amazing, stunning, wonderful | Generic, oversold |
| busy homes, hearty meals, sleek design | Cliché, AI-sounding |
| Australia's trusted choice | SEM compliance |
| quality brands | SEM compliance |
| get great value | SEM compliance |
| perfect for all needs | Too vague |

> **Note:** "save time", "save space", "save energy" used as functional outcomes are NOT banned.

### Brand PLP restrictions (Type B and C only)

Do not use on brand pages: **trusted, reliable, enjoy, features.**
These are permitted in moderation on Type A (generic category) pages.

### Vague language — always replace with specifics

| Avoid | Use instead |
|-------|-------------|
| "advanced technology" | Name the technology (e.g. TwinDos, BubbleWash, InstaView) |
| "a wide range of options" | Name the formats or sub-types |
| "great features" | Name the actual feature |
| "superior performance" | Describe the specific outcome |

### Do not replicate existing copy

Read the `Current Intro` column before writing. Do not repeat the same angle, opening verb, or primary benefit from the existing copy. New copy must approach the page from a different direction.

### Australian English

optimise, colour, organisation, centre, favourite, behaviour, programme, catalogue, grey, aluminium, tyre, recognise, maximise, specialise.

---

## 8. Batch variation check

After every 20 URLs, scan before continuing. Flag and rewrite if:

- 3+ consecutive S1 openers use the same verb or structure
- 3+ consecutive S2 openers use the same word
- The same benefit angle leads more than 30% of the sub-batch
- TGG appears in the same S2 position (early/mid/late) in more than 60% of the sub-batch

---

## 9. Validation — run before writing to output

| Check | Pass condition |
|-------|----------------|
| Character count | 220–250 inclusive |
| Sentence count | Exactly 2 |
| S2 length | Shorter than S1 |
| TGG mention | Exactly 1 |
| Hard-banned words | None present |
| Brand bans (B/C) | trusted / reliable / enjoy / features absent |
| Vague language | No "advanced technology", "wide range of options", "great features" |
| Australian English | Correct spelling throughout |

**On validation failure:** Mark the row `FAIL` with the specific reason. Do not silently drop it. Do not leave the Flag cell blank.

---

## 10. Output format

**File:** `seo/outputs/plp-brand-cat-batch2-4-YYYY-MM-DD.csv`

| Column | Content |
|--------|---------|
| `URL` | Full URL from source CSV |
| `Batch` | Batch 2 / Batch 3 / Batch 4 |
| `Page_Type` | A / B / C |
| `Copy` | Final 2-sentence copy, plain text, no HTML |
| `Chars` | Exact character count |
| `Status` | PASS or FAIL |
| `Flag` | Empty if PASS. Specific failure reason if FAIL (e.g. "261 chars", "contains 'reliable'") |

**Encoding:** UTF-8. No BOM. No smart quotes or encoding artifacts.

---

## 11. Commit and push

```bash
git add seo/outputs/plp-brand-cat-batch2-4-YYYY-MM-DD.csv
git commit -m "feat(outputs): plp brand+cat batch 2-4 copy — [row count] URLs"
git push -u origin HEAD
```

---

## 12. Issue reply

Post a summary comment to the triggering issue containing:

- Total URLs processed
- PASS count and FAIL count
- Breakdown by batch (Batch 2 / 3 / 4)
- Breakdown by page type (A / B / C)
- File path written
- Any systematic issues encountered (e.g. "214 URLs below Semrush threshold — written on brand knowledge only")
- End with: `_— Claude Code_`
- Do **not** include `@claude` anywhere in the reply

---

## 13. GitHub issue trigger

Once all pre-flight steps are complete, open an issue with this exact body:

---

```
@claude Use the seo-team-lead to produce PLP intro copy for all Not Started URLs in Batches 2–4 of the brand+category migration.

Source file: TGG_-_SEO_WIP___SM_-_PLP_Intro__Brand_Cat_.csv
Filter: BATCH = "Batch 2" OR "Batch 3" OR "Batch 4" AND Status = "Not Started"

Agent chain per URL:
1. eav-researcher — map brand + category entity landscape
2. seo-keyword-researcher — pull url_organic from Semrush (database: au, display_limit: 8, display_sort: tr_desc, export_columns: Ph,Po,Nq,Tr) ONLY if Non brand clicks (3mnt) > 200
3. plp-copywriter — write copy using 01-plp-intros.md and 00-tov.md rules

Copy rules:
- 220–250 chars. Lower end preferred (225–235 ideal). Floor 220, ceiling 250 hard stop
- Exactly 2 sentences. S2 shorter than S1
- S1: brand name + at least one specific technology, format, or differentiator
- S2: TGG anchor + 2–3 specific sub-types, series, tech, or capacity ranges
- Vary S1 angles across batch: outcome-first, feature-first, format-first, spec-first. No single angle > 30% of batch
- Vary S2 openers: Find / Shop / Discover / Explore / Choose. Never 3+ consecutive same opener
- TGG placement must vary across batch — not always end of S2
- Hard bans: sale, discount, save-as-price-framing, amazing, stunning, wonderful, busy homes, sleek design, Australia's trusted choice, quality brands, get great value, perfect for all needs
- Brand pages (B/C) additionally ban: trusted, reliable, enjoy, features
- Do not replicate angle or phrasing from Current Intro column
- Australian English throughout
- Run variation check every 20 URLs — flag and rewrite repeats before continuing

Validation per row before output:
- 220–250 chars
- Exactly 2 sentences
- S2 shorter than S1
- TGG appears exactly once
- No hard-banned words
- No brand-banned words on Type B/C
- Vague language check: no "advanced technology", "wide range of options", "great features"
- On failure: mark FAIL with specific reason — do not drop silently

Output: seo/outputs/plp-brand-cat-batch2-4-YYYY-MM-DD.csv
Columns: URL, Batch, Page_Type, Copy, Chars, Status, Flag
Encoding: UTF-8, no smart quotes, no encoding artifacts

After writing: git add, commit with message "feat(outputs): plp brand+cat batch 2-4 copy — [n] URLs", push.

Reply with: total processed, PASS/FAIL counts, batch breakdown, page type breakdown, file path, any systematic issues. End with _— Claude Code_. Do not include @claude in the reply.
```

---

*Brief version: 1.0 — 19 March 2026*
