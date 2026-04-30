#!/usr/bin/env python3
"""Pull top queries from Google Search Console and write a CSV.

Used by .github/workflows/gsc-weekly-pull.yml. Works with either:
  - OAuth refresh-token credentials JSON (`installed` / `web` client + token), or
  - A service account JSON (the service account must be added as a user on the
    GSC property in Search Console settings).

Usage:
    python scripts/gsc_weekly_pull.py \\
        --credentials /tmp/creds/gsc.json \\
        --site-url https://www.thegoodguys.com.au/ \\
        --days 28 \\
        --output seo/outputs/gsc/gsc-2026-04-29.csv
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path

from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def load_credentials(path: Path):
    raw = json.loads(path.read_text())
    if raw.get("type") == "service_account":
        return service_account.Credentials.from_service_account_info(raw, scopes=SCOPES)
    if "refresh_token" in raw:
        return Credentials(
            token=raw.get("token"),
            refresh_token=raw["refresh_token"],
            token_uri=raw.get("token_uri", "https://oauth2.googleapis.com/token"),
            client_id=raw["client_id"],
            client_secret=raw["client_secret"],
            scopes=SCOPES,
        )
    raise SystemExit("Unrecognised credentials JSON — need service account or OAuth refresh token.")


def pull_queries(service, site_url: str, days: int, row_limit: int = 1000):
    end = dt.date.today() - dt.timedelta(days=2)
    start = end - dt.timedelta(days=days)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": ["query"],
        "rowLimit": row_limit,
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=body).execute()
    return response.get("rows", []), start, end


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--credentials", required=True, type=Path)
    parser.add_argument("--site-url", required=True)
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    creds = load_credentials(args.credentials)
    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    rows, start, end = pull_queries(service, args.site_url, args.days)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["query", "clicks", "impressions", "ctr", "position", "start_date", "end_date"])
        for row in rows:
            keys = row.get("keys", [""])
            writer.writerow([
                keys[0],
                row.get("clicks", 0),
                row.get("impressions", 0),
                round(row.get("ctr", 0.0), 6),
                round(row.get("position", 0.0), 2),
                start.isoformat(),
                end.isoformat(),
            ])

    print(f"Wrote {len(rows)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
