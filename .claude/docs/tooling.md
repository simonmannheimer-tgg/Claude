# Tooling Reference

---

## Active MCP Servers

| Server | Entry point | Purpose |
|--------|-------------|---------|
| `context-mode` | `context_mode/server.py` | Token-efficient context indexing |
| `gtmetrix` | `main.py` | GTMetrix performance audits |
| `semrush` | `npx semrush-mcp` | Keyword, competitor, backlink data (AU database) |
| `firecrawl` | `npx firecrawl-mcp` | Live page scraping, competitor crawls |
| `airtable` | `npx @domdomegg/airtable-mcp-server` | Base appS4NfrOth5cVo7P |

Optional MCP servers (inactive): see `.claude/optional/` for GSC, Google Workspace, Linear.

---

## Optional Tool Activation

When a task comes in that one of these would meaningfully improve, **offer it before proceeding**. Use this exact pattern:

> "I could activate **[tool]** to help with this — it would let me [specific benefit]. Want me to set it up? Setup takes [X minutes] and is documented in `.claude/optional/[tool]/SETUP.md`."

Wait for confirmation. Do not activate anything without explicit approval.

### Trigger map

| Task type | Offer this tool |
|-----------|----------------|
| Complex multi-step task, batch job, deck build, audit pipeline (5+ steps) | **Superpowers plugin** — enforces plan-before-execute, prevents runaway iteration |
| GSC data, query analysis, CTR by position, ranking opportunities, non-brand performance | **GSC MCP** — pull query data directly, no CSV export needed |
| Email drafting, calendar check, reading/writing Sheets or Slides | **Google Workspace MCP** — Gmail, Calendar, Sheets, Slides from Claude Code |
| Sprint tracking, task status, what's in-flight, creating tickets | **Linear MCP** — project management connected to Claude Code |
| End-of-week review, goal tracking, career reflection, session learning | **Obsidian PKM** — weekly reviews and goal alignment in a local vault |
| Schema audit, GEO/AEO scoring, backlink gap, E-E-A-T, AI Overview optimisation | **claude-seo skill suite** — 19 sub-skills, deeper than current aeo-optimizer agent |
| AEO audit, llms.txt gaps, agent discoverability score, token budget, robots.txt for AI crawlers | **agentic-seo** — repo at `.claude/optional/agentic-seo/repo/`, scores sites 0–100, no API keys needed |

### Already active (no offer needed)
- Semrush MCP — keyword, competitor, backlink data
- Firecrawl MCP — live page scraping, competitor crawls, sitemap pulls
- Airtable MCP — base appS4NfrOth5cVo7P tracker tables
- GTMetrix MCP — performance audits
- Context Mode MCP — token-efficient context indexing
- Google Drive — file access

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

## Local Python Tools (`tools/`)

For local use. Not run in GitHub Actions. Run from repo root: `python tools/<script>.py`

| Script | Purpose |
|--------|---------|
| `tgg_plp_auditor.py` | Audits live TGG PLP pages against intro copy rules |
| `tgg_transcript_scraper.py` | Extracts YouTube transcripts in bulk |
| `mhtml_parser.py` | Parses browser-saved MHTML files for Claude ingestion |
| `mhtml_transformer.py` | Converts MHTML to self-contained .ai.html |
| `check_status.py` | Checks URL status codes from a CSV |
| `merge_and_split.py` | Merges/splits CSVs (Semrush keyword exports) |
| `split_csv.py` | Splits a large CSV into two halves |

**Note:** Some scripts have hardcoded Windows paths. Update the path variables at the top for your machine.

---

## Slash Skills

| Skill | What it does |
|-------|-------------|
| `check-github` | Poll GitHub Issues for @claude tasks, route to seo-team-lead, post replies |
| `start-chat` | Start Chat UI server on port 7860 |
| `tgg-conversation-indexer` | Weekly indexer — scans conversations, updates Google Drive index, flags abandoned projects |
| `tgg-repo-manager` | Commit messages, PR descriptions, CLAUDE.md entries, process file updates |

Run `tgg-conversation-indexer` weekly, or trigger with: "run tgg-conversation-indexer" or "what have I left unfinished".
