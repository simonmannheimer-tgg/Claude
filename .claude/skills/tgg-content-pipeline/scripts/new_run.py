#!/usr/bin/env python3
"""
new_run.py — creates the run folder skeleton for a tgg-content-pipeline run.

Usage:
    python3 .claude/skills/tgg-content-pipeline/scripts/new_run.py \
        --keyword "heat pump dryer" \
        --type buying-guide \
        --slug /buying-guides/heat-pump-dryer

Outputs:
    - Prints the run-id (YYYY-MM-DD-<slug-hash>) to stdout
    - Creates runs/<run-id>/ with empty placeholder files
"""

import argparse
import hashlib
import os
import sys
from datetime import date
from pathlib import Path

ARTEFACTS = [
    "intake.md",
    "seo-data.md",
    "competitive-extract.md",
    "existing-content.md",
    "brief.md",
    "outline.md",
    "draft.md",
    "qa-report.md",
    "humanised-draft.md",
    "final.md",
    "metadata.md",
    "internal-links.md",
    "faq.json",
]

VALID_TYPES = {"buying-guide", "how-to", "comparison", "eav-explainer"}


def make_run_id(slug: str) -> str:
    today = date.today().strftime("%Y-%m-%d")
    slug_clean = slug.strip("/").replace("/", "-").replace(" ", "-").lower()
    slug_hash = hashlib.sha1(slug_clean.encode()).hexdigest()[:6]
    return f"{today}-{slug_clean}-{slug_hash}"


def create_run(keyword: str, content_type: str, slug: str, runs_dir: Path) -> str:
    if content_type not in VALID_TYPES:
        print(
            f"Error: content_type must be one of {sorted(VALID_TYPES)}",
            file=sys.stderr,
        )
        sys.exit(1)

    run_id = make_run_id(slug)
    run_path = runs_dir / run_id

    if run_path.exists():
        print(f"Run folder already exists: {run_path}", file=sys.stderr)
        print(run_id)
        return run_id

    run_path.mkdir(parents=True)

    for artefact in ARTEFACTS:
        (run_path / artefact).touch()

    # Write a minimal status file so the orchestrator can track stage progress
    status_path = run_path / "pipeline-status.md"
    status_path.write_text(
        f"# Pipeline status\n\n"
        f"run_id: {run_id}\n"
        f"keyword: {keyword}\n"
        f"content_type: {content_type}\n"
        f"slug: {slug}\n"
        f"started: {date.today().isoformat()}\n\n"
        f"## Stages\n\n"
        + "\n".join(f"- [ ] Stage {i+1}" for i in range(9))
        + "\n"
    )

    return run_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new content pipeline run folder.")
    parser.add_argument("--keyword", required=True, help="Target keyword or topic")
    parser.add_argument(
        "--type",
        dest="content_type",
        required=True,
        choices=sorted(VALID_TYPES),
        help="Content type",
    )
    parser.add_argument("--slug", required=True, help="Proposed URL slug")
    parser.add_argument(
        "--runs-dir",
        default="runs",
        help="Path to runs directory (default: runs/)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    runs_dir = repo_root / args.runs_dir

    run_id = create_run(args.keyword, args.content_type, args.slug, runs_dir)
    print(run_id)


if __name__ == "__main__":
    main()
