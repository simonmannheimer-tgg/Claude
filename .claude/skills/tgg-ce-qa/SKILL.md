---
name: tgg-ce-qa
description: Content engineering pipeline stage — QA. Validates draft.md against the typed constraint set for the current content type. Routes to verification-gate-protocol with the correct --type flag, then calls tgg-seo-specialist for on-page SEO checks. Returns qa-report.md with PASS/FAIL per constraint. Blocks Stage 8 if any block_delivery constraint fails. Use only within the content pipeline.
---

# CE QA — Stage 7

Produces `runs/<run-id>/qa-report.md`. Owns constraint routing and report format. Does not own constraint logic — that lives in `verification-gate-protocol`. Does not own SEO judgement — that lives in `tgg-seo-specialist`.

## Inputs required

- `runs/<run-id>/draft.md`
- `runs/<run-id>/intake.md` (for content_type and angle)
- Constraint file: `.claude/skills/verification-gate-protocol/constraints/<content_type>.yaml`

## Step 1: Load constraints

Read the constraint YAML for the content type from intake.md. List every `qa_gate` entry — these are what you will check.

Also apply the universal constraints (all types):
- Australian English spelling
- No em dashes as sentence connectors
- No AI banned phrases (flag any from the tgg-humanizer 29-pattern list that appear)
- Claim-evidence pairing on factual statements

## Step 2: Run verification-gate-protocol

Invoke `verification-gate-protocol --type <content_type>` on `draft.md`. Pass the constraint file path. Use Phase 1 (criteria extraction) and Phase 3 (final validation) only — not Phase 2 checkpoints, since this is a single-document check.

## Step 3: SEO on-page check

Hand `draft.md` and `seo-data.md` to `tgg-seo-specialist` with this request:

> Check the following for the draft at `runs/<run-id>/draft.md`:
> 1. Primary keyword present in: H1, first 100 words, at least one H2, at least one image alt text placeholder
> 2. Internal link count: count all `[LINK: /slug]` placeholders — report the total
> 3. Claim-evidence pairing: flag any factual claim (statistic, product specification, standard reference) not followed by a source or link
> 4. FAQ schema readiness: confirm all FAQ answers are plain prose (no markdown formatting)
> 5. Meta title and description not yet present — skip
>
> Return a structured list of pass/fail results only. No recommendations yet.

## Step 4: Assemble qa-report.md

```markdown
# QA Report — <content_type> — <keyword>
Run: <run-id> | Date: <YYYY-MM-DD>

## Constraint check

| Constraint | Target | Actual | Result | Block? |
|---|---|---|---|---|
| word_count | <min>–<max> | <actual> | ✓/✗ | NO/YES |
| h2_count | <min>–<max> | <actual> | ✓/✗ | NO/YES |
| internal_links | <min>–<max> | <actual> | ✓/✗ | NO/YES |
| faq_count | <min>–<max> | <actual> | ✓/✗ | NO/YES |
| faq_answer_words | <min>–<max> per answer | <range found> | ✓/✗ | NO/YES |
| required_sections | all present | <list missing> | ✓/✗ | YES |
| australian_english | no US spellings | <violations if any> | ✓/✗ | YES |
| claim_evidence | all claims sourced | <unsourced claims if any> | ✓/✗ | NO |
| keyword_in_h1 | present | present/absent | ✓/✗ | NO |
| keyword_in_first_100_words | present | present/absent | ✓/✗ | NO |
| faq_schema_safe | no markdown in answers | <violations if any> | ✓/✗ | YES |

## Overall result: PASS / FAIL

Block delivery: YES / NO

## Items requiring fix before Stage 8
<List only FAIL items with Block: YES>

## Items to fix at next revision (non-blocking)
<List FAIL items with Block: NO>
```

## Step 5: Gate decision

If Block delivery: YES → stop. Present `qa-report.md` to the human. Wait for instruction before proceeding.

If Block delivery: NO (all failures are non-blocking) → proceed to Stage 8, noting non-blocking issues in the humanised-draft.md humaniser log.

## What this skill does NOT do

- Does not check constraints itself — `verification-gate-protocol` does
- Does not fix the draft — it reports failures for the human or the orchestrator to act on
- Does not apply SEO recommendations — `tgg-seo-specialist` provides the checks, not fixes
- Does not validate metadata (title, description) — that is produced at Stage 9
