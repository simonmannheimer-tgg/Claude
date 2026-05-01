#!/usr/bin/env python3
"""
csv_validator.py — validates a batch input CSV before dispatching subagents.

Checks required columns, valid content_type values, slug format, and byline values.
Exits 0 if valid, 1 if any rows fail validation (prints failure details to stderr).

Usage:
    python3 .claude/skills/tgg-ce-batch/scripts/csv_validator.py \
        --input batches/plp-intros-2026-q2.csv

Outputs:
    - Prints validation summary to stdout
    - Prints per-row failures to stderr (if any)
    - Exits 0 (valid) or 1 (invalid)
"""

import argparse
import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = {"keyword", "slug", "content_type", "angle", "byline"}
VALID_CONTENT_TYPES = {
    "buying-guide",
    "how-to",
    "comparison",
    "eav-explainer",
    "plp-intro",
    "faq-block",
}
VALID_BYLINES = {"simon", "editorial", "uncredited"}
OPTIONAL_COLUMNS = {"priority", "must_cover", "existing_url"}


def validate_row(row: dict, row_num: int) -> list[str]:
    errors: list[str] = []

    slug = row.get("slug", "").strip()
    if not slug.startswith("/"):
        errors.append(f"slug must start with '/' (got: '{slug}')")

    content_type = row.get("content_type", "").strip()
    if content_type not in VALID_CONTENT_TYPES:
        errors.append(
            f"content_type '{content_type}' not valid — must be one of: {sorted(VALID_CONTENT_TYPES)}"
        )

    byline = row.get("byline", "").strip()
    if byline not in VALID_BYLINES:
        errors.append(
            f"byline '{byline}' not valid — must be one of: {sorted(VALID_BYLINES)}"
        )

    keyword = row.get("keyword", "").strip()
    if not keyword:
        errors.append("keyword is empty")

    angle = row.get("angle", "").strip()
    if not angle:
        errors.append("angle is empty — use 'none' to explicitly skip")

    priority = row.get("priority", "").strip()
    if priority and not priority.isdigit():
        errors.append(f"priority must be an integer (got: '{priority}')")
    elif priority and not (1 <= int(priority) <= 5):
        errors.append(f"priority must be 1–5 (got: '{priority}')")

    return [f"Row {row_num}: {e}" for e in errors]


def validate_csv(path: Path) -> tuple[int, list[str]]:
    all_errors: list[str] = []

    try:
        with path.open(encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            columns = set(reader.fieldnames or [])

            missing = REQUIRED_COLUMNS - columns
            if missing:
                all_errors.append(f"Missing required columns: {sorted(missing)}")
                return 0, all_errors

            unexpected = columns - REQUIRED_COLUMNS - OPTIONAL_COLUMNS
            if unexpected:
                print(f"Warning: unexpected columns (will be ignored): {sorted(unexpected)}")

            row_count = 0
            for row_num, row in enumerate(reader, start=2):
                row_count += 1
                errors = validate_row(row, row_num)
                all_errors.extend(errors)

    except FileNotFoundError:
        all_errors.append(f"File not found: {path}")
        return 0, all_errors
    except Exception as exc:
        all_errors.append(f"Failed to read CSV: {exc}")
        return 0, all_errors

    return row_count, all_errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a batch input CSV.")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    args = parser.parse_args()

    path = Path(args.input)
    row_count, errors = validate_csv(path)

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        print(f"\nValidation FAILED — {len(errors)} error(s) in {path}")
        sys.exit(1)

    print(f"Validation PASSED — {row_count} rows in {path}")


if __name__ == "__main__":
    main()
