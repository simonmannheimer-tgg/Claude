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
| `.claude/optional/` | Staged optional tools (most now active — see Trigger map) |
| `.github/workflows/` | GitHub Actions workflows |
| `.devcontainer/` | Codespaces config + shared setup script |
| `vault/` | Logseq PKM graph (markdown files, browser-edited via logseq.com) |

---

## Optional Tool Activation — IMPORTANT

Several powerful tools are staged but inactive. When a task comes in that one of these would meaningfully improve, **offer it before proceeding**.

Use this exact pattern:
> "I could activate **[tool]** to help with this — it would let me [specific benefit]. Want me to set it up? Setup takes [X minutes] and is documented in `.claude/optional/[tool]/SETUP.md`."

Then wait for confirmation. Do not activate anything without explicit approval.

### Trigger map

| Task type | Offer this tool |
|-----------|----------------|
| Sprint tracking, task status, what's in-flight, creating tickets | **Linear MCP** — project management connected to Claude Code |

### Already active (no offer needed)
- Semrush MCP — keyword, competitor, backlink data
- Firecrawl MCP — live page scraping, competitor crawls, sitemap pulls
- Airtable MCP — base appS4NfrOth5cVo7P tracker tables
- GTMetrix MCP — performance audits
- Context Mode MCP — token-efficient context indexing
- Google Drive — file access
- **Superpowers plugin** — enforces plan-before-execute on complex multi-step tasks
- **GSC MCP** (`gsc`) — Search Console queries, CTR, position data
- **Google Workspace MCP** (`google-workspace`) — Gmail, Calendar, Drive, Sheets, Slides
- **claude-seo plugin** — schema, GEO/AEO, backlink, E-E-A-T sub-skills (19 total)
- **Logseq vault** (filesystem MCP scoped to `vault/`) — daily notes, weekly reviews, goal tracking

---

## Where this runs (cloud-only)

This workspace is designed to run *without* a local Claude install. Three execution layers:

| Layer | What runs | Auth | When |
|-------|-----------|------|------|
| **Codespaces VM** | Full Claude Code session, all MCPs live | `claude login` once per Codespace (Pro/Max) | Long interactive sessions, audits |
| **Claude Code on the web** | Same MCPs, bootstrapped by SessionStart hook | Already logged in via claude.ai | Quick browser sessions |
| **GitHub Actions (non-AI batch)** | `vault-autocommit.yml`, `gsc-weekly-pull.yml`, scrapers | Service-specific API keys only | Scheduled jobs |

**No Anthropic API key.** Claude Code authenticates via Pro/Max OAuth, so anything that *invokes Claude in CI* won't run. The two existing AI-driven workflows (`seo-on-demand.yml`, `seo-weekly-report.yml`) already guard on `secrets.ANTHROPIC_API_KEY` being empty — they post a notice and exit green when no key is set.

**OAuth credentials** for GSC and Google Workspace are stored as base64-encoded GitHub secrets (`GSC_CREDENTIALS_JSON`, `GOOGLE_WORKSPACE_CREDENTIALS_JSON`) and materialised at session start by `.devcontainer/setup.sh` into `/tmp/creds/`. Run the OAuth flow once on a personal device, then save the credentials JSON as a secret.

**Bootstrap files:**
- `.devcontainer/devcontainer.json` — Codespaces image + features
- `.devcontainer/setup.sh` — installs MCPs, materialises credentials (reused by SessionStart hook)
- `.claude/hooks/session_start.sh` — wrapper for Claude Code on the web

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

## Conversation & Session Indexing

The Logseq vault under `vault/` is the long-memory layer. Every Claude
conversation (web/desktop) **and** every Claude Code session that touches this
repo is indexed into it as a tagged page, with a per-project MOC.

### Build script

```
python3 scripts/build_logseq_chat_index.py [export_dir] [vault_dir]
```

Inputs:
- `export_dir` — unzipped Anthropic conversation export
  (default `/tmp/chat-export`); contains `conversations.json` + `projects.json`.
- `vault_dir` — Logseq vault root (default `vault/`).

Outputs (writes to `vault/pages/`):
- `Chat___Light___<slug>.md` — short summary (1–2 paragraphs, 240-char excerpt)
- `Chat___Medium___<slug>.md` — user messages only, full text
- `Chat___Full___<slug>.md` — full transcript (human + assistant)
- `Chat___Code___<slug>.md` — Claude Code session (commits + files touched)
- `Projects___<project>.md` — per-project MOC listing every chat/session
- `Projects___Claude-Code.md` — master MOC of all Claude Code branches
- `Conversations Master Index.md` — by-status / by-project / by-topic index

### Tag taxonomy

Every page is tagged with all of: `#project/<slug>`, `#status/<active|completed|abandoned|tactical>`, `#topic/<keyword>` (one per detected topic), `#skill/<seo|development|reporting|...>`. Project tags use a 40-char slug; project MOC pages use the human-readable name as title.

### Convention: every Claude Code branch is a project

Each `claude/<feature>-<id>` branch the harness assigns is treated as its own project in the vault. The indexer extracts `claude.ai/code/session_<id>` URLs from commit messages, groups commits by session, infers the owning branch, and writes:
- one `Chat___Code___<slug>.md` per session (commits + files touched)
- one `Projects___<branch>.md` MOC per branch
- one row in `Projects___Claude-Code.md`

This means every piece of work that lands on a Claude Code branch is automatically discoverable from the vault, even though the underlying transcript lives on Anthropic's side and is not in the export.

### When to re-run

Re-run the build script:
- Whenever a fresh Anthropic conversation export is available (replaces `vault/pages/Chat___*.md` and `Projects___*.md`)
- After landing significant work on a Claude Code branch (picks up new commits + sessions)
- As part of the weekly `tgg-conversation-indexer` skill run

The script is idempotent — it deletes all `Chat___*.md` and `Projects___*.md` pages before regenerating, so manual edits to those files will be lost. Hand-written notes belong in journal pages (`vault/journals/`) or non-`Chat`/`Projects` pages.

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
6. **Vault hygiene** — after a substantive Claude Code session lands on a `claude/*` branch (i.e. before you create a PR or merge), re-run `python3 scripts/build_logseq_chat_index.py` so the new commits become a `Chat/Code/<slug>` page and the branch shows up in `Projects/Claude-Code`. Skip for trivial single-line fixes; required for any work that adds files or new functionality.

---

## GitHub Actions

**Note:** Claude Pro subscription does NOT include API access. GitHub Actions requires a separate key from console.anthropic.com.

| Workflow | Trigger | Anthropic API needed |
|----------|---------|---------------|
| `seo-weekly-report.yml` | Manual only (cron disabled) | Yes — guards on missing key, exits green |
| `seo-on-demand.yml` | @claude in issues/PRs | Yes — guards on missing key, exits green |
| `shopping-scraper.yml` | Manual only | Yes |
| `gtmetrix-audit.yml` | Manual only | No |
| `issue-receiver.yml` | Issue events | No |
| `plp-merge.yml` | Push to branch | No |
| `vault-autocommit.yml` | Daily 13:15 UTC + manual | No |
| `gsc-weekly-pull.yml` | Mondays 07:00 UTC + manual | No (needs `GSC_CREDENTIALS_JSON`) |

Required secrets: `SEMRUSH_API_KEY`, `FIRECRAWL_API_KEY`, `GSC_CREDENTIALS_JSON`, `GOOGLE_WORKSPACE_CREDENTIALS_JSON`. `ANTHROPIC_API_KEY` is optional — the AI-driven workflows skip cleanly when it's absent.

---

## Remote

- Origin: `http://local_proxy@127.0.0.1:38487/git/simonmannheimer-tgg/Claude`

---

*Update this file when project structure, active tools, or conventions change.*
