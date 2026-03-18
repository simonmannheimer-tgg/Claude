#!/usr/bin/env bash
# Post a reply to Discussion #5 and mark the task as processed.
# Usage: BODY="text" TASK_ID="disc:xyz" ./scripts/github-post-comment.sh

set -euo pipefail

GITHUB_TOKEN="${GITHUB_TOKEN:-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}"
DISCUSSION_NODE_ID="${DISCUSSION_NODE_ID:-D_kwDORZ5UB84Ak6Oa}"
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel 2>/dev/null || echo '/home/user/Claude')"
TRACKING_FILE="$ROOT/.claude/processed-comments.txt"
touch "$TRACKING_FILE"

# Use Python to build + send the GraphQL mutation cleanly
python3 - <<PYEOF
import json, os, subprocess

body      = os.environ["BODY"]
disc_id   = os.environ.get("DISCUSSION_NODE_ID", "D_kwDORZ5UB84Ak6Oa")
token     = os.environ["GITHUB_TOKEN"]
task_id   = os.environ.get("TASK_ID", "")
tracking  = os.environ.get("TRACKING_FILE", ".claude/processed-comments.txt")

mutation = (
    'mutation { addDiscussionComment(input: { discussionId: '
    + json.dumps(disc_id)
    + ', body: '
    + json.dumps(body)
    + ' }) { comment { url } } }'
)

r = subprocess.run(
    ["curl", "-sf", "-X", "POST", "https://api.github.com/graphql",
     "-H", f"Authorization: Bearer {token}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps({"query": mutation})],
    capture_output=True, text=True, timeout=20
)
d = json.loads(r.stdout)
url = d.get("data", {}).get("addDiscussionComment", {}).get("comment", {}).get("url", "")
if url:
    print("Posted:", url)
    if task_id:
        with open(tracking, "a") as f:
            f.write(task_id + "\n")
else:
    print("ERROR:", r.stdout[:300])
    raise SystemExit(1)
PYEOF
