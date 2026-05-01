# TGG SEO Deck — Component Specifications

Reusable components that appear across multiple slides. Each has a layout spec,
content rules, and XML pattern notes.

---

## 1. Slide title block

Appears at the top of every content slide.

**Structure (top to bottom):**
1. Title text: `"Monthly SEO Overview"` in bold + `" - "` + subtitle in regular weight, all in one text box, left-aligned
2. Red separator bar: short solid red rectangle, ~0.5" × 0.06", immediately below the title text, left-aligned to the title
3. Period/metadata line: `"Period: [Month Year] | Compared to: MoM & YoY | Migration: Jul-25"` — 10pt gray, italic

**Title formatting rule:** The bold prefix and the regular-weight subtitle must be in the same text box using two separate `<a:r>` runs with different `b` values. Never split them into two text boxes.

**"Factor" slide variant:**
Title reads `"Factor N - [description]"` where "Factor N" is bold and the description is regular weight. Same structure, same fonts.

---

## 2. KPI tiles (headline metric row)

Four dark navy boxes in a horizontal row below the title block. This is the first data element on overview/summary slides.

**Layout:**
- 4 tiles, evenly spaced across the slide width
- Each tile: approximately 2.8" wide × 1.5" tall
- Total row width: ~11.5" centred on slide
- Gap between tiles: ~0.2"

**Each tile contains (top to bottom):**
1. Metric name — 11pt bold white, centred within tile
2. Value — 36–44pt bold white, centred, this is the dominant visual element
3. MoM% label — 10pt white, format: `"MoM %: [value]"` — negative values in same white (tile communicates bad news via context, not colour)
4. YoY% label — 10pt white, format: `"YoY %: [value]"`

**Tile background:** Solid navy `#003087`, rounded corners optional (match existing file).

**Common tile metrics by slide type:**

*Overview slide:*
- Organic Sessions + MoM% + YoY%
- Organic Revenue + MoM% + YoY%  
- AI Visibility Score (rank) — YoY shown as N/A if tracking <12 months
- Variable: AIO Keywords, LLM Sessions, or Keywords in Top 3 depending on month's story

*AI metrics slide:*
- AI Visibility % (rank)
- AI Citation Rate % (rank)
- LLM Sessions + MoM%
- Owned AIO Keywords + MoM%

---

## 3. Organic sessions table

Multi-year YoY comparison table. Present on the main organic performance slide.

**Columns:** Month | 2023 | 2024 | 2025 | 2026 | YoY 24v23 | YoY 25v24 | YoY 26v25

**Formatting:**
- Header row: navy background, white bold text
- Current reporting month row: yellow fill `#FFC000` or bold to draw attention
- YoY cells: colour-coded (red text = negative, standard = neutral/positive)
- TOTAL row: navy background, white bold text (matches header style)
- Font: 10pt Calibri throughout
- Left column (Month): bold

**Width guidance:** Table fills ~55% of slide width. Right 45% holds bullet insights or an average rank chart.

---

## 4. Non-branded clicks table

Separate from sessions. Shows absolute non-brand clicks by month across years.

**Columns:** Month | 2024 | 2025 | 2026 | YoY 25v24 | YoY 26v25

**Same formatting rules as sessions table.** Typically paired with branded clicks table and a non-brand % of total table on the same slide — three narrow tables side by side.

---

## 5. AI Visibility competitor table

The core AI leadership evidence. Appears on the AI metrics slide.

**Two tables, stacked:**

*Table 1 — AI Visibility (Profound):*
- Columns: Brand | Sep-25 | Oct-25 | Nov-25 | Dec-25 | Jan-26 | Feb-26 | [current month]
- Rows: TGG, HN, AO, JB
- TGG row: bold, no special fill
- Other rows: standard
- Header: navy/white

*Table 2 — AI Citations (Profound):*
- Same column structure as Table 1
- Same row structure

**Important:** Show all months since Sep-25 (tracking start). Never truncate historical columns — the trend showing TGG's consistent #1 position is the story.

---

## 6. Focus & Outcomes table

The workstream status table. Appears at end of every deck.

**Columns:** Focus | Status | Outcomes | Latest Result

**Status indicator values:** ⚪ Scoping/Not Started | 🟡 In-progress | 🟢 Completed

**Formatting:**
- Header row: navy, white bold
- Status column: narrow (fits the circle emoji only, roughly)
- Focus column: italic text
- Outcomes column: bullet list of 2–3 outcome metrics
- Latest Result column: widest — plain prose, current month's update
- Alternating rows: light blue fill `#DEEAF1` on odd rows, white on even (or all white — match existing)
- Footer: small italic text `"+ Ongoing SEO fundamentals"` below table

**Content rule:** Every Latest Result cell must contain month-specific content. Identical text across consecutive months is a QA failure.

---

## 7. Organic shopping chart slide

**Layout:** Two-column.
- Left column (~55% width): Bar chart — GMC clicks by month, Jul-25 to current. Blue bars (`#003087`). Pink/dashed reference line at the pre-peak baseline (~265K). Month labels on x-axis.
- Right column (~40% width): Line chart — Organic shopping keyword footprint, TGG vs competitors Jul-25 to current. Use competitor colour tokens from design-tokens.md.

**Chart title:** Left chart — no title (context from slide title). Right chart — small label: `"ORGANIC SHOPPING KEYWORDS — TGG VS COMPETITORS [DATE RANGE]"`

**Supporting text block:** 3–4 bullet points in left column above or below the chart summarising: GMC click trend, footprint growth %, feed optimisation implication.

---

## 8. Factor slides

Used when a significant external event (algorithm update, SERP change) needs its own dedicated explanation. Feb-26 used three Factor 1 slides plus a Factor 2 slide.

**Title pattern:** `"Factor [N] - [one-line description of the factor]"`

**Content:** Free-form — can include screenshots, charts from Semrush/Semrush Sensor, comparison tables, bullet explanations. No fixed layout but always left-aligned body text.

**Decision rule:** Only add Factor slides when there is a discrete external event that changed results in a way that requires evidence, not just acknowledgement. Do not add a Factor slide for gradual structural changes — those belong in the main narrative bullets.

---

## 9. Conclusion / summary tile slide

Optional. Used when the month has a clean 3–4 point story. Jan-26 used this; Feb-26 did not (too complex).

**Layout:** 3–4 equal navy tiles arranged in a 2×2 or 1×3 grid, centred on slide, below a minimal title.

**Each tile:** Metric name (bold white small), large bold white value or short label, 2–3 lines of white body text explanation.

**Use when:** The deck tells a recovery or leadership story cleanly. Skip when the month needs nuance that tiles would oversimplify.
