---
name: tgg-content-pipeline
description: Content engineering pipeline stage — ORCHESTRATOR. Runs the full TGG long-form content pipeline end-to-end for a single article, buying guide, comparison page, how-to, or EAV explainer. Invoke with /run or when the user says "run the pipeline", "take this through the content pipeline", "start the content engineer on", or "build a [type] for [topic]". Always Australian English. Delegates every domain task to the correct existing TGG skill — does not duplicate voice, SEO, or humanising logic. Refuses to progress past intake if the angle field is missing.
disable-model-invocation: false
---

# TGG Content Pipeline — Orchestrator

This skill runs the single-article content engineering pipeline. It owns stage order, artefact filenames, hard gates, and delegation routing. It does not own voice rules, SEO knowledge, copy schemas, or validation logic — those live in the skills it calls.

## Operating principles

1. Australian English throughout. No em dashes as sentence connectors.
2. Every stage writes a named artefact to `runs/<run-id>/` before proceeding.
3. Stop at any hard gate and wait for explicit confirmation before continuing.
4. Delegate domain logic entirely — never re-implement what an existing skill does.
5. The `angle` field in `intake.md` is mandatory. Accept `angle: none` to skip. Never draft without it.
6. Invoke `tgg-session-anchor` implicitly at the start of every `/run`.
7. Emit a structured commit message at each stage milestone via `tgg-repo-manager`.
8. `tgg-prompt-architect` continues to pre-process all prompts — do not replicate its logic here.

## Run setup

When triggered, immediately call `scripts/new_run.py` to create the run folder:

```
python3 .claude/skills/tgg-content-pipeline/scripts/new_run.py \
  --keyword "<keyword>" \
  --type <content_type> \
  --slug <slug>
```

This outputs a `run-id` (format: `YYYY-MM-DD-<slug-hash>`) and creates `runs/<run-id>/` with empty placeholder files. All artefact paths below use this `run-id`.

---

## Stage 1: Intake

**Artefact:** `runs/<run-id>/intake.md`

Collect the following fields. Ask for any that are missing. Do not proceed to Stage 2 until all required fields are confirmed.

```markdown
# Intake

keyword: <target keyword or topic>
content_type: <buying-guide | how-to | comparison | eav-explainer>
slug: <proposed URL slug, e.g. /buying-guides/heat-pump-dryer>
primary_intent: <informational | commercial | navigational>
must_cover:
  - <sub-topic 1>
  - <sub-topic 2>
angle: <free-text direction — angle, must-mention brands/features, tone notes. Write "none" to skip.>
byline: <simon | editorial | uncredited>
run_id: <from new_run.py output>
date: <YYYY-MM-DD>
```

**Hard rule:** If `angle` is absent and user does not supply `angle: none`, stop and request it. Do not generate a default angle.

**Hard rule:** If `byline` is absent, stop and request it. The `simon-voice` gate depends on this.

Save the completed intake to `runs/<run-id>/intake.md` before Stage 2.

---

## Stage 2: Research and SEO data

**Artefact:** `runs/<run-id>/seo-data.md`

Hand off to `tgg-marketing-analyst` with these exact queries:

- GSC impressions and clicks for the target keyword and close variants (last 90 days)
- GA4 engagement rate on existing TGG content in this category
- Semrush KD, volume (AU database), parent topic, and top-5 ranking URLs for the keyword
- Query fan-out: top 15 related queries by volume

Tell `tgg-marketing-analyst` to return a single structured markdown file, not a chat-friendly summary. Save the output verbatim to `runs/<run-id>/seo-data.md`.

Also run `scripts/run_research.py` for the deterministic data fetch:
```
python3 .claude/skills/tgg-ce-research/scripts/run_research.py \
  --keyword "<keyword>" \
  --market au \
  --competitors jbhifi.com.au,harveynorman.com.au,appliancesonline.com.au
```

Merge the script output with `tgg-marketing-analyst`'s markdown into the single `seo-data.md` artefact.

---

## Stage 3: Competitor and existing content scan

**Artefacts:** `runs/<run-id>/competitive-extract.md`, `runs/<run-id>/existing-content.md`

**Competitor scan:** Hand off to `tgg-seo-specialist`. Provide competitor list: jbhifi.com.au, harveynorman.com.au, appliancesonline.com.au. Request H1/H2/H3 structure, key claims, and content gaps for each.

Also run `scripts/extract_competitors.py` for the deterministic page fetch:
```
python3 .claude/skills/tgg-ce-competitor-extract/scripts/extract_competitors.py \
  --keyword "<keyword>" \
  --competitors jbhifi.com.au,harveynorman.com.au,appliancesonline.com.au
```

Save to `runs/<run-id>/competitive-extract.md`.

**Existing TGG content:** Hand off to `tgg-contentful-linker`. Ask it to return any existing TGG pages matching the keyword or slug pattern. Save to `runs/<run-id>/existing-content.md`.

---

## Stage 4: Brief

**Artefact:** `runs/<run-id>/brief.md`

Hand off all of the following to `tgg-content-strategist`:
- `runs/<run-id>/intake.md`
- `runs/<run-id>/seo-data.md`
- `runs/<run-id>/competitive-extract.md`
- `runs/<run-id>/existing-content.md`

Request a full brief with: target audience, primary and secondary keywords, content angle (verbatim from `intake.md`), must-cover topics, differentiation from competitors, EAV attributes to define (for eav-explainer and buying-guide types), schema requirements, internal-link opportunities.

Call `tgg-template-generator` with `content_type=<content_type>` to get the base brief scaffold, then have `tgg-content-strategist` populate it.

Save to `runs/<run-id>/brief.md`.

**HARD GATE:** Run `verification-gate-protocol --type <content_type>` on the brief (pre-draft check). The gate checks that all required sections are planned, not yet written. Do not proceed to Stage 5 until the gate returns PASS.

---

## Stage 5: Outline

**Artefact:** `runs/<run-id>/outline.md`

Hand off `runs/<run-id>/brief.md` to `tgg-content-strategist`. Request a markdown outline.

Numeric constraints (enforce here, not in the called skill):

| Content type | H2 target | Notes |
|---|---|---|
| buying-guide | 6–9 | Must include Australian retail considerations block and FAQ H2 |
| how-to | 4–7 | Steps must be numbered H2s or H3s, each starting with a verb |
| comparison | 4–6 | Must include comparison table H2 and recommendation H2 |
| eav-explainer | 4–7 | Must include EAV mapping H2 with attribute table |

All types: include a "Frequently asked questions" H2 targeting 5–8 questions.

Save to `runs/<run-id>/outline.md`.

State the H2 count and confirm it meets the target before proceeding.

---

## Stage 6: Draft

**Artefact:** `runs/<run-id>/draft.md`

Hand off the following to `tgg-content-strategist` for the body:
- `runs/<run-id>/brief.md`
- `runs/<run-id>/outline.md`
- `runs/<run-id>/seo-data.md` (for keyword placement)
- `runs/<run-id>/competitive-extract.md` (for differentiation)

For short-form blocks (FAQ section, PLP intro if present, metadata fields), hand off to `tgg-copywriting`.

Word count targets (from `references/numeric-constraints.md`):
- buying-guide: 1,800–2,500
- how-to: 800–1,400
- comparison: 1,200–2,000
- eav-explainer: 1,000–1,800

Instruct `tgg-content-strategist` to reference `runs/<run-id>/existing-content.md` for internal-link anchor opportunities. Do not insert final Contentful entry IDs at this stage — use placeholder text `[LINK: <slug>]` instead.

Save to `runs/<run-id>/draft.md`.

---

## Stage 7: Fact-check and SEO QA

**Artefact:** `runs/<run-id>/qa-report.md`

Run `verification-gate-protocol --type <content_type>` on `runs/<run-id>/draft.md`. Load the constraint file from `.claude/skills/verification-gate-protocol/constraints/<content_type>.yaml`.

Also hand off to `tgg-seo-specialist` for:
- On-page keyword placement check (H1, first paragraph, subheadings, image alt text)
- Internal-link count check (target: 8–12 for buying-guide, see constraints file for others)
- Claim-evidence pairing check (every factual claim must have a source or linked reference)
- Schema readiness check (FAQ block schema-safe, no markdown in answers)

Consolidate all QA results into `runs/<run-id>/qa-report.md`.

**HARD GATE:** If `qa-report.md` contains any `FAIL` or `block_delivery` items, do not proceed to Stage 8. Present the report and wait for human decision.

---

## Stage 8: Humanise

**Artefact:** `runs/<run-id>/humanised-draft.md`

Hand off `runs/<run-id>/draft.md` to `tgg-humanizer`. This step is always called. No exceptions.

Save the humanised output to `runs/<run-id>/humanised-draft.md`.

If `tgg-humanizer` flags any patterns that required rewriting, note them in a brief `## Humaniser log` block appended to the artefact.

---

## Stage 9: Voice pass and finalise

**Artefacts:** `runs/<run-id>/final.md`, `runs/<run-id>/metadata.md`, `runs/<run-id>/faq.json`, `runs/<run-id>/internal-links.md`

**Voice pass:** If `byline: simon` in `intake.md`, hand off `runs/<run-id>/humanised-draft.md` to `simon-voice`. Otherwise skip voice pass and use `humanised-draft.md` as the base for final.

**Internal links:** Hand off to `tgg-contentful-linker` with the list of `[LINK: <slug>]` placeholders from the draft. Request Contentful entry IDs for each. Replace all placeholders. Save resolved link map to `runs/<run-id>/internal-links.md`.

**Metadata:** Hand off the article to `tgg-copywriting` to produce: meta title (≤60 chars), meta description (≤155 chars), slug (confirm or update), OG title. Save to `runs/<run-id>/metadata.md`.

**FAQ JSON:** Extract the FAQ block and write schema-ready JSON-LD to `runs/<run-id>/faq.json`. Format:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "<question>",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<answer — plain text, no markdown>"
      }
    }
  ]
}
```

**Final assembly:** Combine into `runs/<run-id>/final.md` with YAML front matter:
```yaml
---
slug: <slug>
content_type: <content_type>
keyword: <keyword>
byline: <byline>
run_id: <run_id>
date: <date>
word_count: <final count>
status: ready-for-review
---
```

**STOP before delivering.** State: "Stage 9 complete. Run `<run-id>` is ready for review. Artefacts in `runs/<run-id>/`. Confirm to commit." Wait for confirmation before calling `tgg-repo-manager`.

---

## Delegation map

| Task | Call this skill | Never do this inline |
|---|---|---|
| Analytics and keyword data | `tgg-marketing-analyst` | GSC queries, GA4 queries, Semrush calls |
| Competitor page analysis | `tgg-seo-specialist` | Scraping, parsing, SEO judgements |
| Contentful URL resolution | `tgg-contentful-linker` | CMS lookups |
| Strategy, brief, outline, draft | `tgg-content-strategist` | Strategy reasoning, structural editing |
| PLP intro, FAQ, metadata copy | `tgg-copywriting` | Short-form copy schemas |
| Template scaffolds | `tgg-template-generator` | Template generation |
| Multi-constraint validation | `verification-gate-protocol` | Constraint checking |
| AI-pattern removal | `tgg-humanizer` | The 29 banned patterns |
| Simon's voice | `simon-voice` | Voice rules (byline: simon only) |
| Commits, CLAUDE.md entries | `tgg-repo-manager` | Git operations |
| Prompt pre-processing | `tgg-prompt-architect` | Already running — do not replicate |
| Scope locking | `tgg-session-anchor` | Call at run start |

## Slash commands

- `/run keyword="..." type=... slug=... angle="..." byline=...` — start a new single-article run
- `/resume run=<run-id> from=<stage>` — restart from a specific stage
- `/qa path=runs/<run-id>/draft.md` — run QA only on an existing draft

## What this skill does NOT do

- Does not know TGG brand voice rules — defers to `tgg-humanizer` and `simon-voice`
- Does not know TGG SEO strategy — defers to `tgg-seo-specialist`
- Does not know Contentful entry structure — defers to `tgg-contentful-linker`
- Does not generate PLP intros or FAQ copy directly — defers to `tgg-copywriting`
- Does not pre-process prompts — `tgg-prompt-architect` handles that upstream
