# Optional Tools — Staged but Inactive

These tools are researched, documented, and ready to activate. None are running by default.

When a task comes in that one of these would help with, CLAUDE.md instructs Claude to ask:
"I can activate [tool] to help with this — want me to set it up?"

Activate any tool by following the SETUP.md inside its folder.

---

## Tool Registry

| Tool | Best for | Status | Effort to activate |
|------|----------|--------|-------------------|
| superpowers | Any complex multi-step task — enforces plan-before-execute | **Active** | — |
| gsc | Pulling GSC query/CTR data without CSV exports | **Active** (declared in `.claude/settings.json`; needs `GSC_CREDENTIALS_JSON` secret) | OAuth once on personal device |
| google-workspace | Gmail, Calendar, Sheets, Slides from Claude Code | **Active** (declared in `.claude/settings.json`; needs `GOOGLE_WORKSPACE_CREDENTIALS_JSON` secret) | OAuth once on personal device |
| linear | Project/task tracking from Claude Code | Not connected | 5 min |
| obsidian-pkm | Weekly reviews, goal tracking, session learning | **Replaced by Logseq** — vault at `vault/`, edited via logseq.com, served to Claude via `vault` filesystem MCP | — |
| claude-seo | Deeper SEO sub-skills: schema, GEO/AEO, backlinks | **Active** (installed via `.devcontainer/setup.sh`) | — |

---

## Trigger map — when Claude should offer these

| You say / ask for... | Claude offers... |
|----------------------|-----------------|
| Project tracking, sprint tasks, what's pending | "Want me to connect Linear?" |

(Superpowers, GSC, Google Workspace, claude-seo, and Logseq vault are all active by default — no offer needed.)

