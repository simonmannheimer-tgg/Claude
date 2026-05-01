# TGG SEO Deck — Chart Design Specification

Companion document to `tgg-chart-templates.py`. Defines the visual language, colour system, and chart types used in the TGG Monthly SEO Update deck. Any AI or developer should be able to recreate these charts exactly from this document and the template code.

---

## Design principles

- White background, no decorative elements
- Horizontal grid lines only, light grey (#e8e8e8), weight 0.7pt
- No top or right spine; left and bottom spines in #cccccc
- No markers on lines unless data points are sparse (≤9 points)
- Smoothing applied to lines for visual clarity — gaussian sigma 1.2 — but all data labels use raw values, never smoothed values
- Labels sit directly above or below the line they belong to, offset 6–9pt, never overlapping
- End-of-series labels (rightmost point) are bold; all others normal weight
- Font: DejaVu Sans (matplotlib default) at 6–8.5pt for labels, 7.5–8.5pt for axis labels
- Legend: top-left, no frame, label colour matches line colour

---

## Colour system

| Metric | Hex | Usage |
|---|---|---|
| Clicks (GMC/GSC) | `#3c83f6` | Blue — matches Google Search Console clicks colour |
| Impressions (GMC/GSC) | `#8762d0` | Purple — matches Google Search Console impressions colour |
| Shopping / Purchases | `#1e8c45` | Green — differentiates shopping metrics from traffic metrics |
| Difference shading positive | `#70ad47` | Green fill, alpha 0.15 — current month above prior |
| Difference shading negative | `#e12b23` | Red fill, alpha 0.12 — current month below prior |
| Grid lines | `#e8e8e8` | Light grey |
| Spines | `#cccccc` | Medium grey |
| Axis labels / tick labels | `#7f7f7f` | Mid grey |
| Prior month line | Same as metric colour | Dashed, alpha 0.45–0.5, linewidth 1.4–1.6 |
| Current month line | Same as metric colour | Solid, linewidth 2.0–2.2 |

---

## Chart type 1 — Multi-month trend with dual axis

**Use for:** GMC clicks and impressions over 9 months (Jul–Mar). Any metric where two series share the same seasonal shape but different scales.

**Layout:**
- Single panel, dual y-axis
- Left axis: primary metric (clicks), colour matches line
- Right axis: secondary metric (impressions), colour matches line
- Impressions labels sit ABOVE the impressions line (+7pt offset)
- Clicks labels sit BELOW the clicks line (−9pt offset)
- This separation prevents collision when lines track closely

**Smoothing:** gaussian sigma 1.2 applied to line path only. Labels show raw data values.

**Label format:**
- Clicks: `265K` (divide by 1000, round to nearest integer, append K)
- Impressions: `14.0M` (divide by 1,000,000, one decimal place, append M)
- Final month label bold; prior months normal weight

**Size for PPTX injection:** 6.452" × 2.421" at 150dpi (matches slide placeholder)

**No year dividers, no year labels, no vertical separator lines.**

---

## Chart type 2 — Current vs prior month day-by-day line

**Use for:** Organic shopping purchases, revenue, or any daily metric comparing two consecutive months normalised to the same number of days.

**Layout:**
- Single panel, single y-axis
- Current month: solid line, full opacity, linewidth 2.0–2.2
- Prior month: dashed line, alpha 0.45–0.5, linewidth 1.4–1.6
- Both lines same colour (metric colour — green for shopping)
- End labels: "Mar" bold right of final point; "Feb" faded right of final point

**Difference shading:**
- Fill between the two lines
- Green (#70ad47, alpha 0.15) where current > prior
- Red (#e12b23, alpha 0.12) where current < prior
- Use `matplotlib fill_between` with `interpolate=True`

**Normalisation:** Truncate both months to the shorter month's day count (28 for Feb vs Mar). X-axis runs 1–28.

**Smoothing:** gaussian sigma 1.4 applied to both lines for visual clarity. No point labels on this chart type — the shape is the message.

**X-axis ticks:** [1, 7, 14, 21, 28] only — sparse, clean.

**Size for PPTX injection:** 6.452" × 2.421" at 150dpi (matches slide placeholder)

---

## Slide 3 placeholder positions (EMU)

| Slot | Left | Top | Width | Height |
|---|---|---|---|---|
| Top (GMC chart) | 824,555 | 1,920,575 | 5,899,428 | 2,214,064 |
| Bottom (purchases chart) | 824,555 | 4,362,198 | 5,899,428 | 2,214,064 |

Chart images are injected at these positions after removing the IMAGE placeholder shapes. A text header (9pt, bold, #595959, Calibri) is placed 0.25" above each chart, with a 0.0625" gap between header and chart top edge.

**Header text:**
- Top: `GMC Clicks & Impressions  Jul 2025 to Mar 2026`
- Bottom: `Organic Shopping Purchases  Feb vs Mar 2026`

Note: use two spaces as separator, not a dash or em dash.

---

## Output format

All charts saved as PNG, transparent background except white fill, dpi=150, bbox_inches='tight'. Inject into PPTX using `python-pptx` `add_picture()` at the EMU positions above.
