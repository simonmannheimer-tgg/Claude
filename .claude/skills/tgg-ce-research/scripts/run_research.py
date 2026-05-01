#!/usr/bin/env python3
"""
run_research.py — deterministic keyword and competitor research fetch.

Queries Semrush AU database for keyword metrics and related queries.
Outputs structured JSON for merging into seo-data.md.

Usage:
    python3 .claude/skills/tgg-ce-research/scripts/run_research.py \
        --keyword "heat pump dryer" \
        --market au \
        --competitors jbhifi.com.au,harveynorman.com.au,appliancesonline.com.au \
        --output runs/<run-id>/seo-data-raw.json

Environment:
    SEMRUSH_API_KEY — required

Outputs JSON with keys:
    keyword_metrics, related_queries, competitor_rankings
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

SEMRUSH_BASE = "https://api.semrush.com/"
DATABASE = "au"


def semrush_get(action: str, params: dict) -> list[dict]:
    api_key = os.environ.get("SEMRUSH_API_KEY")
    if not api_key:
        raise EnvironmentError("SEMRUSH_API_KEY environment variable not set")

    params["key"] = api_key
    params["action"] = action
    params["export_columns"] = params.get("export_columns", "")

    url = SEMRUSH_BASE + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            raw = resp.read().decode("utf-8").strip()
    except Exception as exc:
        raise RuntimeError(f"Semrush request failed: {exc}") from exc

    if not raw or raw.startswith("ERROR"):
        raise RuntimeError(f"Semrush API error: {raw[:200]}")

    lines = raw.splitlines()
    if len(lines) < 2:
        return []

    headers = lines[0].split(";")
    rows = []
    for line in lines[1:]:
        values = line.split(";")
        rows.append(dict(zip(headers, values)))
    return rows


def fetch_keyword_metrics(keyword: str) -> dict:
    rows = semrush_get(
        "phrase_this",
        {
            "phrase": keyword,
            "database": DATABASE,
            "export_columns": "Ph,Nq,Cp,Co,Nr,Td",
        },
    )
    if not rows:
        return {}
    r = rows[0]
    return {
        "keyword": r.get("Keyword", keyword),
        "volume_au": r.get("Search Volume", ""),
        "kd": r.get("Keyword Difficulty Index", ""),
        "cpc": r.get("CPC", ""),
        "competition": r.get("Competition", ""),
        "results_count": r.get("Number of Results", ""),
    }


def fetch_related_queries(keyword: str, limit: int = 15) -> list[dict]:
    rows = semrush_get(
        "phrase_related",
        {
            "phrase": keyword,
            "database": DATABASE,
            "display_limit": limit,
            "export_columns": "Ph,Nq,Co",
        },
    )
    return [
        {
            "query": r.get("Keyword", ""),
            "volume_au": r.get("Search Volume", ""),
            "competition": r.get("Competition", ""),
        }
        for r in rows
    ]


def fetch_competitor_rankings(keyword: str, competitors: list[str]) -> list[dict]:
    rows = semrush_get(
        "phrase_organic",
        {
            "phrase": keyword,
            "database": DATABASE,
            "display_limit": 20,
            "export_columns": "Dn,Ur,Po,Tr,Nq",
        },
    )
    results = []
    for r in rows:
        domain = r.get("Domain", "")
        if any(comp in domain for comp in competitors) or not competitors:
            results.append(
                {
                    "domain": domain,
                    "url": r.get("URL", ""),
                    "position": r.get("Position", ""),
                    "traffic": r.get("Traffic", ""),
                }
            )
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch SEO research data from Semrush.")
    parser.add_argument("--keyword", required=True)
    parser.add_argument("--market", default="au")
    parser.add_argument("--competitors", default="", help="Comma-separated competitor domains")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    args = parser.parse_args()

    competitor_list = [c.strip() for c in args.competitors.split(",") if c.strip()]

    output: dict = {
        "keyword": args.keyword,
        "market": args.market,
        "keyword_metrics": {},
        "related_queries": [],
        "competitor_rankings": [],
        "errors": [],
    }

    try:
        output["keyword_metrics"] = fetch_keyword_metrics(args.keyword)
    except Exception as exc:
        output["errors"].append(f"keyword_metrics: {exc}")

    try:
        output["related_queries"] = fetch_related_queries(args.keyword)
    except Exception as exc:
        output["errors"].append(f"related_queries: {exc}")

    try:
        output["competitor_rankings"] = fetch_competitor_rankings(args.keyword, competitor_list)
    except Exception as exc:
        output["errors"].append(f"competitor_rankings: {exc}")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))

    if output["errors"]:
        print(f"Completed with {len(output['errors'])} error(s):", file=sys.stderr)
        for err in output["errors"]:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)

    print(f"Research data written to {out_path}")


if __name__ == "__main__":
    main()
