---
name: tgg-monthly-seo-report
description: >
  End-of-month SEO report creator for The Good Guys. Use this skill whenever Simon asks to
  build, draft, structure, or review the monthly SEO update — including the slide deck narrative,
  the stakeholder email, the focus & outcomes table, or any component of the monthly reporting
  cycle. Also trigger when asked to "prep the March report", "what should go in this month's update",
  "check if anything's missing from the report", or "help me write the send-out email". This skill
  encodes Simon's reporting structure, narrative style, data source requirements, QA checks,
  and the external research workflow that contextualises monthly findings.
---

# TGG Monthly SEO Report Creator

## Purpose

Build the monthly SEO update for The Good Guys: a stakeholder-ready slide deck narrative, a supporting email send-out, and a self-QA pass that catches stale data, missing sources, and inconsistencies before publish.

The report is not a data dump. It tells a story — what happened, why it happened, whether it matters, and what we're doing about it. Every metric earns its place by supporting that story.

---

## Step 0 — Data intake and gap check

Before building anything, run through the checklist below. Request any missing items from Simon explicitly. Do not proceed with gaps if they change the story.

### Required data inputs

| Source | What to pull | Tool |
|---|---|---|
| GA4 | Organic Sessions (MoM, YoY), Organic Revenue (MoM, YoY), Conversion Rate | GA4 / provided screenshot |
| GSC / Semrush | Non-branded clicks (MoM, YoY), Keywords in Top 3 / Top 10 / Top 100 (MoM, YoY), Average Position trend | Semrush or GSC export |
| Semrush | Total AIO keywords, Owned AIO keywords (TGG + competitors) | Semrush |
| Profound | AI Visibility % (TGG + HN + AO + JB), AI Citation Rate % (TGG + HN + AO + JB), LLM-referred sessions | Profound dashboard |
| GMC / Shopping | Organic shopping clicks (MoM trend), Shopping keyword footprint | GMC / Semrush |
| SERP volatility | Current volatility score, notable algo events in the month | MozCast, Semrush Sensor, or provided |
| Focus & Outcomes | Status updates on all active workstreams | Simon's input |

### Cross-report consistency checks (run before writing)

- Do this month's AI Visibility numbers match the trend from prior months? Flag any jump >10pp that isn't explained.
- Is AI Citation Rate directionally consistent with Owned AIO keyword growth?
- Do organic sessions align with the non-branded clicks trend (they should move roughly together)?
- Are the Focus & Outcomes status indicators (⚪🟡🟢) updated, or are any rows copy-pasted from last month with no change? Flag unchanged rows — Simon must confirm they are genuinely unchanged.
- Check whether competitor AI Visibility numbers have changed. If they haven't moved at all MoM, flag as likely stale.
- Are the LLM sessions numbers from GA4 or Profound? Confirm source matches prior months for consistency.

---

## Step 1 — External research (do this in parallel, always cite as speculation)

Before writing the narrative, search for:

1. **Google algorithm updates** in the reporting month. Check: https://moz.com/google-algorithm-change, https://semrush.com/sensor/, and search "Google algorithm update [month year]" on LinkedIn and SEO newsletters (Search Engine Roundtable, Growth Memo, Barry Schwartz).
2. **AI Overview / SGE changes** — any announcements from Google about AI Overview expansion, changes to how products appear, new SERP features.
3. **Retail SERP trends** — any reports on how shopping carousels, product grids, or paid ad density changed in the month.
4. **AI in search** — ChatGPT Shopping, Perplexity commerce, Gemini updates, any LLM changes that affect referral traffic patterns.
5. **Competitor moves** — any public signals (news, job postings, announcements) that explain competitor AI visibility changes.

**Mandatory disclaimer:** All externally sourced context must be labelled "Speculation / External Context" in the report. Never present it as confirmed fact for TGG's own data.

---

## Step 2 — Narrative architecture

Every monthly report follows this spine. Adjust emphasis based on what actually happened — not every section needs equal depth.

### The narrative arc

```
Opening headline → What happened → Why it happened → What it means → What we're doing
```

The opening headline (slide title / email subject line) must be honest but framed positively where possible. Examples from prior months:
- "March rankings recovered strongly — structural headwinds remain"
- "February SERP volatility hit non-brand clicks hard — AI leadership holds"
- "January: official migration recovery — AI and Shopping growing where it counts"

Do not write a bland descriptor ("March 2026 SEO Update"). The headline should give stakeholders the story in one line.

### Section order (slide deck)

1. **Overview KPI tile** — 4 headline numbers with MoM and YoY. Always: Organic Sessions, Organic Revenue (or Non-Brand Clicks if Revenue not available), AI Visibility Score (rank), and one variable metric (AIO Keywords or LLM Sessions depending on what moved most).
2. **Organic performance** — Sessions trend table (3 years), non-branded clicks table, average rank trend chart. Explain the why, not just the what.
3. **AI & LLM metrics** — AI Visibility competitive table (all months since Sep-25), AI Citation Rate table, Owned AIO keyword trend, LLM sessions trend. TGG's lead vs competitors is the anchor.
4. **Organic Shopping** — GMC clicks trend chart, shopping keyword footprint vs competitors, feed optimisation narrative.
5. **Focus & Outcomes table** — All active workstreams. Status, outcome, latest result. Must be updated — stale rows are a credibility risk.
6. **Contextual / external slide** (include when there's a meaningful algo event or structural SERP change) — Framed as "Factor 1/2", with screenshots or data where available.
7. **Conclusion / thank you** — Optional summary tile with 3-4 key callouts. Used when the month has a clear clean story.

---

## Step 3 — Metric framing rules

These are non-negotiable. Apply every time.

**Sessions**
- Report MoM% and YoY%. If YoY is negative, contextualise against the prior year's YoY (e.g., "-5.7% YoY on top of +2.4% YoY in Mar-25").
- If sessions recovered after a volatile prior month, lead with the recovery, then add the structural caveat.

**Non-branded clicks**
- Always compare YoY. MoM is seasonal noise. Flag if the YoY trend is worsening vs the previous month's YoY.
- Note the current non-brand % of total clicks. If it's trending down, that matters.

**AI Visibility**
- Always report TGG vs HN, AO, JB. The lead margin is the headline number, not the absolute %.
- Note the historical trend since Sep-25. The narrative is: TGG has held #1 every single month.
- If AO overtakes TGG on citations, that is a red flag to escalate — it happened in Nov-25 and was recovered.

**AI Citations vs AI Visibility**
- These are different metrics. Visibility = mentions. Citations = source links. Report both, explain the difference if stakeholders might confuse them.
- TGG can rank #1 on Visibility but #2 on Citations (which happened in Mar-26 per the MD report). Explain that distinction in the report.

**LLM Sessions**
- Report absolute number and MoM%. Flag if MoM growth is slowing — this matters for the narrative about AI traffic translating to real sessions.
- Source must be GA4. Confirm this matches prior months.

**Organic Shopping**
- GMC clicks as absolute number per month, trending over ~8 months.
- Shopping keyword footprint growth since Jul-25 (migration baseline).
- If clicks are flat but footprint is growing, the story is "more impressions, feed quality is the unlock".

**Revenue**
- If Organic Revenue YoY is positive while Sessions YoY is negative, lead with this — it's the "doing more with less" story.
- Always include Conversion Rate YoY alongside Revenue YoY.

---

## Step 4 — Focus & Outcomes table

This table lives in every report. Rules:

- Status uses: ⚪ Scoping/Not Started, 🟡 In-progress, 🟢 Completed
- Every row needs a "Latest Result" that has actually changed from last month. If Simon hasn't provided an update, flag the row and ask.
- Items that move from 🟡 to 🟢 should be highlighted in the narrative (signal of momentum).
- New items (scoped but not yet started) should appear as ⚪ with a brief description of what's being planned.
- Workstreams currently active (as of Mar-26): AI tracking foundation, SERP Changes CTR, Blog AI summaries, AI-ready PLP intro copy, PLP Query Fanouts, Blog Briefs, PDP FAQs V2, PDP AI rendering audit, Video schema, AI Commerce Content (PDP), AI-optimised product descriptions, Product feed optimisation, Technical Infrastructure Roadmap.

---

## Step 5 — Stakeholder email

The email accompanies the report link. It is not a copy of the slides. It is a human-written summary that:

- Opens with what this month is about in 1-2 sentences (the "so what").
- Lists 3-5 key facts with bold labels, like the Feb-26 email structure.
- Closes with the strategic response — what the team is doing differently or doubling down on.
- Tone: confident, honest, no corporate fluff. Simon writes as the expert who is on top of it, not as someone reporting problems.

**Email structure template:**
```
Hi all,

Sharing the [Month] SEO Update. [1-sentence framing of the month's story.]

[Link to deck]

Here's a short overview:

[1-2 sentence setup — what the context is / what changed]

**[Key metric 1 label]:** [Fact + brief explanation]
**[Key metric 2 label]:** [Fact + brief explanation]
**[Key metric 3 label]:** [Fact + brief explanation]
[Add 1-2 more if the month warrants depth — Feb needed 5 because of the CTR story]

[Closing paragraph: what we're doing in response / what to watch next month]

Please let me know if there are any questions!
```

Do not over-explain. If a metric is stable and unremarkable, it doesn't need to appear in the email even if it's in the deck.

---

## Step 6 — QA checklist before delivery

Run these checks and report any failures. Fix before delivering.

- [ ] All MoM and YoY figures have been confirmed against source data (not estimated)
- [ ] AI Visibility table shows all months since Sep-25 (or flags if new data not yet available)
- [ ] No Focus & Outcomes row is a copy-paste from last month with zero update
- [ ] Competitor data (HN, AO, JB) is current — not last month's numbers relabelled
- [ ] Any external algo/SERP context is labelled as speculation
- [ ] The email matches the deck narrative — no contradictions between them
- [ ] Organic Sessions YoY is contextualised against last year's YoY for the same month
- [ ] The opening headline is specific and honest — not a generic month descriptor
- [ ] Revenue and conversion rate YoY are included if sessions YoY is negative (the "doing more with less" framing needs both)
- [ ] LLM sessions source confirmed as GA4

---

## Known report patterns / history to carry forward

| Month | Headline narrative | Key unusual factor |
|---|---|---|
| Jan-26 | Migration recovery confirmed, AI growing fast | First clean month post-migration |
| Feb-26 | Algorithm volatility hit rankings, CTR compression confirmed | Deep CTR analysis added (54-67% decline pos 1-3); more slides than usual |
| Mar-26 | Recovery from Feb, but structural non-brand decline ongoing | AIO keywords +22.6%, LLM +2.4%, AI citations dipped -8% MoM industry-wide |

Feb was deliberately deeper than usual due to the CTR compression story needing stakeholder buy-in. That level of depth is not the default for every month.

---

## Tone and style rules

- Australian English throughout.
- Prose over bullets for narrative sections. Tables for data.
- No em dashes. Use a full stop or comma.
- Specific numbers, not vague qualifiers. "2.26M sessions" not "over 2 million".
- Lead with the finding, follow with the implication. Never bury the lede.
- Avoid: "it's worth noting", "it's important to highlight", "as you can see", "it's clear that".
- If results are mixed, say so plainly. Do not spin negatives into positives — explain why they happened and what the response is.
- The tone is: expert, calm, on top of it, honest. Not defensive, not over-excited.

---

## Data sources reference

| Metric | Source |
|---|---|
| Organic Sessions / Revenue / Conversion | GA4 — TGG Channel Group Organic Search |
| Keywords in Top 3/10/100 (non-brand) | Semrush Organic Rankings |
| Total / Owned AIO Keywords | Semrush |
| AI Visibility Score | Profound |
| AI Citation Rate | Profound |
| LLM-referred Sessions | GA4 (Semrush secondary) |
| Shopping keyword footprint | Semrush |
| GMC / Shopping clicks | Google Merchant Centre |
| SERP Volatility | Semrush Sensor / MozCast |
| Competitor share of voice / avg rank | Semrush |
