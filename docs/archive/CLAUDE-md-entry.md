## PLP Intro Copy — Brand+Category Batch Production

**Status:** Active — fix pass outstanding
**Last updated:** 27 March 2026

### Context
Writing 2-sentence intro copy for all brand+category PLP pages on thegoodguys.com.au. Source file has 1,335 URLs across 4 batches. Batch 1 (30 priority URLs) is complete and shipped. Batches 2–4 (843 URLs) have been written but require a mandatory entity-depth fix pass before upload to Contentful.

### Current state
- **Batch 1 (30 URLs):** Complete. File: `seo/outputs/plp-batch1-priority30-2026-03-19.md`
- **Batches 2–4 (843 URLs):** Written. File: `seo/outputs/plp-all-batches-2026-03-19.csv`
- **QA audit run:** Identified 733 rows with issues. 75 hard-violation rows fixed. 658 rows outstanding.
- **Outstanding backlog:** `seo/outputs/plp-fix-candidates-2026-03-19.csv` — 658 rows flagged `entity:no_named_tech_in_S1` or `clone:first5_words`
- **Root cause of backlog:** Entity standard was originally too narrow (proprietary trademark only). Corrected standard added — entity anchor can be named tech, series name, specific attribute+value, or brand-defining characteristic. See `01-plp-intros.md` v2.1 for full standard.

### Active rules / constraints
- Char range: 220–250, lower end preferred (225–235 ideal), floor 220, ceiling 250 hard stop
- Entity anchor required in S1: must pass competitor substitution test (could this S1 work for a competitor? if yes, rewrite)
- Brand pages (B/C): additionally ban trusted / reliable / enjoy / features
- Semrush pull conditional: only if Non brand clicks (3mnt) > 200
- Storage: GitHub only (`seo/outputs/`). Do NOT use Airtable.
- Output destination: Contentful (upload-ready CSV, UTF-8, no BOM, no smart quotes)

### Next actions
- [ ] **PRIORITY:** Run `plp-fix-pass` agent on 658-row backlog → `seo/outputs/plp-all-batches-2026-03-19-fixed.csv`
- [ ] Validate fix pass output with same QA script
- [ ] Upload final fixed CSV to Contentful
- [ ] Confirm `01-plp-intro-copy.md` is synced with `01-plp-intros.md` (both should reflect v2.1 content)
- [ ] Add `plp-fix-pass.md` agent to repo and commit
- [ ] Resolve `00-tov-language-reference.md` vs `00-tov.md` naming inconsistency (agents reference different files)
- [ ] After upload: mark status Complete and archive this entry

### Files / resources
- `seo/outputs/plp-batch1-priority30-2026-03-19.md` — Batch 1 (done, shipped)
- `seo/outputs/plp-all-batches-2026-03-19.csv` — Batches 2–4 (843 rows, pre-fix)
- `seo/outputs/plp-fix-candidates-2026-03-19.csv` — 658 rows requiring entity fix
- `01-plp-intros.md` — Process file v2.1 (canonical rules)
- `01-plp-intro-copy.md` — Duplicate process file (needs sync to v2.1)
- `.claude/agents/plp-copywriter.md` — Writing agent (updated v2, includes competitor substitution test)
- `.claude/agents/plp-fix-pass.md` — Fix pass agent (new — must be committed to repo)
- `PLP-Batch-Production-Brief-2026-03-19.md` — Original batch brief
- `TGG_-_SEO_WIP___SM_-_PLP_Intro__Brand_Cat_.csv` — Source file (local, not in repo)

---

## Repo Housekeeping — Pending

**Status:** Active
**Last updated:** 27 March 2026

### Context
Several structural issues were identified during the batch 2–4 production session. Not urgent but should be resolved before the next major batch to prevent agent confusion.

### Issues identified
1. **Duplicate process files:** `01-plp-intro-copy.md` and `01-plp-intros.md` both exist. Agents have referenced different files. Both should contain identical v2.1 content.
2. **TOV file naming conflict:** `00-tov-language-reference.md` and `00-tov.md` both exist. Some agents reference the old name, some the new. Standardise to `00-tov.md` and update all agent references.
3. **`plp-copywriter.md` in repo:** Still contains old char range (230–260) and references `01-plp-intro-copy.md`. Replace with v2 (from `.claude/agents/plp-copywriter.md` patch).
4. **`plp-fix-pass.md` not yet in repo:** New agent created for the fix pass. Must be added.
5. **Skills directory incomplete:** `.claude/skills/` only contains `tgg-repo-manager`. The skills `tgg-copywriting`, `tgg-seo-specialist`, `tgg-content-strategist`, `tgg-template-generator` are Claude.ai UI skills and exist there — not in repo (this is correct). Document this distinction clearly in CLAUDE.md or README.
6. **Airtable exclusion note missing:** CLAUDE.md and the GitHub issue trigger template should explicitly state "Storage: use GitHub only (seo/outputs/). Do not use Airtable."
7. **`seo-content-auditor` references stale filenames:** The agent lists `01-plp-intro-copy.md` in its content file locations. Update to `01-plp-intros.md`.

### Next actions
- [ ] Sync `01-plp-intro-copy.md` with `01-plp-intros.md` v2.1 content (or delete one and update all refs)
- [ ] Standardise TOV filename to `00-tov.md`, update all agent `ctx_read_file` calls
- [ ] Replace `plp-copywriter.md` in repo with v2 version
- [ ] Add `plp-fix-pass.md` agent to repo
- [ ] Add Airtable exclusion note to CLAUDE.md and issue trigger template
- [ ] Update `seo-content-auditor.md` — change `01-plp-intro-copy.md` to `01-plp-intros.md`
- [ ] Document skills directory scope (Claude.ai UI skills vs repo-tracked skills)

### Files / resources
- `.claude/agents/plp-copywriter.md` — needs replacement (patches in `/plp-docs/repo-patches/`)
- `.claude/agents/plp-fix-pass.md` — needs to be added
- `.claude/agents/seo-content-auditor.md` — needs filename update
- `01-plp-intro-copy.md` — needs sync or deletion
- `00-tov-language-reference.md` — needs rename or alias to `00-tov.md`
