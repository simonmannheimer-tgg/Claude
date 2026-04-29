# Google Search Console MCP — Setup

**What it does:** Connects Claude Code directly to GSC. Pull query data, CTR by position, page performance, indexing issues — without exporting a CSV.

**Best for:** Monthly reporting, keyword gap analysis, identifying quick-win ranking opportunities, pulling non-brand performance for stakeholder decks.

**Status:** Not connected. Requires OAuth setup (~20 min one-time).

## MCP server

`AminForou/mcp-gsc` — MIT, actively maintained, OAuth 2.0.

## Activate

### Step 1 — Google Cloud credentials
1. Go to console.cloud.google.com
2. Create a project (or use existing)
3. Enable the "Google Search Console API"
4. Go to Credentials → Create OAuth 2.0 Client ID → Desktop App
5. Download the JSON file → save as `gsc-credentials.json` somewhere safe (NOT in this repo)

### Step 2 — Install
```bash
npm install -g @aminforou/mcp-gsc
```

### Step 3 — Add to settings.local.json
Copy `.claude/settings.local.json.example` to `.claude/settings.local.json` and fill in:
```json
"gsc": {
  "command": "npx",
  "args": ["-y", "mcp-gsc"],
  "env": {
    "GSC_CREDENTIALS_PATH": "/absolute/path/to/gsc-credentials.json",
    "GSC_SITE_URL": "https://www.thegoodguys.com.au/"
  }
}
```

### Step 4 — First run auth
On first use, Claude Code will open a browser auth flow. Approve it. Token is cached locally after that.

## What you can ask once connected

- "Pull the top 50 non-brand queries by impressions for the last 30 days"
- "Show me pages ranked 4–10 for washing machine terms with >500 impressions"
- "What's the CTR trend for /refrigerators over the last 3 months vs prior period"
- "Find queries where we rank on page 2 but have high impressions — quick-win targets"

## Security: CLEAN
- MIT licence, active maintainer
- OAuth 2.0 only — no password storage
- Credentials file stays local, never in repo
- Reviewed April 2026
