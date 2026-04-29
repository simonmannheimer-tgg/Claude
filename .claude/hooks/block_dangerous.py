#!/usr/bin/env python3
"""
PreToolUse hook — blocks dangerous bash patterns before execution.
Exit 2 = block. Exit 0 = allow.
"""
import sys, json

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

if payload.get("tool_name") != "Bash":
    sys.exit(0)

cmd = payload.get("tool_input", {}).get("command", "")

BLOCKED = [
    "rm -rf /", "rm -rf ~", "rm -rf .",
    "git push --force", "git push -f ",
    "git reset --hard",
    "> .env", ">> .env",
    "curl | bash", "curl|bash",
    "wget | bash", "wget|bash",
    "irm |", "Invoke-Expression",
    "DROP TABLE", "DROP DATABASE",
]

for pattern in BLOCKED:
    if pattern.lower() in cmd.lower():
        print(f"[block_dangerous] BLOCKED: matched '{pattern}'", file=sys.stderr)
        sys.exit(2)

sys.exit(0)
