# Repo Housekeeping Audit
**Date:** 27 March 2026
**Prepared by:** Claude (claude.ai)
**Scope:** simonmannheimer-tgg/Claude — `.claude/` directory and process files

---

## Summary

7 issues identified across 3 severity levels. None are blockers but several will cause agent confusion on the next major batch if left unresolved. Estimated fix time: 30–45 minutes with Claude Code.

---

## Issues

### CRITICAL — Fix Before Next Production Run

#### 1. `plp-copywriter.md` agent contains outdated rules
**File:** `.claude/agents/plp-copywriter.md`
**Problem:** Still references the old char range (230–260 in some prompts) and references `01-plp-intro-copy.md` instead of `01-plp-intros.md`. The entity depth standard is also the old version (proprietary trademark only) which caused the 658-row fix backlog.
**Fix:** Replace entirely with the v2 version from `plp-docs/repo-patches/.claude/agents/plp-copywriter.md`
**Commit:** `fix(agents): plp-copywriter v2 — entity anchor standard corrected, char range 220-250`

#### 2. `plp-fix-pass.md` agent missing from repo
**File:** `.claude/agents/plp-fix-pass.md` — does not exist
**Problem:** The fix pass agent was written during the session but never committed. Without it, the 658-row backlog cannot be processed by Claude Code via GitHub Issues.
**Fix:** Add the file from `plp-docs/repo-patches/.claude/agents/plp-fix-pass.md`
**Commit:** `feat(agents): add plp-fix-pass agent for mandatory entity-depth backlog`

---

### HIGH — Fix Within This Week

#### 3. Duplicate process files: `01-plp-intro-copy.md` vs `01-plp-intros.md`
**Files:** `01-plp-intro-copy.md` and `01-plp-intros.md` (both in repo root)
**Problem:** Two files with the same content purpose. During the batch session, agents were referencing different filenames, creating inconsistency. The v2.1 content (entity anchor standard, corrected char range) exists in `01-plp-intros.md` but `01-plp-intro-copy.md` may still carry old content.
**Fix options (pick one):**
- Option A: Delete `01-plp-intro-copy.md`. Update any agent that references it to use `01-plp-intros.md`.
- Option B: Keep both but sync content — copy v2.1 content into `01-plp-intro-copy.md` and add a header note: `_Alias for 01-plp-intros.md — kept for backward compatibility with older agent references._`
**Recommendation:** Option A (delete). Less confusion. One source of truth.
**Agents to update if deleting:** `plp-copywriter.md`, `seo-content-auditor.md`, `seo-team-lead.md` (check all for filename references)
**Commit:** `chore(process): remove 01-plp-intro-copy.md — consolidated into 01-plp-intros.md`

#### 4. TOV filename inconsistency: `00-tov-language-reference.md` vs `00-tov.md`
**Files:** `00-tov-language-reference.md` (old name) and `00-tov.md` (new name, from v2 tgg-copywriting skill)
**Problem:** Agents in `.claude/agents/` call `ctx_read_file("00-tov-language-reference.md")`. The Claude.ai skill references `00-tov.md`. If both files exist with different content, agents get inconsistent rules.
**Current state:**
- `seo-team-lead.md` references `00-tov-language-reference.md`
- `plp-copywriter.md` (v2) references `00-tov.md`
- `faq-writer.md` references `00-tov-language-reference.md`
- `inlink-migrator.md` references `00-tov-language-reference.md`
**Fix:** Standardise on `00-tov.md`. Either:
- Rename `00-tov-language-reference.md` → `00-tov.md` and update all agent references
- Or keep both but make `00-tov-language-reference.md` a symlink/redirect file with one line: `_Renamed to 00-tov.md. Please update your reference._`
**Commit:** `chore(process): standardise TOV filename to 00-tov.md, update agent references`

#### 5. `seo-content-auditor.md` references stale filename
**File:** `.claude/agents/seo-content-auditor.md`
**Problem:** Line in "Content file locations" section lists `01-plp-intro-copy.md`. Should be `01-plp-intros.md`.
**Fix:** Update the filename reference.
**Commit:** `fix(agents): seo-content-auditor — update process file reference to 01-plp-intros.md`

---

### MEDIUM — Fix When Convenient

#### 6. Airtable exclusion not documented
**Files:** `CLAUDE.md`, GitHub issue trigger template in `PLP-Batch-Production-Brief-2026-03-19.md`
**Problem:** During the batch session, there was a risk of the agent trying to use Airtable (which is connected as an MCP). The rule "Storage: use GitHub only (seo/outputs/). Do not use Airtable." exists in session context but is not written anywhere in the repo.
**Fix:** Add to CLAUDE.md under "SEO Agent Team → Storage rules":
```
### Storage rules
- All SEO outputs: `seo/outputs/` directory in this GitHub repo only
- Do NOT use Airtable for outputs — write to disk and commit
- Do NOT write to local paths outside `seo/outputs/`
```
Also add to the GitHub issue trigger template so every `@claude` task inherits the rule.
**Commit:** `docs(claude.md): add storage rules — GitHub only, no Airtable`

#### 7. `.claude/skills/` directory scope undocumented
**File:** `.claude/skills/` — only contains `tgg-repo-manager/SKILL.md`
**Problem:** The repo's skills directory only has one skill, but there are 5 active TGG skills in Claude.ai (tgg-copywriting, tgg-seo-specialist, tgg-content-strategist, tgg-template-generator, tgg-repo-manager). Someone reading the repo would not know the full skill set exists.
**Fix:** Add a `README.md` to `.claude/skills/`:
```markdown
# Claude.ai Skills

This directory contains skills tracked in the repo. Additional skills exist in Claude.ai that are not repo-tracked:

| Skill | Location | Purpose |
|-------|----------|---------|
| tgg-repo-manager | This repo (.claude/skills/) | Commit messages, PRs, process file updates |
| tgg-copywriting | Claude.ai UI only | PLP intros, metadata, FAQ copy production |
| tgg-seo-specialist | Claude.ai UI only | Full SEO audits, keyword analysis, AEO |
| tgg-content-strategist | Claude.ai UI only | Content strategy, briefs, copy planning |
| tgg-template-generator | Claude.ai UI only | Template and scaffold creation |
| tgg-marketing-analyst | Claude.ai UI only | Organic search analytics, GSC/GA4 reporting |

Claude.ai skills are managed via the Claude.ai interface (Edit with Claude). To update them, open the skill in Claude.ai and use Edit. Changes do not require a git commit.
```
**Commit:** `docs(skills): add README documenting all Claude.ai skills and their location`

---

## Recommended Commit Sequence

Run in this order to keep the diff clean:

```bash
# 1. Process file consolidation
git rm 01-plp-intro-copy.md
git add 01-plp-intros.md  # ensure v2.1 content
git commit -m "chore(process): remove 01-plp-intro-copy.md — consolidated into 01-plp-intros.md"

# 2. TOV standardisation
git mv 00-tov-language-reference.md 00-tov.md
# (update all agent ctx_read_file calls in the same commit)
git add .claude/agents/
git commit -m "chore(process): standardise TOV filename to 00-tov.md, update 4 agent references"

# 3. Agent fixes
git add .claude/agents/plp-copywriter.md  # v2 replacement
git add .claude/agents/plp-fix-pass.md    # new agent
git add .claude/agents/seo-content-auditor.md  # filename fix
git commit -m "fix(agents): plp-copywriter v2, add plp-fix-pass, fix seo-content-auditor filename ref"

# 4. Documentation
git add CLAUDE.md  # storage rules + plp project entry + housekeeping entry
git add .claude/skills/README.md
git commit -m "docs(claude.md): add storage rules, PLP project status, repo housekeeping audit"
```

---

## What NOT to Change

- `.claude/agents/seo-team-lead.md` — core routing is correct. Only update the TOV filename reference if standardising.
- `PLP-Batch-Production-Brief-2026-03-19.md` — historical document. Add storage note but otherwise leave intact.
- `.github/workflows/` — these are functional. No changes needed.
- `CLAUDE.md` MCP server section — correct and current.
- Any `seo/outputs/` files — don't reorganise. The naming convention (`plp-*`, `faq-*`, `metadata-*`) is working.
