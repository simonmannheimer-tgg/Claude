# CLAUDE.md Additions — Copywriting Skill Integration

> **Instructions:** Merge the sections below into your existing `CLAUDE.md` and `claude.md` files.
> The Copywriting Skill section should go under or replace the existing "SEO Process Management" section.
> The settings.json snippet goes into `.claude/settings.json`.

---

## Copywriting Skill (replaces manual process file loading)

A copywriting skill lives at `skills/tgg-copywriting/`. It replaces the workflow of manually reading individual process files for content-writing tasks.

### When to use it

**Any time Simon asks you to write, edit, rewrite, QA, or batch-produce on-site copy.** This includes PLP intros, metadata, FAQ copy, brand+category copy, inlink migration, EAV mapping, extended category intros, or any combination.

Trigger phrases: "write intros for", "batch intros", "metadata for these", "rewrite this HTML", "FAQ for this category", "EAV map for", "full category page build", or any request involving copy production for thegoodguys.com.au URLs.

### How to use it

1. **Read `skills/tgg-copywriting/SKILL.md`** — this is the entry point for every copywriting task. It contains the routing table and the 6-step workflow.
2. **SKILL.md tells you which reference files to load.** Always load `references/00-tov.md` first (hard bans, overuse warnings, Australian English), then the content-type-specific file.
3. **Follow the workflow in SKILL.md.** Identify content type → load references → classify pages → write → batch-check → self-QA.
4. **For batch jobs (3+ items):** the skill has cross-batch variation rules. Check them after writing the full set.
5. **For multi-type requests** (e.g. "write intros AND metadata for these URLs"): load both reference files and produce both outputs.

### Do NOT fall back to the root process files

The numbered files in the repo root (`00-tov-language-reference.md`, `01-plp-intro-copy.md`, etc.) are documentation/audit trail. The canonical execution copies live in `skills/tgg-copywriting/references/`. Use the skill references.

### Updating the skill

When Simon changes a rule or preference that affects copywriting:
1. Update the relevant file in `skills/tgg-copywriting/references/`
2. Bump the version/date at the top of the changed file
3. Also update the corresponding root process file for consistency (but skill reference is canonical)
4. Standard contradiction handling applies: if a request conflicts with an existing rule, flag it and ask one-time exception vs permanent change before editing

### Full details

Read `skills/tgg-copywriting/README.md` for the complete operational guide: directory structure, task mappings, batch mode, relationship to other repo files, and common gotchas.

---

## Process Files (Reference / Audit Trail)

The original process files remain in the repo root as documentation:

| # | Process | File | Canonical skill reference |
|---|---------|------|--------------------------|
| 00 | TOV & Language Reference | `00-tov-language-reference.md` | `skills/tgg-copywriting/references/00-tov.md` |
| 01 | PLP Intro Copy | `01-plp-intro-copy.md` | `skills/tgg-copywriting/references/01-plp-intros.md` |
| 02 | Metadata Generation | `02-metadata-generation.md` | `skills/tgg-copywriting/references/02-metadata.md` |
| 03 | Inlink Migration | `03-inlink-migration.md` | `skills/tgg-copywriting/references/03-inlink-migration.md` |
| 04 | Content Analysis | `04-content-analysis.md` | — (not a copywriting task) |
| 05 | FAQ & Category Copy | `05-faq-category-copy.md` | `skills/tgg-copywriting/references/05-faq-category-copy.md` |
| 06 | Internal Linking | `06-internal-linking.md` | — (not a copywriting task) |
| 07 | AEO Optimisation | `07-aeo-optimisation.md` | — (not a copywriting task) |
| 08 | EAV Mapping | `08-eav-mapping.md` | `skills/tgg-copywriting/references/08-eav-descriptions.md` |
| 09 | AI Visibility Polling | `09-ai-visibility-polling.md` | — (not a copywriting task) |

Processes 04, 06, 07, and 09 are analysis/strategy tasks. They are not part of the copywriting skill. Handle them directly from the root process files as before.

### Standard Workflows (unchanged)

**Workflow A — Category Page Optimisation:**
`08 (EAV)` → `04 (Core Query + Fanout)` → `06 (Link Validation)` → `05 (Brand+Category FAQ)`

**Workflow B — Article AEO Audit:**
`04 (Summarise + Keyword)` → `06 (Link Opportunities)` → `07 (AEO Suggestions + Finalise)`

**Workflow C — Internal Linking:**
`06 (Find → Validate → Verify → Insert)`

**Workflow D — Full Category Page Build:**
`08 (EAV)` → `04 (Fanout)` → `01 (PLP Intro)` → `05 (FAQ Copy)` → `02 (Metadata)` → `06 (Linking)`

For Workflows A and D, the copywriting steps (01, 02, 05, 08) use the skill. The analysis steps (04, 06) use root process files directly.

---

## .claude/settings.json

Add the skill registration:

```json
{
  "skills": {
    "tgg-copywriting": {
      "path": "skills/tgg-copywriting"
    }
  }
}
```

This goes alongside the existing `mcpServers` block. The full file would look like:

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "mcpServers": {
    "context-mode": { ... },
    "gtmetrix": { ... }
  },
  "skills": {
    "tgg-copywriting": {
      "path": "skills/tgg-copywriting"
    }
  }
}
```
