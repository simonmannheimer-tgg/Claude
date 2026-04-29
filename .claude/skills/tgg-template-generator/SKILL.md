---
name: tgg-template-generator
description: Full-context template and scaffolding skill for The Good Guys SEO workflow. Use when asked to generate a template, scaffold a new document structure, create a brief, or produce a starter format for any repeatable TGG SEO task — including copy briefs, process docs, campaign planning, analytics reports, and meeting/stakeholder documents.
---

# TGG Template Generator

You generate clean, production-ready scaffolding for Simon's SEO workflow at The Good Guys. Every template must use realistic TGG placeholders (not generic ones), confirm any character-limited fields, and follow the formatting conventions already established across Simon's process files and working documents.

---

## Who this is for

**Simon Mannheimer**, SEO Strategist at The Good Guys (thegoodguys.com.au), Melbourne. Works across PLP copy production, AEO/AI visibility, technical SEO, Semrush position tracking, GSC/GA4 analysis, internal linking, and cross-team briefs for dev, merch, and content.

---

## Template catalogue

### 1. Copy Brief

Use when briefing any page for copy production.

```markdown
# Copy Brief — [Page / Category Name]

**Date:** [DD Month YYYY]
**Owner:** Simon Mannheimer
**Deadline:** [date]
**Priority:** High / Medium / Low

---

## Objective
[What this copy needs to achieve — organic traffic, AEO citation, conversion, campaign support]

## Page details
- **URL:** https://www.thegoodguys.com.au/[slug]
- **Page type:** PLP / Editorial / Campaign landing / Brand PLP
- **Category path:** [e.g. Televisions > OLED TVs > Samsung OLED]
- **Is this a brand PLP?** Yes / No
  - If yes: ban "trusted", "reliable", "enjoy", "features" from intro

## Target keywords
- **Primary:** [keyword]
- **Secondary:** [keyword], [keyword]
- **AEO question targets:** [question 1], [question 2], [question 3]

## Copy required
- [ ] H1 suggestion
- [ ] PLP intro (230–260 chars)
- [ ] EAV description (250–265 chars) — if different field
- [ ] Meta title (≤60 chars)
- [ ] Meta description (145–160 chars)
- [ ] FAQ section — [n] questions, interleaved in body
- [ ] Other: [specify]

## Formatting rules (always apply)
- No em dashes (period+space for independent clauses; comma for non-essential phrases)
- S1 of PLP intro: action verb, not Discover/Explore/Shop
- "The Good Guys" in S2 only
- FAQ headings interleaved — not collected at end of page
- Internal links: full absolute URLs (https://www.thegoodguys.com.au/...)

## Reference pages
- **Competitor:** [JB Hi-Fi or other URL for benchmarking]
- **Existing TGG page (tone ref):** [URL]
- **Other:** [brief or GSC report link]

## Notes
[Anything else relevant — seasonal context, CMS constraints, dev dependency, launch date]
```

---

### 2. SEO Audit Brief

Use when scoping an audit for a page or category.

```markdown
# SEO Audit Scope — [Category / Page Name]

**Date:** [date]
**URL:** https://www.thegoodguys.com.au/[slug]
**Priority:** High / Medium / Low
**Trigger:** [Ranking drop / New page / Quarterly review / Campaign prep]

---

## Scope
- [ ] Technical (canonicals, indexability, structured data, CWV)
- [ ] On-page (H1, headings, copy, internal links)
- [ ] Metadata (title, description)
- [ ] Schema (type needed: FAQPage / Product / CollectionPage)
- [ ] AEO readiness (question headings, definitional copy, comparison content)
- [ ] Keyword alignment (current rankings vs target keywords)

## Current performance baseline
- **GSC non-brand clicks (last 28 days):** [n]
- **Average position:** [n]
- **Top ranking keyword:** [keyword]
- **Known issues:** [brief description or "none identified"]

## Deliverable
- [ ] Audit findings doc
- [ ] Prioritised recommendation list
- [ ] Revised copy (if on-page changes needed)
- [ ] Schema markup (if applicable)

## Deadline
[date]
```

---

### 3. Semrush / GSC Analytics Report

Use when presenting data to stakeholders or logging a performance review.

```markdown
# Organic Performance Report — [Category / Period]

**Report date:** [date]
**Period:** [date range]
**Data sources:** GSC / Semrush (AU) / GA4
**URL scope:** https://www.thegoodguys.com.au/[slug or "site-wide"]

---

## Headline metrics

| Metric | Current period | Prior period | YoY change |
|--------|---------------|-------------|------------|
| Non-brand clicks | | | |
| Total impressions | | | |
| Average position | | | |
| CTR | | | |
| Organic sessions (GA4) | | | |

---

## Key findings
1. [Finding — quantified, e.g. "Non-brand clicks down 18% YoY, driven by position losses on [keyword cluster]"]
2. [Finding]
3. [Finding]

---

## Traffic concentration
- Top 3 keywords account for: [n]% of total clicks
- Non-brand share of organic: [n]%
- Risk level: Low / Medium / High

---

## Root cause (if performance changed)
[What drove the change — structural (URL/nav), content quality, algorithm, competition]

---

## Competitor context
[JB Hi-Fi or other relevant competitor data if available]

---

## Recommended actions

| Action | Priority | Owner | Deadline |
|--------|----------|-------|---------|
| [Action] | High/Med/Low | Simon / Dev / Content | [date] |

---

## Supporting data
[Link to GSC export / Semrush report / GA4 segment]
```

---

### 4. Campaign Planning Template

Use for BFCM, Mother's Day, Back to School, or any seasonal campaign.

```markdown
# Campaign SEO Plan — [Campaign Name] [Year]

**Campaign dates:** [start] – [end]
**Planning deadline:** [date copy/tech work must be complete]
**Owner:** Simon Mannheimer

---

## Campaign objective
[What SEO needs to achieve — ranking, traffic, AEO citation, page retention]

---

## URL strategy
- **Dedicated page:** https://www.thegoodguys.com.au/[slug] ← recommended
- **Or generic /deals/ path:** [flag risk — see note below]

> ⚠️ **BFCM URL risk note:** In 2025 TGG used generic /deals/ URLs instead of dedicated BF pages, removed BF from navigation, and saw non-brand BFCM clicks fall 41.2% YoY. Dedicated seasonal URLs with navigation placement are strongly recommended.

---

## Priority pages / categories

| Category | URL | Current avg position | Target position | Copy needed |
|----------|-----|---------------------|----------------|------------|
| [e.g. TVs] | /televisions | | | Yes / No |

---

## Keyword targets

| Keyword | Volume (AU) | Current position | Target |
|---------|-------------|-----------------|--------|
| [e.g. black friday tv deals] | | | |

---

## Copy checklist
- [ ] Campaign landing page: H1, intro, meta title, meta description
- [ ] Category PLP updates for priority categories
- [ ] FAQ section (campaign-specific questions interleaved)
- [ ] Internal linking plan (nav + body links to campaign page)

---

## Technical checklist
- [ ] Dedicated URL confirmed (not /deals/)
- [ ] Page added to navigation by [date]
- [ ] Schema applied (CollectionPage or FAQPage)
- [ ] Redirect plan if URL changes from prior year

---

## Timeline

| Task | Owner | Deadline |
|------|-------|---------|
| Copy brief finalised | Simon | |
| Copy produced | | |
| Dev implementation | Dev | |
| QA / publish | | |
| Post-launch GSC check | Simon | |
```

---

### 5. Cross-Team Dev Brief

Use when raising an SEO technical request with the dev team.

```markdown
# SEO Dev Request — [Brief description]

**Date:** [date]
**Requested by:** Simon Mannheimer, SEO
**Priority:** Critical / High / Medium / Low
**Required by:** [date]

---

## What is needed
[Plain English description — one paragraph, no jargon]

---

## Why it matters (SEO impact)
[Quantify or qualify the impact — e.g. "affects 230 category pages", "blocking indexation of new product range", "estimated +X% non-brand clicks if resolved"]

---

## Technical specification

**Affected URLs:**
- https://www.thegoodguys.com.au/[example-1]
- https://www.thegoodguys.com.au/[example-2]
- [or: "all pages matching pattern /[pattern]/"]

**What needs to change:**
[Specific technical instruction — e.g. "Add FAQPage schema to all category pages with FAQ sections", "Set canonical tag on all ?colour= parameter URLs to the base URL", "Add rel=next/prev to paginated category pages"]

**Example of correct implementation:**
```[code or markup example]```

**Acceptance criteria:**
- [ ] [How to verify it's done correctly]
- [ ] [Second check]

---

## References
- [Spec doc / Google documentation URL]
- [GSC error report or Screaming Frog export if relevant]

---

## Notes
[Edge cases, exceptions, staging environment, rollout order]
```

---

### 6. Stakeholder Update (SEO performance)

Use for weekly or monthly updates to head of marketing, GM, or other stakeholders.

```markdown
# SEO Update — [Month/Period]

**Date:** [date]
**Prepared by:** Simon Mannheimer

---

## Headline

[One sentence: the most important thing that happened in organic search this period]

---

## Organic performance

| Metric | This period | Last period | Change |
|--------|------------|------------|--------|
| Non-brand clicks | | | |
| Total organic sessions | | | |
| Average position (top 50 keywords) | | | |

---

## Wins this period
- [Win — quantified where possible]
- [Win]

---

## Issues / risks
- [Issue — with context and what's being done about it]

---

## Work completed
- [Task completed]
- [Task completed]

---

## In progress
- [Task in progress — ETA]

---

## Upcoming priorities
1. [Next priority]
2. [Next priority]

---

## Needs from stakeholders
- [Decision / resource / access needed — be specific]
```

---

## Generation rules

When generating any template:
1. Fill placeholders with **realistic TGG examples** — use actual category names, real URL patterns, plausible keyword examples. Never use "[Product Name]" when "Robot Vacuums" is more useful.
2. Confirm character counts for any copy fields.
3. Flag the em dash rule in any copy-facing template.
4. Flag the BFCM URL risk in any seasonal campaign template.
5. Note where full absolute URLs are required (https://www.thegoodguys.com.au/...).
