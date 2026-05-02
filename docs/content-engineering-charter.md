# Content Engineering Charter

**Owner:** Simon Mannheimer, SEO Lead, The Good Guys
**Last updated:** 2026-05-02
**Source of truth:** This file. When `tgg-content-pipeline` and `tgg-content-engineer` disagree, this is canonical.

---

## Purpose

This charter defines the contract between every skill in the TGG content engineering pipeline. It specifies what each skill owns, what it delegates, and the artefact format that connects them. Update this file whenever a pipeline rule changes permanently.

For one-off exceptions, note them in the pipeline run's `pipeline-status.md` — do not update the charter for exceptions.

---

## System map

### Claude Code pipeline

```
tgg-content-pipeline (orchestrator)
├── Stage 1: Intake          — orchestrator (no delegation)
├── Stage 2: Research        — tgg-ce-research → tgg-marketing-analyst + run_research.py
├── Stage 3: Competitor      — tgg-ce-competitor-extract → tgg-seo (technical mode) + extract_competitors.py
│                              tgg-contentful-linker (existing TGG content)
├── Stage 4: Brief           — tgg-ce-brief → tgg-seo (strategy mode) + tgg-template-generator
│                              GATE: verification-gate-protocol --type <type>
├── Stage 5: Outline         — tgg-ce-outline → tgg-seo (strategy mode)
│                              VALIDATES: H2 count vs numeric-constraints.md
├── Stage 6: Draft           — tgg-ce-draft → tgg-seo (strategy mode) (body)
│                              tgg-seo (production mode) (FAQ block, PLP intro if present)
├── Stage 7: QA              — tgg-ce-qa → verification-gate-protocol + tgg-seo (technical mode)
│                              GATE: block_delivery items stop pipeline
├── Stage 8: Humanise        — tgg-humanizer (always called)
└── Stage 9: Finalise        — tgg-ce-finalise → tgg-contentful-linker (links)
                               tgg-seo (production mode) (metadata)
                               simon-voice (byline: simon only)
```

### Claude.ai pipeline (mirrors the above, no filesystem)

`tgg-content-engineer` — single Claude.ai skill, same 9 stages, same delegation map, same artefact contracts (presented as code blocks in chat rather than files on disk).

---

## Numeric constraints (canonical)

Source files: `.claude/skills/verification-gate-protocol/constraints/<type>.yaml`

| Type | Words | H2s | Int. links | FAQ Q | FAQ A words |
|---|---|---|---|---|---|
| buying-guide | 1,800–2,500 | 6–9 | 8–12 | 5–8 | 50–120 |
| how-to | 800–1,400 | 4–7 | 4–8 | — | — |
| comparison | 1,200–2,000 | 4–6 | 6–10 | — | — |
| eav-explainer | 1,000–1,800 | 4–7 | 6–10 | — | — |
| plp-intro | 220–250 chars | — | — | — | — |
| faq-block | — | — | — | 5–8 | 50–120 |

---

## Delegation contract (canonical)

| Task | Owner skill | What the pipeline passes in | What it receives back |
|---|---|---|---|
| Analytics and keyword data | `tgg-marketing-analyst` | keyword, date range, market | `seo-data.md` structured markdown |
| SEO data (deterministic) | `run_research.py` | keyword, market, competitors | JSON merged into `seo-data.md` |
| Competitor page fetch | `extract_competitors.py` | keyword, competitor domains | JSON merged into `competitive-extract.md` |
| Competitor SEO analysis | `tgg-seo (technical mode)` | competitor JSON, keyword | Gap analysis in markdown |
| Existing TGG content | `tgg-contentful-linker` | keyword, slug pattern | `existing-content.md` with Contentful IDs |
| Brief template | `tgg-template-generator` | `content_type` slug | Base brief scaffold markdown |
| Brief + strategy reasoning | `tgg-seo (strategy mode)` | all inputs + template | `brief.md` |
| Outline | `tgg-seo (strategy mode)` | `brief.md` | `outline.md` |
| Body draft | `tgg-seo (strategy mode)` | brief + outline + seo-data + competitive | Body copy markdown |
| Short-form copy | `tgg-seo (production mode)` | content_type, keyword, angle | FAQ block / PLP intro / metadata block |
| Multi-constraint validation | `verification-gate-protocol` | draft + constraint YAML path | PASS/FAIL per constraint |
| AI-pattern removal | `tgg-humanizer` | draft markdown | Humanised draft |
| Voice pass | `simon-voice` | humanised draft | Voice-passed draft (byline: simon only) |
| Internal link resolution | `tgg-contentful-linker` | list of `[LINK: /slug]` | Contentful entry IDs + resolved markdown links |
| Metadata copy | `tgg-seo (production mode)` | first 300 words + keyword + slug | `metadata.md` |
| Commit messages | `tgg-repo-manager` | stage name + run-id | Structured commit |
| Prompt pre-processing | `tgg-prompt-architect` | all prompts (upstream, always-on) | Re-routed prompt |
| Session scope lock | `tgg-session-anchor` | called at `/run` start | Scope confirmation |

---

## Artefact filenames (canonical)

All artefacts live in `runs/<run-id>/`. The run-id format is `YYYY-MM-DD-<slug-sanitised>-<sha1-6char>`.

| File | Stage | Required | Content |
|---|---|---|---|
| `intake.md` | 1 | Yes | All intake fields including angle and byline |
| `seo-data.md` | 2 | Yes | Keyword metrics, related queries, competitor rankings, GSC/GA4 data |
| `competitive-extract.md` | 3 | Yes | H1/H2/H3 structure, key claims, content gaps per competitor |
| `existing-content.md` | 3 | Yes | Existing TGG pages matching keyword/slug |
| `brief.md` | 4 | Yes | Full production brief including angle, EAV, schema, and internal link opportunities |
| `outline.md` | 5 | Yes | H2 list with word budgets |
| `draft.md` | 6 | Yes | Full article body + FAQ block, with `[LINK: /slug]` placeholders |
| `qa-report.md` | 7 | Yes | Per-constraint PASS/FAIL with block_delivery flags |
| `humanised-draft.md` | 8 | Yes | AI-pattern-free draft + humaniser log |
| `final.md` | 9 | Yes | Full article with resolved links + YAML front matter |
| `metadata.md` | 9 | Yes | Meta title, description, slug, OG title |
| `faq.json` | 9 | Yes | JSON-LD FAQPage schema |
| `internal-links.md` | 9 | Yes | Resolved link map (slug → Contentful entry ID) |
| `pipeline-status.md` | all | Yes | Stage completion tracking |

---

## Hard gates (canonical)

Two stages have hard gates that block pipeline progression:

1. **Stage 4 (Brief):** `verification-gate-protocol --type <type>` must return PASS on the brief in pre-draft mode. Checks required sections are planned, angle is present, EAV attributes listed (for relevant types).

2. **Stage 7 (QA):** `verification-gate-protocol --type <type>` must return no `block_delivery: YES` items. Any blocking constraint failure halts the pipeline until resolved.

Non-blocking QA failures (e.g., non-critical claim-evidence items) are noted in `qa-report.md` and logged in the humaniser log at Stage 8, but do not stop progression.

---

## Universal content rules

Applied to all content types, enforced by `verification-gate-protocol` and `tgg-humanizer`:

- Australian English spelling (organise, colour, optimise, etc.)
- No em dashes as sentence connectors (use full stop + space)
- No AI banned phrases (see `tgg-humanizer` 29-pattern list — do not duplicate here)
- Claim-evidence pairing for factual statements
- "The Good Guys" max once per 200 words in body copy; in S2 only for PLP intros

---

## Batch pipeline specifics

- `plp-intro` and `faq-block` use a 3-stage micro-pipeline (no research, competitor extract, brief, or outline)
- Concurrency cap: 10 parallel subagents by default (configurable, max 20)
- Idempotency: stable run-ids per slug — re-running resumes from last successful stage
- Pause at 30% failure rate and report to human before continuing

---

## Shared resource locations (do not duplicate)

| Resource | Location |
|---|---|
| Voice rules | `simon-voice` + `tgg-humanizer` skills |
| Constraint logic | `verification-gate-protocol` + `constraints/*.yaml` |
| Base templates | `tgg-template-generator` skill |
| TGG-specific augmentations | `tgg-ce-draft/references/content-type-templates/` |
| Australian retail language | `tgg-ce-draft/references/australian-retail-language.md` |
| Numeric constraints reference | `tgg-content-pipeline/references/numeric-constraints.md` |
| Stage contracts | `tgg-content-pipeline/references/stage-contracts.md` |

---

## Quarterly housekeeping (tgg-repo-manager remit)

- Run Anthropic's `skill-creator` evaluation on every `tgg-ce-*` skill
- Remove any skill whose absence does not measurably degrade output
- Review trigger collision risk: all `tgg-ce-*` descriptions must start with "Content engineering pipeline stage"
- Check `runs/` folder size — delete runs older than 90 days
