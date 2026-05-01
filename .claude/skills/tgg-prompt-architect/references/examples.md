# tgg-prompt-architect: Examples

Trigger and non-trigger pairs, plus before/after rewrites for the major TGG task types. Read this when you need a concrete reference for what restructuring looks like in practice.

---

## Hard-skip examples (return user message unchanged)

| User prompt | Why skip |
|---|---|
| `thanks` | Acknowledgement |
| `yes do option 2` | Continuation |
| `continue` | Steering |
| `https://www.thegoodguys.com.au/lg-televisions` | URL only |
| `* draft a meta description` | Bypass prefix |
| `Error: ENOENT: no such file or directory` | Error message |
| `// raw mode on` | Bypass-equivalent |
| Any prompt under 12 tokens following Claude's previous response | Likely a clarification |

For all of these, return the user's message unchanged. Do not announce the skip.

---

## Soft-skip (minimum-edit mode)

Original: `meta description for the lg fridge plp, 155 chars max`

Minimum edit: `Write one meta description for the LG fridge PLP. Hard limit: 155 characters. Lift the LG fridge PLP context from tgg-copywriting.`

No full contract template, no invented role, no length inflation.

---

## Full restructure examples

### SEO copywriting

**Before:**
> can you do plp intros for the new samsung phone pages we just got, the s26 ones

**After:**
> Using `tgg-copywriting`, write PLP intros for the new Samsung Galaxy S26 pages.
>
> Constraints (hard limits):
> - 220-250 characters per intro, 225-235 ideal.
> - Sentence 1 opens with an action verb. Banned openers: Discover, Explore, Shop.
> - "The Good Guys" appears in Sentence 2 only.
> - Brand PLP banned terms: trusted, reliable, enjoy, features.
> - Australian English.
> - No padding.
>
> Output: one intro per page, plain text, page slug as a heading above each.
> Verify each intro hits the character range and the banned-word list before delivering.

### Metadata

**Before:**
> need title tags for the lg 2026 tv launch pages

**After:**
> Using `tgg-copywriting` and `tgg-seo-specialist`, write title tags for the LG 2026 TV launch pages.
>
> Constraints (hard limits):
> - 60 character hard ceiling, including spaces.
> - Brand name "The Good Guys" excluded (the site appends it automatically).
> - No prices.
> - No discount percentages.
> - Australian English.
>
> Output: one title per page, page URL above each. Confirm each title is at or below 60 characters before delivering.

### Monthly SEO update

**Before:**
> start drafting this month's seo update, march data is in drive

**After:**
> Using `tgg-monthly-seo-report` and `tgg-marketing-analyst`, start drafting the March 2026 SEO update.
>
> Source data: Google Drive, March 2026 folder.
>
> Constraints:
> - Follow Simon's monthly report structure (deck narrative + stakeholder email + focus & outcomes table).
> - Use exact numbers from source data, no rounding without flagging.
> - Australian English.
> - Flag any missing data sources before drafting.
>
> Disclosure: Reading this as a March 2026 report draft. Tell me if you meant a different month.

### Data analysis / scripting

**Before:**
> write a script to compare our gsc clicks vs jb hifi semrush traffic for the last 90 days

**After:**
> Using `tgg-marketing-analyst`, write a Python script that compares The Good Guys' GSC clicks against JB Hi-Fi's Semrush organic traffic for the last 90 days.
>
> Inputs (assumed, flag if wrong):
> - GSC export (CSV) for thegoodguys.com.au.
> - Semrush AU database export for jbhifi.com.au, organic traffic by day.
>
> Output:
> - Single Python file.
> - Joined daily DataFrame with both metrics.
> - Side-by-side line chart saved as PNG.
> - Print top 5 days where TGG outperformed and top 5 where JB Hi-Fi outperformed.
>
> Constraints: AU English in any printed output. No hardcoded paths, accept paths as CLI args.
>
> Disclosure: Reading this as a script deliverable, not a one-off analysis. Tell me if you wanted the analysis run inline instead.

### Strategy / brief

**Before:**
> ideas for how we should respond to JB Hi-Fi launching their new comparison tool

**After:**
> Using `tgg-content-strategist`, draft a strategic response brief for JB Hi-Fi's new comparison tool launch.
>
> Constraints:
> - Australian English.
> - 3-5 concrete options, each with effort, impact, and dependencies.
> - No filler. No exec summary unless I ask.
> - Treat this as an internal brief for SEO leadership, not a deck.
>
> Output: structured brief, headings per option.
>
> If you need source material on JB Hi-Fi's tool, ask before assuming what it does.

### Batch processing

**Before:**
> rewrite these 47 product titles to add the colour in brackets

**After:**
> Using `tgg-copywriting` and `verification-gate-protocol`, rewrite the 47 product titles to add the standard colour term in brackets where the supplier colour is non-standard (e.g. "Midnight" → "Midnight (Black)").
>
> Constraints:
> - Process all 47. Do not stop at a checkpoint without flagging.
> - Use Simon's existing colour standardisation logic. Brand-name colours and material descriptions are excluded.
> - Preserve original capitalisation.
> - Hard limit: per-title length unchanged (no padding).
>
> Output: CSV with columns `original_title`, `rewritten_title`, `colour_added` (Y/N).
> After processing, validate that 100% of non-standard colours have a bracket addition before delivering.

### Deck building

**Before:**
> build a slide on aio visibility for the march deck

**After:**
> Using `tgg-pptx-style` and `tgg-chart-creator`, build one slide on AIO visibility for the March 2026 SEO update deck.
>
> Constraints:
> - Match the existing TGG SEO deck visual style (colours, fonts, layout tokens defined in `tgg-pptx-style`).
> - Headline metric: TGG AIO visibility share vs JB Hi-Fi and Harvey Norman.
> - Use March 2026 data from Profound (apply 3.2x normalisation factor for pre-Feb-26 historical comparison only if showing trend).
> - Australian English.
>
> Output: single .pptx slide, ready to inject into the master deck.
>
> If the data file is not in the working directory, ask for the path.

### Project management / process

**Before:**
> remind me what's still abandoned from february

**After:**
> Using `tgg-conversation-indexer`, list projects from February 2026 conversations that were flagged high-upside but never completed.
>
> Constraints:
> - Only February 2026.
> - Only projects flagged as significant or high-upside in the index.
> - Australian English.
>
> Output: short prose list, one line per project, with the original conversation reference.

### File work

**Before:**
> read the mhtml i just uploaded and tell me what's in it

**After:**
> Using `mhtml-reader`, read the MHTML file in `/mnt/user-data/uploads/` and identify whether it is an AI conversation transcript or a web page snapshot. Then ask Simon what he wants to do with it.
>
> No additional restructuring needed. Hand off directly.

---

## Disclosure examples

When to surface the one-line disclosure (Step 8):

| Situation | Disclosure? |
|---|---|
| User said "draft a meta description"; rewrite specifies "for the LG fridge PLP" because that's the active context | No (context is implied) |
| User said "do PLP intros"; rewrite assumes Samsung S26 because last conversation was about S26 | Yes ("Reading this as Samsung S26 PLP intros. Tell me if you meant a different range.") |
| User said "build a slide"; rewrite assumes the March deck | Yes ("Reading this as the March 2026 deck. Tell me if you meant a different month.") |
| User said "rewrite these titles"; rewrite adds output format = CSV | No (CSV is the obvious format for a batch deliverable) |
| User said "rewrite these titles"; rewrite adds output format = .docx | Yes (format inference is non-trivial) |

Default to silence unless the inference is non-trivial.

---

## Anti-patterns

These are rewrites the skill should never produce.

**Anti-pattern 1: Padding**

User: `meta description for lg fridge plp, 155 chars`

Bad rewrite: `You are a senior SEO copywriter at Australia's largest electronics retailer with deep expertise in the appliance category. Your task is to craft a compelling, click-worthy meta description for the LG fridge product listing page that drives qualified traffic from search results.`

Why bad: violates Simon's no-padding rule, inflates a 12-token ask into a 50+ token rewrite, and adds invented role detail.

**Anti-pattern 2: Invented constraints**

User: `write 3 faqs for the dishwasher deals page`

Bad rewrite: `Write 3 FAQs for the dishwasher deals page. Each must be 50-75 words, include a primary keyword, end with a CTA, and use H3 headings.`

Why bad: 50-75 words, primary keyword, CTA, and H3 are all invented constraints. The user did not ask for any of these. Defer to `tgg-copywriting` for the actual FAQ rules.

**Anti-pattern 3: Restating the brief**

Bad disclosure: `Just to confirm, you want me to write 3 FAQs for the dishwasher deals page. I will use the existing FAQ format and ensure each answer is well-structured. Let me know if this matches your intent before I proceed.`

Why bad: restates the brief, asks for confirmation Simon did not request, and adds an exec summary. Replace with silent execution.

**Anti-pattern 4: XML overuse**

User: `what's the gsc indexability count for blocked-by-robots`

Bad rewrite: `<role>SEO analyst</role><task>Look up GSC indexability count</task><context>The Good Guys</context><constraints>None</constraints>`

Why bad: single-section lookup wrapped in XML for no reason. Use plain prose, or hard-skip if it's a simple lookup.
