"""
Trigger a GTMetrix audit via GitHub Actions and stream results back.

Usage:
    python trigger_audit.py https://example.com https://other.com
    python trigger_audit.py --location 7 --adblock https://example.com
    python trigger_audit.py --no-wait https://example.com   # fire and forget

Required env vars:
    GITHUB_TOKEN   — personal access token with 'actions: write' permission
    GITHUB_REPO    — default: simonmannheimer-tgg/Claude

The script:
  1. Dispatches the gtmetrix-audit workflow
  2. Waits for the run to start
  3. Polls until complete
  4. Downloads and prints the results artifact
"""

import argparse
import json
import os
import subprocess
import sys
import time
import zipfile
from datetime import datetime, timezone
from io import BytesIO

import httpx

REPO = os.getenv("GITHUB_REPO", "simonmannheimer-tgg/Claude")
WORKFLOW_FILE = "gtmetrix-audit.yml"
GH_API = "https://api.github.com"


def _client(token: str) -> httpx.Client:
    return httpx.Client(
        base_url=GH_API,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        timeout=30,
        follow_redirects=True,
    )


def _current_branch() -> str:
    try:
        return subprocess.check_output(
            ["git", "branch", "--show-current"], text=True
        ).strip()
    except Exception:
        return "main"


def dispatch(client: httpx.Client, urls: list[str], location_id: int, adblock: bool, ref: str) -> None:
    payload = {
        "ref": ref,
        "inputs": {
            "urls": json.dumps(urls),
            "location_id": str(location_id),
            "adblock": "true" if adblock else "false",
        },
    }
    resp = client.post(
        f"/repos/{REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches", json=payload
    )
    if resp.status_code != 204:
        print(f"Failed to trigger workflow ({resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)


def wait_for_run(client: httpx.Client, after_ts: float, timeout: int = 60) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(5)
        resp = client.get(
            f"/repos/{REPO}/actions/workflows/{WORKFLOW_FILE}/runs",
            params={"per_page": 10},
        )
        resp.raise_for_status()
        for run in resp.json().get("workflow_runs", []):
            created = run.get("created_at", "")
            run_ts = datetime.fromisoformat(created.replace("Z", "+00:00")).timestamp()
            if run_ts >= after_ts:
                return run
    print("Timed out waiting for run to appear. Check Actions tab.", file=sys.stderr)
    sys.exit(1)


def poll_until_done(client: httpx.Client, run_id: int, run_url: str) -> str:
    while True:
        resp = client.get(f"/repos/{REPO}/actions/runs/{run_id}")
        resp.raise_for_status()
        run = resp.json()
        status = run["status"]
        if status == "completed":
            return run.get("conclusion", "unknown")
        print(f"  {status}…", end="\r")
        time.sleep(10)


def fetch_results(client: httpx.Client, run_id: int) -> list[dict] | None:
    resp = client.get(f"/repos/{REPO}/actions/runs/{run_id}/artifacts")
    resp.raise_for_status()
    artifacts = resp.json().get("artifacts", [])
    target = next((a for a in artifacts if a["name"] == "gtmetrix-results"), None)
    if not target:
        return None

    dl = client.get(f"/repos/{REPO}/actions/artifacts/{target['id']}/zip")
    dl.raise_for_status()

    with zipfile.ZipFile(BytesIO(dl.content)) as z:
        with z.open("gtmetrix_results.json") as f:
            return json.load(f)


def _grade(score) -> str:
    if score is None:
        return "?"
    return "🟢" if score >= 90 else "🟡" if score >= 50 else "🔴"


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
    if len(parts) == 1:
        return "Product"
    return "Category"


_CATEGORY_ORDER = ["Home", "Category", "Product", "Guide", "Blog", "Other"]


def print_results(results: list[dict]) -> None:
    from collections import defaultdict
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in results:
        groups[_classify(r.get("url", ""))].append(r)

    sep = "─" * 72
    print(f"\n{sep}")
    print("  GTMetrix Audit Results")
    print(sep)

    for cat in _CATEGORY_ORDER:
        if cat not in groups:
            continue
        print(f"\n  ── {cat} ──")
        for r in groups[cat]:
            if "error" in r:
                print(f"\n  ❌  {r['url']}")
                print(f"      Error: {r['error']}")
                continue
            g = _grade(r.get("performance_score"))
            print(f"\n  {g}  {r['url']}")
            print(
                f"      Perf: {r.get('performance_score')}   "
                f"Structure: {r.get('structure_score')}   "
                f"LCP: {r.get('lcp_ms')} ms   "
                f"TBT: {r.get('tbt_ms')} ms   "
                f"CLS: {r.get('cls')}"
            )
            for audit in r.get("failing_audits", [])[:3]:
                print(f"      ⚠  {audit['title']}  {audit.get('displayValue', '')}")
    print(f"\n{sep}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Trigger GTMetrix audit via GitHub Actions"
    )
    parser.add_argument("urls", nargs="+", help="URLs to audit")
    parser.add_argument(
        "--location", type=int, default=4,
        help="GTMetrix location ID (4=San Antonio, 1=Vancouver, 7=Sydney)"
    )
    parser.add_argument("--adblock", action="store_true", help="Enable adblock")
    parser.add_argument(
        "--no-wait", action="store_true",
        help="Dispatch and exit without waiting for results"
    )
    parser.add_argument(
        "--ref", default=None,
        help="Git ref to run workflow on (default: current branch)"
    )
    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: set GITHUB_TOKEN env var (needs actions: write permission)", file=sys.stderr)
        sys.exit(1)

    ref = args.ref or _current_branch()
    trigger_ts = time.time() - 2  # small buffer for clock skew

    with _client(token) as client:
        print(f"Dispatching GTMetrix audit for {len(args.urls)} URL(s) on {ref}…")
        dispatch(client, args.urls, args.location, args.adblock, ref)
        print("Workflow triggered.")

        if args.no_wait:
            print(f"Track it at: https://github.com/{REPO}/actions")
            return

        print("Waiting for run to start…")
        run = wait_for_run(client, trigger_ts)
        run_id = run["id"]
        print(f"Run #{run['run_number']} started → {run['html_url']}")

        print("Running", end="")
        conclusion = poll_until_done(client, run_id, run["html_url"])
        print(f"\nWorkflow finished: {conclusion}")

        results = fetch_results(client, run_id)
        if results:
            print_results(results)
        else:
            print("Could not download results artifact.", file=sys.stderr)

        sys.exit(0 if conclusion == "success" else 1)


if __name__ == "__main__":
    main()
