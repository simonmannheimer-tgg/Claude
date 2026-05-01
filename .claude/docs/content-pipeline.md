# Content Engineering Pipeline

Adapted from Ahrefs' content engineering system. Every production step saves its own output file before passing to the next stage — any step can be reviewed, corrected, or re-run independently.

---

## The Pipeline Skill

`/tgg-category-pipeline [URL or slug]` — chains all agents in sequence.

Optional context parameter (front-load expert input):
```
/tgg-category-pipeline /air-fryers context: "focus on compact models, Ninja is priority brand this season"
```

---

## Output Folder Structure

```
seo/outputs/
├── briefs/      ← context files + content briefs
├── eav/         ← entity/attribute/value mappings
├── keywords/    ← keyword research outputs
├── plp/         ← PLP intro copy (2-sentence)
├── faqs/        ← FAQ sections + category copy
├── metadata/    ← meta titles + descriptions
└── links/       ← internal link outputs
```

Full assembled build: `seo/outputs/[slug]-build-[date].md`

---

## Recursive Improvement

After every pipeline run, note any step that needed manual correction under `## Pipeline notes` in the assembly file. These feed the CONNECTIONS TASK — reviewing what tools or rules to improve.

---

## Writing Philosophy

- Guardrails not templates. Ban harmful patterns; don't prescribe "allowed" ones.
- Vary everything. Sentence openers, TGG placement, benefit angles.
- Be specific. Name brands, features, use cases.
- Sound human. If it reads like a chatbot, rewrite.

---

## Process Update Rule

When Simon changes a rule, update the relevant process file immediately. Add a changelog note at the top (version + date + what changed). If a request conflicts with a process rule, flag it and ask: one-off exception or permanent change?

---

## Open Items

- **ONBOARDING:** Walk Simon through the full system (agents, skills, pipeline, outputs, MCPs). Trigger: "run onboarding" or "walk me through the system".
- **CONNECTIONS REVIEW:** Audit what tools/MCPs should connect to the pipeline. Trigger: "what should we connect" or "connections review".
- **RULE CONFLICTS (open questions for Simon):**
  - PLP char count: Process 01 says **220–250**; `tgg-seo-specialist` skill says 230–260. Which is correct?
  - Execution path: For production copy, do you prefer agents (via seo-team-lead) or skills (e.g. tgg-copywriting, tgg-category-pipeline)?
