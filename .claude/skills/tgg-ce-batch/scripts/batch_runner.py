#!/usr/bin/env python3
"""
batch_runner.py — assigns stable run-ids and checks idempotency for batch jobs.

Reads the validated input CSV, assigns a run-id to each row (idempotent —
same slug always gets same run-id for a given date), checks which runs are
already complete, and outputs a JSON manifest for subagent dispatch.

Usage:
    python3 .claude/skills/tgg-ce-batch/scripts/batch_runner.py \
        --input batches/plp-intros-2026-q2.csv \
        --runs-dir runs \
        --output runs/batch-<id>/dispatch-manifest.json

Outputs JSON list of job objects with keys:
    run_id, keyword, slug, content_type, angle, byline, status
    status: PENDING | ALREADY_COMPLETE | RESUMABLE
"""

import argparse
import csv
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

MICRO_PIPELINE_TYPES = {"plp-intro", "faq-block"}


def make_run_id(slug: str) -> str:
    today = date.today().strftime("%Y-%m-%d")
    slug_clean = slug.strip("/").replace("/", "-").replace(" ", "-").lower()
    slug_hash = hashlib.sha1(slug_clean.encode()).hexdigest()[:6]
    return f"{today}-{slug_clean}-{slug_hash}"


def check_run_status(run_dir: Path) -> str:
    if not run_dir.exists():
        return "PENDING"

    final = run_dir / "final.md"
    if final.exists() and final.stat().st_size > 100:
        return "ALREADY_COMPLETE"

    status_file = run_dir / "pipeline-status.md"
    if status_file.exists() and status_file.stat().st_size > 0:
        text = status_file.read_text(encoding="utf-8")
        if "- [x]" in text:
            return "RESUMABLE"

    return "PENDING"


def get_last_completed_stage(run_dir: Path) -> int:
    status_file = run_dir / "pipeline-status.md"
    if not status_file.exists():
        return 0
    text = status_file.read_text(encoding="utf-8")
    completed = sum(1 for line in text.splitlines() if line.strip().startswith("- [x]"))
    return completed


def main() -> None:
    parser = argparse.ArgumentParser(description="Assign run-ids and build dispatch manifest.")
    parser.add_argument("--input", required=True, help="Validated input CSV path")
    parser.add_argument("--runs-dir", default="runs")
    parser.add_argument("--output", required=True, help="Output JSON manifest path")
    parser.add_argument("--concurrency", type=int, default=10, help="Max parallel subagents")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    runs_dir = repo_root / args.runs_dir
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    jobs: list[dict] = []

    with input_path.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row["slug"].strip()
            run_id = make_run_id(slug)
            run_dir = runs_dir / run_id
            status = check_run_status(run_dir)
            last_stage = get_last_completed_stage(run_dir) if status == "RESUMABLE" else 0
            content_type = row["content_type"].strip()

            jobs.append({
                "run_id": run_id,
                "keyword": row["keyword"].strip(),
                "slug": slug,
                "content_type": content_type,
                "angle": row.get("angle", "none").strip(),
                "byline": row.get("byline", "editorial").strip(),
                "pipeline_path": "micro" if content_type in MICRO_PIPELINE_TYPES else "full",
                "status": status,
                "resume_from_stage": last_stage + 1 if status == "RESUMABLE" else 1,
                "priority": int(row.get("priority", "3") or "3"),
            })

    jobs.sort(key=lambda j: (j["priority"], j["slug"]))

    pending = [j for j in jobs if j["status"] == "PENDING"]
    resumable = [j for j in jobs if j["status"] == "RESUMABLE"]
    already_done = [j for j in jobs if j["status"] == "ALREADY_COMPLETE"]

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(jobs, indent=2, ensure_ascii=False))

    print(f"Dispatch manifest written to {out_path}")
    print(f"  Total jobs: {len(jobs)}")
    print(f"  Pending: {len(pending)}")
    print(f"  Resumable: {len(resumable)}")
    print(f"  Already complete (skipping): {len(already_done)}")
    print(f"  Concurrency cap: {args.concurrency}")

    active = len(pending) + len(resumable)
    batches = (active + args.concurrency - 1) // args.concurrency
    print(f"  Estimated subagent batches: {batches}")


if __name__ == "__main__":
    main()
