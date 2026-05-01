"""
AEO (Agentic Engine Optimisation) audit script for GitHub Actions.

Reads config from environment variables:
  AEO_URLS      optional — JSON array of {"url": "...", "label": "..."} objects
                or plain URL strings. Leave unset to audit TGG + key competitors.
  AEO_CHECKS    optional — comma-separated checker IDs (blank = all 10 checks)
  AEO_THRESHOLD optional — minimum score % (blank = no threshold; logs a warning)

Writes:
  $GITHUB_STEP_SUMMARY                         — markdown table in Actions UI
  seo/outputs/aeo/aeo-results-YYYYMMDD-HHMM.json — timestamped archive
  seo/outputs/aeo/latest.json                  — committed to repo via GitHub API

Retail checks used (AEO_CHECKS):
  discovery, content-structure, token-economics
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

DEFAULT_URLS = [
    # TGG — all page types
    {"url": "https://www.thegoodguys.com.au",                              "label": "TGG · Home"},
    {"url": "https://www.thegoodguys.com.au/televisions",                  "label": "TGG · Category"},
    {"url": "https://www.thegoodguys.com.au/buying-guide/best-tvs",        "label": "TGG · Buying Guide"},
    {"url": "https://www.thegoodguys.com.au/whats-new",                    "label": "TGG · Editorial"},
    # JB Hi-Fi — equivalent page types
    {"url": "https://www.jbhifi.com.au",                                               "label": "JB Hi-Fi · Home"},
    {"url": "https://www.jbhifi.com.au/collections/tvs",                               "label": "JB Hi-Fi · Category"},
    {"url": "https://www.jbhifi.com.au/collections/headphones",                        "label": "JB Hi-Fi · Category 2"},
    # Harvey Norman — equivalent page types
    {"url": "https://www.harveynorman.com.au",                                                          "label": "Harvey Norman · Home"},
    {"url": "https://www.harveynorman.com.au/tv-blu-ray-home-theatre/tvs-by-screen-size/all-tvs",       "label": "Harvey Norman · Category"},
    {"url": "https://www.harveynorman.com.au/buying-guides/security-camera-buying-guide",               "label": "Harvey Norman · Guide"},
    # Appliances Online — note: uses /category/[dept]/[sub]/ structure, no flat slugs
    {"url": "https://www.appliancesonline.com.au",                                         "label": "Appliances Online · Home"},
    {"url": "https://www.appliancesonline.com.au/category/refrigeration/fridges/",         "label": "Appliances Online · Category"},
    {"url": "https://www.appliancesonline.com.au/article/refrigerator-size-guide/",        "label": "Appliances Online · Guide"},
]

# Ecommerce-relevant categories: discovery, content-structure, token-economics.
# Scored out of 75 — the agentic-seo tool's other categories target dev tools, not retail.
CATEGORIES = [
    ("discovery", 25),
    ("content-structure", 25),
    ("token-economics", 25),
]

GRADE_EMOJI = {"A": "🟢", "B": "🟢", "C": "🟡", "D": "🟠", "F": "🔴"}


def run_aeo(url: str, checks: str | None = None) -> dict:
    """Run `agentic-seo --json --url <url>` and return the parsed report."""
    cmd = ["agentic-seo", "--json", "--url", url]
    if checks:
        cmd += ["--checks", checks]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        output = result.stdout.strip()
        if output:
            return json.loads(output)
        return {
            "url": url,
            "error": f"No output (exit {result.returncode}): {result.stderr[:300]}",
        }
    except subprocess.TimeoutExpired:
        return {"url": url, "error": "Timeout after 90s"}
    except json.JSONDecodeError as e:
        return {
            "url": url,
            "error": f"JSON parse error: {e}. stdout: {result.stdout[:200]}",
        }
    except Exception as e:
        return {"url": url, "error": str(e)}


def apply_retail_adjustment(result: dict) -> dict:
    """
    Recalculates score over the three ecommerce-relevant categories only:
    discovery, content-structure, token-economics (75 pts max).
    """
    if "error" in result or "categories" not in result:
        return result

    cats = result.get("categories", {})
    retail_max = sum(m for _, m in CATEGORIES)
    retail_score = sum(cats.get(k, {}).get("score", 0) for k, _ in CATEGORIES)
    adjusted_pct = round(retail_score / retail_max * 100) if retail_max else 0

    result["retail_adjusted"] = True
    result["retail_score"] = retail_score
    result["retail_max"] = retail_max
    result["retail_percentage"] = adjusted_pct
    return result


def cat_cell(report: dict, key: str, max_pts: int) -> str:
    c = report.get("categories", {}).get(key, {})
    return f"{c.get('score', '?')}/{max_pts}"


def build_summary(entries: list[dict]) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# AEO Audit Results\n",
        f"**{len(entries)} URL(s)** | {ts}\n",
        "## Score Overview\n",
        "| Site | Grade | Score | Discovery (/25) | Structure (/25) | Tokens (/25) | Capability (/15) | UX (/10) | Errors | Warns |",
        "|------|:-----:|------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|",
    ]
    for e in entries:
        label = e.get("label", e.get("url", "?"))
        r = e.get("result", {})
        if "error" in r:
            lines.append(f"| {label} | ❌ | — | — | — | — | — | — | — | — |")
            continue
        grade = r.get("grade", "?")
        pct = r.get("percentage", 0)
        s = r.get("summary", {})
        cats = " | ".join(cat_cell(r, k, m) for k, m in CATEGORIES)
        lines.append(
            f"| [{label}]({e['url']}) "
            f"| {GRADE_EMOJI.get(grade, '❓')} **{grade}** "
            f"| {pct}% "
            f"| {cats} "
            f"| {s.get('failed', s.get('errors', '?'))} "
            f"| {s.get('warned', s.get('warnings', '?'))} |"
        )

    lines += ["\n## Errors & Fixes\n"]
    for e in entries:
        label = e.get("label", e.get("url", "?"))
        r = e.get("result", {})
        if "error" in r:
            lines.append(f"### ❌ {label}\n```\n{r['error']}\n```\n")
            continue
        findings = r.get("findings", {})
        errors = findings.get("errors", [])
        warnings = findings.get("warnings", [])
        if not errors and not warnings:
            continue
        lines.append(f"### {label}\n")
        for f in errors:
            fix_line = f.get("fix", "").split("\n")[0]
            lines.append(f"- **✗ [{f.get('checkerName', '')}]** {f.get('message', '')}")
            if fix_line:
                lines.append(f"  - *Fix:* `{fix_line}`")
        for f in warnings:
            lines.append(f"- △ [{f.get('checkerName', '')}] {f.get('message', '')}")
        lines.append("")

    return "\n".join(lines)


def push_to_repo(entries: list[dict]) -> None:
    import base64

    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    ref = os.getenv("GITHUB_REF_NAME")
    run_number = os.getenv("GITHUB_RUN_NUMBER", "?")
    if not (token and repo and ref):
        return

    path = "seo/outputs/aeo/latest.json"
    b64 = base64.b64encode(json.dumps(entries, indent=2).encode()).decode()
    api = "https://api.github.com"
    hdrs = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=hdrs, timeout=30)
    sha = existing.json().get("sha") if existing.status_code == 200 else None

    payload = {
        "message": f"AEO audit results run #{run_number}",
        "content": b64,
        "branch": ref,
    }
    if sha:
        payload["sha"] = sha

    resp = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=hdrs, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"Committed to repo: {path} on {ref}")
    else:
        print(f"Warning: could not commit ({resp.status_code})", file=sys.stderr)


def main():
    checks = os.getenv("AEO_CHECKS") or None
    threshold = os.getenv("AEO_THRESHOLD") or None

    urls_raw = os.getenv("AEO_URLS", "").strip()
    if urls_raw:
        try:
            raw = json.loads(urls_raw)
            entries = [{"url": u, "label": u} if isinstance(u, str) else u for u in raw]
        except json.JSONDecodeError:
            entries = [
                {"url": u.strip(), "label": u.strip()}
                for u in urls_raw.splitlines()
                if u.strip()
            ]
    else:
        entries = DEFAULT_URLS

    print(f"AEO audit: {len(entries)} URL(s)")
    for e in entries:
        url = e["url"]
        label = e.get("label", url)
        print(f"  [{label}] {url}")
        r = run_aeo(url, checks)
        r = apply_retail_adjustment(r)
        e["result"] = r
        if "error" in r:
            print(f"  ✗ {r['error']}", file=sys.stderr)
        else:
            s = r.get("summary", {})
            retail_pct = r.get("retail_percentage", r.get("percentage", 0))
            print(
                f"  ✓ Grade {r.get('grade', '?')} ({r.get('percentage', 0)}% raw"
                f" / {retail_pct}% retail-adjusted)"
                f" | {s.get('failed', s.get('errors', '?'))} errors, {s.get('warned', s.get('warnings', '?'))} warnings"
            )

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    out_file = out_dir / f"aeo-results-{ts}.json"
    out_file.write_text(json.dumps(entries, indent=2))
    print(f"\nSaved {out_file}")

    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        Path(summary_path).write_text(build_summary(entries))

    push_to_repo(entries)

    if threshold:
        t = int(threshold)
        for e in entries:
            r = e.get("result", {})
            pct = r.get("percentage", 0)
            if "error" not in r and pct < t:
                print(
                    f"⚠  {e.get('label', e['url'])}: {pct}% is below threshold {t}%",
                    file=sys.stderr,
                )

    if any("error" in e.get("result", {}) for e in entries):
        sys.exit(1)


if __name__ == "__main__":
    main()
