#!/usr/bin/env bash
# github-poll.sh — polls open GitHub Issues for unprocessed @claude messages

set -euo pipefail

TOKEN="${PAT_TOKEN_GH:?PAT_TOKEN_GH is not set}"
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel 2>/dev/null || echo '/home/user/Claude')"
TRACKING_FILE="$ROOT/.claude/processed-comments.txt"
touch "$TRACKING_FILE"

RESULT=$(curl -sf "https://api.github.com/repos/simonmannheimer-tgg/Claude/issues?state=open&per_page=50" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json")

python3 - <<PYEOF
import json, os

tracking_file = "$TRACKING_FILE"
tracking = set(open(tracking_file).read().splitlines()) if os.path.exists(tracking_file) else set()

issues = json.loads(r"""$RESULT""")

pending = []
for issue in issues:
    if 'pull_request' in issue:
        continue
    number = issue['number']
    task_id = f'issue:{number}'
    if task_id in tracking:
        continue
    body  = issue.get('body') or ''
    title = issue.get('title') or ''
    if '@claude' not in body.lower() and '@claude' not in title.lower():
        continue
    task = (body or title).replace('@claude', '').replace('@Claude', '').strip()
    pending.append({'id': task_id, 'number': number, 'task': task})

print(json.dumps({'pending': pending}))
PYEOF
