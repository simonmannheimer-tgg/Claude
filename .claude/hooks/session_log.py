#!/usr/bin/env python3
"""
Stop hook — appends session-end marker to .claude/session_log.txt
"""
import sys, json, os
from datetime import datetime

try:
    payload = json.load(sys.stdin)
except Exception:
    payload = {}

log = os.path.join(os.path.dirname(__file__), "..", "session_log.txt")
reason = payload.get("stop_reason", "unknown")

with open(log, "a") as f:
    f.write(f"--- SESSION END {datetime.now().isoformat()} | {reason} ---\n")

sys.exit(0)
