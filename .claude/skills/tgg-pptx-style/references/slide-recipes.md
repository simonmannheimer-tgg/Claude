# TGG SEO Deck — Slide Recipes

Standard slide sequences used in the monthly deck. Each recipe covers: purpose,
title format, layout, data required, and which components to use.

---

## Standard deck sequence

| # | Slide type | Title pattern | Required data |
|---|---|---|---|
| 1 | Overview KPIs | `Monthly SEO Overview - [one-line summary subtitle]` | Sessions, Revenue, AI Visibility, variable KPI |
| 2 | Organic sessions trend | `Monthly SEO Overview - [organic story subtitle]` | 3-year sessions table, non-brand clicks table, avg rank chart |
| 3 | AI & LLM metrics | `Monthly SEO Overview - [AI story subtitle]` | AI Visibility table, Citations table, LLM sessions, Owned AIO trend |
| 4 | Organic shopping | `Monthly SEO Overview - [shopping story subtitle]` | GMC clicks chart, shopping keyword footprint |
| 5 | Factor slides (conditional) | `Factor N - [event description]` | SERP screenshots, Semrush data, volatility chart |
| 6 | Focus & Outcomes | `Monthly SEO Overview - How we are adapting to changes` | Updated workstream table |
| 7 | Thank you / close | `[Month Year] - Thank You!` | None — the Google search box visual |

Depth and order adjusts based on the month's story. Feb-26 ran three Factor slides and no
conclusion tile. Jan-26 added a second Focus & Outcomes slide with programme-level KPI tiles.

---

## Recipe 1: Overview KPI slide

**Purpose:** First thing stakeholders see — the four numbers that define the month.

**Title:** Should communicate the narrative. Not `"March 2026 SEO Update"`. Examples:
- `"Monthly SEO Overview - March rankings recovered, structural headwinds persist"`
- `"Monthly SEO Overview - Feb organic traffic down, revenue up, AI leadership strong"`

**Layout:**
```
[Title block]
[4 KPI tiles in a row]
[Organic sessions table — left 55%] | [Bullet insights — right 40%]
[Footnote definitions — bottom]
```

**Footnote block (standard, always include):**
```
Organic Sessions: Sessions from TGG Channel Group Organic Search (GA4) (contains both branded & non-branded searches)
Organic Revenue: Total Revenue from TGG Channel Group Organic Search (GA4)
Keywords in Top 3: Non-branded Keywords in Top 3 (SEMRush Organic Rankings)
Non-branded keywords: Keywords that don't contain variations of "good guys"
AI Visibility Score: Brand mention rate (%) of TGG mentioned across prompts (Profound)
AI Citations: TGG Website citation rate (%) across prompts (Profound)
```

**Bullet insights (right column):** 4 bullet points max. Each addresses one KPI tile:
- Why sessions moved (season, algo, structural)
- Revenue/conversion context (the "more with less" story when applicable)
- Rankings context (non-brand Top 3/10/100 direction)
- AI visibility context (rank, comp gap, prompt count)

**Competitor table (when included on this slide):**
Small 5×3 table (TGG, HN, AO, JB, Other) with AI Visibility % and Citation Rate % columns.
Position below bullet points in the right column.

---

## Recipe 2: Organic performance slide

**Purpose:** Show the ranking and click picture with the "why" clearly explained.

**Title variants:**
- Recovery month: `"Monthly SEO Overview - [Month] rankings recovered / grew across core verticals"`
- Volatile month: `"Monthly SEO Overview - [Month] SERP volatility hit non-brand clicks hard"`

**Layout:**
```
[Title block]
[Average rank chart — left 55%, full height] | [Non-brand clicks table — right 40%]
[Explanatory body text spanning full width — bottom third]
```

Or, when clicks data is the lead:
```
[Title block]
[Non-brand clicks table — left 55%] | [Branded clicks table — right 40%]
[Average rank chart — full width, lower half]
```

Match the layout to whichever dataset carries the story.

---

## Recipe 3: AI & LLM metrics slide

**Purpose:** Establish and maintain TGG's AI leadership narrative.

**Title:** `"Monthly SEO Overview - Despite headwinds, TGG is growing where it counts: AI"`
(Use this framing when organic is soft. Adjust if AI metrics also declined.)

**Layout:**
```
[Title block]
[AI Visibility table — full width, top half]
[AI Citations table — full width, below Visibility table]
[Body text / callout italic — below tables]
[Owned AIO keyword line chart — left 55%] | [Top domains in AIO table — right 40%]
```

**Body callout text (italic, positioned between tables and charts):**
Summarise the competitive lead in one sentence. Example:
`"We appear inside AI Overview results nearly twice as often as the nearest competitor, and are the #2 highest cited website after YouTube for relevant prompts."`

This sentence should update every month to reflect current margin.

---

## Recipe 4: Organic shopping slide

**Purpose:** Show that shopping is holding or growing, and why feed optimisation matters.

**Title:** `"Monthly SEO Overview - Despite headwinds, TGG is growing where it counts: Organic Shopping"`

**Layout:**
```
[Title block]
[3 bullet points — full width]
[GMC clicks bar chart — left 55%] | [Shopping keyword footprint line chart — right 40%]
```

**Required data points:**
- GMC clicks absolute number, current month
- GMC clicks trend (is it holding at the ~265K baseline or growing?)
- Shopping keyword footprint % growth since Jul-25 (migration baseline)
- TGG vs competitor footprint comparison

---

## Recipe 5: Factor slide

**Purpose:** Explain a specific external event — algorithm update, SERP structural change, industry shift.

**When to use:** Only when there is discrete, evidenced cause-and-effect between an external event and TGG's data. Not for general structural observations.

**Title:** `"Factor [N] - [plain English description of the event]"`

**Structure:** No fixed layout. Content drives the design. Typical pattern:
- Left body text explaining the factor
- Right: screenshot, Semrush chart, or SERP example image
- If the factor has multiple sub-points, consider separate slides (Factor 1a, 1b) rather than overcrowding

**Naming discipline:** If Feb needed four Factor slides because of two distinct events (algo volatility + CTR compression), use `Factor 1` for all algo slides and `Factor 2` for CTR slides. Don't mix events under the same factor number.

---

## Recipe 6: Focus & Outcomes

**Purpose:** Accountability — what we said we'd do, what we actually did.

**Title:** `"Monthly SEO Overview - How we are adapting to changes"` (fixed, every month)

**Layout:** Full-width table spanning the usable slide area.

**Footers to always include:**
- `"+ Ongoing SEO fundamentals"` immediately below table, small italic
- Status legend above or beside table: `"⚪ Scoping/Not Started 🟡 In-progress 🟢 Completed"`

**Active workstreams as of Mar-26 (update list as items complete or are added):**
- AI tracking foundation
- SERP Changes: CTR
- Blog AI summaries
- AI-ready PLP intro copy rollout
- PLP Query Fanouts
- Blog Briefs
- PDP FAQs V2
- PDP AI rendering audit
- Video rendering / Video schema
- AI Commerce Content (PDP)
- AI-optimised product descriptions
- Product feed optimisation
- Technical Infrastructure Roadmap

---

## Recipe 7: Close slide

**Purpose:** Visual full stop. Invites questions without being fussy.

**Content:** `"[Month Year] - Thank You!"` as title. Body: the Google search bar graphic with "Questions?" as the query — a recurring device across all three decks, keep it.

**Layout:** Title + lone centred graphic. No data. No bullets.

---

## QA checklist for TGG decks specifically

- [ ] Every slide has the left red accent bar and bottom red corner block
- [ ] Title format matches `"Monthly SEO Overview - [subtitle]"` on content slides
- [ ] KPI tiles are aligned horizontally; no tile taller or wider than its neighbours
- [ ] AI Visibility table shows all months since Sep-25 (do not truncate)
- [ ] Footnote/definition block present on slide 1
- [ ] Status legend present on Focus & Outcomes slide
- [ ] Competitor colour tokens match (TGG navy, HN orange, AO purple, JB green)
- [ ] Focus & Outcomes Latest Result column has updated text — not copy-pasted from prior month
- [ ] No slide title is centre-aligned
- [ ] Close slide uses the Google search bar graphic
