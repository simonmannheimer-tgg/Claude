#!/usr/bin/env python3
"""
PostToolUse hook — logs every file write/edit to .claude/write_log.txt
"""
import sys, json, os
from datetime import datetime

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

if payload.get("tool_name") not in ("Write", "Edit", "MultiEdit"):
    sys.exit(0)

file_path = payload.get("tool_input", {}).get("file_path", "unknown")
log = os.path.join(os.path.dirname(__file__), "..", "write_log.txt")

try:
    with open(log, "a") as f:
        f.write(f"{datetime.now().isoformat()} | {payload.get('tool_name')} | {file_path}\n")
except Exception:
    pass

sys.exit(0)
