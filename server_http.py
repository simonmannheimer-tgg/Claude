"""
GTMetrix MCP — HTTP server for the Claude.ai browser UI.

Exposes the same four tools as main.py (stdio) but over streamable HTTP,
which is the transport Claude.ai uses for remote integrations.

Quick start (local + ngrok):
    python server_http.py          # starts on http://localhost:8000
    ngrok http 8000                # get a public HTTPS URL

Add to Claude.ai → Settings → Integrations:
    URL: https://<your-ngrok-id>.ngrok.io/mcp

Optional bearer-token auth (recommended when exposed publicly):
    MCP_AUTH_TOKEN=<secret> python server_http.py
    Then set the Authorization header in Claude.ai to: Bearer <secret>

Environment variables (same .env as the stdio server):
    GTMETRIX_API_KEY        required
    GTMETRIX_DEFAULT_LOCATION  default 4 (San Antonio)
    GTMETRIX_CREDIT_FLOOR   default 10
    PORT                    default 8000
    MCP_AUTH_TOKEN          optional, enables bearer-token auth
"""

import asyncio
import logging
import os
from datetime import datetime
from typing import Optional

import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from config import settings
from gtmetrix_client import GTMetrixClient

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
log = logging.getLogger("gtmetrix-mcp-http")

# ---------------------------------------------------------------------------
# FastMCP instance — stateless so each request is self-contained
# (Claude.ai doesn't maintain long-lived MCP sessions)
# ---------------------------------------------------------------------------
mcp = FastMCP(
    name="GTMetrix",
    instructions=(
        "Performance auditing tool powered by GTMetrix. "
        "Use check_credits first to verify you have budget, "
        "then analyze_url for a single page or bulk_audit for a list."
    ),
    stateless_http=True,
    host="0.0.0.0",
    port=int(os.getenv("PORT", "8000")),
)

_client: Optional[GTMetrixClient] = None


def get_client() -> GTMetrixClient:
    global _client
    if _client is None:
        _client = GTMetrixClient(settings.api_key)
    return _client


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------
@mcp.tool()
async def check_credits() -> str:
    """Check remaining GTMetrix API credits, account type, and credit refill date. Always run this before bulk jobs."""
    data = await get_client().get_status()
    attrs = data.get("attributes", {})
    return (
        f"**GTMetrix Account Status**\n"
        f"- Credits remaining: {attrs.get('api_credits', 'unknown')}\n"
        f"- Account type: {attrs.get('api_tier', 'unknown')}\n"
        f"- Credit refill: {attrs.get('api_refill_date', 'unknown')}\n"
        f"- Credit floor (abort threshold): {settings.credit_floor}"
    )


@mcp.tool()
async def list_locations() -> str:
    """List available GTMetrix test locations with their IDs. Sydney is closest to AU."""
    locations = await get_client().get_locations()
    lines = ["**Available GTMetrix Test Locations**\n"]
    for loc in locations:
        lid = loc.get("id", "?")
        name = loc.get("attributes", {}).get("name", "Unknown")
        country = loc.get("attributes", {}).get("country", "")
        lines.append(f"- ID `{lid}` — {name}, {country}")
    return "\n".join(lines)


@mcp.tool()
async def analyze_url(
    url: str,
    location_id: Optional[int] = None,
    adblock: bool = False,
) -> str:
    """
    Run a full GTMetrix performance test on a single URL.
    Returns Core Web Vitals (LCP, TBT, CLS), performance score,
    failing Lighthouse audits, and the 10 slowest resources.
    """
    client = get_client()
    loc = location_id if location_id is not None else settings.default_location

    credits_ok, credits_left = await client.check_credit_floor(settings.credit_floor)
    if not credits_ok:
        return (
            f"Aborted: only {credits_left} credits remaining "
            f"(floor is {settings.credit_floor}). Run check_credits for details."
        )

    result = await client.run_test(url, location_id=loc, adblock=adblock)
    return _format_result(result)


@mcp.tool()
async def bulk_audit(
    urls: list[str],
    location_id: Optional[int] = None,
    adblock: bool = False,
    dry_run: bool = False,
) -> str:
    """
    Test multiple URLs. Respects credit floor — aborts if credits would drop too low.
    Use dry_run=true to preview URLs and credit cost without firing any tests.
    """
    client = get_client()
    loc = location_id if location_id is not None else settings.default_location

    if dry_run:
        lines = [f"**Dry run — {len(urls)} URL(s) queued (no tests fired)**\n"]
        lines.extend(f"- {u}" for u in urls)
        lines.append(f"\nEach test costs 1 credit. Current floor: {settings.credit_floor}.")
        return "\n".join(lines)

    credits_ok, credits_left = await client.check_credit_floor(
        settings.credit_floor + len(urls)
    )
    if not credits_ok:
        return (
            f"Aborted: {len(urls)} tests need ~{len(urls)} credits, "
            f"but only {credits_left} remain (floor is {settings.credit_floor}). "
            f"Reduce URL count or top up credits."
        )

    lines = [f"**Bulk audit — {len(urls)} URL(s)**\n"]
    for i, url in enumerate(urls, 1):
        lines.append(f"Testing {i}/{len(urls)}: {url}")
        try:
            result = await client.run_test(url, location_id=loc, adblock=adblock)
            score = result.get("performance_score", "n/a")
            lcp = result.get("largest_contentful_paint_ms", "n/a")
            lines.append(f"  ✓ Score: {score} | LCP: {lcp}ms\n")
        except Exception as e:
            lines.append(f"  ✗ Failed: {e}\n")

        if i < len(urls):
            await asyncio.sleep(settings.bulk_delay_seconds)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Optional bearer-token auth middleware
# ---------------------------------------------------------------------------
class _BearerAuth(BaseHTTPMiddleware):
    def __init__(self, app, token: str):
        super().__init__(app)
        self._token = token

    async def dispatch(self, request: Request, call_next):
        # Let health check through unauthenticated
        if request.url.path == "/health":
            return await call_next(request)
        auth = request.headers.get("authorization", "")
        if not auth.startswith("Bearer ") or auth[7:] != self._token:
            return Response("Unauthorized", status_code=401)
        return await call_next(request)


# ---------------------------------------------------------------------------
# Build the Starlette app
# ---------------------------------------------------------------------------
async def _health(request: Request):
    return JSONResponse({"status": "ok", "server": "gtmetrix-mcp"})


def build_app():
    app = mcp.streamable_http_app()
    app.routes.insert(0, Route("/health", _health))

    auth_token = os.getenv("MCP_AUTH_TOKEN")
    if auth_token:
        log.warning("Bearer token auth enabled")
        return _BearerAuth(app, auth_token)
    return app


app = build_app()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print(f"GTMetrix MCP HTTP server running on http://0.0.0.0:{port}/mcp")
    print("Add this URL to Claude.ai → Settings → Integrations")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
