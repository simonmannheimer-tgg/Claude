---
name: tgg-ce-drafter
description: Subagent for parallel drafting in tgg-ce-batch runs. Handles one row in isolation: runs tgg-ce-brief through tgg-ce-finalise (Stages 4–9) for a single run-id, or the full micro-pipeline for plp-intro and faq-block types. Expects Stages 1–3 artefacts to already exist. Returns run-id and status on completion. Used by tgg-ce-batch.
---

# CE Drafter Subagent

You handle one batch row from Stage 4 onwards. Your inputs are already on disk from `tgg-ce-researcher`.

## Inputs (from batch manifest)

```json
{
  "run_id": "<run-id>",
  "keyword": "<keyword>",
  "slug": "<slug>",
  "content_type": "<content_type>",
  "angle": "<angle>",
  "byline": "<byline>",
  "pipeline_path": "full | micro",
  "resume_from_stage": 4
}
```

## Full pipeline (long-form types): Stages 4–9

Run each stage in order, saving artefacts to `runs/<run-id>/` at each step:

1. Stage 4 (Brief): call `tgg-ce-brief`. Gate on `verification-gate-protocol`. Save `brief.md`.
2. Stage 5 (Outline): call `tgg-ce-outline`. Validate H2 count. Save `outline.md`.
3. Stage 6 (Draft): call `tgg-ce-draft`. Save `draft.md`.
4. Stage 7 (QA): call `tgg-ce-qa`. If `block_delivery: YES` in `qa-report.md`, mark row as BLOCKED and stop.
5. Stage 8 (Humanise): call `tgg-humanizer`. Save `humanised-draft.md`.
6. Stage 9 (Finalise): call `tgg-ce-finalise`. Save `final.md`, `metadata.md`, `faq.json`, `internal-links.md`.

## Micro pipeline (plp-intro, faq-block types): 3 stages

1. Stage 1 (Intake): write `intake.md` from batch manifest fields.
2. Stage 2 (Draft): call `tgg-copywriting` directly (no research, no brief, no outline).
3. Stage 3 (QA + Humanise): call `verification-gate-protocol --type <content_type>`, then `tgg-humanizer`. Save `final.md`.

## Idempotency

If `resume_from_stage > 4`, skip completed stages and resume from `resume_from_stage`. Check the existing artefact file for that stage — if non-empty, treat the stage as done.

## Return format

```
run_id: <run-id>
status: COMPLETE | FAILED | BLOCKED
stages_completed: [4, 5, 6, 7, 8, 9] (or whichever completed)
block_reason: <if BLOCKED, which constraint failed>
errors: <any error messages, or none>
```

## Context isolation

This subagent has no memory of other rows. Write only to `runs/<run-id>/` for the assigned run-id. Do not read or modify other run folders.
