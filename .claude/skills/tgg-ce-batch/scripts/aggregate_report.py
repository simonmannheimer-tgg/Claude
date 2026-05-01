#!/usr/bin/env python3
"""
aggregate_report.py — builds the batch aggregate report after all subagents complete.

Scans runs/<batch-id>/ subfolders, reads pipeline-status.md and qa-report.md
from each run, and produces aggregate.md and aggregate.csv.

Usage:
    python3 .claude/skills/tgg-ce-batch/scripts/aggregate_report.py \
        --batch-id batch-2026-05-01-plp-intros \
        --runs-dir runs

Outputs:
    runs/<batch-id>/aggregate.md
    runs/<batch-id>/aggregate.csv
"""

import argparse
import csv
import re
import sys
from datetime import date
from pathlib import Path


def parse_status_file(status_path: Path) -> dict:
    """Read pipeline-status.md and return key fields."""
    data: dict = {
        "run_id": status_path.parent.name,
        "slug": "",
        "content_type": "",
        "status": "UNKNOWN",
    }
    if not status_path.exists():
        return data

    text = status_path.read_text(encoding="utf-8")
    for field in ("slug", "content_type", "run_id"):
        m = re.search(rf"^{field}:\s*(.+)$", text, re.MULTILINE)
        if m:
            data[field] = m.group(1).strip()

    stages_done = text.count("- [x]")
    stages_total = text.count("- [")
    if stages_done == stages_total and stages_total > 0:
        data["status"] = "COMPLETE"
    elif stages_done > 0:
        data["status"] = "IN_PROGRESS"
    else:
        data["status"] = "NOT_STARTED"

    return data


def parse_qa_report(qa_path: Path) -> tuple[str, str]:
    """Return (qa_result, fail_reasons) from qa-report.md."""
    if not qa_path.exists() or qa_path.stat().st_size == 0:
        return "", ""

    text = qa_path.read_text(encoding="utf-8")

    result = ""
    m = re.search(r"Overall result:\s*(PASS|FAIL)", text)
    if m:
        result = m.group(1)

    fails = re.findall(r"\| .+? \| .+? \| .+? \| ✗ \| .+? \|", text)
    fail_reasons = "; ".join(
        re.search(r"\| (.+?) \|", f).group(1).strip() for f in fails if re.search(r"\| (.+?) \|", f)
    )

    return result, fail_reasons


def count_words_in_final(final_path: Path) -> int:
    if not final_path.exists() or final_path.stat().st_size == 0:
        return 0
    text = final_path.read_text(encoding="utf-8")
    text = re.sub(r"^---.*?---\n", "", text, flags=re.DOTALL)
    return len(text.split())


def count_faq(final_path: Path) -> int:
    if not final_path.exists():
        return 0
    text = final_path.read_text(encoding="utf-8")
    m = re.search(r"## Frequently asked questions(.+?)(?=^##|\Z)", text, re.MULTILINE | re.DOTALL)
    if not m:
        return 0
    return len(re.findall(r"^\*\*.+\*\*", m.group(1), re.MULTILINE))


def count_links(links_path: Path) -> tuple[int, int]:
    if not links_path.exists():
        return 0, 0
    text = links_path.read_text(encoding="utf-8")
    total = len(re.findall(r"^\|", text, re.MULTILINE)) - 2
    unresolved = text.count("unresolved")
    return max(0, total), unresolved


def main() -> None:
    parser = argparse.ArgumentParser(description="Build batch aggregate report.")
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--runs-dir", default="runs")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    runs_dir = repo_root / args.runs_dir
    batch_dir = runs_dir / args.batch_id

    if not batch_dir.exists():
        print(f"Batch directory not found: {batch_dir}", file=sys.stderr)
        sys.exit(1)

    rows: list[dict] = []

    for run_dir in sorted(runs_dir.iterdir()):
        if run_dir.name == args.batch_id or not run_dir.is_dir():
            continue
        if not (run_dir / "pipeline-status.md").exists():
            continue

        status = parse_status_file(run_dir / "pipeline-status.md")
        qa_result, qa_fails = parse_qa_report(run_dir / "qa-report.md")
        word_count = count_words_in_final(run_dir / "final.md")
        faq_count = count_faq(run_dir / "final.md")
        link_count, unresolved = count_links(run_dir / "internal-links.md")

        if (run_dir / "final.md").exists() and (run_dir / "final.md").stat().st_size > 100:
            display_status = "COMPLETE"
        else:
            display_status = status.get("status", "UNKNOWN")

        rows.append({
            "run_id": status["run_id"],
            "slug": status["slug"],
            "content_type": status["content_type"],
            "status": display_status,
            "word_count": word_count or "",
            "faq_count": faq_count or "",
            "internal_link_count": link_count or "",
            "unresolved_links": unresolved or "",
            "qa_result": qa_result,
            "qa_fail_reasons": qa_fails,
            "time_seconds": "",
        })

    complete = sum(1 for r in rows if r["status"] == "COMPLETE")
    failed = sum(1 for r in rows if r["status"] == "FAILED")
    blocked = sum(1 for r in rows if r["status"] == "BLOCKED")
    total = len(rows)

    md_lines = [
        f"# Batch Report",
        f"Batch ID: {args.batch_id}",
        f"Date: {date.today().isoformat()}",
        f"Total rows: {total}",
        "",
        "## Summary",
        f"- Complete: {complete}",
        f"- Failed: {failed}",
        f"- Blocked (QA gate): {blocked}",
        f"- Other: {total - complete - failed - blocked}",
        "",
        "## Per-row results",
        "| Slug | Type | Status | Word count | FAQ count | Int. links | QA result |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        md_lines.append(
            f"| {r['slug']} | {r['content_type']} | {r['status']} | "
            f"{r['word_count']} | {r['faq_count']} | {r['internal_link_count']} | {r['qa_result']} |"
        )

    fail_reasons = [r for r in rows if r["qa_fail_reasons"]]
    if fail_reasons:
        md_lines += ["", "## QA failures", ""]
        for r in fail_reasons:
            md_lines.append(f"- **{r['slug']}**: {r['qa_fail_reasons']}")

    batch_dir.mkdir(parents=True, exist_ok=True)

    (batch_dir / "aggregate.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    csv_path = batch_dir / "aggregate.csv"
    fieldnames = [
        "run_id", "slug", "content_type", "status", "word_count",
        "faq_count", "internal_link_count", "unresolved_links",
        "qa_result", "qa_fail_reasons", "time_seconds",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Aggregate report written to {batch_dir}/")
    print(f"  {complete}/{total} complete, {failed} failed, {blocked} blocked")


if __name__ == "__main__":
    main()
