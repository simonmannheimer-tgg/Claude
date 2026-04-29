---
name: tgg-chart-creator
description: >
  Create, style, and inject data charts into the TGG Monthly SEO Update deck.
  Use this skill whenever Simon asks to build, update, or regenerate charts for
  the monthly SEO deck — including GMC clicks/impressions trend charts, organic
  shopping day-by-day purchase charts, GSC non-brand performance charts, or any
  other metric visualisation destined for the PPTX. Also trigger when Simon asks
  to "rebuild the charts", "update the chart data", "inject into the deck",
  "new month data", or references chart colours, smoothing, label positions, or
  placeholder injection. This skill encodes the exact colour tokens, chart types,
  smoothing parameters, label conventions, and PPTX injection coordinates used
  across the TGG Mar-26 deck and forward.
---

# TGG Chart Creator

Generates styled matplotlib charts and injects them into the TGG Monthly SEO
Update PPTX. Two primary chart types. All design decisions are fixed — do not
deviate without explicit instruction from Simon.

Read `references/design-spec.md` before writing any chart code.
Read `references/chart-templates.py` to get the base code — swap data only.

---

## Colour tokens (never change without instruction)

| Metric | Hex | Notes |
|---|---|---|
| Clicks | `#3c83f6` | Matches GSC UI blue |
| Impressions | `#8762d0` | Matches GSC UI purple |
| Shopping / Purchases | `#1e8c45` | Green — differentiates from traffic |
| Diff shading positive | `#70ad47` | Alpha 0.15 |
| Diff shading negative | `#e12b23` | Alpha 0.12 |
| Grid | `#e8e8e8` | |
| Spines | `#cccccc` | |
| Axis labels | `#7f7f7f` | |

---

## Chart type 1 — Multi-month dual axis trend

**When:** Traffic volume over time. GMC clicks + impressions. GSC clicks + avg position.

**Key rules:**
- Gaussian sigma 1.2 for smoothing — line path only, never labels
- Labels use raw data values, not smoothed
- Impressions labels: ABOVE line, +7pt offset
- Clicks labels: BELOW impressions line position, −22pt offset (prevents collision)
- Final month label bold; all others normal weight
- No year dividers, no year labels, no vertical separator lines
- Dual y-axis: left = clicks (blue), right = impressions (purple)
- Figure size: 6.452" × 2.421" at 150dpi for slide injection

---

## Chart type 2 — Day-by-day MoM comparison

**When:** Shopping purchases, revenue, CVR compared month on month.

**Key rules:**
- Normalise both months to shorter month's day count (truncate longer)
- Current month: solid line, linewidth 2.0, full opacity
- Prior month: dashed line, linewidth 1.4, alpha 0.5
- Both lines same colour (GREEN `#1e8c45` for shopping)
- Difference shading: fill_between with interpolate=True
- Gaussian sigma 1.4 — no point labels, shape is the message
- X-axis ticks: [1, 7, 14, 21, N] only
- End labels right of final point: current bold, prior faded
- Figure size: 6.452" × 2.421" at 150dpi

---

## PPTX injection

Slide 3 (index 2). Two IMAGE placeholder shapes are removed and replaced.

| Slot | Left EMU | Top EMU | Width EMU | Height EMU |
|---|---|---|---|---|
| Top | 824,555 | 1,920,575 | 5,899,428 | 2,214,064 |
| Bottom | 824,555 | 4,362,198 | 5,899,428 | 2,214,064 |

Header text box: 9pt Calibri bold, colour `#595959`, height 0.25" (228,600 EMU), gap 0.0625" (57,150 EMU) between header and chart.

Header wording format: `[Metric]  [Date range]` — two spaces as separator, no dash.

---

## Workflow

1. Read `references/design-spec.md` for full spec
2. Get data from Simon (CSV, screenshot, or values pasted in)
3. Load `references/chart-templates.py`, swap data arrays only
4. Build charts, verify visually before injecting
5. Inject into PPTX using `inject_charts_into_deck()`
6. QA: convert to PDF, check slide visually, confirm no label collisions

---

## Common mistakes to avoid

- Never use smoothed values for data labels — always raw
- Never add year dividers or year labels to the GMC chart
- Never put impressions labels below the line (they go above)
- Never put clicks labels above (they go below)
- Never change colour tokens without explicit instruction
- Never smooth with sigma > 1.4 — it distorts the seasonal shape
- Never use markers on monthly trend charts (9 points — no markers needed)
