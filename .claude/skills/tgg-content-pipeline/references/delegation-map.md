# Delegation Map

Single source of truth for what logic lives where in the TGG content engineering pipeline.
When `tgg-content-pipeline` and `tgg-content-engineer` disagree, `docs/content-engineering-charter.md` is canonical.

---

## What lives in the orchestrator (`tgg-content-pipeline`)

- Stage order (1 through 9)
- Artefact filenames and folder structure (`runs/<run-id>/`)
- Hard gate conditions (when to stop and wait for human)
- Numeric constraints table (which type needs which counts) — see `numeric-constraints.md`
- Decision rule for `simon-voice` invocation (byline: simon only)
- Commit milestone triggers (calls `tgg-repo-manager` at stage milestones)
- Delegation routing (what to call, what inputs to pass)

## What lives in sub-skills

| Sub-skill | Owns |
|---|---|
| `tgg-ce-research` | Structured research bundle format, `run_research.py` script |
| `tgg-ce-competitor-extract` | Competitor page fetch logic, `extract_competitors.py` script |
| `tgg-ce-brief` | Brief template augmentation for TGG (AU retail, EAV, schema requirements) |
| `tgg-ce-outline` | Outline validation for numeric H2 targets |
| `tgg-ce-draft` | Voice references, Australian retail language, content-type augmentations |
| `tgg-ce-qa` | Constraint routing (which YAML file per type), QA report format |
| `tgg-ce-finalise` | FAQ JSON-LD assembly, metadata block assembly, final.md YAML front matter |
| `tgg-ce-batch` | CSV input validation, subagent dispatch, aggregate report |

## What lives in existing TGG skills (not the pipeline)

| Domain | Skill | Do NOT replicate in pipeline |
|---|---|---|
| Analytics and keyword data | `tgg-marketing-analyst` | GSC/GA4/Semrush API calls, query fan-out |
| SEO strategy and on-page | `tgg-seo` (technical mode) | Technical SEO, keyword placement, backlinks |
| Contentful resolution | `tgg-contentful-linker` | CMS URL → entry ID mapping |
| Content strategy and drafting | `tgg-seo` (strategy mode) | Brief reasoning, outline craft, body drafting |
| Short-form copy production | `tgg-seo` (production mode) | PLP intro, FAQ copy, metadata copy |
| Template scaffolds | `tgg-template-generator` | Brief and outline templates by content type |
| Multi-constraint validation | `verification-gate-protocol` | Constraint checking, gate logic |
| AI-pattern removal | `tgg-humanizer` | All 29 banned patterns |
| Simon's voice | `simon-voice` | Voice rules, ghostwriting |
| Commit messages and docs | `tgg-repo-manager` | Git, CLAUDE.md, PR descriptions |
| Prompt pre-processing | `tgg-prompt-architect` | Prompt triage (always-on, upstream) |
| Scope locking | `tgg-session-anchor` | Session focus, drift detection |

---

## Shared resources (one location, referenced everywhere)

| Resource | Location | Do NOT copy into pipeline skills |
|---|---|---|
| Voice rules | `simon-voice` and `tgg-humanizer` skills | |
| Validation logic | `verification-gate-protocol` + `constraints/*.yaml` | |
| Content templates | `tgg-template-generator` | |
| Content engineering contract | `docs/content-engineering-charter.md` | |
