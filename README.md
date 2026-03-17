# GTMetrix MCP Server

Privacy-first GTMetrix MCP server for Claude Code. Runs locally — your API key never leaves your machine.

## Setup

### 1. Install dependencies

```bash
cd /path/to/gtmetrix-mcp
pip install -e .
```

Or with uv:

```bash
uv sync
```

### 2. Create your .env file

```bash
cp .env.example .env
```

Open `.env` and set your GTMetrix API key:

```
GTMETRIX_API_KEY=your_real_key_here
```

The `.env` file is in `.gitignore` — it will never be committed.

### 3. Add to Claude Code

Add this to your `~/.claude/settings.json` (or project-level `.mcp.json`):

```json
{
  "mcpServers": {
    "gtmetrix": {
      "command": "python",
      "args": ["/absolute/path/to/gtmetrix-mcp/main.py"],
      "cwd": "/absolute/path/to/gtmetrix-mcp"
    }
  }
}
```

If using uv, replace `"command": "python"` with the full path to uv:

```json
{
  "mcpServers": {
    "gtmetrix": {
      "command": "/opt/homebrew/bin/uv",
      "args": ["run", "--directory", "/absolute/path/to/gtmetrix-mcp", "python", "main.py"],
      "cwd": "/absolute/path/to/gtmetrix-mcp"
    }
  }
}
```

> Run `which python` or `which uv` if unsure of the full path.

Restart Claude Code after editing settings.

---

## Tools

| Tool | What it does |
|---|---|
| `check_credits` | Credits remaining, account type, refill date |
| `list_locations` | All available test locations with IDs |
| `analyze_url` | Full test on one URL — CWV, failing audits, slow resources |
| `bulk_audit` | Test a list of URLs; supports dry_run=true |

## Example usage in Claude Code

```
Check my GTMetrix credits

List available test locations

Test https://www.thegoodguys.com.au/televisions

Run a dry run bulk audit on these URLs:
- https://www.thegoodguys.com.au/laptops
- https://www.thegoodguys.com.au/washing-machines
- https://www.thegoodguys.com.au/refrigerators

Now run the bulk audit for real
```

## Output

Each session creates two files in `./reports/`:

- `gtmetrix_YYYYMMDD_HHMMSS.json` — full structured results
- `gtmetrix_YYYYMMDD_HHMMSS.csv` — flat CSV ready for PPTX/reporting

CSV columns:
```
url, performance_score, structure_score, largest_contentful_paint_ms,
total_blocking_time_ms, cumulative_layout_shift, test_date, location_id,
top_failing_audit, error
```

## Privacy

- API key is loaded from `.env` only — never hardcoded, never logged
- Authorization headers are stripped before any log output
- No data is sent anywhere except GTMetrix's official API (`gtmetrix.com/api/2.0`)
- Reports stay local in `./reports/`
- `.env` and `reports/` are in `.gitignore`

## Credit protection

Set `GTMETRIX_CREDIT_FLOOR` in `.env` (default: 10).
Any run that would drop below this threshold is aborted before firing a single test.
Use `dry_run=true` on bulk jobs to preview credit cost first.

## Location IDs (common)

| ID | Location |
|---|---|
| 4 | San Antonio, TX (free tier default) |
| 2 | London, UK |
| 13 | Amsterdam, Netherlands |
| Use `list_locations` | Full list for your account |

> GTMetrix does not currently have an AU server. Sydney CDN tests are best approximated from Singapore or the US west coast depending on your account tier.
