# SEO Agent Team

This directory powers the automated SEO research and reporting system built on Claude subagents + GitHub Actions.

## Architecture

```
Claude (Team Leader / Orchestrator)
├── @seo-keyword-researcher   — Semrush keyword & organic data  [Haiku]
├── @seo-competitor-analyst   — Semrush backlink & competitor data  [Haiku]
├── @seo-content-auditor      — Reads .md content files, checks on-page SEO  [Haiku]
└── @seo-reporter             — Synthesises all findings into actionable report  [Sonnet]
```

**Token efficiency**: Haiku subagents handle all data gathering (~40x cheaper). Sonnet only touches the final synthesis. The Context Mode MCP caches large Semrush result sets so they're not repeated across agents.

## Triggers

| Trigger | How |
|---|---|
| Weekly (Mon 08:00 UTC) | `seo-weekly-report.yml` runs automatically |
| On-demand (any time) | Mention `@claude` in a GitHub issue or PR comment |
| Manual with parameters | GitHub Actions → SEO Weekly Report → Run workflow |
| One-off task | GitHub Actions → SEO On-Demand → Run workflow → enter prompt |

## How to run a weekly report manually

1. Go to **Actions** → **SEO Weekly Report** → **Run workflow**
2. Optionally fill in:
   - **domain**: your target domain (e.g. `example.com`)
   - **topics**: comma-separated keyword topics (e.g. `electric bikes, e-bike accessories`)
   - **competitors**: competitor domains (e.g. `wiggle.com, chainreactioncycles.com`)
3. Click **Run workflow**

The report will be saved to `seo/outputs/report-YYYY-MM-DD.md` and a GitHub issue will be created with the key findings.

## How to trigger on-demand via issue comment

Open any issue and comment:
```
@claude research keywords for "waterproof hiking boots" and give me a content brief
```
```
@claude analyse competitors for domain.com vs competitor1.com and competitor2.com
```
```
@claude audit the content in 04-content-analysis.md for SEO gaps
```

Claude will respond in the issue thread and save outputs to `seo/outputs/`.

## Required GitHub Secrets

| Secret | Purpose |
|---|---|
| `ANTHROPIC_API_KEY` | Claude API access |
| `SEMRUSH_API_KEY` | Semrush data API |

Add at: **Settings → Secrets and variables → Actions → New repository secret**

## Output files

All outputs land in `seo/outputs/`:
- `keywords-YYYY-MM-DD.json` — raw keyword data
- `competitor-<domain>-YYYY-MM-DD.json` — competitor analysis data
- `report-YYYY-MM-DD.md` — synthesised weekly report

These are committed to the repo by the GitHub Actions bot so you have a historical record.

## Customising the default target / domain

Edit `CLAUDE.md` → SEO section to set your default domain, competitors, and keyword topics. The weekly workflow falls back to these if no inputs are provided.

## Prompts directory

`seo/prompts/` contains reusable task prompt templates you can copy into issue comments or workflow dispatch inputs.
