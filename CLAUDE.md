# CLAUDE.md

This file provides guidance to AI assistants working in this repository.

---

## Who this is for

Simon Mannheimer — SEO Lead, The Good Guys (thegoodguys.com.au), Melbourne.
Daily work: batch copy production, technical SEO audits, Python/JS scripting, GMC feed work, Semrush reporting, stakeholder decks, monthly SEO reports, internal linking audits, schema, AI visibility tracking.

---

## Repository Overview

Central Claude Code workspace containing:
- GTMetrix MCP server (Python/uv)
- Context Mode MCP server (token-efficient sessions)
- 14-agent SEO team (seo-team-lead orchestrates all)
- 10 numbered process files (00–09) governing all TGG copy and SEO work
- Local Python tools in `tools/` for PLP auditing, MHTML parsing, CSV manipulation
- GitHub Actions workflows for on-demand and scheduled SEO tasks
- Optional tools staged in `.claude/optional/` — inactive until needed

**Setup:**
- Language: Python 3.11 / Package manager: uv
- Install: `uv sync`
- Run GTMetrix MCP: `uv run python3 main.py`
- Run Context Mode MCP: `uv run python3 context_mode/server.py`
- All MCP paths use `.` (repo root) — portable across machines and GitHub Actions

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

| Workflow | Trigger | API key needed |
|----------|---------|---------------|
| `seo-weekly-report.yml` | Manual only (cron disabled) | Yes |
| `seo-on-demand.yml` | @claude in issues/PRs | Yes |
| `shopping-scraper.yml` | Manual only | Yes |
| `gtmetrix-audit.yml` | Manual only | Yes |
| `issue-receiver.yml` | Issue events | No |
| `plp-merge.yml` | Push to branch | No |
| `drive-skill-sync.yml` | Manual only — pull skill ZIPs from Drive | Yes |

Required secrets: `ANTHROPIC_API_KEY`, `SEMRUSH_API_KEY`, `FIRECRAWL_API_KEY`.

---

## Chat ↔ Code Sync Pipeline

Bridges Claude.ai chat sessions and this repo. Two directions:

### Skills: Chat → Code

When a chat session creates or updates a skill, package it as a ZIP and upload to Google Drive root using this naming convention:

```
skill-name_YYYYMMDD-HHMM.zip
```

Example: `tgg-copywriting_20260501-1430.zip`

The ZIP must contain a `SKILL.md` at the root and a `metadata.json` with:
```json
{
  "change": "Short description of what changed",
  "timestamp": "2026-05-01T14:30:00+00:00"
}
```

To pull all pending skill ZIPs into the repo:
- Run `skill-zip-sync` in a Claude Code session, or
- Trigger `drive-skill-sync.yml` from GitHub Actions (manual dispatch)

Processed ZIPs are logged to `.claude/skill-sync-cleanup.log` for manual Drive deletion (Drive delete not yet automated — activate Google Workspace MCP to enable).

### Conversations: Chat → Vault

When you have a fresh Anthropic conversation export:

1. Upload the ZIP to Google Drive as `claude-export_YYYYMMDD.zip`
2. Run locally: `python3 scripts/drive_conversation_sync.py --from-file /path/to/export.zip`
3. Vault pages regenerate automatically; `vault-autocommit.yml` commits them nightly

Or run the script without arguments for full usage instructions.

---

## Remote

- Origin: `http://local_proxy@127.0.0.1:38487/git/simonmannheimer-tgg/Claude`

---

*Update this file when project structure, active tools, or conventions change.*


---

## Plan-Before-Execute (Superpowers equivalent — no CLI required)

Claude Code CLI and the Superpowers plugin are not available on this machine (no Node/npm). This rule replicates the same discipline natively.

**For any task with 3 or more steps:**
1. Write a numbered plan with checkboxes to `seo/outputs/plan-YYYY-MM-DD-[task].md` before starting
2. State the plan in chat and wait for confirmation
3. Check off each step as completed — do not skip ahead
4. Do not begin execution until the plan is confirmed

**For batch jobs (10+ outputs):** include a checkpoint after every 10 items. Stop, validate, report pass/fail, wait before continuing.

**Override:** Simon can say "skip the plan, just do it" to bypass for simple tasks.
