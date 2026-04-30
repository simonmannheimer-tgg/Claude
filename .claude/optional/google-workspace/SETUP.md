# Google Workspace MCP — Setup

**What it does:** Connects Claude Code to Gmail, Google Calendar, Docs, Sheets, Slides, Drive, Tasks, Forms, Chat — all in one MCP server.

**Best for:** Drafting stakeholder emails in context, checking calendar before scheduling, reading/writing Sheets data, pushing content into Docs, prepping for meetings.

**Status:** Not connected. Requires OAuth setup (~20 min one-time).

## MCP server

`taylorwilsdon/google_workspace_mcp` — MIT, actively maintained, 12 Google services.

## Important

You already have Google Drive MCP connected. This replaces or supplements it. If you activate this, you can remove the standalone Drive MCP to avoid duplication.

## Activate

### Step 1 — Install
```bash
pip install google-workspace-mcp
```

### Step 2 — Google Cloud credentials
Same Google Cloud project as GSC (or new one):
1. Enable: Gmail API, Calendar API, Drive API, Sheets API, Slides API, Docs API
2. Create OAuth 2.0 Client ID → Desktop App
3. Download JSON → save as `google-workspace-credentials.json` (NOT in repo)

### Step 3 — Add to settings.local.json
```json
"google-workspace": {
  "command": "uvx",
  "args": ["google-workspace-mcp"],
  "env": {
    "GOOGLE_CREDENTIALS_PATH": "/absolute/path/to/google-workspace-credentials.json",
    "GOOGLE_TOOL_TIER": "core"
  }
}
```

`GOOGLE_TOOL_TIER=core` limits to the most useful tools and reduces token overhead. Remove the line to enable all 12 services.

## What you can ask once connected

- "Draft a reply to Alison's email about the GMC feed audit — match her tone"
- "What meetings do I have tomorrow morning?"
- "Open the TGG SEO WIP sheet and update the PLP intro status column for these 5 URLs"
- "Read the March SEO deck and summarise the key metrics for a quick stakeholder update"

## Security: CLEAN
- MIT licence, OAuth 2.0 only
- Tool tier limiting reduces blast radius
- Credentials local only, never committed
- Reviewed April 2026
