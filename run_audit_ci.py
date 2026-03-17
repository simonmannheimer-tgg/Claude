"""
GTMetrix audit script for GitHub Actions.

Reads config from environment variables (set by the workflow):
  GTMETRIX_API_KEY      required
  GTMETRIX_URLS         required — JSON array of URLs
  GTMETRIX_LOCATION_ID  default 4 (San Antonio)
  GTMETRIX_ADBLOCK      default false
  GTMETRIX_MAX_WAIT     default 300 (seconds per test)
  GTMETRIX_POLL_INTERVAL default 5 (seconds between polls)

Writes:
  $GITHUB_STEP_SUMMARY  — markdown table visible in the Actions UI
  gtmetrix_results.json — uploaded as a workflow artifact
"""

import asyncio
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

GTMETRIX_API_BASE = "https://gtmetrix.com/api/2.0"


async def run_test(api_key: str, url: str, location_id: int, adblock: bool) -> dict:
    max_wait = int(os.getenv("GTMETRIX_MAX_WAIT", "300"))
    poll_interval = int(os.getenv("GTMETRIX_POLL_INTERVAL", "5"))

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

    async with httpx.AsyncClient(
        auth=(api_key, ""),
        base_url=GTMETRIX_API_BASE,
        timeout=30,
        headers={"Content-Type": "application/vnd.api+json"},
    ) as client:
        resp = await client.post("/tests", content=json.dumps(payload))
        if resp.status_code not in (200, 201):
            raise RuntimeError(
                f"Submission failed ({resp.status_code}): {resp.text[:200]}"
            )

        test_id = resp.json()["data"]["id"]
        elapsed = 0

        while elapsed < max_wait:
            await asyncio.sleep(poll_interval)
            elapsed += poll_interval

            poll = await client.get(f"/tests/{test_id}")
            poll.raise_for_status()
            data = poll.json().get("data", {})
            state = data.get("attributes", {}).get("state", "")

            if state == "completed":
                return _parse(data, url, location_id)

            if state in ("error", "failed"):
                msg = data.get("attributes", {}).get("error", "unknown error")
                raise RuntimeError(f"GTMetrix test failed: {msg}")

    raise TimeoutError(f"Test for {url} timed out after {max_wait}s")


def _parse(data: dict, url: str, location_id: int) -> dict:
    report = data.get("attributes", {}).get("report", {})
    metrics = report.get("metrics", {})

    def pct(v):
        if v is None:
            return None
        return round(float(v) * 100) if float(v) <= 1 else int(v)

    def ms(v):
        return int(float(v)) if v is not None else None

    audits = report.get("audits", {})
    failing = sorted(
        [
            {
                "title": v.get("title", k),
                "score": v.get("score"),
                "displayValue": v.get("displayValue", ""),
            }
            for k, v in audits.items()
            if isinstance(v, dict) and v.get("score") is not None and v.get("score") < 0.9
        ],
        key=lambda a: (a["score"] or 1),
    )

    return {
        "url": url,
        "performance_score": pct(report.get("scores", {}).get("performance")),
        "structure_score": pct(report.get("scores", {}).get("structure")),
        "lcp_ms": ms(metrics.get("largestContentfulPaint")),
        "tbt_ms": ms(metrics.get("totalBlockingTime")),
        "cls": metrics.get("cumulativeLayoutShift"),
        "location_id": location_id,
        "test_date": datetime.now(timezone.utc).isoformat(),
        "failing_audits": failing[:5],
    }


def _grade(score) -> str:
    if score is None:
        return "❓"
    if score >= 90:
        return "🟢"
    if score >= 50:
        return "🟡"
    return "🔴"


# ---------------------------------------------------------------------------
# Page-type classification (used to group results in the summary)
# ---------------------------------------------------------------------------
_CATEGORY_ORDER = ["Home", "Category", "Product", "Guide", "Blog", "Other"]


def _classify(url: str) -> str:
    from urllib.parse import urlparse
    path = urlparse(url).path.rstrip("/")
    if path == "":
        return "Home"
    parts = [p for p in path.split("/") if p]
    if not parts:
        return "Home"
    top = parts[0].lower()
    if top in ("buying-guide", "buying-guides"):
        return "Guide"
    if top in ("whats-new", "blog", "news", "articles"):
        return "Blog"
    # On The Good Guys (and many retailers): single slug = product, multi-segment = category
    if len(parts) == 1:
        return "Product"
    return "Category"


def _section_table(results: list[dict]) -> list[str]:
    """Build the markdown summary grouped by page type."""
    from collections import defaultdict
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in results:
        groups[_classify(r.get("url", ""))].append(r)

    lines = []
    for cat in _CATEGORY_ORDER:
        if cat not in groups:
            continue
        lines.append(f"\n## {cat}\n")
        lines.append("| URL | Perf | Structure | LCP | TBT | CLS |")
        lines.append("|-----|:----:|:---------:|----:|----:|----:|")
        for r in groups[cat]:
            if "error" in r:
                lines.append(f"| {r['url']} | ❌ | ❌ | — | — | — |")
            else:
                lines.append(
                    f"| {r['url']} "
                    f"| {_grade(r['performance_score'])} {r['performance_score']} "
                    f"| {_grade(r['structure_score'])} {r['structure_score']} "
                    f"| {r.get('lcp_ms')} ms "
                    f"| {r.get('tbt_ms')} ms "
                    f"| {r.get('cls')} |"
                )
    return lines


async def main():
    api_key = os.environ["GTMETRIX_API_KEY"]
    location_id = int(os.getenv("GTMETRIX_LOCATION_ID", "4"))
    adblock = os.getenv("GTMETRIX_ADBLOCK", "false").lower() == "true"

    urls_raw = os.environ["GTMETRIX_URLS"]
    try:
        urls = json.loads(urls_raw)
    except json.JSONDecodeError:
        urls = [u.strip() for u in urls_raw.strip().splitlines() if u.strip()]

    print(f"GTMetrix audit: {len(urls)} URL(s), location {location_id}, adblock={adblock}")

    results = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url}")
        try:
            r = await run_test(api_key, url, location_id, adblock)
            results.append(r)
            print(f"  ✓ Perf {r['performance_score']} | LCP {r['lcp_ms']}ms | TBT {r['tbt_ms']}ms")
        except Exception as e:
            results.append({"url": url, "error": str(e)})
            print(f"  ✗ {e}", file=sys.stderr)

    # Write GitHub step summary (grouped by page type)
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        header = [
            "# GTMetrix Audit Results\n",
            f"**{len(urls)} URL(s)** | Location `{location_id}` | {ts}\n",
        ]
        Path(summary_path).write_text("\n".join(header + _section_table(results)))

    # Write artifact
    out = Path("gtmetrix_results.json")
    out.write_text(json.dumps(results, indent=2))
    print(f"\nSaved {out}")

    # Push results back to repo via GitHub Contents API so they can be
    # fetched by trigger_audit.py without hitting blob storage redirects.
    _push_results_to_repo(results)

    if any("error" in r for r in results):
        sys.exit(1)


def _push_results_to_repo(results: list[dict]) -> None:
    import base64
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    ref = os.getenv("GITHUB_REF_NAME")
    run_number = os.getenv("GITHUB_RUN_NUMBER", "?")
    if not (token and repo and ref):
        return

    path = "gtmetrix_results/latest.json"
    content_b64 = base64.b64encode(json.dumps(results, indent=2).encode()).decode()
    api = "https://api.github.com"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # Fetch existing SHA so we can update rather than create
    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=headers)
    sha = existing.json().get("sha") if existing.status_code == 200 else None

    payload = {
        "message": f"GTMetrix results run #{run_number}",
        "content": content_b64,
        "branch": ref,
    }
    if sha:
        payload["sha"] = sha

    r = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=headers, json=payload)
    if r.status_code in (200, 201):
        print(f"Results committed to repo: {path} on {ref}")
    else:
        print(f"Warning: could not commit results to repo ({r.status_code})", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
