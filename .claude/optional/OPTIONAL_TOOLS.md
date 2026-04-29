# Optional Tools — Staged but Inactive

These tools are researched, documented, and ready to activate. None are running by default.

When a task comes in that one of these would help with, CLAUDE.md instructs Claude to ask:
"I can activate [tool] to help with this — want me to set it up?"

Activate any tool by following the SETUP.md inside its folder.

---

## Tool Registry

| Tool | Best for | Status | Effort to activate |
|------|----------|--------|-------------------|
| superpowers | Any complex multi-step task — enforces plan-before-execute | Not installed | 2 min |
| gsc | Pulling GSC query/CTR data without CSV exports | Not connected | 20 min (OAuth) |
| google-workspace | Gmail, Calendar, Sheets, Slides from Claude Code | Not connected | 20 min (OAuth) |
| linear | Project/task tracking from Claude Code | Not connected | 5 min |
| obsidian-pkm | Weekly reviews, goal tracking, session learning | Not set up | 30 min |
| claude-seo | Deeper SEO sub-skills: schema, GEO/AEO, backlinks | Not installed | 5 min |

---

## Trigger map — when Claude should offer these

| You say / ask for... | Claude offers... |
|----------------------|-----------------|
| Complex multi-step task, deck, batch, report | "Want me to use Superpowers to plan this first?" |
| GSC data, query analysis, CTR, ranking positions | "Want me to connect GSC MCP to pull this directly?" |
| Email draft, calendar check, slide update | "Want me to activate Google Workspace MCP?" |
| Project tracking, sprint tasks, what's pending | "Want me to connect Linear?" |
| Weekly review, what did I work on, career goals | "Want me to set up the Obsidian PKM workflow?" |
| Schema markup, GEO/AEO, backlink audit, local SEO | "Want me to install the claude-seo skill suite?" |

