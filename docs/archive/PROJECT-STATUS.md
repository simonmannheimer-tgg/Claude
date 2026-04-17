# PLP Intro Copy — Project Status
**Last updated:** 27 March 2026
**Owner:** Simon Mannheimer, SEO Strategist, The Good Guys
**Project:** Brand+Category PLP intro copy migration — all brand+category PLPs on thegoodguys.com.au

---

## What This Project Is

Every brand+category Product Listing Page on thegoodguys.com.au needs a 2-sentence intro paragraph. These appear above the product grid, serve as the semantic anchor for search crawlers, and act as the entity source for AI systems (ChatGPT, Perplexity, Google AI Overviews). Without specific, named-entity copy in this position, the pages compete only on URL structure — not on content signals.

The source file (`TGG_-_SEO_WIP___SM_-_PLP_Intro__Brand_Cat_.csv`) tracks 1,335 URLs across 4 batches. This project writes, QAs, and uploads copy for all Not Started rows to Contentful.

---

## Overall Progress

| Batch | URLs | Status | File |
|-------|------|--------|------|
| Batch 1 (priority) | 30 | ✅ Complete | `seo/outputs/plp-batch1-priority30-2026-03-19.md` |
| Batch 2 | 281 | ⚠️ Written, fix pass outstanding | `seo/outputs/plp-all-batches-2026-03-19.csv` |
| Batch 3 | 281 | ⚠️ Written, fix pass outstanding | Same file |
| Batch 4 | 281 | ⚠️ Written, fix pass outstanding | Same file |
| **Total** | **843** | **658 rows need entity fix** | |

---

## Current Blocker: Entity-Depth Fix Pass

### What happened
The Claude Code agent completed all 843 rows but the QA audit flagged 733 rows with issues. 75 hard-violation rows (wrong char count, missing TGG, banned words, structural clones) were fixed. The remaining 658 rows are flagged for entity depth — S1 does not contain anything specific enough to distinguish the brand from a generic category description.

### Root cause
The entity standard given to the agent was too narrow: it only looked for proprietary brand technology names (trademarks like BubbleWash, TwinCooling Plus). Brands like Solt, CHiQ, Belkin, Uniden, Westinghouse, Baileys, and others have no proprietary trademarks — the agent treated them as unfixable and left them. But these brands still have valid entity anchors in the form of named product lines, specific format+attribute+value combinations, or brand-defining characteristics.

### Corrected entity standard (v2.1)
Four forms of entity anchoring, in order of preference:
1. **Named proprietary technology** — use where genuine (TwinCooling Plus, BubbleWash, ThermoJet, etc.)
2. **Named product line or series** — model families that anchor the copy to a specific brand reality (Vertuo/Creatista for Nespresso, BRAVIA 7/8/9 for Sony, Surface Pro/Laptop/Go for Microsoft, 50s Style pastels for Smeg)
3. **Specific product attribute + real value** — format + spec + finish for brands without trademarks (frost-free performance across 280L to 450L, ceramic cartridge valves with spray and stream modes)
4. **Brand-defining characteristic** — something real and verifiable about the brand (retro 50s design in pastel colours, Irish Cream signature flavour pods, silent external motor for ducted extraction)

**Competitor substitution test:** If S1 could be copy-pasted onto a competitor's page with minimal word changes and still make sense — it fails. Rewrite it.

### What the 658 outstanding rows look like
Most are not terrible copy — they're just not brand-specific enough. Examples:
- `/belkin/computers-tablets-and-gaming` — "stable connections and fast data transfer" (could be any accessories brand)
- `/solt/fridges-and-freezers` — "flexible storage, compact bar options" (could be any fridge brand)
- `/philips/heating-and-cooling/air-treatment` — "powerful purification, smart sensors and quiet operation" (could be any air purifier brand)

These need S1 rewritten to include a genuine entity anchor for that brand in that category.

### Fix pass status
- **Outstanding:** 658 rows in `seo/outputs/plp-fix-candidates-2026-03-19.csv`
- **Agent ready:** `plp-fix-pass.md` (needs to be committed to repo)
- **Issue trigger:** `plp-docs/fix-pass-issue-trigger.md` (ready to post once agent is committed)

---

## Copy Rules Reference (v2.1)

### Character count
- Range: 220–250 (floor 220, ceiling 250 hard stop)
- Target: 225–235
- Count every letter, space, and punctuation mark

### Structure
- Exactly 2 sentences
- Both sentences must end with a full stop
- S2 must be shorter than S1
- "The Good Guys" exactly once per piece

### Entity anchor in S1 (mandatory)
See corrected standard above. Every S1 must contain at least one of the four entity anchor types.

### S1 openers — vary across batch
- Angles: outcome-first, feature-first, format-first, spec-first, problem-first
- Never open S1 with: Discover, Explore, Shop
- No opener should exceed 20% of a sub-batch

### S2 openers — vary across batch
- Valid: Find, Shop, Discover, Explore, Choose
- Never 3+ consecutive rows with same S2 opener

### Brand page extra rules (Types B, C)
Additional banned words on brand+category pages: **trusted**, **reliable**, **enjoy**, **features**
Reason: these words make every brand page feel identical. "Enjoy Samsung's trusted features" says nothing about Samsung.

### Hard bans (all pages)
sale/sales, discount, save-as-price-framing (save money / save on / save with Price Beat), exclusive (re deals), amazing, stunning, wonderful, busy homes, hearty meals, sleek design, Australia's trusted choice, quality brands, get great value, perfect for all needs

Note: "save time", "save water", "save energy" as functional outcomes are NOT banned.

---

## File Index

| File | Purpose | Status |
|------|---------|--------|
| `TGG_-_SEO_WIP___SM_-_PLP_Intro__Brand_Cat_.csv` | Source file — 1,335 URLs, local only | Do not commit |
| `seo/outputs/plp-batch1-priority30-2026-03-19.md` | Batch 1 complete | ✅ Done |
| `seo/outputs/plp-all-batches-2026-03-19.csv` | Batches 2–4 raw output (843 rows) | ⚠️ Pre-fix |
| `seo/outputs/plp-fix-candidates-2026-03-19.csv` | 658 rows outstanding | ⚠️ Needs fix pass |
| `seo/outputs/plp-all-batches-2026-03-19-fixed.csv` | Fix pass output | ⏳ Not yet created |
| `01-plp-intros.md` | Process file v2.1 — canonical rules | ✅ Current |
| `01-plp-intro-copy.md` | Duplicate — needs sync or deletion | ⚠️ Stale |
| `PLP-Batch-Production-Brief-2026-03-19.md` | Original batch brief | Historical |
| `.claude/agents/plp-copywriter.md` | Writing agent v2 | ⚠️ Needs repo update |
| `.claude/agents/plp-fix-pass.md` | Fix pass agent | ⚠️ Not yet in repo |
| `seo/scripts/plp-qa-audit.py` | QA audit script | ✅ Created |

---

## Process Chain (how it works)

```
Source CSV (local)
    │
    ├── eav-researcher → brand+category entity map (per URL)
    │
    ├── seo-keyword-researcher → url_organic from Semrush (if Non brand clicks > 200)
    │
    ├── plp-copywriter → 2-sentence copy using EAV + keyword signal
    │
    ├── plp-qa-audit.py → automated validation
    │       ├── PASS → write to output CSV
    │       └── FAIL → flag to plp-fix-candidates.csv
    │
    └── plp-fix-pass → rewrite flagged rows with correct entity standard
            │
            └── plp-qa-audit.py → re-validate → final output CSV
                    │
                    └── Upload to Contentful
```

---

## Agent Roster for This Project

| Agent | Role | State |
|-------|------|-------|
| `seo-team-lead` | Orchestrator — routes tasks to agents | Current |
| `eav-researcher` | Maps brand+category entity landscape | Current |
| `seo-keyword-researcher` | Pulls Semrush `url_organic` data | Current |
| `plp-copywriter` | Writes the copy | Needs v2 update in repo |
| `plp-fix-pass` | Rewrites entity-flagged rows | Not yet in repo |

---

## Next Steps (in order)

1. **Commit repo patches** (pre-flight for fix pass):
   - `plp-copywriter.md` v2 replacement
   - `plp-fix-pass.md` new agent
   - `01-plp-intros.md` v2.1 confirmed
   - Storage rule added to CLAUDE.md

2. **Post GitHub issue** using trigger in `plp-docs/fix-pass-issue-trigger.md`

3. **Validate fix pass output** with `seo/scripts/plp-qa-audit.py`

4. **Merge all batches** into single upload-ready CSV:
   - Batch 1 (30 rows, from `.md` file — convert to CSV)
   - Batches 2–4 fixed (658 rows)
   - Batches 2–4 already-clean (185 rows — no fix needed)

5. **Upload to Contentful**

6. **Mark complete** in CLAUDE.md

---

## Known Issues and Decisions

### Why 658 rows and not 733?
The QA audit flagged 733 rows total. 75 were hard violations (wrong char count, missing TGG, banned words, structural clones) — those were fixed in the first pass. The remaining 658 are the entity-depth flags. The 75 fixed rows are included in the final output.

### Why not re-run the whole batch?
The 185 rows that passed QA are good copy — no reason to regenerate them. Only the flagged rows need work.

### Why was the entity standard wrong?
The original brief used "named technology in S1" as the entity anchor requirement. This was correct for Samsung, LG, Bosch, Miele, Dyson, Breville, and other major brands with proprietary tech names. It was wrong for smaller or commodity brands (Solt, CHiQ, Belkin, etc.) that have no trademarks. The standard has been corrected in v2.1 to cover all four anchor types.

### Contentful upload format
UTF-8, no BOM, no smart quotes, no encoding artefacts. The CSV columns must match what Contentful expects — verify column names before final upload.

### Airtable
Do not use Airtable for any outputs. All files go to `seo/outputs/` in the GitHub repo.
