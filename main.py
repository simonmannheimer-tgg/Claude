"""
GTMetrix MCP Server
Privacy-first: API key via .env only, auth headers stripped from all logs.
"""

import asyncio
import json
import logging
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from config import settings
from gtmetrix_client import GTMetrixClient

# ---------------------------------------------------------------------------
# Logging — auth headers are never printed
# ---------------------------------------------------------------------------
logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
log = logging.getLogger("gtmetrix-mcp")


# ---------------------------------------------------------------------------
# MCP Server setup
# ---------------------------------------------------------------------------
server = Server("gtmetrix-mcp")
_client: GTMetrixClient | None = None


def get_client() -> GTMetrixClient:
    global _client
    if _client is None:
        _client = GTMetrixClient(settings.api_key)
    return _client


# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------
TOOLS = [
    Tool(
        name="check_credits",
        description="Check remaining GTMetrix API credits, account type, and credit refill date. Always run this before bulk jobs.",
        inputSchema={"type": "object", "properties": {}, "required": []},
    ),
    Tool(
        name="list_locations",
        description="List available GTMetrix test locations with their IDs. Sydney is closest to AU.",
        inputSchema={"type": "object", "properties": {}, "required": []},
    ),
    Tool(
        name="analyze_url",
        description=(
            "Run a full GTMetrix performance test on a single URL. "
            "Returns Core Web Vitals (LCP, TBT, CLS), performance score, "
            "failing Lighthouse audits, and the 10 slowest resources. "
            "Also saves JSON and appends to the session CSV."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Full URL to test, including https://"},
                "location_id": {
                    "type": "integer",
                    "description": "GTMetrix location ID (use list_locations to find IDs). Defaults to config value.",
                },
                "adblock": {
                    "type": "boolean",
                    "description": "Enable adblock during test. Default false.",
                },
            },
            "required": ["url"],
        },
    ),
    Tool(
        name="bulk_audit",
        description=(
            "Test multiple URLs from a newline-separated list. "
            "Respects credit floor — aborts if credits would drop too low. "
            "Use dry_run=true to preview URLs without firing tests. "
            "Results saved to CSV and JSON in the configured output directory."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "urls": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of URLs to test.",
                },
                "location_id": {"type": "integer", "description": "Override default location."},
                "adblock": {"type": "boolean", "description": "Enable adblock. Default false."},
                "dry_run": {
                    "type": "boolean",
                    "description": "If true, lists URLs and credit cost without running tests.",
                },
            },
            "required": ["urls"],
        },
    ),
]


@server.list_tools()
async def list_tools():
    return TOOLS


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------
@server.call_tool()
async def call_tool(name: str, arguments: dict):
    client = get_client()

    if name == "check_credits":
        return await _handle_check_credits(client)

    elif name == "list_locations":
        return await _handle_list_locations(client)

    elif name == "analyze_url":
        return await _handle_analyze_url(client, arguments)

    elif name == "bulk_audit":
        return await _handle_bulk_audit(client, arguments)

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------
async def _handle_check_credits(client: GTMetrixClient):
    data = await client.get_status()
    credits_left = data.get("attributes", {}).get("api_credits", "unknown")
    account_type = data.get("attributes", {}).get("api_tier", "unknown")
    refill = data.get("attributes", {}).get("api_refill_date", "unknown")

    summary = (
        f"**GTMetrix Account Status**\n"
        f"- Credits remaining: {credits_left}\n"
        f"- Account type: {account_type}\n"
        f"- Credit refill: {refill}\n"
        f"- Credit floor (abort threshold): {settings.credit_floor}"
    )
    return [TextContent(type="text", text=summary)]


async def _handle_list_locations(client: GTMetrixClient):
    locations = await client.get_locations()
    lines = ["**Available GTMetrix Test Locations**\n"]
    for loc in locations:
        lid = loc.get("id", "?")
        name = loc.get("attributes", {}).get("name", "Unknown")
        country = loc.get("attributes", {}).get("country", "")
        lines.append(f"- ID `{lid}` — {name}, {country}")
    return [TextContent(type="text", text="\n".join(lines))]


async def _handle_analyze_url(client: GTMetrixClient, args: dict):
    url = args["url"]
    location_id = args.get("location_id", settings.default_location)
    adblock = args.get("adblock", False)

    # Credit check
    credits_ok, credits_left = await client.check_credit_floor(settings.credit_floor)
    if not credits_ok:
        return [TextContent(
            type="text",
            text=f"Aborted: only {credits_left} credits remaining (floor is {settings.credit_floor}). Run check_credits for details.",
        )]

    result = await client.run_test(url, location_id=location_id, adblock=adblock)
    summary = _format_result(result)

    # Persist outputs
    _save_outputs([result])

    return [TextContent(type="text", text=summary)]


async def _handle_bulk_audit(client: GTMetrixClient, args: dict):
    urls = args["urls"]
    location_id = args.get("location_id", settings.default_location)
    adblock = args.get("adblock", False)
    dry_run = args.get("dry_run", False)

    if dry_run:
        lines = [f"**Dry run — {len(urls)} URL(s) queued (no tests fired)**\n"]
        for u in urls:
            lines.append(f"- {u}")
        lines.append(f"\nEach test costs 1 credit. Current floor: {settings.credit_floor}.")
        return [TextContent(type="text", text="\n".join(lines))]

    # Credit check upfront
    credits_ok, credits_left = await client.check_credit_floor(settings.credit_floor + len(urls))
    if not credits_ok:
        return [TextContent(
            type="text",
            text=(
                f"Aborted: {len(urls)} tests would require ~{len(urls)} credits, "
                f"but only {credits_left} remain (floor is {settings.credit_floor}). "
                f"Reduce URL count or top up credits."
            ),
        )]

    results = []
    lines = [f"**Bulk audit — {len(urls)} URL(s)**\n"]

    for i, url in enumerate(urls, 1):
        lines.append(f"Testing {i}/{len(urls)}: {url}")
        try:
            result = await client.run_test(url, location_id=location_id, adblock=adblock)
            results.append(result)
            score = result.get("performance_score", "n/a")
            lcp = result.get("largest_contentful_paint_ms", "n/a")
            lines.append(f"  ✓ Score: {score} | LCP: {lcp}ms\n")
        except Exception as e:
            lines.append(f"  ✗ Failed: {e}\n")
            results.append({"url": url, "error": str(e), "test_date": datetime.utcnow().isoformat()})

        # Polite delay between tests
        if i < len(urls):
            await asyncio.sleep(settings.bulk_delay_seconds)

    _save_outputs(results)

    output_path = settings.output_dir / _session_filename("csv")
    lines.append(f"\nResults saved to: {output_path}")
    return [TextContent(type="text", text="\n".join(lines))]


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------
def _format_result(r: dict) -> str:
    if "error" in r:
        return f"**Test failed for {r.get('url', 'unknown')}**\nError: {r['error']}"

    failing = r.get("failing_audits", [])
    failing_lines = "\n".join(
        f"  - {a.get('title', '?')} ({a.get('displayValue', '')})"
        for a in failing[:5]
    ) or "  None"

    slow = r.get("top_resources", [])
    slow_lines = "\n".join(
        f"  - {s.get('url', '?')[:80]} — {s.get('duration_ms', '?')}ms"
        for s in slow[:5]
    ) or "  None"

    return (
        f"**GTMetrix Report: {r.get('url')}**\n"
        f"- Performance score: {r.get('performance_score', 'n/a')}\n"
        f"- Structure score: {r.get('structure_score', 'n/a')}\n"
        f"- LCP: {r.get('largest_contentful_paint_ms', 'n/a')}ms\n"
        f"- TBT: {r.get('total_blocking_time_ms', 'n/a')}ms\n"
        f"- CLS: {r.get('cumulative_layout_shift', 'n/a')}\n"
        f"- Test date: {r.get('test_date', 'n/a')}\n\n"
        f"**Top failing audits:**\n{failing_lines}\n\n"
        f"**Slowest resources:**\n{slow_lines}"
    )


_session_ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")


def _session_filename(ext: str) -> str:
    return f"gtmetrix_{_session_ts}.{ext}"


def _save_outputs(results: list[dict]):
    out_dir = settings.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    # JSON
    json_path = out_dir / _session_filename("json")
    existing = []
    if json_path.exists():
        existing = json.loads(json_path.read_text())
    existing.extend(results)
    json_path.write_text(json.dumps(existing, indent=2))

    # CSV
    csv_path = out_dir / _session_filename("csv")
    csv_cols = [
        "url", "performance_score", "structure_score",
        "largest_contentful_paint_ms", "total_blocking_time_ms",
        "cumulative_layout_shift", "test_date", "location_id",
        "top_failing_audit", "error",
    ]
    write_header = not csv_path.exists()
    with csv_path.open("a", encoding="utf-8") as f:
        if write_header:
            f.write(",".join(csv_cols) + "\n")
        for r in results:
            top_audit = ""
            if r.get("failing_audits"):
                top_audit = r["failing_audits"][0].get("title", "").replace(",", ";")
            row = [
                str(r.get(col, "")).replace(",", ";") if col != "top_failing_audit" else top_audit
                for col in csv_cols
            ]
            f.write(",".join(row) + "\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
