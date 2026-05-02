# Stage Contracts

Defines the input and output shape for each pipeline stage. Both `tgg-content-pipeline` and `tgg-content-engineer` (Claude.ai) use these contracts to hand off between stages.

---

## Stage 1: Intake

**Input:** User-supplied fields (keyword, content_type, slug, angle, byline, must_cover)
**Output file:** `runs/<run-id>/intake.md`
**Required fields:** keyword, content_type, slug, angle (or "none"), byline
**Gate:** Hard stop if angle or byline missing

---

## Stage 2: Research

**Input:** `intake.md` (keyword, content_type)
**Output file:** `runs/<run-id>/seo-data.md`
**Required content:**
- GSC impressions + clicks (last 90 days)
- GA4 engagement rate (existing TGG category content)
- Semrush KD, volume (AU), parent topic
- Top 5 ranking URLs for keyword
- Top 15 related queries by volume
- SERP intent classification (informational / commercial / navigational)

**Produced by:** `tgg-marketing-analyst` + `tgg-ce-research/scripts/run_research.py`

---

## Stage 3: Competitor and existing content

**Input:** `intake.md` (keyword, slug)
**Output files:** `runs/<run-id>/competitive-extract.md`, `runs/<run-id>/existing-content.md`

`competitive-extract.md` required content:
- For each competitor (JB Hi-Fi, Harvey Norman, Appliances Online):
  - URL
  - H1 / H2 / H3 structure
  - Key claims (3–5 bullet points)
  - Content gaps (topics they miss that TGG could own)

`existing-content.md` required content:
- Existing TGG pages matching keyword or slug pattern
- Contentful entry ID (if resolved)
- Current word count and last published date (if available)

**Produced by:** `tgg-seo (technical mode)` + `tgg-ce-competitor-extract/scripts/extract_competitors.py` + `tgg-contentful-linker`

---

## Stage 4: Brief

**Input:** `intake.md`, `seo-data.md`, `competitive-extract.md`, `existing-content.md`
**Output file:** `runs/<run-id>/brief.md`
**Required sections:**
- Target audience
- Primary keyword + secondary keywords
- Content angle (verbatim from intake.md)
- Must-cover topics (verbatim from intake.md)
- Differentiation from competitors
- EAV attributes to define (buying-guide and eav-explainer only)
- Schema requirements (FAQ, HowTo, etc.)
- Internal-link opportunities (slugs, not yet Contentful IDs)
- Australian retail considerations (energy ratings, finance, click-and-collect)

**Gate:** `verification-gate-protocol --type <content_type>` pre-draft check → must return PASS

**Produced by:** `tgg-seo (strategy mode)` using `tgg-template-generator` scaffold

---

## Stage 5: Outline

**Input:** `brief.md`
**Output file:** `runs/<run-id>/outline.md`
**Required:** H2 list with estimated word budget per section, H2 count within type target, FAQ H2 present

**Produced by:** `tgg-seo (strategy mode)`

---

## Stage 6: Draft

**Input:** `brief.md`, `outline.md`, `seo-data.md`, `competitive-extract.md`
**Output file:** `runs/<run-id>/draft.md`
**Required:** Word count within type range, internal-link placeholders as `[LINK: <slug>]`, FAQ block present

**Produced by:** `tgg-seo (strategy mode)` (body) + `tgg-seo (production mode)` (FAQ, PLP intro, metadata blocks)

---

## Stage 7: QA

**Input:** `draft.md`, constraint file from `verification-gate-protocol/constraints/<type>.yaml`
**Output file:** `runs/<run-id>/qa-report.md`
**Format:**
```
QA Report — <content_type> — <keyword>
Run: <run-id>

PASS/FAIL per constraint:
✓ word_count: <actual> within <min>–<max>
✓ h2_count: <actual> within <min>–<max>
✓ internal_links: <actual> within <min>–<max>
✗ faq_block: <failure detail>
...

Overall: PASS / FAIL
Block delivery: YES / NO
```

**Gate:** Any `block_delivery: YES` item → hard stop, present to human, wait

**Produced by:** `verification-gate-protocol` + `tgg-seo (technical mode)`

---

## Stage 8: Humanise

**Input:** `draft.md`
**Output file:** `runs/<run-id>/humanised-draft.md`
**Appended block:** `## Humaniser log` listing any patterns rewritten

**Produced by:** `tgg-humanizer` (always called, no exceptions)

---

## Stage 9: Finalise

**Inputs:** `humanised-draft.md` (or `simon-voice` output if byline: simon), `internal-links.md`, `metadata.md`
**Output files:**
- `runs/<run-id>/final.md` — assembled article with YAML front matter
- `runs/<run-id>/metadata.md` — title, description, slug, OG title
- `runs/<run-id>/faq.json` — JSON-LD FAQPage schema
- `runs/<run-id>/internal-links.md` — resolved Contentful entry IDs

**Produced by:** `tgg-contentful-linker` (links) + `tgg-seo (production mode)` (metadata) + optional `simon-voice`
