#!/usr/bin/env bash
# github-poll.sh — polls open GitHub Issues for unprocessed @claude messages
# Checks both issue bodies and issue comments.

set -euo pipefail

TOKEN="${PAT_TOKEN_GH:?PAT_TOKEN_GH is not set}"
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel 2>/dev/null || echo '/home/user/Claude')"
TRACKING_FILE="$ROOT/.claude/processed-comments.txt"
touch "$TRACKING_FILE"

RESULT=$(curl -sf "https://api.github.com/repos/simonmannheimer-tgg/Claude/issues?state=open&per_page=50" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json")

python3 - "$TOKEN" "$TRACKING_FILE" <<PYEOF
import json, os, sys, urllib.request

token = sys.argv[1]
tracking_file = sys.argv[2]
tracking = set(open(tracking_file).read().splitlines()) if os.path.exists(tracking_file) else set()

def gh_get(url):
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.load(r)
    except Exception:
        return []

issues = json.loads(r"""$RESULT""")

pending = []
for issue in issues:
    if 'pull_request' in issue:
        continue
    number = issue['number']

    # Check issue body
    task_id = f'issue:{number}'
    if task_id not in tracking:
        body  = issue.get('body') or ''
        title = issue.get('title') or ''
        if '@claude' in body.lower() or '@claude' in title.lower():
            task = (body or title).replace('@claude', '').replace('@Claude', '').strip()
            pending.append({'id': task_id, 'number': number, 'task': task})

    # Check comments for @claude mentions
    comments = gh_get(
        f'https://api.github.com/repos/simonmannheimer-tgg/Claude/issues/{number}/comments?per_page=100'
    )
    for comment in comments:
        cid = comment.get('id')
        if not cid:
            continue
        cid_str = f'comment:{cid}'
        if cid_str in tracking:
            continue
        cbody = comment.get('body') or ''
        if '@claude' not in cbody.lower():
            continue
        user = comment.get('user', {})
        if user.get('type') == 'Bot' or user.get('login', '').endswith('[bot]'):
            continue
        task = cbody.replace('@claude', '').replace('@Claude', '').strip()
        pending.append({'id': cid_str, 'number': number, 'task': task})

print(json.dumps({'pending': pending}))
PYEOF
