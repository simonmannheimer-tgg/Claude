# TGG SEO Deck — Design Tokens

Derived from the Jan-26, Feb-26, and Mar-26 monthly SEO update decks.
These are the exact values to use when writing or editing XML.

---

## Colours

### Primary palette

| Token | Hex | RGB | Usage |
|---|---|---|---|
| `navy` | `#1553a2` | 21, 83, 162 | KPI tile backgrounds, table header rows, primary dark background |
| `red` | `#e12b23` | 225, 43, 35 | Left accent bar, bottom corner block, alert/negative values |
| `white` | `#FFFFFF` | 255, 255, 255 | Text on dark backgrounds, slide body background |
| `black` | `#000000` | 0, 0, 0 | Slide titles, body text on white |
| `gray-text` | `#595959` | 89, 89, 89 | Footnote/definition text, secondary labels |

### Table conditional formatting

| Token | Hex | Usage |
|---|---|---|
| `table-neg` | `#FF0000` (15% opacity fill) or full red cell text | Negative YoY/MoM values in data tables |
| `table-pos` | `#70AD47` | Positive performance highlights |
| `table-warn` | `#FFC000` | Borderline / watch values |
| `table-tgg-row` | No fill — bold text only | TGG rows in competitor comparison tables |
| `table-alt-row` | `#DEEAF1` | Alternating row fill (light blue) where used |

### Competitor colour coding (charts)

| Competitor | Colour | Hex |
|---|---|---|
| TGG | Navy / Dark Blue | `#1553a2` |
| Harvey Norman | Orange | `#FF7F27` |
| Appliances Online | Purple | `#7030A0` |
| JB Hi-Fi | Green | `#00B050` |

These apply to all multi-line charts, SOV charts, and any visual comparing the four competitors.

---

## Fonts

| Element | Typeface | Size | Weight | Colour |
|---|---|---|---|---|
| Slide title | Calibri | 28–32pt | Bold | Black `#000000` |
| Title subtitle (after dash) | Calibri | 28–32pt | Regular | Black `#000000` |
| Period/metadata line | Calibri | 10pt | Regular | `#595959` |
| KPI tile metric name | Calibri | 11–12pt | Bold | White |
| KPI tile value | Calibri | 36–44pt | Bold | White |
| KPI tile MoM/YoY label | Calibri | 10pt | Regular | White |
| Table header text | Calibri | 11pt | Bold | White |
| Table body text | Calibri | 10–11pt | Regular | Black |
| Body bullet text | Calibri | 13–14pt | Regular | Black |
| Body bold inline labels | Calibri | 13–14pt | Bold | Black |
| Footnote/definition text | Calibri | 9pt | Italic | `#595959` |
| Factor label ("Factor 1") | Calibri | 28–32pt | Bold | Black |

**Note:** If the deck uses a non-Calibri font (check the XML `<a:latin typeface="">` attribute),
match the existing typeface — do not substitute Calibri if something else is in use.

---

## Slide dimensions

Standard widescreen 16:9. All EMU values:

| Dimension | Inches | EMUs |
|---|---|---|
| Slide width | 13.33" | 12192000 |
| Slide height | 7.5" | 6858000 |
| Safe margin (left/right) | 0.5" | 457200 |
| Safe margin (top) | 0.75" | 685800 |
| Safe margin (bottom) | 0.6" | 548640 |

---

## Persistent structural elements

Every content slide must have both of these. Never remove them.

### Left red accent bar

Thin vertical rectangle on the far left edge of the slide.

```
x:      0 (flush with slide left edge)
y:      ~4,572,000 EMU (≈5.0" from top, lower two-thirds of slide)
width:  ~91,440 EMU (0.1")
height: ~2,286,000 EMU (2.5")
fill:   solid red #CC0000
line:   none
```

*(Exact values vary slightly across slides — match the existing file's XML when editing.)*

### Bottom-left red corner block

Small filled rectangle locked to the bottom-left corner.

```
x:      0
y:      ~6,400,000 EMU (near slide bottom)
width:  ~457,200 EMU (0.5")
height: ~457,200 EMU (0.5")
fill:   solid red #CC0000
line:   none
```

---

## Spacing rules

- Minimum gap between any two content blocks: 0.25" (228,600 EMU)
- KPI tile internal padding: 0.15" top/bottom, 0.2" left/right
- Table row height: minimum 0.35" (320,040 EMU) for readability
- Footnote text sits at least 0.15" above the slide bottom margin
- Title block (title + red separator line + period line) occupies top ~1.2" of slide
