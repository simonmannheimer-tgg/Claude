# Obsidian + Claude Code PKM — Setup

**What it does:** Turns an Obsidian vault into a living second brain connected to Claude Code. Weekly reviews, goal tracking, session learning capture, project continuity.

**Best for:** Friday end-of-week reviews. Tracking what you're actually working on vs what you said you'd work on. Career growth. Not losing good ideas from sessions.

**Status:** Not set up.

## Repo

`ballred/obsidian-claude-pkm` — MIT, cross-platform (Windows/macOS).

## Prerequisites

- Obsidian installed (free — obsidian.md)
- A vault (folder) set up — can be new or existing

## Activate

### Step 1 — Install
```bash
git clone https://github.com/ballred/obsidian-claude-pkm.git
cd obsidian-claude-pkm
```

### Step 2 — Point it at your vault
Edit `config.yml`:
```yaml
vault_path: "C:/Users/simonma/OneDrive - JB HI-FI Group Pty Ltd/Obsidian/TGG"
```

### Step 3 — Install the slash commands
```bash
npm install
npm run install-commands
```

This adds these slash commands to Claude Code:
- `/daily` — create today's daily note
- `/weekly` — run weekly review (pulls from daily notes, checks goals)
- `/review` — goal alignment check (what you did vs what you said you'd do)
- `/project new [name]` — scaffold a new project in the vault

### Step 4 — First weekly review
```
/weekly
```
Claude reads your last 7 days of notes, summarises what got done, flags anything that dropped off, and asks whether your current work is aligned to your 3-month goals.

## What a Friday looks like

10 minutes:
1. `/weekly` — summary of the week
2. `/review` — goal check
3. Capture anything Claude surfaces as worth continuing

## Security: CLEAN
- MIT licence, no network calls outside Claude API
- All data stays local in your Obsidian vault
- No telemetry, no external services
- Reviewed April 2026
