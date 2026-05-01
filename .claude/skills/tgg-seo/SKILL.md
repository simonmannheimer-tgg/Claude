---
name: tgg-seo
description: Single source of truth for all SEO work at The Good Guys (thegoodguys.com.au), an Australian electronics and appliances retailer. Use for copy production (PLP intros, metadata, FAQ, category copy, EAV, inlink migration), content strategy (briefs, calendars, AEO frameworks), and technical SEO (audits, schema, internal linking, keyword research, AEO/GEO). Trigger on any SEO request for TGG including "write copy for these URLs", "batch intros", "metadata for these pages", "rewrite this HTML copy", "audit this page", "schema for", "keyword research", "internal linking", "FAQ section", "campaign brief", "content calendar", or when context (Australian retailer, appliance/electronics categories) implies TGG SEO work even without explicit mention. Replaces the former tgg-copywriting, tgg-content-strategist, and tgg-seo-specialist skills.
---

# TGG SEO Skill

Single source of truth for SEO work at The Good Guys. Three modes:

1. **Production**: copy delivery (PLP intros, metadata, FAQ, EAV, category copy, inlink migration)
2. **Strategy**: briefs, content calendars, AEO frameworks, editorial planning
3. **Technical**: audits, schema, internal linking, keyword research, AEO/GEO

State at the start of any response which mode you're in: `[tgg-seo: production]`, `[tgg-seo: strategy]`, or `[tgg-seo: technical]`. Multi-mode tasks can chain: `[tgg-seo: strategy → production]`.

---

## Hard rules — non-negotiable, apply to every output

### PLP intro copy
- **Length: 220-250 characters. Strict. Confirm count before every delivery.**
- **Lower end preferred (225-235 ideal).**
- **Two sentences.** S1 opens with an action verb, S2 brings in The Good Guys.
- **S1 opens with an action verb** — never Discover, Explore, or Shop.
- **"The Good Guys" appears in S2 only.** Never in S1. Never more than once.
- **Brand PLPs** (Apple, Samsung, LG, Dyson, etc.) additionally ban these words anywhere in the intro: **trusted, reliable, enjoy, features**

### Em dash rule
- Never use an em dash to connect independent clauses. Replace with a period and space.
- Never use an em dash to set off a non-essential phrase. Replace with a comma.
- Zero tolerance. Check every output before delivering.

### Metadata
- **Title tags**: under 60 characters. Format `[Primary keyword] | The Good Guys` or `[Primary keyword] - [modifier] | The Good Guys`. Lead with the keyword, not the brand.
- **Meta descriptions**: 145-160 characters. Action-oriented. Include primary keyword naturally. No keyword stuffing. Unique per page.

### EAV descriptions
- **Length: 250-265 characters**
- May serve a different CMS field than PLP intros. Treat as separate unless confirmed otherwise.
- No brand name requirement. Write as a standalone product or category description.

### FAQ / AEO copy
- Question headings must be **interleaved throughout content**, never bunched at the end.
- Use explicit H2 or H3 question headings, not just question-style body copy.
- **Answer directly in the first 40-60 words** for featured snippet targeting. Expand below if needed.
- Question phrasing should match how a person would search ("What should I look for in a robot vacuum?" not "Robot vacuum buying guide").

### URLs in any output
- Always use full absolute URLs: `https://www.thegoodguys.com.au/[slug]`
- Never relative paths.
- Confirm 200 OK before providing in copy or FAQ output.
- No UTM tracking parameters.

### Australian English everywhere
optimise, colour, organisation, centre, favourite, behaviour, recognise.

---

## Production mode

### Step 1 — Identify content type

| Type | Trigger phrases | Reference file |
|------|----------------|----------------|
| PLP intro | "PLP intro", "2-sentence intro", category/brand URL | `references/01-plp-intros.md` |
| Metadata | "meta title", "meta description", "metadata", "title tag" | `references/02-metadata.md` |
| Inlink migration | "rewrite HTML", "top to bottom copy", "inlink migration", "bottom copy" | `references/03-inlink-migration.md` |
| FAQ / category copy | "FAQ", "category copy", "brand+category copy", "extended intro" | `references/05-faq-category-copy.md` |
| EAV descriptions | "EAV", "entity attribute value", "category entity mapping" | `references/08-eav-descriptions.md` |

If the request spans multiple types, load each relevant reference file.

### Step 2 — Load references

**Always load `references/00-tov.md` first.** Hard-banned words, overuse warnings, Australian English rules, phrasing principles. Then load the specific reference for the content type. Do not work from memory. Use the `view` tool.

### Step 3 — Classify the page

| Type | URL pattern | Examples |
|------|-------------|----------|
| A. Generic category | No brand slug | /audio, /coffee-machines |
| B. Brand hub | Brand slug only | /samsung, /lg |
| C. Brand + category | Brand slug + category | /samsung/fridges, /dyson/vacuums |
| D. Promo / deals | /deals/ path | /deals/black-friday-fridges |

Page type affects which rules apply.

### Step 4 — Write the copy

Cross-cutting principles:

1. **Sound human.** If it reads like a chatbot or a keyword list disguised as prose, rewrite it.
2. **Be specific.** Name brands, features, use cases. Specificity makes copy useful to humans and citable by AI.
3. **Vary everything.** Sentence openers, TGG placement, benefit angles, structure. No two pieces in a batch should follow the same skeleton.
4. **Guardrails, not templates.** The banned-word list tells you what to avoid. There is no "allowed words" list.

### Step 5 — Batch mode (3+ items)

After writing, run the cross-batch variation check:

- **Opener repetition**: Do 3+ pieces start with the same structure? Rewrite the duplicates with different angles.
- **TGG placement repetition**: Is "The Good Guys" always in the same position? Vary it.
- **Benefit-angle repetition**: Do most pieces lead with the same angle? Mix in use-case-first, product-first, or outcome-first angles.
- **Vocabulary clustering**: Are certain words appearing in 50%+ of pieces (e.g. "range", "perfect", "upgrade")? Diversify.

**Batch sizes**:
- Up to 20 items: write all, then run variation check
- 21-50: write in sub-batches of ~15, variation check per sub-batch and across full set
- 50+: flag as large batch, suggest breaking into thematic groups

### Step 6 — Self-QA

Run the QA checklist from the relevant reference file before presenting. Don't present and then list QA failures as caveats. Fix first, present second.

---

## Strategy mode

### Campaign briefs

```
## Campaign Brief - [Name]

**Objective:** [traffic / conversion / brand awareness]
**Deadline:** [date]
**Owner:** [name]

### Target keywords
- Primary: [keyword]
- Supporting: [keyword], [keyword]
- AEO question targets: [question 1], [question 2]

### Page details
- URL: [slug or full URL]
- Page type: [PLP / editorial / landing / campaign]
- Category: [e.g. Televisions > OLED TVs]

### Copy required
- [ ] H1
- [ ] PLP intro (220-250 chars)
- [ ] Meta title (≤60 chars)
- [ ] Meta description (145-160 chars)
- [ ] FAQ section ([n] questions, interleaved)
- [ ] Other: [specify]

### Constraints
[Brand PLP rules / seasonal rules / any exceptions]

### Reference pages
[Competitor or TGG benchmark URLs]
```

### AEO content framework

For any page targeting AI citation:

1. **Definitional opening** in the first 100 words. AI engines cite early definitional text.
2. **Explicit question headings** (H2/H3 phrased as questions, not topic labels).
3. **Direct answer first**, then elaborate.
4. **Comparison framing** ("X vs Y", "corded vs cordless") where natural.
5. **Category and collection pages are TGG's strongest AI citation asset.** Treat as authoritative reference documents.
6. **Vacuums is a known competitive gap.** Prioritise structured, comprehensive copy.

### Seasonal campaign context

| Campaign | Period | Key SEO consideration |
|----------|--------|-----------------------|
| Black Friday / Cyber Monday | November | Structural risk: TGG replaced dedicated BF pages with generic /deals/ URLs in 2025. Combined BFCM sessions fell 23.5% YoY; non-brand organic clicks fell 41.2% YoY. Always flag if seasonal content is being directed to a generic URL. |
| Boxing Day | Late December | Dedicated page recommended |
| Back to School | Jan/Feb | Laptops, tablets, printers. High volume. |
| Mother's Day | May | Kitchen appliances, coffee machines, beauty devices |
| Father's Day | September | BBQs, audio, power tools adjacent |
| EOFY | June | Hub-led approach confirmed (single /eofy-sale page, not category pages). Generic deals pages launched July 2025, June 2026 is first like-for-like measurement point. |
| Apple launches | Rolling | New iPhone/MacBook. High-volume brand + category opportunity. |
| Samsung launches | Rolling | Galaxy S series, TVs. Similar pattern. |

---

## Technical mode

### Page audit checklist

When auditing any TGG category or product page:

1. **Canonical**: self-referencing, no conflicts with faceted navigation
2. **Indexability**: confirm not noindexed, check robots.txt for category paths
3. **Structured data**: Product, BreadcrumbList, FAQPage where applicable
4. **Core Web Vitals**: LCP < 2.5s, CLS < 0.1, INP < 200ms
5. **Internal linking**: parent-child circular links are intentional per TGG strategy. Verify alignment with mega-menu structure.
6. **Heading structure**: H1 contains primary keyword. Question headings interleaved, not bunched.
7. **Pagination**: rel=next/prev or canonical to first page for filtered/paginated PLPs
8. **Redirect chains**: flag any 301 → 301 sequences
9. **Duplicate content**: colour variants, parameterised filter URLs, tag pages

### On-page optimisation

- One H1 per page, containing primary keyword
- H2s and H3s should include secondary keywords and question variants
- Image alt text: descriptive and keyword-relevant, not stuffed
- Internal links: intent-driven, descriptive anchor text, mirror mega-menu hierarchy

### Internal linking strategy

Intent-driven, mega-menu-mirroring approach:
- Parent-to-child and child-to-parent circular links are intentional. Do not flag as issues.
- Anchor text must be descriptive and intent-matched (not "click here" or "learn more")
- Link targets should mirror the mega-menu category hierarchy
- Brand + category combinations should link to the relevant brand PLP within that category (e.g. "Samsung TVs" links to `/samsung-tvs`, not just `/televisions`)
- Deals pages serve distinct intent from category pages
- Gift pages cross-link by budget level

### Keyword research output format

| Type | Keyword | AU volume (est.) | Intent | Difficulty |
|------|---------|------------------|--------|------------|
| Primary | [head term] | [range] | [informational/commercial/transactional] | [low/medium/high] |
| Secondary | [modifier + category] | | | |
| Long-tail / AEO | [question variant] | | | |

Always include:
- Intent classification per keyword
- At least 3 question-format variants for AEO/FAQ use
- Notes on SERP features (featured snippets, PAA, shopping)

### Schema templates

#### CollectionPage (PLP)
```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "[Category Name]",
  "description": "[PLP intro copy - 220-250 chars]",
  "url": "https://www.thegoodguys.com.au/[slug]",
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.thegoodguys.com.au/"},
      {"@type": "ListItem", "position": 2, "name": "[Category]", "item": "https://www.thegoodguys.com.au/[slug]"}
    ]
  }
}
```

#### FAQPage
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text - match H2/H3 exactly]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[40-60 word answer for featured snippet targeting]"
      }
    }
  ]
}
```

#### Product (individual product page)
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product name]",
  "brand": {"@type": "Brand", "name": "[Brand]"},
  "sku": "[SKU]",
  "offers": {
    "@type": "Offer",
    "url": "https://www.thegoodguys.com.au/[product-slug]",
    "priceCurrency": "AUD",
    "price": "[price]",
    "availability": "https://schema.org/InStock",
    "seller": {"@type": "Organization", "name": "The Good Guys"}
  }
}
```

---

## Production checklist — run before every delivery

- [ ] PLP intro: character count confirmed (220-250, lower end preferred)
- [ ] EAV description: character count confirmed (250-265) if applicable
- [ ] No em dashes anywhere in output
- [ ] S1 opens with action verb (not Discover, Explore, or Shop)
- [ ] "The Good Guys" appears in S2 only (PLP intros)
- [ ] Brand PLPs: no "trusted", "reliable", "enjoy", "features"
- [ ] Meta title: ≤60 chars
- [ ] Meta description: 145-160 chars
- [ ] FAQ question headings: interleaved, not bunched at end
- [ ] Internal links: full absolute URLs (https://www.thegoodguys.com.au/...)
- [ ] No UTM parameters on URLs
- [ ] All URLs verified 200 OK

---

## Standard output formats

### Copy delivery (single or batch)

```
## [Page Name / Category]

**URL:** https://www.thegoodguys.com.au/[slug]
**Page type:** [A. Generic / B. Brand hub / C. Brand + category / D. Promo]

### H1
[H1 text]

### PLP Intro
[Copy text]
**Character count: [n] / 220-250** ✓ or ✗

### EAV Description (if required)
[Copy text]
**Character count: [n] / 250-265** ✓ or ✗

### Meta Title
[Title text]
**Character count: [n] / 60 max** ✓ or ✗

### Meta Description
[Description text]
**Character count: [n] / 145-160** ✓ or ✗

### FAQ Section
*(Note: these headings interleave into body content, not collected as a block)*

**[H2: Question 1]**
[40-60 word answer for snippet targeting]

[Expanded answer if needed.]

**[H2: Question 2]**
[40-60 word answer]

### Production checklist
- [ ] Em dashes: none present
- [ ] S1 action verb confirmed
- [ ] The Good Guys in S2 only
- [ ] All char limits confirmed
- [ ] Internal links use full absolute URLs
```

### Batch PLP intros

```
| URL | Page Type | Copy | Chars |
|-----|-----------|------|-------|
| ... | ... | ... | ... |
```

### SEO audit

```
## SEO Audit - [Page/Category Name]

**URL:** https://www.thegoodguys.com.au/[slug]
**Audit date:** [date]

### Critical issues
- [Issue] - [Location] - [Recommended fix]

### On-page
- H1: [current] → [recommended]
- Title: [current] / [char count] → [recommended] / [char count]
- Meta description: [current] / [char count] → [recommended] / [char count]
- Heading structure: [assessment]
- FAQ headings: [interleaved / bunched - flag if bunched]

### Technical
| Check | Status | Notes |
|-------|--------|-------|
| Canonical | Pass/Fail/Warn | |
| Indexable | Pass/Fail | |
| Structured data | Pass/Fail/Missing | |
| Core Web Vitals | Pass/Fail | |
| Internal linking | Pass/Fail/Warn | |

### Recommendations (prioritised)
1. [Highest impact - estimated effort]
2. [Second priority]
3. [Third priority]
```

---

## Reference file index

| File | Content |
|------|---------|
| `references/00-tov.md` | Hard bans, overuse warnings, phrasing principles, Australian English. **Read first, always.** |
| `references/01-plp-intros.md` | 2-sentence PLP intro rules: char limits, page types, sentence structure, formatting |
| `references/02-metadata.md` | Meta title (≤60 chars) and description (145-160 chars) rules |
| `references/03-inlink-migration.md` | HTML rewrite rules: Slate/CSS formatting, link preservation, intent differentiation |
| `references/05-faq-category-copy.md` | FAQ generation, brand+category FAQ, extended PLP intro |
| `references/08-eav-descriptions.md` | Entity-attribute-value mapping for category research |

---

## Competitor context

**JB Hi-Fi (jbhifi.com.au)** - Primary competitor across all categories. Runs a dual-page strategy for major seasonal campaigns. Strong internal linking architecture mirroring category hierarchy. Generally matches or exceeds TGG on category page depth.

**Other tracked competitors**: Harvey Norman, Appliances Online.

**Known TGG structural issue (2025)**: TGG replaced dedicated Black Friday/Cyber Monday pages with generic `/deals/` URLs and removed BF pages from navigation. Combined BFCM sessions fell 23.5% YoY; non-brand organic clicks fell 41.2% YoY despite all-channel sessions growing +11.3%. Root cause is the URL and navigation strategy change. Flag this context when advising on any seasonal campaign page decisions.

---

## What this skill does NOT cover

- **Content humanisation** of AI-drafted text. Use `tgg-humanizer` as a post-edit filter.
- **Word document creation** with TGG branding. Use `docx-human-style` plus the public `docx` skill.
- **PowerPoint deck building**. Use `tgg-pptx-style`.
- **Monthly SEO report**. Use `tgg-monthly-seo-report`.
- **301 redirect mapping**. Use `tgg-301-mapper`.
- **Contentful entry lookup**. Use `tgg-contentful-linker`.
- **Templates and scaffolding for new artefact types**. Use `tgg-template-generator`.

If the user asks for something in this list, defer to the relevant skill and continue with the in-scope SEO work alongside.
