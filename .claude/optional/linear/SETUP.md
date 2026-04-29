# Linear MCP — Setup

**What it does:** Connects Claude Code to Linear for project/task management. Create issues, update status, pull sprint state, check what's pending.

**Best for:** If you're using Linear for SEO sprint tracking, campaign planning, or cross-team coordination with Overdose Digital.

**Status:** Not connected.

## MCP server

Official Linear remote MCP — hosted by Linear, OAuth 2.1, no install required.

## Activate

Run in terminal:
```bash
claude mcp add --transport http linear-server https://mcp.linear.app/mcp
```

Claude Code will open a browser OAuth flow. Approve it. Done.

No credentials file, no npm package, no local server. Linear hosts it.

## Add to settings.local.json (optional — for explicit control)
```json
"linear": {
  "type": "http",
  "url": "https://mcp.linear.app/mcp"
}
```

## What you can ask once connected

- "What SEO tasks are in the current sprint?"
- "Create a Linear issue: write PLP intros for 20 refrigeration URLs, assign to me, label SEO"
- "Mark the EOFY hub page task as complete"
- "What's blocked in the current sprint?"

## Security: CLEAN
- Official Linear product, OAuth 2.1
- Hosted by Linear — no third-party code running locally
- Reviewed April 2026
