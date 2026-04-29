# CLAUDE.md

This file provides guidance to AI assistants working in this repository.

---

## Who this is for

Simon Mannheimer — SEO Lead, The Good Guys (thegoodguys.com.au), Melbourne.
Daily work: batch copy production, technical SEO audits, Python/JS scripting, GMC feed work, Semrush reporting, stakeholder decks, monthly SEO reports, internal linking audits, schema, AI visibility tracking.

---

## Repository Overview

Central Claude Code workspace containing:
- GTMetrix MCP server (Python/uv) — `main.py` + `gtmetrix_client.py`
- Context Mode MCP server (token-efficient sessions) — `context_mode/server.py`
- 14-agent SEO team (seo-team-lead orchestrates all)
- 10 numbered process files (`00-*.md` … `09-*.md`) at the **repo root** governing all TGG copy and SEO work
- Local Python tools in `tools/` for PLP auditing, MHTML parsing, CSV manipulation
- Repo-level shell/Python helpers in `scripts/` (GitHub polling, task processor, loop daemon)
- Chat UI server in `chat_ui/` (port 7860, started by `/start-chat`)
- GitHub Actions workflows for on-demand and scheduled SEO tasks
- Optional tools staged in `.claude/optional/` — inactive until needed
- Working directories: `seo/` (briefs, prompts, outputs, scripts), `docs/` (internal documentation), `gtmetrix_results/` (persisted audit JSON/CSV)

**Setup:**
- Language: Python 3.11 / Package manager: uv
- Install: `uv sync`
- Run GTMetrix MCP: `uv run python3 main.py`
- Run Context Mode MCP: `uv run python3 context_mode/server.py`
- All MCP paths use `.` (repo root) — portable across machines and GitHub Actions

---

## Repo Layout

Quick reference so agents can locate things without `ls`.

| Path | Purpose |
|------|---------|
| `main.py` | GTMetrix MCP server entry point |
| `gtmetrix_client.py` | GTMetrix API client used by `main.py` |
| `config.py` | Shared config loader (env vars) |
| `plp-qa-audit.py` | PLP QA audit runner (root-level) |
| `run_audit_ci.py` | Audit runner invoked by GitHub Actions |
| `00-*.md` … `09-*.md` | Process files governing all TGG copy work |
| `context_mode/` | Context Mode MCP server (`server.py`) |
| `chat_ui/` | Chat UI server (port 7860, started by `/start-chat`) |
| `tools/` | Local Python utilities (PLP audit, MHTML, CSV ops) |
| `scripts/` | Repo-level helpers: `github-poll.sh`, `github-post-comment.sh`, `loop-daemon.sh`, `process-tasks.py` |
| `seo/` | Briefs, prompts, outputs, scripts for SEO workflows |
| `docs/` | Internal documentation (archive, drafts, all-time conversation index) |
| `gtmetrix_results/` | Persisted GTMetrix audit JSON/CSV |
| `.claude/agents/` | 14 SEO agent definitions |
| `.claude/skills/` | 4 slash skills |
| `.claude/hooks/` | 3 active hooks |
| `.claude/optional/` | 6 staged optional tools (inactive) |
| `.github/workflows/` | 6 GitHub Actions workflows |

---

## Optional Tool Activation — IMPORTANT

Several powerful tools are staged but inactive. When a task comes in that one of these would meaningfully improve, **offer it before proceeding**.

Use this exact pattern:
> "I could activate **[tool]** to help with this — it would let me [specific benefit]. Want me to set it up? Setup takes [X minutes] and is documented in `.claude/optional/[tool]/SETUP.md`."

Then wait for confirmation. Do not activate anything without explicit approval.

### Trigger map

| Task type | Offer this tool |
|-----------|----------------|
| Complex multi-step task, batch job, deck build, audit pipeline, anything likely to involve 5+ steps | **Superpowers plugin** — enforces plan-before-execute, prevents runaway iteration |
| GSC data, query analysis, CTR by position, ranking opportunities, non-brand performance | **GSC MCP** — pull query data directly, no CSV export needed |
| Email drafting in context, calendar check, reading/writing Sheets, Slides updates | **Google Workspace MCP** — Gmail, Calendar, Sheets, Slides from Claude Code |
| Sprint tracking, task status, what's in-flight, creating tickets | **Linear MCP** — project management connected to Claude Code |
| End-of-week review, goal tracking, what did I work on, career reflection, session learning | **Obsidian PKM** — weekly reviews and goal alignment in a local vault |
| Schema audit, GEO/AEO content scoring, backlink gap analysis, E-E-A-T scoring, AI Overview optimisation | **claude-seo skill suite** — 19 sub-skills, deeper than current aeo-optimizer agent |

### Already active (no offer needed)
- Semrush MCP — keyword, competitor, backlink data
- Firecrawl MCP — live page scraping, competitor crawls, sitemap pulls
- Airtable MCP — base appS4NfrOth5cVo7P tracker tables
- GTMetrix MCP — performance audits
- Context Mode MCP — token-efficient context indexing
- Google Drive — file access

---

## Git Workflow

### Branch naming
Each Claude Code session is assigned a branch: `claude/<feature-name>-<session-id>`. Always push to the branch specified in the session system prompt. Never push directly to `main`.

### Commits
Imperative mood. `Add user authentication module` not `stuff`. Sign with SSH. Keep commits focused.

### Pushing
```bash
git push -u origin <branch-name>
```
Retry with exponential backoff (2s, 4s, 8s, 16s) on network errors. HTTP 403 = wrong branch, do not retry.

### Pull Requests and Merging

After pushing, use this rule to decide whether to create and merge a PR automatically:

- **Create and merge automatically** — when the task is clearly scoped, completed exactly as asked, and the change is low-risk (docs, config, copy, refactors with no functional side-effects).
- **Create PR and ask before merging** — when the change is experimental, architecturally significant, or there is any doubt about whether the output matches intent.
- **Never create a PR** — only if Simon explicitly says not to.

Use the GitHub MCP tools (`mcp__github__create_pull_request`, `mcp__github__merge_pull_request`) to create and merge. Default merge method: squash.

### Fetching / Pulling

Prefer fetching specific branches:

```bash
git fetch origin <branch-name>
git pull origin <branch-name>
```

Apply the same exponential backoff retry strategy on network failures.

---

## Context Mode (Token Efficiency — MANDATORY)

**Rules — follow in every session:**
1. Files over 50 lines: use `ctx_read_file` instead of Read
2. Large tool outputs over ~100 lines: pipe through `ctx_index(key, content)` immediately
3. Session start: run `ctx_list` to check what is already indexed
4. Never dump raw files into context when Context Mode tools are available

| Tool | Purpose |
|------|---------|
| `ctx_read_file(path)` | Index file; return section map |
| `ctx_index(key, content)` | Index arbitrary large text |
| `ctx_search(key, query)` | Retrieve matching sections only |
| `ctx_list()` | Show all indexed keys |
| `ctx_drop(key?)` | Remove from index |

---

## Permission Rules and Hooks

`settings.json` contains explicit `permissions.allow` and `permissions.deny` blocks. These eliminate the constant allow prompts in VS Code for routine operations.

**Pre-approved (no prompt):** uv, python3, node, npx, all git read/log operations, writes to seo/outputs, seo/briefs, docs, scripts, tools, .claude/skills.

**Always blocked:** `.env` reads, `curl`, `wget`, `rm -rf`, `git push --force`, writes to `.env`.

**Active hooks in `.claude/hooks/`:**
- `block_dangerous.py` — PreToolUse: blocks dangerous patterns before execution
- `log_writes.py` — PostToolUse: logs every file write to `.claude/write_log.txt`
- `session_log.py` — Stop: logs session end to `.claude/session_log.txt`

**Other config files in `.claude/`:**
- `mcp-actions.json` — declarative MCP action shortcuts referenced by tooling
- `settings.local.json.example` — template for activating optional MCP servers (GSC, Google Workspace, Linear). Copy to `settings.local.json` and fill in credentials when activating an optional tool.

---

## MCP Servers (Active)

| Server | Entry point | Purpose |
|--------|-------------|---------|
| `context-mode` | `context_mode/server.py` | Token-efficient context indexing |
| `gtmetrix` | `main.py` | GTMetrix performance audits |
| `semrush` | `npx semrush-mcp` | Keyword, competitor, backlink data (AU database) |
| `firecrawl` | `npx firecrawl-mcp` | Live page scraping, competitor crawls |
| `airtable` | `npx @domdomegg/airtable-mcp-server` | Base appS4NfrOth5cVo7P |

Optional MCP servers (inactive): see `.claude/optional/` for GSC, Google Workspace, Linear.

---

## SEO Agent Team

### Project defaults
```
TARGET_DOMAIN=thegoodguys.com.au
COMPETITORS_PRIMARY=jbhifi.com.au,harveynorman.com.au,officeworks.com.au
COMPETITORS_SECONDARY=kogan.com,appliancesonline.com.au
DEFAULT_DATABASE=au
SEMRUSH_DATABASE=au
```

### Chain of command
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

### How to invoke
```
Use the seo-team-lead to [task]
```
Or directly: `Use the plp-copywriter to write copy for /air-fryers`

### Standard workflows
- **Category Page Build:** `08 (EAV)` → `04 (Fanout)` → `01 (PLP Intro)` → `05 (FAQ Copy)` → `02 (Metadata)` → `06 (Linking)`
- **AEO Audit:** `04 (Summarise)` → `06 (Link Opportunities)` → `07 (AEO Suggestions)`
- **Internal Linking:** `06 (Find → Validate → Verify → Insert)`
- **Category Optimisation:** `08 (EAV)` → `04 (Fanout)` → `06 (Link Validation)` → `05 (Brand+Category FAQ)`

Always read `00-tov-language-reference.md` before any content task.

### Writing philosophy
- Guardrails not templates. Ban harmful patterns; don't prescribe "allowed" ones.
- Vary everything. Sentence openers, TGG placement, benefit angles.
- Be specific. Name brands, features, use cases.
- Sound human. If it reads like a chatbot, rewrite.

### Process updates
When Simon changes a rule, update the relevant process file immediately. Add changelog note at top (version + date + what changed). If a request conflicts with a process rule, flag it and ask: one-off exception or permanent change?

### `seo/` layout
- `seo/briefs/` — production briefs (e.g. `PLP-Batch-Production-Brief-2026-03-19.md`)
- `seo/prompts/` — reusable prompt templates: `competitor-audit.md`, `keyword-research.md`
- `seo/scripts/` — Python utilities: `fix-clone-openers.py`, `fix-critical-rows.py`, `generate-md-files.py`, `merge-plp-outputs.py`
- `seo/outputs/` — generated content (PLP intros, metadata batches, FAQ copy)

---

## Slash Skills

| Skill | What it does |
|-------|-------------|
| `check-github` | Poll GitHub Issues for @claude tasks, route to seo-team-lead, post replies |
| `start-chat` | Start Chat UI server on port 7860 |
| `tgg-conversation-indexer` | Weekly indexer — scans conversations, updates Google Drive index, flags abandoned projects |
| `tgg-repo-manager` | Commit messages, PR descriptions, CLAUDE.md entries, process file updates |

**Conversation Indexer:** Run weekly. Trigger: "run tgg-conversation-indexer" or "what have I left unfinished".

---

## Local Python Tools (`tools/`)

For local use on Windows/PowerShell or macOS. Not run in GitHub Actions.

| Script | Purpose |
|--------|---------|
| `tgg_plp_auditor.py` | Audits live TGG PLP pages against intro copy rules |
| `tgg_transcript_scraper.py` | Extracts YouTube transcripts in bulk |
| `mhtml_parser.py` | Parses browser-saved MHTML files for Claude ingestion |
| `mhtml_transformer.py` | Converts MHTML to self-contained .ai.html |
| `check_status.py` | Checks URL status codes from a CSV |
| `merge_and_split.py` | Merges/splits CSVs (Semrush keyword exports) |
| `split_csv.py` | Splits a large CSV into two halves |

Run from repo root: `python tools/tgg_plp_auditor.py`

A `tools/run.bat` Windows runner is included for double-click invocation on Windows.

**Note on paths:** Some scripts have hardcoded Windows paths. Update the path variables at the top for your machine.

---

## AI Assistant Guidelines

1. Read before modifying — always read existing files first
2. Minimise scope — only change what was explicitly requested
3. No over-engineering — no feature flags, backwards-compat shims, speculative abstractions
4. Prefer editing over creating
5. Confirm before: deleting files, force-pushing, destructive resets, modifying CI/CD

---

## GitHub Actions

**Note:** Claude Pro subscription does NOT include API access. GitHub Actions requires a separate key from console.anthropic.com.

| Workflow | Trigger | API key needed |
|----------|---------|---------------|
| `seo-weekly-report.yml` | Manual only (cron disabled) | Yes |
| `seo-on-demand.yml` | @claude in issues/PRs | Yes |
| `shopping-scraper.yml` | Manual only | Yes |
| `gtmetrix-audit.yml` | Manual only | Yes |
| `issue-receiver.yml` | Issue events | No |
| `plp-merge.yml` | Push to branch | No |

Required secrets: `ANTHROPIC_API_KEY`, `SEMRUSH_API_KEY`, `FIRECRAWL_API_KEY`.

---

## Remote

- Origin: `http://local_proxy@127.0.0.1:38487/git/simonmannheimer-tgg/Claude`

---

*Update this file when project structure, active tools, or conventions change.*
