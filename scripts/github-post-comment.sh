#!/usr/bin/env bash
# Post a reply to a GitHub Issue and mark the task as processed.
# Usage: BODY="text" TASK_ID="issue:123" ISSUE_NUMBER=123 ./scripts/github-post-comment.sh

set -euo pipefail

ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel 2>/dev/null || echo '/home/user/Claude')"
TRACKING_FILE="$ROOT/.claude/processed-comments.txt"
touch "$TRACKING_FILE"

python3 - <<PYEOF
import json, os, subprocess

body         = os.environ["BODY"]
issue_number = os.environ["ISSUE_NUMBER"]
token        = os.environ["PAT_TOKEN_GH"]
task_id      = os.environ.get("TASK_ID", "")
tracking     = "$TRACKING_FILE"
repo         = "simonmannheimer-tgg/Claude"

# Post comment
r = subprocess.run(
    ["curl", "-sf", "-X", "POST",
     f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments",
     "-H", f"Authorization: Bearer {token}",
     "-H", "Accept: application/vnd.github+json",
     "-H", "Content-Type: application/json",
     "-d", json.dumps({"body": body})],
    capture_output=True, text=True, timeout=20
)
d = json.loads(r.stdout)
url = d.get("html_url", "")
if url:
    print("Posted:", url)
    if task_id:
        with open(tracking, "a") as f:
            f.write(task_id + "\n")
    # Close the issue as completed
    subprocess.run(
        ["curl", "-sf", "-X", "PATCH",
         f"https://api.github.com/repos/{repo}/issues/{issue_number}",
         "-H", f"Authorization: Bearer {token}",
         "-H", "Accept: application/vnd.github+json",
         "-H", "Content-Type: application/json",
         "-d", json.dumps({"state": "closed", "state_reason": "completed"})],
        capture_output=True, timeout=20
    )
else:
    print("ERROR:", r.stdout[:300])
    raise SystemExit(1)
PYEOF
