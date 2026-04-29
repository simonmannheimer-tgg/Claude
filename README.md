# Claude Code SEO, Analytics, and Automation Suite

**Purpose:**

This repository is a comprehensive workflow, automation, and skill management system built for The Good Guys' SEO, content, and reporting stack, powered by Claude Code. It supports privacy-first remote API orchestration, automated SEO and AEO analysis, modular process documentation, customizable agents and skills for Claude, and seamless GitHub Actions pipelines.

---

## Repository Highlights

- **Modular Numbered Processes:** (`00-tov-...`, `01-plp-intros.md`, ..., `09-ai-visibility-polling.md`) — for content production, metadata, linking, FAQs, AEO, EAV, and audits.
- **Claude Agents & Skills:** Defined in `.claude/agents/` and `.claude/skills/`, designed for high reuse across Claude Code/Claude.ai.
- **SEO Research/Reporting Automation:** `seo/` directory contains multi-agent pipelines and GitHub Actions for keyword research, competitor tracking, content auditing, and automated weekly reports.
- **GTMetrix MCP Server:** Privacy-first server and scripts for page speed audit automation.
- **Tools for Scale:** Python scripts in `tools/` for in-house site auditing, content QA, and batch processing.
- **Personal Knowledge Management:** `vault/` directory integrates a versioned Logseq graph, with nightly GitHub Actions backup, for daily notes and project tracking.
- **Security & Privacy:** `.env`, robust secret handling, and CI-based backup routines keep tokens/private data safe.
- **Comprehensive Documentation:** All major components and workflows are documented. Commit conventions, PR templates, and onboarding rules included.

---

## Directory Map

- `.claude/agents/` — Project-specific agents (SEO, copywriting, automation)
- `.claude/skills/` — Claude skills (repo-tracked & UI-only ones; see `.claude/skills/README.md` for scope)
- `tools/` — Python CLI utilities for multi-step audits and data processing
- `seo/` — Automated research/reporting pipelines and prompt templates
- `vault/` — Logseq PKM graph and project memory
- `docs/` — Archived audits, process notes, and findings
- `[process files]` — Modular numbered markdowns for each core workflow

---

## Core Workflows

- **Batch SEO Audits** and copy QA via agents and GitHub Actions
- **PLP/metadata production** with automated quality guardrails (character limits, language, banned terms)
- **Automated Logseq Vault backup** and weekly reviews
- **GTMetrix Page-Speed Audits** for transactional and category pages
- **Secure Secret Handling** for API keys and sensitive output

---

## Getting Started

1. Clone the repository
2. Copy `.env.example` to `.env` and add your secrets (never committed)
3. Set up Claude agent settings in `.claude/settings.json`
4. Optional: Activate GitHub Actions workflows for automation
5. Consult each directory or process file for agent-specific usage

---

## Contribution & PRs

- Follow commit/PR guides in `.claude/skills/tgg-repo-manager/SKILL.md`
- Keep process files and agent definitions standardized and up-to-date
- Document any changes in `CLAUDE.md`
- Run `vault-autocommit.yml` before closing major documentation sessions

---

## Status & Audit

Last audited: 2026-04-29 (see docs/archive for full audit history and recommendations)

This repository is a model for modular, agent-driven, and privacy-first tooling for in-house SEO, analytics, and reporting.