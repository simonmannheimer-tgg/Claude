# AgriciDaniel/claude-seo — Setup

**What it does:** 19 SEO sub-skills and 12 subagents covering schema markup, GEO/AEO (AI search optimisation), backlink analysis, local SEO, Google API integration (PageSpeed, CrUX, GSC, GA4), and PDF/Excel reporting. Built specifically for Claude Code with Semrush MCP integration.

**Best for:** Deeper schema audits, AEO content scoring against AI Overviews, backlink gap analysis, local SEO (if TGG ever goes there), automated PDF performance reports.

**Overlap with existing setup:** Your current `aeo-optimizer` agent covers the basics. This goes significantly deeper on GEO/AEO and schema. The E-E-A-T scoring framework is more detailed than what you have.

**Status:** Not installed.

## Repo

`AgriciDaniel/claude-seo` — MIT, Anthropic marketplace validated, ~5k stars.

## Activate

Option A — Anthropic marketplace (easiest):
```bash
claude plugin install claude-seo
```

Option B — Direct install:
```bash
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
bash install.sh
```

The install script uses `git clone` then visible bash — not a pipe install. Safe to run.

## Sub-skills you'd actually use

| Sub-skill | When |
|-----------|------|
| `/seo:schema-audit` | Audit TGG product/category schema against current Google requirements |
| `/seo:geo-drift-check` | Check if your AEO content is drifting from current AI Overview patterns |
| `/seo:eeat-score` | Score a page against 80-item E-E-A-T checklist |
| `/seo:backlink-gap` | Compare TGG vs JB Hi-Fi backlink profile via Semrush MCP |
| `/seo:pagespeed-audit` | Pull CrUX data for category pages |
| `/seo:aeo-brief` | Generate AEO content brief for a query cluster |

## Security: CLEAN
- MIT licence, Anthropic marketplace validated
- `install.sh` is readable bash — reviewed
- No undisclosed telemetry or network calls
- Reviewed April 2026
