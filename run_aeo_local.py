"""
Run agentic-seo in local directory mode against a crawled site snapshot.
Run crawl_site_snapshot.py first to populate the directory.

Usage:
    AEO_DIR=site-snapshots/thegoodguys.com.au python run_aeo_local.py
    AEO_DIR=site-snapshots/thegoodguys.com.au AEO_LABEL="TGG" python run_aeo_local.py

Writes:
  $GITHUB_STEP_SUMMARY              — appended to any existing URL-mode summary
  seo/outputs/aeo/aeo-local-<label>-YYYYMMDD-HHMM.json  — timestamped archive
  seo/outputs/aeo/local-latest-<label>.json              — committed via GitHub API
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

GRADE_EMOJI = {"A": "🟢", "B": "🟢", "C": "🟡", "D": "🟠", "F": "🔴"}

CATEGORIES = [
    ("discovery",            "Discovery",            25),
    ("content-structure",    "Content Structure",    25),
    ("token-economics",      "Token Economics",      25),
    ("capability-signaling", "Capability Signaling", 15),
    ("ux-bridge",            "UX Bridge",            10),
]


def run_local_aeo(dir_path: str) -> dict:
    cmd = ["agentic-seo", "--json", dir_path]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        output = result.stdout.strip()
        if output:
            return json.loads(output)
        return {"error": f"No output (exit {result.returncode}): {result.stderr[:300]}"}
    except subprocess.TimeoutExpired:
        return {"error": "Timeout after 120s"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {e}. stdout: {result.stdout[:200]}"}
    except Exception as e:
        return {"error": str(e)}


def progress_bar(pct: int, width: int = 20) -> str:
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def build_summary(report: dict, label: str, dir_path: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    grade = report.get("grade", "?")
    pct = report.get("percentage", 0)
    score = report.get("score", 0)
    max_score = report.get("maxScore", 100)
    s = report.get("summary", {})

    lines = [
        f"# AEO Local Audit — {label}\n",
        f"**Directory:** `{dir_path}` | {ts}\n",
        f"## {GRADE_EMOJI.get(grade, '❓')} Grade {grade} &nbsp; {score}/{max_score} ({pct}%)\n",
        f"{s.get('passed', 0)} passed · {s.get('warned', 0)} warned · {s.get('failed', 0)} failed\n",
        "## Category Breakdown\n",
        "| | Category | Score | % |",
        "|--|----------|------:|--:|",
    ]

    for key, name, max_pts in CATEGORIES:
        c = report.get("categories", {}).get(key, {})
        pts = c.get("score", 0)
        cat_pct = c.get("percentage", 0)
        icon = "✓" if cat_pct >= 75 else "◑" if cat_pct >= 50 else "✗"
        lines.append(f"| {icon} | {name} | {pts}/{max_pts} | {cat_pct}% |")

    findings = report.get("findings", {})
    errors = findings.get("errors", [])
    warnings = findings.get("warnings", [])

    if errors:
        lines.append("\n## Errors\n")
        for f in errors:
            fix = f.get("fix", "").split("\n")[0]
            lines.append(f"- **✗ [{f.get('checkerName', '')}]** {f.get('message', '')}")
            if fix:
                lines.append(f"  - *Fix:* `{fix}`")

    if warnings:
        lines.append("\n## Warnings\n")
        for f in warnings:
            fix = f.get("fix", "").split("\n")[0]
            lines.append(f"- △ [{f.get('checkerName', '')}] {f.get('message', '')}")
            if fix:
                lines.append(f"  - *Fix:* {fix}")

    return "\n".join(lines)


def push_to_repo(data: dict, label: str) -> None:
    import base64

    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    ref = os.getenv("GITHUB_REF_NAME")
    run_number = os.getenv("GITHUB_RUN_NUMBER", "?")
    if not (token and repo and ref):
        return

    slug = re.sub(r"[^a-z0-9-]", "-", label.lower())
    path = f"seo/outputs/aeo/local-latest-{slug}.json"
    b64 = base64.b64encode(json.dumps(data, indent=2).encode()).decode()
    api = "https://api.github.com"
    hdrs = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=hdrs, timeout=30)
    sha = existing.json().get("sha") if existing.status_code == 200 else None
    payload = {
        "message": f"AEO local audit ({label}) run #{run_number}",
        "content": b64,
        "branch": ref,
    }
    if sha:
        payload["sha"] = sha
    resp = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=hdrs, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"Committed to repo: {path}")
    else:
        print(f"Warning: could not commit ({resp.status_code})", file=sys.stderr)


def main():
    dir_path = os.getenv("AEO_DIR", "").strip()
    if not dir_path:
        print("ERROR: AEO_DIR not set. Example: AEO_DIR=site-snapshots/thegoodguys.com.au python run_aeo_local.py", file=sys.stderr)
        sys.exit(1)

    label = os.getenv("AEO_LABEL", Path(dir_path).name)
    print(f"AEO local audit: {dir_path} ({label})")

    report = run_local_aeo(dir_path)

    if "error" in report:
        print(f"✗ {report['error']}", file=sys.stderr)
        sys.exit(1)

    grade = report.get("grade", "?")
    pct = report.get("percentage", 0)
    s = report.get("summary", {})
    print(f"✓ Grade {grade} ({pct}%) | {s.get('failed', s.get('errors', '?'))} errors, {s.get('warned', s.get('warnings', '?'))} warnings")

    for key, name, _ in CATEGORIES:
        c = report.get("categories", {}).get(key, {})
        print(f"  {name:<22} {c.get('score', 0)}/{c.get('maxScore', '?')} ({c.get('percentage', 0)}%)")

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    slug = re.sub(r"[^a-z0-9-]", "-", label.lower())
    out_file = out_dir / f"aeo-local-{slug}-{ts}.json"
    payload = {"label": label, "dir": dir_path, "report": report}
    out_file.write_text(json.dumps(payload, indent=2))
    print(f"\nSaved {out_file}")

    # Append to step summary (URL-mode summary may already be there)
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as f:
            f.write("\n\n---\n\n")
            f.write(build_summary(report, label, dir_path))

    push_to_repo(payload, label)


if __name__ == "__main__":
    main()
