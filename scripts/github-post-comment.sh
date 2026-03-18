#!/usr/bin/env bash
# github-post-comment.sh <issue_number> <body_text>
# Posts a comment on a GitHub issue and marks the task ID as processed.
#
# Usage: ./scripts/github-post-comment.sh 42 "Here are your results..." comment:987654321

set -euo pipefail

ISSUE_NUM="${1:?Issue number required}"
BODY="${2:?Body text required}"
TASK_ID="${3:-}"

REPO="${GITHUB_REPO:-simonmannheimer-tgg/Claude}"
TRACKING_FILE="$(git rev-parse --show-toplevel 2>/dev/null || echo '.')/.claude/processed-comments.txt"
API="https://api.github.com"

touch "$TRACKING_FILE"

# Post the comment
response=$(curl -sf -X POST "$API/repos/$REPO/issues/$ISSUE_NUM/comments" \
  -H "Authorization: Bearer ${GITHUB_TOKEN:?GITHUB_TOKEN required}" \
  -H "Accept: application/vnd.github+json" \
  -H "Content-Type: application/json" \
  -d "$(python3 -c "import sys,json; print(json.dumps({'body': sys.argv[1]}))" "$BODY")")

comment_url=$(echo "$response" | python3 -c "import sys,json; print(json.load(sys.stdin)['html_url'])")

# Mark as processed
if [ -n "$TASK_ID" ]; then
  echo "$TASK_ID" >> "$TRACKING_FILE"
fi

echo "Posted: $comment_url"
