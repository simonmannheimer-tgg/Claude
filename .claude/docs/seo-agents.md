# SEO Agent Team Reference

---

## Project Defaults

```
TARGET_DOMAIN=thegoodguys.com.au
COMPETITORS_PRIMARY=jbhifi.com.au,harveynorman.com.au,officeworks.com.au
COMPETITORS_SECONDARY=kogan.com,appliancesonline.com.au
DEFAULT_DATABASE=au
SEMRUSH_DATABASE=au
```

---

## Chain of Command

```
seo-team-lead  (Sonnet — Orchestrator)
├── RESEARCH
│   ├── eav-researcher         (Haiku) — category entity/attribute mapping
│   ├── content-analyst        (Haiku) — query, entity, keyword extraction
│   ├── seo-keyword-researcher (Haiku) — Semrush keyword + organic data
│   └── seo-competitor-analyst (Haiku) — Semrush competitor + backlink data
├── CONTENT
│   ├── plp-copywriter         (Sonnet) — Process 01: 2-sentence PLP intros
│   ├── metadata-writer        (Haiku)  — Process 02: meta titles + descriptions
│   ├── inlink-migrator        (Sonnet) — Process 03: top→bottom copy migration
│   ├── faq-writer             (Sonnet) — Process 05: FAQs + category copy
│   └── aeo-optimizer          (Sonnet) — Process 07: AI answer optimisation
├── LINKING
│   └── internal-linking-agent (Haiku)  — Process 06: find, validate, insert links
├── VISIBILITY
│   └── ai-visibility-analyst  (Haiku)  — Process 09: AI visibility polling
└── REPORTING
    ├── seo-content-auditor    (Haiku)  — on-page audit of repo content files
    └── seo-reporter           (Sonnet) — synthesise findings into reports
```

---

## How to Invoke

```
Use the seo-team-lead to [task]
```

Or directly: `Use the plp-copywriter to write copy for /air-fryers`

Always read `00-tov-language-reference.md` before any content task.

---

## Standard Workflows

| Workflow | Agent / skill sequence |
|----------|----------------------|
| **Full category page build** | `/tgg-category-pipeline [URL]` — chains all steps, saves output per step |
| **Manual category build** | 08 (EAV) → 04 (Fanout) → 01 (PLP Intro) → 05 (FAQ Copy) → 02 (Metadata) → 06 (Linking) |
| **AEO audit** | 04 (Summarise) → 06 (Link Opportunities) → 07 (AEO Suggestions) |
| **Internal linking** | 06 (Find → Validate → Verify → Insert) |
| **Category optimisation** | 08 (EAV) → 04 (Fanout) → 06 (Link Validation) → 05 (Brand+Category FAQ) |
