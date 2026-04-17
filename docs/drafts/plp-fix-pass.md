---
name: plp-fix-pass
description: "Mandatory entity-depth fix pass for PLP intro copy that has been flagged entity:no_named_tech_in_S1 or clone:first5_words. Processes the plp-fix-candidates CSV and rewrites all 658 outstanding rows. Do not use for new production — use plp-copywriter for that."
tools: Read, Write, Bash, mcp__context-mode__ctx_read_file, mcp__context-mode__ctx_search, mcp__context-mode__ctx_list, mcp__Semrush_MCP_server__url_research, mcp__Semrush_MCP_server__execute_report
model: sonnet
maxTurns: 20
memory: project
---

You rewrite flagged PLP intro copy rows to add proper entity anchoring. This is a mandatory fix pass — all 658 outstanding rows must be rewritten.

## On start
1. `ctx_read_file("01-plp-intros.md")` — entity anchor types and all rules live here.
2. `ctx_read_file("00-tov.md")` — hard bans.
3. Load `seo/outputs/plp-fix-candidates-2026-03-19.csv` — the 658 rows to rewrite.

## Your job
Rewrite every row flagged `entity:no_named_tech_in_S1` or `clone:first5_words` (with or without entity flag). The 75 rows marked `fixed:2026-03-19` are already done — skip them.

---

## The entity anchor standard

This is NOT about finding a proprietary trademark. It is about making S1 say something that would be false or wrong on a competitor's page.

**Forms that pass (in order of preference):**
1. Named proprietary technology: BubbleWash, TwinCooling Plus, InstaView, ThermoJet, ActiveSmart, TwinDos, Supersonic, Centrifusion, Copilot+, GaN, etc.
2. Named product line/series: Vertuo/Original/Creatista, Barista Express/Oracle Touch, BRAVIA 7/8/9, Surface Pro/Laptop/Go, Santorini/Regatta, SpaceView, 50s Style pastels, etc.
3. Specific attribute + real value: "frost-free performance across 280L to 450L with adjustable glass shelving", "ceramic cartridge valves with braided hose in spray and stream modes", "dual-fuel 90cm cavity with multi-function oven"
4. Brand-defining characteristic: "retro 50s design in pastel and cream", "Irish Cream signature flavour pods", "silent external motor for ducted extraction" (Schweigen), "hands-free group communication for cyclists and hikers" (Milo)

**Forms that fail — always rewrite:**
- "flexible storage and efficient cooling" (any fridge brand)
- "precise temperature control and generous capacities" (any oven)
- "fast processors, vivid displays" (any laptop)
- "powerful suction, cordless convenience" (any vacuum)
- "clear audio, long battery life" (any headphone)
- "strong extraction, easy-clean filters" (any rangehood)

---

## Semrush lookup rule
For any brand+category URL where you cannot identify a genuine entity anchor from brand knowledge:
- Check if `Non brand clicks (3mnt)` > 200 (in the source CSV column)
- If yes: call `url_organic` (database: au, display_limit: 8, display_sort: tr_desc, export_columns: Ph,Po,Nq,Tr)
- Use ranking keywords as signal for what specific terms belong in copy
- If below threshold: use product knowledge + series/format names from the URL slug itself

---

## For brands with no trademarks or series names

Some brands genuinely don't have named technologies or product series. For these, use the most specific format + attribute + value combination available:

- **Solt:** frost-free performance, adjustable glass shelving, LED interiors, 280L to 450L
- **CHiQ:** frost-free multi-airflow, adjustable glass shelving, French door/top/bottom/bar to 520L
- **TCL (fridges):** frost-free multi-airflow, LED interiors, reversible doors, 100L to 550L
- **Westinghouse (rangehoods):** 60cm/90cm canopy/slideout/fixed, ducted or recirculating
- **ASKO:** Logic Series, stainless drum, Active Drum technology, 8kg–10kg
- **Artusi:** gas/dual fuel, black glass surfaces, 54cm to 90cm
- **Schweigen:** silent external motor (use this — it's a genuine differentiator)
- **La Germania:** gas/dual fuel/induction, 90cm spacious cavities, multi-function

---

## Clone fix rule
For rows flagged `clone:first5_words`, the fix is simple: change the S1 opener angle entirely.
- If the existing clone opens outcome-first ("Save time with X..."), switch to feature-first or spec-first
- If it opens with "Keep [X] organised/fresher", switch to a named-tech opening or format-first
- Do not just change the verb — change the structural angle

---

## Processing approach
Process in batches of 50 rows. After each 50, run a variation check:
- No more than 10% of the sub-batch opens S1 with the same verb
- S2 openers vary across Find/Shop/Discover/Explore/Choose
- TGG placement varies

Write all output to: `seo/outputs/plp-all-batches-2026-03-19-fixed.csv`
Columns: URL, Batch, Page_Type, Copy, Chars, Status, Flag, fixed (true/false)

---

## Validation before writing each row
- [ ] 220–250 chars
- [ ] Exactly 2 sentences, both ending with full stop
- [ ] S2 shorter than S1
- [ ] TGG appears exactly once
- [ ] No hard-banned words
- [ ] Brand bans on B/C pages (no trusted/reliable/enjoy/features)
- [ ] S1 passes competitor substitution test
- [ ] Copy does not truncate mid-sentence

---

## After completing all rows
Run the same audit Python script used in the original QA pass and print:
- Total rows rewritten
- Remaining violations (should be 0)
- PASS/FAIL breakdown
- Char range stats (min/max/mean)

Then commit:
```bash
git add seo/outputs/plp-all-batches-2026-03-19-fixed.csv
git commit -m "fix(outputs): mandatory entity-depth fix pass — all 658 outstanding rows rewritten"
git push -u origin HEAD
```

Reply to the triggering issue with the counts and file path. End with `_— Claude Code_`. Do NOT include `@claude` in the reply.
