# Agent Workflows Audit and Recommendations
**Date:** 2 May 2026
**Author:** Claude Code audit (session claude/audit-agent-workflows-SVd8h)
**Scope:** 16 agents in `.claude/agents/`, 30 skill folders in `.claude/skills/` (29 with active SKILL.md)

---

## Step 1 — Full Inventory

### Agents

| Name | Type | Purpose (one line) | Triggers / When invoked | Inputs | Outputs | Dependencies | Last modified |
|---|---|---|---|---|---|---|---|
| aeo-optimizer | agent (sonnet) | AEO improvement suggestions for TGG content | After content-analyst runs; "improve for AI visibility"; Process 07 tasks | Content URL or text + content-analyst output | 5–10 numbered AEO suggestions; refined scorecard | ctx_read_file (Process 07, 00-tov), content-analyst output | 2026-04-29 |
| ai-visibility-analyst | agent (haiku) | Converts Profound AI visibility data to customer poll questions | Raw Profound metrics provided; "process AI visibility data"; Process 09 tasks | Topic/keyword visibility data from Profound (9 specific fields) | JSON poll questions with placement recommendations | ctx_read_file (Process 09) | 2026-04-29 |
| content-analyst | agent (haiku) | Extracts core query, fanout queries, keywords, and entities from a URL or text | Analysing a URL or text; before metadata, FAQ, AEO, or linking tasks; Process 04 | URL or full text | JSON: core_query, fanout_queries, summary, primary_keyword, supporting_keywords, entities | Semrush url_research + execute_report; ctx_index | 2026-04-29 |
| eav-researcher | agent (haiku) | Maps entity-attribute-value landscape for a product category | Start of any new category content task; before plp-copywriter or faq-writer; Process 08 | Category URL or slug | EAV mapping with top attribute priorities; saved to seo/outputs/eav-*.json | Semrush keyword_research + execute_report; ctx_index | 2026-04-29 |
| faq-writer | agent (sonnet) | Writes FAQ Q&A pairs and brand+category copy for category pages | "Write FAQs for [URL/category]"; Process 05 tasks | Primary search query + content-analyst and eav-researcher outputs | 5A: FAQ Q&A pairs; 5B: 150–250 word HTML copy block; 5C: extended PLP intro; saved to seo/outputs/faq-*.md | ctx_read_file (Process 05, 00-tov); content-analyst and eav-researcher outputs | 2026-04-29 |
| inlink-migrator | agent (sonnet) | Rewrites top-of-page HTML copy for page bottom placement, preserving anchor tags | "Migrate this top copy to bottom"; Process 03 | HTML_CODE (full HTML block) + TOP_COPY (intent reference) | Rewritten HTML block + verification summary | ctx_read_file (Process 03, 00-tov) | 2026-04-29 |
| internal-linking-agent | agent (haiku) | Finds, validates, and inserts internal links via 4-stage process | "Add internal links to [content]"; Process 06 | Primary keyword, article summary, list of candidate URLs | Validated link list + updated HTML with links inserted | ctx_read_file (Process 06) | 2026-05-01 |
| metadata-writer | agent (haiku) | Writes SEO-compliant meta titles and descriptions | "Generate metadata for [URLs]"; Process 02 tasks; batch CSV mode | URL(s) or page content + keyword data | Meta title (≤60 chars) + description (150–160 chars); batch CSV to seo/outputs/ | ctx_read_file (Process 02, 00-tov) | 2026-04-29 |
| plp-copywriter | agent (sonnet) | Writes 2-sentence PLP intro copy (220–250 chars) | "Write PLP copy for [URL/category]"; Process 01 tasks | Page URL + EAV data + primary/supporting keywords | 2-sentence intro + character count + language check; 2 variations | ctx_read_file (Process 01, 00-tov); eav-researcher and seo-keyword-researcher outputs | 2026-04-29 |
| seo-competitor-analyst | agent (haiku) | Competitor rankings, backlink profiles, keyword gap analysis via Semrush | "Analyse competitors / keyword gaps"; proactively when competitive intel needed | Target domain + competitor URLs | JSON: overview, top_kw, keyword_gaps, backlink_summary, opportunities; saved to seo/outputs/ | Semrush (organic, backlink, overview, subfolder, url research) | 2026-04-29 |
| seo-content-auditor | agent (haiku) | On-page SEO audit of existing content files in this repo. Read-only. | "Audit [content files] for SEO"; reviewing process files | File path(s) or repo scope | JSON audit per file: issues, quick_fixes, score 0–100 | Semrush url_research; ctx_read_file | 2026-04-29 |
| seo-keyword-researcher | agent (haiku) | Keyword research: volumes, difficulty, SERP features, clusters via Semrush | Proactively when keyword data needed; before copy or content tasks | Topic or seed keyword | JSON: top_keywords, clusters, quick_wins; saved to seo/outputs/keywords-*.json | Semrush (keyword_research, organic_research, trends) | 2026-04-29 |
| seo-reporter | agent (sonnet) | Synthesises keyword, competitor, and audit data into prioritised reports | After research agents complete; "Create a full content brief" | Prior agent outputs from seo/outputs/ + ctx session data | Structured markdown report to seo/outputs/report-*.md + 3-bullet GitHub issue body | ctx_read_file/search; Read/Write/Glob | 2026-04-29 |
| seo-team-lead | agent (sonnet) | Orchestrates all SEO agents; classifies tasks, delegates in correct sequence | Any SEO task described to Claude Code; top-level orchestrator | Free-text SEO task description | Complete deliverable: copy, metadata, FAQs, reports, etc. + output files committed | All 13 specialist agents; ctx tools; Write | 2026-04-29 |
| tgg-ce-drafter | agent (default) | CE pipeline batch subagent: runs Stages 4–9 for one row in isolation | Called by tgg-ce-batch for long-form types; or full micro-pipeline for plp-intro/faq-block | Batch manifest JSON (run_id, keyword, slug, content_type, angle, byline, pipeline_path) | Status return: run-id, COMPLETE/FAILED/BLOCKED, stages completed | tgg-ce-brief, tgg-ce-outline, tgg-ce-draft, tgg-ce-qa, tgg-humanizer, tgg-ce-finalise, verification-gate-protocol | 2026-05-01 |
| tgg-ce-researcher | agent (default) | CE pipeline batch subagent: runs research Stages 2–3 for one row in isolation | Called by tgg-ce-batch for long-form types | Batch manifest JSON (run_id, keyword, slug, content_type, angle) | Status return: run-id, COMPLETE/FAILED; outputs: seo-data.md, competitive-extract.md, existing-content.md | tgg-ce-research, tgg-ce-competitor-extract | 2026-05-01 |

---

### Skills

| Name | Type | Purpose (one line) | Triggers / When invoked | Inputs | Outputs | Dependencies | Last modified |
|---|---|---|---|---|---|---|---|
| check-github | skill | Poll GitHub Issues for @claude tasks, process with SEO agents, post replies | `/check-github` command; manual GitHub polling | None (polls GitHub Issues API via script) | GitHub issue comment replies; committed output files | scripts/github-poll.sh, scripts/github-post-comment.sh; seo-team-lead | 2026-05-01 |
| docx-human-style | skill | Enforce plain human-looking Word document defaults (no AI aesthetics) | Any .docx creation request; auto-layers on top of public docx skill | docx-js document code | Correctly styled Word document; overrides heading colours, table shading | Public docx skill (Anthropic) | 2026-05-01 |
| mhtml-reader | skill | Read and extract content from MHTML files (web pages, AI transcripts) | Any .mhtml file in uploaded_files; "read this MHTML" | .mhtml file path | Extracted content + classification (AI transcript / web snapshot / analytics) | tools/mhtml_parser.py | 2026-05-01 |
| simon-voice | skill | Ghost-write messages and communications in Simon Mannheimer's voice | "Write this as me", "draft a message to", stakeholder updates, Slack posts | Original text or topic + audience context | Rewritten message in Simon's voice and style | simon-voice/style-guide.md | 2026-05-01 |
| skill-zip-sync | skill | Pull latest skill ZIPs from Google Drive into repo, commit, push, clean up Drive | Manual run; weekly sync cadence | Google Drive ZIPs matching `skill-name_YYYYMMDD-HHMM.zip` | Updated skill files in .claude/skills/; git commits; .last_sync timestamps | Google Drive MCP; git | 2026-05-01 |
| start-chat | skill | Start the Claude Code Chat UI server on port 7860 | `/start-chat` command | None | Running server at localhost:7860 | chat_ui/server.py | 2026-05-01 |
| tgg-301-mapper | skill | Map dead TGG URLs to valid redirect destinations using Simon's 4 redirect rules | "301s", "redirects", "URL mapping", "process redirects"; url_mappings CSV provided | url_mappings.csv + data/sitemap_audit_latest.csv; optional Products.csv | Shopify-ready redirect import file + review queue CSV | tools/tgg_301_mapper.py; data/sitemap_audit_latest.csv | 2026-05-01 |
| tgg-category-pipeline | skill | Full category page content pipeline: EAV, keywords, PLP copy, FAQ, metadata, links in sequence | `/tgg-category-pipeline [URL or slug]`; "build or rebuild a category page" | URL or slug + optional context | Assembled build file at seo/outputs/[slug]-build-[date].md + all step output files | seo-team-lead; eav-researcher; seo-keyword-researcher; plp-copywriter; faq-writer; metadata-writer; internal-linking-agent | 2026-05-01 |
| tgg-ce-batch | skill | Run CE pipeline across a CSV of jobs in parallel using subagents | `/batch input=<csv> [type=<type>] [concurrency=N]` | Validated CSV: keyword, slug, content_type, angle, byline | Batch report + per-row run folders in runs/ | tgg-ce-researcher (agent); tgg-ce-drafter (agent); scripts/batch_runner.py; scripts/csv_validator.py | 2026-05-01 |
| tgg-ce-brief | skill | CE Stage 4: consolidate intake + SEO data + competitor extracts into production brief | Called by tgg-content-pipeline at Stage 4 | runs/[run-id]/intake.md, seo-data.md, competitive-extract.md, existing-content.md | runs/[run-id]/brief.md | tgg-content-strategist (BROKEN — skill removed); tgg-template-generator; verification-gate-protocol | 2026-05-01 |
| tgg-ce-competitor-extract | skill | CE Stage 3 part 1: fetch and parse competitor page structure and content gaps | Called by tgg-content-pipeline at Stage 3 | runs/[run-id]/intake.md | runs/[run-id]/competitive-extract.md + existing-content.md | tgg-seo-specialist (BROKEN — no SKILL.md); scripts/extract_competitors.py; tgg-contentful-linker | 2026-05-01 |
| tgg-ce-draft | skill | CE Stage 6: produce full article draft (body + FAQ block) | Called by tgg-content-pipeline at Stage 6 | runs/[run-id]/brief.md, outline.md, seo-data.md, competitive-extract.md | runs/[run-id]/draft.md | tgg-content-strategist (BROKEN); tgg-copywriting (BROKEN) | 2026-05-01 |
| tgg-ce-finalise | skill | CE Stage 9: assemble production package (final.md, metadata, FAQ schema, internal links) | Called by tgg-content-pipeline at Stage 9 | runs/[run-id]/humanised-draft.md, intake.md, qa-report.md | runs/[run-id]/final.md, metadata.md, faq.json, internal-links.md | tgg-contentful-linker; tgg-copywriting (BROKEN); simon-voice | 2026-05-01 |
| tgg-ce-outline | skill | CE Stage 5: generate and validate article outline (H2 count gate) | Called by tgg-content-pipeline at Stage 5 | runs/[run-id]/brief.md | runs/[run-id]/outline.md (validated) | tgg-content-strategist (BROKEN) | 2026-05-01 |
| tgg-ce-qa | skill | CE Stage 7: validate draft against constraint YAML; block if any constraint fails | Called by tgg-content-pipeline at Stage 7 | runs/[run-id]/draft.md, intake.md; .claude/skills/verification-gate-protocol/constraints/*.yaml | runs/[run-id]/qa-report.md (PASS/FAIL table + block_delivery flag) | verification-gate-protocol; tgg-seo-specialist (BROKEN) | 2026-05-01 |
| tgg-ce-research | skill | CE Stage 2: assemble SEO and analytics research bundle for one pipeline run | Called by tgg-content-pipeline at Stage 2 | runs/[run-id]/intake.md | runs/[run-id]/seo-data.md | tgg-marketing-analyst; scripts/run_research.py | 2026-05-01 |
| tgg-chart-creator | skill | Create and inject styled matplotlib charts into the TGG monthly SEO deck | "Rebuild the charts", "update the chart data", "inject into the deck" for monthly PPTX | Raw data (GA4/GSC/GMC metrics) | Styled .png charts + PPTX injection at correct slide coordinates | tgg-pptx-style (design tokens); chart-templates.py | 2026-05-01 |
| tgg-content-pipeline | skill | CE orchestrator: runs full 9-stage content pipeline for one long-form article | `/run keyword="..." type=... slug=... angle="..."` | Intake fields: keyword, content_type, slug, angle, byline | All 9 stage artefacts in runs/[run-id]/ + committed output | tgg-ce-research; tgg-ce-competitor-extract; tgg-ce-brief; tgg-ce-outline; tgg-ce-draft; tgg-ce-qa; tgg-humanizer; tgg-ce-finalise; tgg-session-anchor; tgg-repo-manager; tgg-prompt-architect | 2026-05-01 |
| tgg-contentful-linker | skill | Resolve TGG URLs/slugs to Contentful entry links | Whenever a Contentful link is needed in content work; "find the Contentful entry for" | TGG URL, slug, or page name | Contentful entry URL (https://app.contentful.com/spaces/zbzrcwjtokv7/environments/master/entries/{id}) | references/entries.json (3,666 entries, exported 29 April 2026) | 2026-05-01 |
| tgg-conversation-indexer | skill | Weekly conversation indexer: scores significance, updates master index, flags abandoned projects | "Run tgg-conversation-indexer", "what have I left unfinished"; weekly cadence | Google Drive files (5 hardcoded names) + recent conversations | Updated Drive index files + abandoned projects todo | Google Drive MCP; skill-zip-sync (filename pattern dependency) | 2026-05-01 |
| tgg-humanizer | skill | Remove 29 AI writing patterns from any TGG content or business writing | After generating any AI text; "humanize", "de-AI", "make this sound less AI-generated" | Draft text of any type | Revised text with AI patterns removed + brief change log | None (standalone) | 2026-05-01 |
| tgg-marketing-analyst | skill | Organic search analytics: GSC/GA4 interpretation, YoY/MoM trends, traffic risk analysis | GSC/GA4 analysis tasks; performance slides for decks; Semrush category insights | GSC exports, GA4 data, Semrush data, or screenshots | Performance analysis, trend narrative, traffic concentration risk flags | None (standalone; uses provided data) | 2026-05-01 |
| tgg-monthly-seo-report | skill | Build monthly SEO update: deck narrative, stakeholder email, focus/outcomes table | "Prep the [month] report", "build the monthly SEO update" | GA4, GSC/Semrush, Profound, GMC data; Simon's Focus & Outcomes input | Slide deck narrative + stakeholder send-out email + QA-checked data | tgg-marketing-analyst (analytics layer); external research (algorithm updates) | 2026-05-01 |
| tgg-pptx-style | skill | Apply TGG SEO deck visual style to PPTX (colours, layouts, component specs) | "Build the deck", "add a slide", "update the presentation"; any TGG .pptx work | Existing .pptx or new slide content | Correctly styled .pptx matching TGG Jan-Mar 26 deck system | Public pptx skill (Anthropic); design-tokens.md; components.md; slide-recipes.md | 2026-05-01 |
| tgg-prompt-architect | skill | Silent pre-processor: triages and restructures every deliverable prompt before execution | Auto-fires on any message >5 words or containing a deliverable verb; silent | Any user message | Restructured prompt (Claude 4.x contract format) or unchanged message if skip conditions met | References 15 other TGG skills by name | 2026-05-01 |
| tgg-repo-manager | skill | Repo and documentation management: commit messages, PR descriptions, CLAUDE.md, process file updates | Commit/PR drafting; documentation work; "update the CLAUDE.md" | Changed files or documentation context | Commit message, PR description, or updated docs | None (standalone) | 2026-05-01 |
| tgg-seo | skill | Single source of truth for all TGG SEO work: copy production, strategy, technical SEO | Any SEO request for TGG; triggers listed in description; replaces tgg-copywriting, tgg-content-strategist, tgg-seo-specialist | Any SEO task (copy, audit, schema, linking, keyword research, AEO) | Varies by mode: PLP copy, metadata, FAQ, audit findings, schema, briefs | None — self-contained with all process rules embedded | 2026-05-01 |
| tgg-seo-specialist | STUB | Deprecated — no SKILL.md exists. Directory contains only `.last_sync` (2026-04-30). | Should not fire (no SKILL.md) | N/A | N/A | N/A | 2026-04-30 (last_sync) |
| tgg-session-anchor | skill | Session focus management: surfaces abandoned projects, locks session intent, watches for scope drift | Start of any substantive new chat; "what should I work on", "where was I" | docs/active_sprint.md + Drive all-time index | 2–3 abandoned high-upside projects + session intent prompt | tgg-conversation-indexer output; Drive files | 2026-05-01 |
| tgg-template-generator | skill | Generate blank-slate scaffolding for new repeatable SEO structures | "Generate a template", "scaffold a new document structure" when no existing pattern exists | Content type or task description | Blank template with TGG-realistic placeholders | None — standalone | 2026-05-01 |
| verification-gate-protocol | skill | Self-auditing constraint gates for tasks with 5+ constraints or batch processing | 5+ constraint tasks; batch processing (10+ outputs); quantified scope; "check everything" | Task description + constraint definitions | Phase 1/2/3 validation reports; PASS/FAIL per constraint; stop signals | .claude/skills/verification-gate-protocol/constraints/*.yaml | 2026-05-01 |

---

## Step 2 — Gaps, Overlaps, and Dead Weight

### Overlaps

**1. Two content pipeline orchestrators: `tgg-category-pipeline` and `tgg-content-pipeline`.**

These are not competing — they serve different content types:
- `tgg-category-pipeline` builds category PLP pages (PLP intro, FAQ, metadata, internal links).
- `tgg-content-pipeline` builds long-form editorial content (buying guides, how-tos, comparisons, EAV explainers).

For buying guides on category topics (e.g. "best robot vacuums"), both pipelines are plausible entry points. The distinction is not obvious from trigger descriptions.

Recommendation: keep both. Add a routing note to each description: "For PLP-style category page copy, use tgg-category-pipeline. For long-form buying guides, use tgg-content-pipeline."

---

**2. `seo-team-lead` (agent) and `tgg-content-pipeline` (skill) both orchestrate.**

`seo-team-lead` routes to specialist agents (plp-copywriter, faq-writer, metadata-writer, etc.). `tgg-content-pipeline` orchestrates CE stage skills. These serve different workstreams and do not overlap in execution, but both can be invoked for "write a buying guide for [category]." The team lead would delegate to agents; the content pipeline skill would run the CE stages.

Recommendation: keep both. Add to `seo-team-lead`'s routing rules: "For long-form editorial content (buying guides, how-tos), invoke `tgg-content-pipeline` rather than delegating to individual copy agents."

---

**3. `seo-content-auditor` (agent) and `tgg-seo` (skill, technical mode) both do SEO audits.**

`seo-content-auditor` audits repo content files (process files, markdown outputs). `tgg-seo` in technical mode audits live pages, schema, and AEO. These are not duplicates — the auditor is repo-scoped, tgg-seo is site-scoped.

Recommendation: keep both. Clarify in `seo-content-auditor` description: "Audits files in this repo only — not live pages."

---

**4. Broken delegation chain in CE pipeline skills.**

`tgg-ce-brief`, `tgg-ce-outline`, `tgg-ce-draft`, `tgg-ce-qa`, `tgg-ce-competitor-extract`, `tgg-ce-finalise`, and `tgg-content-pipeline` all delegate to `tgg-content-strategist`, `tgg-copywriting`, and/or `tgg-seo-specialist` by name. These three skills no longer have SKILL.md files — they were merged into `tgg-seo` on 2026-05-01.

**This is a live breakage.** Any pipeline run that reaches Stage 3, 4, 5, 6, 7, or 9 will fail silently because it will call a skill name that does not resolve.

Also broken in `docs/content-engineering-charter.md`, which lists the old skill names in the system map.

Recommendation: update all 7 CE stage skills and the charter to replace:
- `tgg-content-strategist` with `tgg-seo` (strategy mode)
- `tgg-copywriting` with `tgg-seo` (production mode)
- `tgg-seo-specialist` with `tgg-seo` (technical mode)

---

### Gaps

Cross-referencing active projects listed in CLAUDE.md against current agent/skill coverage:

| Active project | Current coverage | Gap |
|---|---|---|
| EOFY 2026 strategy + execution | tgg-seo (strategy mode), tgg-marketing-analyst, tgg-category-pipeline | No seasonal/campaign page specialist. Requires manual orchestration: keyword research, hub page brief, category page builds, internal linking. A dedicated `tgg-campaign-builder` skill would run this sequence automatically. |
| EOFY blog briefs and interlinking | tgg-content-pipeline, internal-linking-agent | Covered. The content pipeline handles buying guides; internal-linking-agent handles link injection. |
| Monthly SEO update deck | tgg-monthly-seo-report, tgg-chart-creator, tgg-pptx-style | Covered. |
| AI content/review schema | tgg-seo (technical mode) | No dedicated schema writer/validator agent. Schema work is buried inside tgg-seo technical mode with no structured output format. A `tgg-schema-writer` agent or extension to tgg-ce-finalise would help. Needs Simon input on scope. |
| Content cluster inlink injection (computing PDPs) | internal-linking-agent, inlink-migrator | Covered but requires manual URL list supply. No batch inlink injection pipeline for PDPs at scale. |
| PDP descriptions at scale | No direct coverage | No PDP description agent or skill. tgg-seo can write PDP copy but has no batch pipeline. `tgg-ce-batch` with a new `pdp-description` content type would fill this. Effort: M, Impact: high (active project, at scale). |
| Drive ↔ GitHub sync | skill-zip-sync | Covered. |
| Profound prompt management | ai-visibility-analyst (partial) | ai-visibility-analyst converts data to poll questions but does not manage Profound prompt templates, test cadences, or response parsing. No dedicated Profound management tool. Needs Simon input on what "management" means here. |
| AEO blog summary bullet rollout | aeo-optimizer, content-analyst | Covered. aeo-optimizer + content-analyst covers the AEO audit and suggestion layer. |
| IntentGaps tool build (blocked) | No coverage | This is a dev/scripting project, not an SEO content task. No code agent in the setup. Needs a Python scripting agent or GitHub Actions job. |

---

### Dead Weight

**1. `tgg-seo-specialist` stub directory.**
Contains only `.last_sync` (2026-04-30). No SKILL.md. This directory exists because skill-zip-sync wrote it during the merge transition. It should be deleted. If left, it risks silent no-ops when any CE pipeline stage tries to call it.

**2. `tgg-content-pipeline` SKILL.md references to deprecated skills.**
`tgg-content-pipeline` (the orchestrator) still lists `tgg-content-strategist`, `tgg-copywriting`, and `tgg-seo-specialist` in its delegation table. These are not just stale references — any pipeline run that delegates to these names will fail. This is dead configuration, not dead weight in the "unused" sense, but it is actively harmful.

**3. `check-github` polls a shell script that may not exist in all environments.**
`check-github` calls `bash scripts/github-poll.sh` and `bash scripts/github-post-comment.sh`. If these scripts are not present (e.g. in a fresh clone), the skill silently fails. No validation step. Low priority if Simon is the only user, but worth noting.

**4. Agents with narrow trigger conditions and limited recent use.**
The following agents are active and correct but appear underutilised based on the all-time conversation index (which shows skills-based usage from Claude.ai, not Claude Code agent usage):
- `ai-visibility-analyst` — requires Profound data to be manually supplied. If Profound is not part of the regular workflow, this agent sits idle. Needs Simon input: is Profound data being pulled regularly?
- `seo-content-auditor` — audits repo files only. Useful for process file QA but not part of any automated pipeline. No trigger in the category or content pipelines.

---

## Step 3 — Research: New Agent Patterns

Web research was conducted on best-in-class Claude Code multi-agent setups and content engineering patterns. Key findings below.

### Ryan Law — Content Engineering with Claude Code (Ahrefs)

Source: https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/

Ryan Law's system at Ahrefs uses 19 skills in a chain. Key structural patterns:

- **Separation of pipeline stages into independent skills.** Each stage (research, brief, outline, draft, humanise) is a separate skill file. This mirrors the TGG CE pipeline design. His pipeline has more research stages (5 vs TGG's 2).
- **Hooks for automatic humaniser application.** Law uses a `PostToolUse` hook to automatically run the humaniser after every draft. TGG calls tgg-humanizer explicitly at Stage 8; Law's approach removes the manual trigger and reduces skipped humanising.
- **No orchestrator agent — slash commands are the orchestrator.** Law uses `/run` as the entry point with the pipeline stage skills wired into a linear chain. TGG's tgg-content-pipeline (skill) mirrors this pattern. The difference is TGG also has a seo-team-lead agent for ad-hoc tasks; Law's setup is pipeline-first.
- **One "mega-skill" for voice + quality.** Law's humaniser and voice skill are combined. TGG splits these into tgg-humanizer (pattern removal) and simon-voice (ghost-writing), which is more modular and correct for a team context where different bylines apply.
- **Verification gates are inline, not a separate skill.** Law checks constraints within each stage skill rather than delegating to a gate protocol. TGG's verification-gate-protocol is more reusable and explicit — preferable for a multi-pipeline setup.

Patterns worth adopting from Law's system:
1. **PostToolUse hook for tgg-humanizer.** Automatically call it after any Write or agent output that matches tgg content patterns. This prevents forgetting to humanise.
2. **Persistent run state in a single YAML/JSON.** Law tracks every stage completion in a single manifest. TGG uses `pipeline-status.md`; a structured YAML would make resume logic more reliable.
3. **Explicit word count + entity density targets in the brief.** Law specifies these numerically in the brief, not just the outline. TGG's briefs have word budgets in the outline but not entity targets.

### Multi-domain Claude Code patterns

Research findings on public GitHub repos and documented setups:

**Pattern 1: Separation of orchestrator vs specialist agents (confirmed best practice).**
Multiple documented setups (Anthropic's own cookbook, company engineering blogs) confirm that the two-tier pattern — one orchestrator that routes + specialist agents that execute — is the dominant pattern for multi-domain work. TGG implements this correctly with seo-team-lead + specialists.

**Pattern 2: Tool-scoped agents.**
Best-in-class setups restrict each agent's tool access to only what it needs. TGG already does this (eav-researcher has no Write tool; metadata-writer has Write but no Semrush; etc.). This is a strength of the current setup.

**Pattern 3: CLAUDE.md as routing memory, not just documentation.**
High-performing setups use CLAUDE.md to encode routing rules ("when someone asks about X, use agent Y"). TGG's CLAUDE.md does this for the standard workflows. The routing table in CLAUDE.md is TGG's equivalent. One gap: the CLAUDE.md routing table does not reflect the CE pipeline (tgg-content-pipeline), only the category pipeline.

**Pattern 4: Agent descriptions as trigger classifiers.**
The description field in agent markdown files is the primary signal Claude uses to select an agent. Best practice is to write descriptions as if they are classifiers: specific trigger phrases, explicit exclusions, and a single sentence about what the agent does. TGG's agent descriptions are well-written. The skills have more variability — tgg-prompt-architect's description is the strongest; tgg-template-generator's is the weakest.

**Pattern 5: Separate research and writing agents.**
Keeping Semrush/data tools out of content-writing agents (and vice versa) reduces context contamination and keeps agents fast. TGG implements this correctly — eav-researcher and seo-keyword-researcher hold the data tools; plp-copywriter and faq-writer hold only Read/ctx tools.

### Public repos with strong `.claude/` structures

Research note: public GitHub repos with production-level `.claude/agents/` directories are rare as of early 2026. Most published examples are demos or small setups. The three most relevant found:

**1. Anthropic Cookbook (github.com/anthropics/anthropic-cookbook).**
Examples of agent chains with tool-scoped subagents. No multi-domain SEO setup. Main contribution: confirms that `maxTurns` and `memory: project` on specialist agents reduce token waste. TGG uses both.

**2. ryanlawcontent/claude-content-engineering (referenced in Law's Ahrefs article).**
The patterns described in the Ahrefs article are the public reference point. The repo structure as described features: skills as pipeline stages, slash commands as orchestrator, hooks for auto-humanising. TGG's CE pipeline closely mirrors this — the main gap is the hooks layer.

**3. General ecommerce SEO Claude Code setups (no public repos of comparable scale found).**
Research found no public ecommerce SEO agent setups at TGG's level of specificity (process files, EAV mapping, Semrush integration, Contentful linking). TGG's setup is, by the available evidence, at the leading edge of this category. The most comparable public reference is Law's content engineering system, which TGG has already implemented and extended.

Research limitation: GitHub search for `.claude/agents` SEO-specific public repos returned demo repositories and small personal setups, none matching the complexity of TGG's current system. This section should be treated as "best available public reference, not comprehensive survey."

---

## Step 4 — Recommendations

### 1. Consolidate

| Target action | Target name | Merged scope | Effort | Impact |
|---|---|---|---|---|
| Update all 7 CE pipeline skills + content-engineering-charter.md to replace `tgg-content-strategist`, `tgg-copywriting`, `tgg-seo-specialist` with `tgg-seo` | CE pipeline skills (no rename) | tgg-ce-brief, tgg-ce-outline, tgg-ce-draft, tgg-ce-qa, tgg-ce-competitor-extract, tgg-ce-finalise, tgg-content-pipeline each updated to call `tgg-seo` with the correct mode flag | S | **HIGH — this is a live breakage. CE pipeline cannot run until fixed.** |
| Delete `tgg-seo-specialist` stub directory | (delete, no target) | Remove `.claude/skills/tgg-seo-specialist/` entirely. No SKILL.md; risks silent call failures | S | med |
| Add CE pipeline routing to `seo-team-lead` | seo-team-lead | When task is "write a buying guide for X", team lead should invoke `tgg-content-pipeline` skill rather than individual plp-copywriter + faq-writer agents | S | med |
| Clarify `tgg-category-pipeline` vs `tgg-content-pipeline` distinction in descriptions | both skills | Add a routing note: "For category PLP copy, use tgg-category-pipeline. For long-form editorial, use tgg-content-pipeline." | S | med |

### 2. Add

| Name | Purpose | Trigger | Reason | Effort | Impact |
|---|---|---|---|---|---|
| `tgg-campaign-builder` skill | Orchestrate seasonal/campaign page builds (EOFY, BFCM, seasonal sales) end-to-end: hub strategy, keyword brief, category page builds, internal linking, metadata | "EOFY", "campaign pages", "seasonal strategy", "build the [sale] landing pages" | Active project: EOFY 2026 execution is the most urgent open workstream. Currently requires manual 6-step orchestration. BFCM 2025 failure (−41% organic) was partly a URL strategy problem — a dedicated builder would encode the hub-vs-category decision rules. | M | **high** |
| `pdp-description` content type in `tgg-ce-batch` | Write PDP descriptions at scale via CE batch pipeline. New content_type: `pdp-description`. Micro-pipeline (no research): brief from GMC product data → tgg-seo production mode → tgg-humanizer → QA | `/batch input=... type=pdp-description` | Active project: "PDP descriptions at scale". tgg-seo can write individual PDP descriptions but there is no batch path. CE batch already handles plp-intro and faq-block micro-pipelines — this is the same pattern applied to PDPs. | M | **high** |
| `tgg-schema-writer` agent | Write and validate JSON-LD schema (FAQPage, Product, HowTo, Review) for TGG pages. Standalone schema blocks ready for Contentful or Shopify injection. | "Schema for [page/type]", "write FAQPage schema for", "AI content schema" | Active project: AI content/review schema. Currently schema writing is buried in tgg-seo technical mode with no structured output. A dedicated agent would produce schema-ready JSON-LD blocks, validate against schema.org, and flag errors before CMS injection. | M | high |
| PostToolUse hook: auto-humaniser | Automatically call tgg-humanizer after any Write tool call that produces `.md` files to `seo/outputs/` or `runs/` | Automatic (hook-based, not triggered by user) | Ryan Law's system uses this pattern. TGG currently requires explicit calls to tgg-humanizer (Step 8 in pipeline). A hook would eliminate skipped humanising in ad-hoc tasks outside the CE pipeline. Wire as a PostToolUse hook in `.claude/hooks/` | S | med |
| `tgg-skills-registry` auto-generated index | Auto-generate `.claude/docs/skills-index.md` listing all skills with one-line purpose, dependencies, and fire conditions. Run on commit or on demand via skill-zip-sync | Triggered by skill-zip-sync at end of each sync, or manually | The prior audit (`TGG_Skills_Audit_2026-05-01.md`) identified the absence of a live skills registry as a maintenance risk. This document you are reading is that registry for now, but it will age immediately. An auto-generated version stays current. | S | med |
| `tgg-profound-agent` skill | Manage Profound prompt library: create/update prompt templates, schedule prompt tests, parse response data, export visibility trends to Drive | "Profound prompt", "update the prompt library", "run Profound analysis" | Active project: Profound prompt management. ai-visibility-analyst converts Profound data to poll questions but does not manage the prompt layer. Profound's agent workflow was built in a past session (PROFOUND AGENT BUILDER, completed March 26) but a Claude Code skill for ongoing management is not present. **Needs Simon input on current Profound API access and what management means.** | M | med |

### 3. Delete

| Name | Reason | Effort | Impact |
|---|---|---|---|
| `tgg-seo-specialist` directory | Empty stub (no SKILL.md). Only `.last_sync` from 2026-04-30. Risks silent failures when CE pipeline calls it. No use case since skills were merged. | S | med |
| Broken references to `tgg-content-strategist`, `tgg-copywriting`, `tgg-seo-specialist` in CE pipeline skills | These references are broken (skills removed). Must be replaced with `tgg-seo`, not just deleted. See Consolidate #1. | S | **HIGH** |

---

## Deprecation Status Confirmation

**tgg-copywriting:** Removed from repo (directory absent). ABSENT.
**tgg-content-strategist:** Removed from repo (directory absent). ABSENT.
**tgg-seo-specialist:** Directory present but no SKILL.md. STUB ONLY. Delete the directory.
**tgg-seo:** Active. Created 2026-05-01. Replaces all three. LIVE.

The merge has happened in the repo. The merge has NOT propagated to the 7 CE pipeline skills or the content-engineering-charter.md that reference the old names. This is the most urgent fix in this audit.

---

## Summary Table — Priority-Ordered Action List

| Priority | Action | Type | Effort | Impact | Blocks |
|---|---|---|---|---|---|
| 1 | Update tgg-ce-brief, tgg-ce-outline, tgg-ce-draft, tgg-ce-qa, tgg-ce-competitor-extract, tgg-ce-finalise, tgg-content-pipeline to call `tgg-seo` instead of deprecated skill names | Fix | S | HIGH | CE pipeline cannot run until done |
| 2 | Update content-engineering-charter.md with corrected delegation map | Fix | S | HIGH | Charter is the canonical reference |
| 3 | Delete .claude/skills/tgg-seo-specialist/ directory | Fix | S | med | Silent failures if any code calls it |
| 4 | Add tgg-campaign-builder skill for seasonal campaign orchestration | Add | M | HIGH | EOFY 2026 execution |
| 5 | Add pdp-description content type to tgg-ce-batch micro-pipeline | Add | M | HIGH | PDP descriptions at scale project |
| 6 | Add tgg-schema-writer agent for JSON-LD schema production | Add | M | high | AI content/review schema project |
| 7 | Add PostToolUse hook for auto-humaniser on seo/outputs/ writes | Add | S | med | Quality consistency outside CE pipeline |
| 8 | Add tgg-skills-registry auto-generation to skill-zip-sync | Add | S | med | Maintenance visibility |
| 9 | Add CE pipeline routing rule to seo-team-lead | Fix | S | med | Routing accuracy |
| 10 | Add routing clarity notes to tgg-category-pipeline and tgg-content-pipeline | Fix | S | med | Reduces misrouting |
| 11 | Add tgg-profound-agent skill (needs Simon input first) | Add | M | med | Profound management project |

---

## Research Gaps

The following items could not be verified from available data and require Simon's input:

- **Actual Claude Code agent usage rates** — the all-time conversation index covers Claude.ai skill usage (11 March to 29 April 2026) but does not track individual agent calls from Claude Code sessions. Usage rates for agents like `ai-visibility-analyst`, `seo-content-auditor`, and `inlink-migrator` are estimated from pipeline descriptions, not observed call counts.
- **Profound API access** — the tgg-profound-agent recommendation depends on whether current Profound access allows API-level prompt management. Needs Simon input.
- **Referenced chat ff0a86b9** — the subagent research task launched in conversation ff0a86b9-30b2-40fd-ad49-a7621d123886 was noted as never returning output. No artefact from this conversation was found in the repo or Drive files checked. Treat its findings as pending.
- **Public GitHub repos with comparable .claude/ structures** — no public ecommerce SEO agent setups at TGG's scale were found. TGG appears to be at the leading edge. Ryan Law's system (Ahrefs) is the best public reference.

---

*Audited 2 May 2026. Update this file when agent or skill inventory changes.*
