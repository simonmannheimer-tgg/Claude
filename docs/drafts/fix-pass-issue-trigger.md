# GitHub Issue: Mandatory PLP Entity Fix Pass

**Status:** Ready to post once pre-flight steps are complete
**Trigger:** Post to simonmannheimer-tgg/Claude Issues with body below

---

## Pre-flight checklist (complete before posting)

- [ ] `plp-copywriter.md` in repo replaced with v2 (from patches)
- [ ] `plp-fix-pass.md` agent added to repo
- [ ] `01-plp-intros.md` confirmed as v2.1 (entity anchor standard updated)
- [ ] `00-tov.md` exists and is the canonical TOV file (or `00-tov-language-reference.md` still works — check which agents expect)
- [ ] `seo/outputs/plp-fix-candidates-2026-03-19.csv` is committed to repo (658 rows)
- [ ] Storage rule note confirmed in CLAUDE.md

---

## Issue body (copy-paste exactly)

```
@claude Use the plp-fix-pass agent to rewrite all 658 outstanding rows in the entity-depth fix backlog.

Source file: seo/outputs/plp-fix-candidates-2026-03-19.csv
Scope: All rows where fixed != "fixed:2026-03-19" (i.e. the 658 unfixed rows)

The entity flag `entity:no_named_tech_in_S1` is MANDATORY — every flagged row must be rewritten. Do not treat it as advisory.

Entity anchor standard (from 01-plp-intros.md):
The requirement is not a proprietary trademark. It is: S1 must say something specific enough that it would be false or wrong on a competitor's page. Valid forms:
1. Named proprietary tech (TwinCooling Plus, BubbleWash, InstaView, ThermoJet, ActiveSmart, etc.)
2. Named product line/series (Vertuo/Creatista/Original for Nespresso, Barista Express for Breville, SpaceView for eufy, BRAVIA 7/8/9 for Sony, 50s Style pastels for Smeg, Surface Pro/Laptop/Go for Microsoft)
3. Specific attribute + real value (frost-free performance across 280L to 450L, ceramic cartridge valves with braided hose in spray and stream modes, dual-fuel 90cm cavity with multi-function oven)
4. Brand-defining characteristic (retro 50s design in pastel and cream, Irish Cream flavour pods, silent external motor for ducted extraction)

What always fails (rewrite these — they describe the category not the brand):
- "flexible storage, [X] options" 
- "precise temperature control and generous capacities"
- "powerful purification, smart sensors"
- "stable connections and fast data transfer"

Semrush rule: Only call url_organic (database: au, display_limit: 8, display_sort: tr_desc, export_columns: Ph,Po,Nq,Tr) if Non brand clicks (3mnt) > 200 in the source file. Below threshold: use brand knowledge only.

Copy rules:
- 220–250 chars. Floor 220, ceiling 250 hard stop.
- Exactly 2 sentences. Both must end with full stop.
- S2 shorter than S1.
- TGG appears exactly once per row.
- Hard bans: sale, discount, save-as-price-framing, amazing, stunning, wonderful, busy homes, sleek design, Australia's trusted choice, quality brands, get great value, perfect for all needs
- Brand page extra bans (B2/B3/B1): trusted, reliable, enjoy, features

Output: seo/outputs/plp-all-batches-2026-03-19-fixed.csv
Columns: URL, Batch, Page_Type, Copy, Chars, Status, Flag, fixed
Storage: GitHub only — write to seo/outputs/ and commit. Do NOT use Airtable.

After completing all rows:
- Run QA audit and print: total rewritten, remaining violations, PASS/FAIL counts
- git add seo/outputs/plp-all-batches-2026-03-19-fixed.csv
- git commit -m "fix(outputs): mandatory entity-depth fix pass — all 658 outstanding rows rewritten"
- git push -u origin HEAD

Reply with: rows rewritten, PASS/FAIL counts, file path. End with _— Claude Code_. Do not include @claude anywhere in reply.
```

---

## What to expect back

Claude Code should reply within 5–10 minutes with:
- Count of rows rewritten (target: 658)
- PASS/FAIL breakdown (target: 0 FAIL)
- File path: `seo/outputs/plp-all-batches-2026-03-19-fixed.csv`
- Any systematic issues flagged (brands where no entity anchor could be identified)

If it processes only a subset again, check the prompt — the key phrase is "MANDATORY — every flagged row must be rewritten. Do not treat it as advisory."

---

## After the fix pass is confirmed

1. Download `seo/outputs/plp-all-batches-2026-03-19-fixed.csv` from GitHub
2. Merge with Batch 1 output (`plp-batch1-priority30-2026-03-19.md`) — convert Batch 1 to CSV format first
3. QA final combined file (spot check 50 random rows across brands)
4. Upload to Contentful
5. Mark PLP Batch Production entry in CLAUDE.md as Complete
