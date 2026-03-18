#!/usr/bin/env bash
# github-poll.sh — polls GitHub Discussion #5 for unprocessed @claude replies

set -euo pipefail

GITHUB_TOKEN="${GITHUB_TOKEN:-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}"
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel 2>/dev/null || echo '/home/user/Claude')"
TRACKING_FILE="$ROOT/.claude/processed-comments.txt"
touch "$TRACKING_FILE"

# GraphQL: fetch last 50 comments on Discussion #5
GQL='{"query":"{ repository(owner:\"simonmannheimer-tgg\", name:\"Claude\") { discussion(number:5) { comments(last:50) { nodes { id databaseId author { login __typename } body } } } } }"}'

RESULT=$(curl -sf -X POST "https://api.github.com/graphql" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d "$GQL")

python3 - "$TRACKING_FILE" <<'PYEOF'
import json, sys

result = json.loads(sys.stdin.read().split('\n', 1)[0] if False else open('/dev/stdin').read()) if False else None

import subprocess, os
tracking_file = sys.argv[1]
tracking = set(open(tracking_file).read().splitlines()) if os.path.exists(tracking_file) else set()

# Read result from the curl output captured in env
import os
result_str = os.environ.get('_POLL_RESULT', '')
PYEOF

# Do it cleanly in Python
python3 - <<PYEOF
import json, os, sys

tracking_file = "$TRACKING_FILE"
tracking = set(open(tracking_file).read().splitlines()) if os.path.exists(tracking_file) else set()

result = json.loads(r"""$RESULT""")
comments = result['data']['repository']['discussion']['comments']['nodes']

pending = []
for c in comments:
    node_id = c['id']
    author = (c.get('author') or {}).get('login', 'ghost')
    atype   = (c.get('author') or {}).get('__typename', '')
    body    = c.get('body') or ''

    if atype == 'Bot' or '[bot]' in author:
        continue
    if '@claude' not in body.lower():
        continue
    if f'disc:{node_id}' in tracking:
        continue

    task = body.replace('@claude', '').replace('@Claude', '').strip()
    pending.append({'id': f'disc:{node_id}', 'db_id': c['databaseId'], 'task': task})

print(json.dumps({'pending': pending}))
PYEOF
