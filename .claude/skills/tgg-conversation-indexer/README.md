# Indexer Bootstrap — One-Time Setup

The indexer expects a few Drive files to exist before its first proper run. This bundle creates them.

## What's in here

| File | Purpose |
|---|---|
| `TGG_SEO_Indexer_Last_Run.txt` | Seeds the last-run timestamp to 7 days ago so the first run scans the last week. Upload to Drive and rename to `TGG SEO — Indexer Last Run` (em dash, exact). |
| `TGG_SEO_Skills_Export_Last_Date.txt` | Placeholder so the indexer can read it without hitting a not-found. Will be updated by the Claude Code sync. Upload to Drive and rename to `TGG SEO — Skills Export Last Date`. |
| `CLAUDE_CODE_PROMPT.md` | The prompt to paste into Claude Code to generate the skills zip + push to GitHub. |

## Setup sequence

### 1. Rename the existing index file in Drive
The indexer searches for `TGG SEO — Claude Session Index All Time`. Your current Drive file is titled `TGG SEO — Claude Session Index All Time (FULL)`. Rename it: drop ` (FULL)` from the title. Em dash, no extra spaces.

### 2. Upload the two timestamp files to Drive
- Upload `TGG_SEO_Indexer_Last_Run.txt`. Rename to `TGG SEO — Indexer Last Run` (em dash).
- Upload `TGG_SEO_Skills_Export_Last_Date.txt`. Rename to `TGG SEO — Skills Export Last Date` (em dash).

When you upload `.txt` files to Drive, Drive auto-converts them to Google Docs. That's fine. The indexer reads contents either way.

### 3. Run the Claude Code sync
Open Claude Code. Paste the prompt from `CLAUDE_CODE_PROMPT.md`. It will:
- Zip your local `/mnt/skills/user/` folder into `skills_reference.zip`
- Push it to GitHub at `simonmannheimer-tgg/Claude/.claude/skills/tgg-conversation-indexer/skills_reference.zip`
- Update the export-date Drive file with today

### 4. Run the indexer
Download the zip from the GitHub commit. Open a fresh Claude.ai chat. Attach the zip. Paste:

```
Run tgg-conversation-indexer. Scan conversations since last run, score significance, append to index, flag abandoned projects with upside, update todo, check if skills export is due. Use the attached skills_reference.zip to capture Claude Projects conversations.
```

That's the full one-time bootstrap. After that, every weekly run is just step 3 + step 4.

## Why this is two tools

- Claude Code reads local `/mnt/skills/user/` and commits to GitHub. Claude.ai can't.
- Claude.ai runs the indexer logic against `recent_chats` + zip + Drive. Claude Code's `recent_chats` is scoped to its own sessions.

Two tools, two responsibilities, one workflow.
