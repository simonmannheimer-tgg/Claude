"""
Cloudflare Logpush ingestion for AEO bot traffic analysis.

Parses NDJSON log files from Cloudflare Logpush (R2 or local) and reports:
  - Request counts per known AI bot
  - Blocked vs allowed bot requests
  - Cache hit rate per bot
  - Top requested paths per bot

Cloudflare Logpush fields used:
  ClientRequestUserAgent, EdgeResponseStatus, CacheCacheStatus,
  ClientRequestPath, ClientRequestMethod, EdgeResponseBytes

Usage:
    python ingest_cf_logpush.py --file inbox/cf-logs-sample.ndjson
    python ingest_cf_logpush.py --file inbox/cf-logs.ndjson --date 2026-05-01
    python ingest_cf_logpush.py --dir inbox/cf-logs/  # processes all .ndjson files

Writes:
    seo/outputs/aeo/cf-bot-report-YYYYMMDD-HHMM.json
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml as _yaml
    def _load_bots() -> dict[str, str]:
        p = Path(__file__).parent / "shared" / "bots.yaml"
        if p.exists():
            bots = _yaml.safe_load(p.read_text())["bots"]
            return {b["name"]: b["ua"].lower() for b in bots}
        return {}
except ImportError:
    def _load_bots() -> dict[str, str]:
        return {}

# Fallback patterns if YAML unavailable
FALLBACK_BOT_PATTERNS = {
    "GPTBot":          "gptbot",
    "OAI-SearchBot":   "oai-searchbot",
    "ChatGPT-User":    "chatgpt-user",
    "ClaudeBot":       "claudebot",
    "Claude-User":     "claude-user",
    "Claude-SearchBot":"claude-searchbot",
    "PerplexityBot":   "perplexitybot",
    "Perplexity-User": "perplexity-user",
    "Google-Extended": "google-extended",
    "Bingbot":         "bingbot",
    "Applebot-Extended": "applebot-extended",
    "Meta-ExternalAgent": "meta-externalagent",
    "Amazonbot":       "amazonbot",
    "Bytespider":      "bytespider",
    "DuckDuckBot":     "duckduckbot",
    "YouBot":          "youbot",
    "CCBot":           "ccbot",
    "Diffbot":         "diffbot",
}

CACHE_HIT_STATUSES = {"hit", "stale", "revalidated", "updating"}
BLOCKED_HTTP_STATUSES = {403, 429, 503}


def _match_bot(ua: str, patterns: dict[str, str]) -> str | None:
    ua_lower = ua.lower()
    for bot_name, pattern in patterns.items():
        if pattern in ua_lower:
            return bot_name
    return None


def parse_log_file(path: Path, bot_patterns: dict[str, str]) -> dict:
    counts: dict[str, int] = defaultdict(int)
    blocked: dict[str, int] = defaultdict(int)
    cache_hits: dict[str, int] = defaultdict(int)
    cache_totals: dict[str, int] = defaultdict(int)
    top_paths: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    total_lines = 0
    parse_errors = 0

    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        total_lines += 1
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            parse_errors += 1
            continue

        ua = record.get("ClientRequestUserAgent", "") or ""
        bot = _match_bot(ua, bot_patterns)
        if not bot:
            continue

        counts[bot] += 1
        status = int(record.get("EdgeResponseStatus", 0) or 0)
        if status in BLOCKED_HTTP_STATUSES:
            blocked[bot] += 1

        cache_status = (record.get("CacheCacheStatus") or "").lower()
        cache_totals[bot] += 1
        if cache_status in CACHE_HIT_STATUSES:
            cache_hits[bot] += 1

        req_path = record.get("ClientRequestPath", "") or ""
        if req_path:
            top_paths[bot][req_path] += 1

    return {
        "total_lines": total_lines,
        "parse_errors": parse_errors,
        "counts": dict(counts),
        "blocked": dict(blocked),
        "cache_hits": dict(cache_hits),
        "cache_totals": dict(cache_totals),
        "top_paths": {
            bot: dict(sorted(paths.items(), key=lambda x: -x[1])[:10])
            for bot, paths in top_paths.items()
        },
    }


def merge_results(results: list[dict]) -> dict:
    merged: dict = {
        "total_lines": 0, "parse_errors": 0,
        "counts": defaultdict(int), "blocked": defaultdict(int),
        "cache_hits": defaultdict(int), "cache_totals": defaultdict(int),
        "top_paths": defaultdict(lambda: defaultdict(int)),
    }
    for r in results:
        merged["total_lines"] += r["total_lines"]
        merged["parse_errors"] += r["parse_errors"]
        for bot, n in r["counts"].items():
            merged["counts"][bot] += n
        for bot, n in r["blocked"].items():
            merged["blocked"][bot] += n
        for bot, n in r["cache_hits"].items():
            merged["cache_hits"][bot] += n
        for bot, n in r["cache_totals"].items():
            merged["cache_totals"][bot] += n
        for bot, paths in r["top_paths"].items():
            for path, n in paths.items():
                merged["top_paths"][bot][path] += n
    return {k: dict(v) if isinstance(v, defaultdict) else v for k, v in merged.items()}


def build_report(merged: dict) -> dict:
    counts = merged["counts"]
    blocked = merged["blocked"]
    cache_hits = merged["cache_hits"]
    cache_totals = merged["cache_totals"]
    top_paths = {
        bot: dict(sorted(paths.items(), key=lambda x: -x[1])[:10])
        for bot, paths in merged["top_paths"].items()
    }

    cache_hit_rate = {
        bot: round(cache_hits.get(bot, 0) / total * 100) if total else 0
        for bot, total in cache_totals.items()
    }
    blocked_pct = {
        bot: round(blocked.get(bot, 0) / total * 100) if total else 0
        for bot, total in counts.items()
    }

    # Sort bots by request count descending
    ranked = sorted(counts.items(), key=lambda x: -x[1])

    issues = []
    signals = []
    for bot, n in ranked:
        b_pct = blocked_pct.get(bot, 0)
        chr_ = cache_hit_rate.get(bot, 0)
        if b_pct >= 50:
            issues.append(f"{bot}: {b_pct}% of {n} requests blocked")
        elif b_pct == 0 and n > 0:
            signals.append(f"{bot}: {n} requests, all allowed, {chr_}% cache hit rate")

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "total_lines_processed": merged["total_lines"],
        "parse_errors": merged["parse_errors"],
        "bot_request_counts": dict(ranked),
        "blocked_counts": blocked,
        "blocked_pct": blocked_pct,
        "cache_hit_rate_pct": cache_hit_rate,
        "top_paths_per_bot": top_paths,
        "signals": signals[:10],
        "issues": issues[:10],
        "summary": (
            f"{len(counts)} AI bots seen | "
            f"{sum(counts.values())} total bot requests | "
            f"{len([b for b, p in blocked_pct.items() if p >= 50])} bots mostly blocked"
        ),
    }


def main():
    parser = argparse.ArgumentParser(description="Cloudflare Logpush AEO bot analysis")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Single NDJSON log file")
    group.add_argument("--dir", help="Directory of NDJSON log files")
    parser.add_argument("--date", help="Filter label for output filename (YYYY-MM-DD)")
    args = parser.parse_args()

    bot_patterns = _load_bots() or FALLBACK_BOT_PATTERNS

    if args.file:
        files = [Path(args.file)]
    else:
        files = sorted(Path(args.dir).glob("*.ndjson")) + sorted(Path(args.dir).glob("*.json"))
        if not files:
            print(f"ERROR: No .ndjson files found in {args.dir}", file=sys.stderr)
            sys.exit(1)

    print(f"Processing {len(files)} log file(s) with {len(bot_patterns)} bot patterns...")
    results = []
    for f in files:
        print(f"  {f.name}...")
        results.append(parse_log_file(f, bot_patterns))

    merged = merge_results(results)
    report = build_report(merged)

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = args.date or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    out_file = out_dir / f"cf-bot-report-{ts}.json"
    out_file.write_text(json.dumps(report, indent=2))

    print(f"\n{report['summary']}")
    for sig in report["signals"]:
        print(f"  ✓ {sig}")
    for issue in report["issues"]:
        print(f"  ✗ {issue}")
    print(f"\nSaved {out_file}")


if __name__ == "__main__":
    main()
