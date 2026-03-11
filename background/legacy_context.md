# Legacy Context

These files existed in the repository before the workspace was set up. They have **NOT** been confirmed as active workflows or guidelines. Before using any approach described here, ask the user:

> "I found a legacy [X] — would you like to use it, adapt it, or start fresh?"

---

## claude.md — Personal Workflow Guide

A personal workflow guide describing how Claude should work with the user Simon. Covers five working principles (think before acting, remember past work, use subagents for heavy lifting, confirm before committing, keep things simple), a task management process using `tasks/todo.md` and `tasks/lessons.md`, a long-running projects convention using a `projects/` folder, an SEO process management section referencing numbered process files in `processes/`, a writing philosophy section, and core principles such as "context is king" and "preferences stick." Also describes four SEO workflow chains (A–D) for category page optimisation, AEO audits, internal linking, and full category page builds.

---

## PROMPT_AUDIT.md — SEO Prompt Audit

An audit document for "The Good Guys" SEO process. Inventories 10 process files (00–09), documents 5 contradictions that were identified across the original source documents and the resolutions applied, and records key design decisions: using guardrails not templates (hard bans and overuse warnings rather than prescriptive "allowed" lists), integrating the SEM Copy Guide into `00-tov-language-reference.md`, and positioning EAV Mapping (Process 08) as a research/foundation step rather than a writing step. Also documents the same four workflow chains as `claude.md`.

---

## 00–09 SEO Process Files

These 10 files define step-by-step SEO processes for The Good Guys. They are domain-specific and should not be treated as generic workspace instructions.

| File | Process | Brief Description |
|------|---------|-------------------|
| `00-tov-language-reference.md` | TOV & Language Reference | Master tone-of-voice guide: banned words, overuse warnings, tone rules. Must be read before any content-writing task. |
| `01-plp-intro-copy.md` | PLP Intro Copy (2-Sentence) | Process for writing 2-sentence category page intro copy (230–260 chars, ~250 sweet spot). |
| `02-metadata-generation.md` | Metadata Generation | Process for generating page title and meta description for category and product pages. |
| `03-inlink-migration.md` | Inlink Migration (Top→Bottom) | Process for migrating internal links from top-of-page to bottom-of-page placement. |
| `04-content-analysis.md` | Content Analysis | Process for analysing existing content: core query, keyword fanout, content summary. |
| `05-faq-category-copy.md` | FAQ & Category Copy | Process for writing FAQ blocks and brand/category copy sections. |
| `06-internal-linking.md` | Internal Linking | Process for finding, validating, verifying, and inserting internal links. |
| `07-aeo-optimisation.md` | AEO Optimisation | Process for Answer Engine Optimisation: identifying and improving AI-citable content. |
| `08-eav-mapping.md` | EAV Mapping | Research process for mapping entities, attributes, and values — feeds into writing processes. |
| `09-ai-visibility-polling.md` | AI Visibility Polling | Process for polling AI search engines to assess brand and product visibility. |
