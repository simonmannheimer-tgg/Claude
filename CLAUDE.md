# CLAUDE.md

This file provides guidance to AI assistants (Claude and others) working in this repository.

---

## Repository Overview

This repository contains a GTMetrix MCP server (Python/uv) and a Context Mode MCP server for token-efficient Claude Code sessions.

**Project Setup:**
- **Language / Runtime**: Python 3.11
- **Package manager**: uv
- **Install dependencies**: `uv sync` (auto-runs on first `uv run`)
- **Run GTMetrix MCP**: `uv run python3 main.py`
- **Run Context Mode MCP**: `uv run python3 context_mode/server.py`

---

## Git Workflow

### Branch Naming

- Each Claude Code session is assigned a branch by the system prompt in the format:
  `claude/<feature-name>-<session-id>`
  Example: `claude/plp-intro-copy-good-guys-XVTa0`
- **Always push to the branch specified in the current session's system prompt.** The proxy enforces a session-to-branch mapping and will return HTTP 403 if you attempt to push to a branch from a different session.
- Never push directly to `main` or `master` without explicit permission.
- Do not attempt to merge or rebase work onto other branches — stay on the assigned session branch.
- Branch proliferation is a system-level behaviour (one branch per session). Clean up stale branches manually on GitHub.

### Commits

- Write clear, descriptive commit messages in the imperative mood:
  - Good: `Add user authentication module`
  - Bad: `stuff` or `WIP`
- Sign commits using SSH (already configured via `.git/config`).
- Commit only related changes together — keep commits focused.

### Pushing

Always push with the upstream tracking flag:

```bash
git push -u origin <branch-name>
```

If push fails due to network errors, retry with exponential backoff:
- Wait 2s, retry
- Wait 4s, retry
- Wait 8s, retry
- Wait 16s, retry (final attempt)

**If push returns HTTP 403**, do not retry — this means the branch does not match the current session. Stay on the session-assigned branch.

### Fetching / Pulling

Prefer fetching specific branches:

```bash
git fetch origin <branch-name>
git pull origin <branch-name>
```

Apply the same exponential backoff retry strategy on network failures.

---

## Context Mode (Token Efficiency — MANDATORY)

A Context Mode MCP server is registered at `.claude/settings.json`. It indexes large content into SQLite and returns compact summaries, reducing context usage by up to 98%.

### Rules — follow these in every session

1. **Files over 50 lines**: Use `ctx_read_file` instead of the Read tool.
   - `ctx_read_file` returns a section map (~10–15 lines) rather than the raw file.
   - Then use `ctx_search(key, query)` to pull only the sections you need.

2. **Large tool outputs / API responses**: If a tool returns more than ~100 lines, pipe the content through `ctx_index(key, content)` immediately and work from the summary.

3. **Session start**: Run `ctx_list` to see what is already indexed from prior work. Avoid re-indexing content that is already present.

4. **Workflow pattern**:
   ```
   ctx_read_file("main.py")          → get structural summary
   ctx_search("main.py", "bulk_audit handler")  → get only that function
   ```

5. **Never dump raw files into context** when the Context Mode tools are available. Every raw Read of a large file is a context budget violation.

### Available context tools

| Tool | Purpose |
|------|---------|
| `ctx_read_file(path)` | Index a file; return section map |
| `ctx_index(key, content)` | Index arbitrary large text |
| `ctx_search(key, query)` | Retrieve matching sections only |
| `ctx_list()` | Show all indexed keys |
| `ctx_drop(key?)` | Remove from index |

---

## AI Assistant Guidelines

### General Principles

1. **Read before modifying** — always read existing files before editing them to understand current state and conventions.
2. **Minimize scope** — only make changes directly requested or clearly necessary. Do not refactor surrounding code, add extra comments, or introduce new abstractions unless asked.
3. **No over-engineering** — avoid feature flags, backwards-compatibility shims, or premature abstractions. Write the minimum code needed for the current task.
4. **Avoid security vulnerabilities** — never introduce SQL injection, XSS, command injection, or other OWASP top-10 issues.
5. **Prefer editing over creating** — modify existing files rather than creating new ones when possible.

### What NOT to Do

- Do not add docstrings, type annotations, or comments to code you didn't change.
- Do not add error handling for scenarios that cannot happen.
- Do not create helper utilities for one-off operations.
- Do not design for hypothetical future requirements.
- Do not add backwards-compatibility code when you can just change the thing directly.

### Confirming Risky Actions

Always confirm with the user before:
- Deleting files or branches
- Force-pushing (`git push --force`)
- Running destructive resets (`git reset --hard`)
- Modifying CI/CD pipelines
- Pushing to branches other than the designated feature branch

---

## MCP Servers

All MCP servers are registered in `.claude/settings.json` and start automatically with Claude Code.

| Server | Entry point | Purpose |
|--------|-------------|---------|
| `context-mode` | `context_mode/server.py` | Token-efficient context indexing |
| `gtmetrix` | `main.py` | GTMetrix performance audits |
| `semrush` | `npx semrush-mcp` | Semrush keyword, competitor, backlink data |

The context index database is stored at `context_mode/context_index.db` (git-ignored).

**Semrush authentication:**
- In browser Claude Code sessions: Semrush OAuth is already active via the Claude.ai connector — no API key needed.
- For GitHub Actions / headless use: requires `SEMRUSH_API_KEY` from the Semrush API portal. Set as a GitHub secret.
- The npm package is `semrush-mcp` (unscoped). Official remote endpoint: `https://mcp.semrush.com/v1/mcp`

---

## SEO Agent Team

This repo contains a full SEO agent team for The Good Guys (thegoodguys.com.au). See `seo/README.md` for full documentation.

### Project defaults

```
TARGET_DOMAIN=thegoodguys.com.au
COMPETITORS_PRIMARY=jbhifi.com.au,harveynorman.com.au,officeworks.com.au
COMPETITORS_SECONDARY=kogan.com,appliancesonline.com.au
DEFAULT_TOPICS=TVs, washing machines, fridges, air conditioners, vacuum cleaners, coffee machines, air fryers, laptops, headphones, kitchen appliances
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
│   └── ai-visibility-analyst  (Haiku)  — Process 09: AI visibility → poll questions
└── REPORTING
    ├── seo-content-auditor    (Haiku)  — on-page audit of repo content files
    └── seo-reporter           (Sonnet) — synthesise findings into reports
```

### How to invoke

Always start with the team lead:
```
Use the seo-team-lead to [describe your task]
```

Or invoke specialists directly for known tasks:
```
Use the plp-copywriter to write copy for /air-fryers
Use the eav-researcher to map the washing machines category
Use the seo-competitor-analyst to compare us vs jbhifi.com.au for TVs
```

### Token efficiency rules

1. **Always delegate through seo-team-lead** — it routes to the right agent and sequences parallel work.
2. **Haiku for all data gathering** (keyword, EAV, competitor, content analysis, linking, auditing).
3. **Sonnet only for writing** (PLP copy, FAQs, inlink migration, AEO, final reports).
4. **Index large outputs** with `ctx_index` before passing between agents.
5. **No scheduling yet** — all runs are manual or on-demand via @claude in issues.

### GitHub Actions (requires separate Anthropic API key)

- **Note:** Claude Pro subscription does NOT include API access. GitHub Actions needs a separate key from console.anthropic.com (pay-per-token).
- Workflows are ready but disabled until you have an API key: `.github/workflows/seo-weekly-report.yml`, `.github/workflows/seo-on-demand.yml`
- Required secrets when ready: `ANTHROPIC_API_KEY`, `SEMRUSH_API_KEY`

---

## Remote

- **Origin**: `http://local_proxy@127.0.0.1:38487/git/simonmannheimer-tgg/Claude`
- **Proxy**: Local proxy server on `127.0.0.1:38487`

---

*This CLAUDE.md will be updated as the project structure and conventions evolve.*
