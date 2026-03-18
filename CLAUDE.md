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

- Feature branches for Claude sessions must follow the pattern:
  `claude/<feature-name>-<session-id>`
  Example: `claude/claude-md-mm42r61l51dt1g1s-EyZO6`
- Never push directly to `main` or `master` without explicit permission.

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
| `semrush` | `npx @semrush/mcp` | Semrush keyword, competitor, backlink data |

The context index database is stored at `context_mode/context_index.db` (git-ignored).

Semrush requires `SEMRUSH_API_KEY` in the environment. Set it in your shell profile or `.env`.

---

## SEO Agent Team

This repo contains a team of specialised SEO subagents. See `seo/README.md` for full documentation.

### Default SEO targets (update these for your project)

```
TARGET_DOMAIN=your-domain.com
COMPETITORS=competitor1.com,competitor2.com,competitor3.com
DEFAULT_TOPICS=your main product/content topics here
DEFAULT_DATABASE=uk
```

### Subagents

| Agent | Model | Purpose |
|-------|-------|---------|
| `seo-keyword-researcher` | Haiku | Semrush keyword & organic data |
| `seo-competitor-analyst` | Haiku | Backlink & competitor gap analysis |
| `seo-content-auditor` | Haiku | On-page audit of repo content files |
| `seo-reporter` | Sonnet | Synthesises findings into actionable reports |

### Token efficiency rules for SEO tasks

1. **Always use subagents** for Semrush data gathering — never query Semrush in the main conversation.
2. **Index large results immediately** with `ctx_index("kw:<topic>", data)` before summarising.
3. Pass only JSON summaries between agents — not raw API responses.
4. Use `--max-turns 8` for data agents, `--max-turns 10` for the reporter.

### Scheduled automation

- **Weekly report**: every Monday 08:00 UTC via `seo-weekly-report.yml`
- **On-demand**: mention `@claude` in any GitHub issue or PR
- **Manual**: GitHub Actions → Run workflow with optional domain/topic inputs

Required GitHub secrets: `ANTHROPIC_API_KEY`, `SEMRUSH_API_KEY`

---

## Remote

- **Origin**: `http://local_proxy@127.0.0.1:38487/git/simonmannheimer-tgg/Claude`
- **Proxy**: Local proxy server on `127.0.0.1:38487`

---

*This CLAUDE.md will be updated as the project structure and conventions evolve.*
