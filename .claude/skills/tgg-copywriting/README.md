# TGG Copywriting Skill

## What This Is

A modular copywriting skill for producing on-site content for The Good Guys (thegoodguys.com.au), Australia's major electronics and appliances retailer. It packages the SEO content processes (00, 01, 02, 03, 05, 08) into a structured system with a routing layer, per-content-type rules, batch variation enforcement, and self-QA.

## Why It Exists

Before this skill, the copywriting rules lived across 10 separate process files that had to be manually loaded in the right order. The skill consolidates everything into a single entry point that:

- Automatically identifies what content type is being requested
- Loads the correct rules (and always loads TOV first)
- Enforces constraints that are easy to forget mid-batch (char limits, banned words, cross-piece variation)
- Runs a QA checklist before presenting output
- Handles batch mode with variation tracking across 20+ items

## Directory Structure

```
skills/tgg-copywriting/
├── SKILL.md                          ← Entry point. Read this first for every copywriting task.
├── README.md                         ← This file. Operational context for Claude Code.
└── references/
    ├── 00-tov.md                     ← Tone of voice, hard bans, overuse warnings, Australian English.
    │                                    ALWAYS loaded as base layer before any writing.
    ├── 01-plp-intros.md              ← 2-sentence PLP intros. 230–260 chars. Page type rules.
    ├── 02-metadata.md                ← Meta titles (≤60 chars) and descriptions (140–155 chars).
    ├── 03-inlink-migration.md        ← HTML rewrites: Slate/CSS formatting, link preservation.
    ├── 05-faq-category-copy.md       ← FAQ generation, brand+category FAQ, extended PLP intros.
    └── 08-eav-descriptions.md        ← Entity-attribute-value mapping (research, not writing).
```

## How to Use It

### For any copywriting task:

1. Read `SKILL.md` — it contains the 6-step workflow and the routing table
2. SKILL.md will tell you which reference file(s) to load
3. Always load `references/00-tov.md` first (hard bans apply to everything)
4. Then load the content-type-specific reference
5. Follow the workflow: identify → load → classify page → write → batch-check → self-QA

### Common task mappings:

| Simon says... | Content type | Files to load |
|--------------|-------------|---------------|
| "Write PLP intros for these URLs" | PLP Intro | 00-tov + 01-plp-intros |
| "Generate metadata for these pages" | Metadata | 00-tov + 02-metadata |
| "Rewrite this HTML for bottom of page" | Inlink Migration | 00-tov + 03-inlink-migration |
| "Write FAQ copy for this category" | FAQ/Category Copy | 00-tov + 05-faq-category-copy |
| "Do an EAV map for vacuums" | EAV Mapping | 08-eav-descriptions |
| "Write intros and metadata for these 20 URLs" | Multi-type batch | 00-tov + 01-plp-intros + 02-metadata |
| "Full category page build for /samsung/tvs" | Workflow D | 08 → 01 → 05 → 02 (in sequence) |

### Batch mode:

Batches of 3+ items trigger additional rules:
- Cross-batch variation check (openers, TGG placement, benefit angles, vocabulary)
- Output as tables for PLP intros, CSV for metadata
- Sub-batching at 15–20 items with variation checks per sub-batch and across the full set

## Relationship to Other Repo Files

| Repo location | Relationship |
|--------------|-------------|
| `00-tov-language-reference.md` (repo root) | **Source document.** The skill's `references/00-tov.md` is derived from this. If the root file changes, update the skill reference to match. |
| `01-plp-intro-copy.md` through `08-eav-mapping.md` (repo root) | **Source documents.** Same relationship — root files are the audit trail, skill references are the execution copies. |
| `PROMPT_AUDIT.md` | **Design decisions log.** Documents the contradictions that were resolved when building the processes. Consult if a rule seems contradictory. |
| `CLAUDE.md` / `claude.md` | **Workflow config.** References this skill directory and tells Claude Code to use it for copywriting tasks. |
| `processes/` (if it exists) | **Legacy location.** Some sessions may have copied process files here. The skill references are canonical. |

## Updating the Skill

### When Simon changes a rule:
1. Identify which reference file is affected
2. Make the edit in the reference file under `skills/tgg-copywriting/references/`
3. Update the version/date comment at the top of the file
4. If it's a cross-cutting change (affects multiple content types), check whether SKILL.md's routing or workflow needs adjustment
5. If the root process file (e.g. `01-plp-intro-copy.md`) also exists, update it for consistency — but the skill reference is what gets used at execution time

### When Simon adds a new content type:
1. Create a new reference file in `references/` following the naming pattern
2. Add a row to the routing table in SKILL.md (Step 1)
3. Add it to the Reference File Index table in SKILL.md
4. Add a row to the "Common task mappings" table in this README

### Contradiction handling:
If Simon's request conflicts with an existing rule in a reference file, flag it and ask whether it's a one-time exception or a permanent change before editing the file. This is documented in `CLAUDE.md` and applies here too.

## What This Skill Does NOT Do

- **Content analysis** (query fanout, entity extraction) — process 04, separate task
- **Internal linking strategy** (hierarchy validation, status checking) — process 06, separate task
- **AEO auditing** (improvement suggestions) — process 07, separate task
- **AI visibility polling** (poll question generation) — process 09, separate task

These are research/analysis processes. The copywriting skill consumes their outputs but doesn't run them. If Simon asks for one of these, handle it outside the skill.

## Key Constraints to Remember

These are the rules that trip up most often:

- **PLP intros are 230–260 characters, not words.** Process 05C (extended PLP intro) is 230–260 words. Don't confuse them.
- **"The Good Guys" appears exactly once per piece.** Not zero, not twice.
- **Brand PLPs (Type B and C) ban: trusted, reliable, enjoy, features.** These are fine on category PLPs.
- **"across the range" is a legal risk.** Use "across a range" unless the offer genuinely covers everything.
- **"sale", "save", "discount" are hard-banned everywhere.** Use "deal", "pay less", "offer".
- **S2 must be shorter than S1** in PLP intros. Long S2 breaks mobile viewport.
- **No "The Good Guys" in meta titles.** Only in descriptions.
- **Australian English always.** optimise, colour, centre, favourite.
