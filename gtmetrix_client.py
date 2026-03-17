"""
GTMetrix API client.

Privacy guarantee:
- The API key is passed as a SecretStr and accessed via .get_secret_value() only
  at the moment of constructing the Authorization header.
- httpx event hooks strip the Authorization header from all log output.
- No URL, credential, or response body is written to disk by this module
  (that responsibility belongs to main.py's _save_outputs).
"""

import asyncio
import logging
from datetime import datetime, timezone

import httpx
from pydantic import SecretStr

log = logging.getLogger("gtmetrix-mcp.client")

GTMETRIX_API_BASE = "https://gtmetrix.com/api/2.0"


async def _redact_auth(request: httpx.Request) -> None:
    """Strip Authorization header before any logging touches the request."""
    if "authorization" in request.headers:
        request.headers["authorization"] = "[REDACTED]"


class GTMetrixClient:
    def __init__(self, api_key: SecretStr):
        self._api_key = api_key
        self._locations_cache: list[dict] | None = None

    def _make_client(self) -> httpx.AsyncClient:
        """Create a short-lived httpx client. Key is injected here only."""
        return httpx.AsyncClient(
            auth=(self._api_key.get_secret_value(), ""),
            base_url=GTMETRIX_API_BASE,
            timeout=30,
            event_hooks={"request": [_redact_auth]},
        )

    async def get_status(self) -> dict:
        async with self._make_client() as client:
            resp = await client.get("/status")
            resp.raise_for_status()
            return resp.json().get("data", {})

    async def check_credit_floor(self, floor: int) -> tuple[bool, int]:
        """Returns (credits_ok, credits_remaining)."""
        data = await self.get_status()
        credits = data.get("attributes", {}).get("api_credits", 0)
        return credits >= floor, credits

    async def get_locations(self) -> list[dict]:
        if self._locations_cache is not None:
            return self._locations_cache
        async with self._make_client() as client:
            resp = await client.get("/locations")
            resp.raise_for_status()
            self._locations_cache = resp.json().get("data", [])
            return self._locations_cache

    async def run_test(
        self,
        url: str,
        location_id: int = 4,
        adblock: bool = False,
    ) -> dict:
        """
        Submit a test, poll until complete, return structured result dict.
        Raises on timeout or API error.
        """
        from config import settings

        payload = {
            "data": {
                "type": "test",
                "attributes": {
                    "url": url,
                    "location": str(location_id),
                    "adblock": 1 if adblock else 0,
                },
            }
        }

        async with self._make_client() as client:
            # Submit
            resp = await client.post("/tests", json=payload)
            if resp.status_code not in (200, 201):
                raise RuntimeError(f"Test submission failed ({resp.status_code}): {resp.text[:200]}")

            body = resp.json()
            test_id = body["data"]["id"]
            report_link = body.get("links", {}).get("self", f"/tests/{test_id}")

            # Poll
            elapsed = 0
            while elapsed < settings.max_wait:
                await asyncio.sleep(settings.poll_interval)
                elapsed += settings.poll_interval

                poll = await client.get(f"/tests/{test_id}")
                poll.raise_for_status()
                poll_data = poll.json().get("data", {})
                state = poll_data.get("attributes", {}).get("state", "")

                if state == "completed":
                    return _parse_result(poll_data, url, location_id)

                if state in ("error", "failed"):
                    error_msg = poll_data.get("attributes", {}).get("error", "Unknown error")
                    raise RuntimeError(f"GTMetrix test failed: {error_msg}")

            raise TimeoutError(f"Test for {url} did not complete within {settings.max_wait}s")


# ---------------------------------------------------------------------------
# Response parser
# ---------------------------------------------------------------------------
def _parse_result(data: dict, url: str, location_id: int) -> dict:
    attrs = data.get("attributes", {})
    report = attrs.get("report", {})

    # Core Web Vitals live under report.metrics
    metrics = report.get("metrics", {})

    # Failing audits
    audits = report.get("audits", {})
    failing = [
        {
            "id": k,
            "title": v.get("title", k),
            "description": v.get("description", ""),
            "score": v.get("score"),
            "displayValue": v.get("displayValue", ""),
        }
        for k, v in audits.items()
        if isinstance(v, dict) and v.get("score") is not None and v.get("score") < 0.9
    ]
    failing.sort(key=lambda a: (a["score"] or 1))

    # Slowest resources
    resources = report.get("resources", [])
    top_resources = sorted(
        [
            {
                "url": r.get("url", ""),
                "size_bytes": r.get("transferSize", 0),
                "duration_ms": r.get("time", 0),
            }
            for r in resources
            if isinstance(r, dict)
        ],
        key=lambda r: r["duration_ms"],
        reverse=True,
    )[:10]

    return {
        "url": url,
        "test_id": data.get("id", ""),
        "performance_score": _pct(report.get("scores", {}).get("performance")),
        "structure_score": _pct(report.get("scores", {}).get("structure")),
        "largest_contentful_paint_ms": _ms(metrics.get("largestContentfulPaint")),
        "total_blocking_time_ms": _ms(metrics.get("totalBlockingTime")),
        "cumulative_layout_shift": metrics.get("cumulativeLayoutShift"),
        "location_id": location_id,
        "test_date": datetime.now(timezone.utc).isoformat(),
        "failing_audits": failing,
        "top_resources": top_resources,
    }


def _pct(val) -> int | None:
    if val is None:
        return None
    return round(float(val) * 100) if float(val) <= 1 else int(val)


def _ms(val) -> int | None:
    if val is None:
        return None
    return int(float(val))
