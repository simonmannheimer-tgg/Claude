#!/usr/bin/env bash
# github-poll.sh
# Polls GitHub for unprocessed @claude comments and prints them as structured JSON.
# Called by the /check-github slash command.
#
# Required env: GITHUB_TOKEN, GITHUB_REPO (e.g. simonmannheimer-tgg/Claude)
# Tracking file: .claude/processed-comments.txt (git-ignored)

set -euo pipefail

REPO="${GITHUB_REPO:-simonmannheimer-tgg/Claude}"
TRACKING_FILE="$(git rev-parse --show-toplevel 2>/dev/null || echo '.')/.claude/processed-comments.txt"
API="https://api.github.com"
HEADER_AUTH="Authorization: Bearer ${GITHUB_TOKEN:?GITHUB_TOKEN env var is required}"
HEADER_ACCEPT="Accept: application/vnd.github+json"

touch "$TRACKING_FILE"

pending=()

# Fetch open issues (up to 50)
issues=$(curl -sf "$API/repos/$REPO/issues?state=open&per_page=50" \
  -H "$HEADER_AUTH" -H "$HEADER_ACCEPT")

issue_count=$(echo "$issues" | python3 -c "import sys,json; print(len(json.load(sys.stdin)))")

for i in $(seq 0 $((issue_count - 1))); do
  issue_num=$(echo "$issues" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$i]['number'])")
  issue_title=$(echo "$issues" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$i]['title'])")

  # Check issue body for @claude
  issue_body=$(echo "$issues" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$i].get('body') or '')")
  issue_id=$(echo "$issues" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$i]['id'])")

  if echo "$issue_body" | grep -q '@claude' && ! grep -qxF "issue:$issue_id" "$TRACKING_FILE"; then
    pending+=("{\"type\":\"issue\",\"id\":\"issue:$issue_id\",\"number\":$issue_num,\"title\":$(echo "$issue_title" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().rstrip()))"),\"task\":$(echo "$issue_body" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().rstrip()))")}")
  fi

  # Fetch comments for this issue
  comments=$(curl -sf "$API/repos/$REPO/issues/$issue_num/comments?per_page=50" \
    -H "$HEADER_AUTH" -H "$HEADER_ACCEPT")

  comment_count=$(echo "$comments" | python3 -c "import sys,json; print(len(json.load(sys.stdin)))")

  for j in $(seq 0 $((comment_count - 1))); do
    comment_id=$(echo "$comments" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$j]['id'])")
    author_type=$(echo "$comments" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$j]['user'].get('type','User'))")
    author=$(echo "$comments" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$j]['user']['login'])")
    body=$(echo "$comments" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[$j]['body'])")

    # Skip bots and already-processed
    [ "$author_type" = "Bot" ] && continue
    [[ "$author" == *"[bot]"* ]] && continue
    echo "$body" | grep -q '@claude' || continue
    grep -qxF "comment:$comment_id" "$TRACKING_FILE" && continue

    pending+=("{\"type\":\"comment\",\"id\":\"comment:$comment_id\",\"number\":$issue_num,\"title\":$(echo "$issue_title" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().rstrip()))"),\"task\":$(echo "$body" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().rstrip()))")}")
  done
done

if [ ${#pending[@]} -eq 0 ]; then
  echo '{"pending":[]}'
else
  echo '{"pending":['$(IFS=,; echo "${pending[*]}")']}'
fi
