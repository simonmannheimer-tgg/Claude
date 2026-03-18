#!/usr/bin/env bash
# loop-daemon.sh — background daemon that polls GitHub Discussion #5
# and processes @claude messages using the claude CLI.
# Started automatically by the SessionStart hook.
# Uses a lock file to prevent multiple instances.

LOCK="/tmp/claude-loop.lock"
LOG="/tmp/claude-loop.log"
ROOT="/home/user/Claude"

# Single-instance guard
if [ -f "$LOCK" ] && kill -0 "$(cat "$LOCK")" 2>/dev/null; then
  exit 0  # already running
fi
echo $$ > "$LOCK"
trap 'rm -f "$LOCK"' EXIT

export GITHUB_TOKEN="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"
export GITHUB_REPO="simonmannheimer-tgg/Claude"

echo "[$(date)] Loop daemon started (PID $$)" >> "$LOG"

cd "$ROOT"

while true; do
  POLL=$(bash scripts/github-poll.sh 2>>"$LOG" || echo '{"pending":[]}')
  COUNT=$(echo "$POLL" | python3 -c "import sys,json; print(len(json.load(sys.stdin).get('pending',[])))" 2>/dev/null || echo 0)

  if [ "$COUNT" -gt 0 ]; then
    echo "[$(date)] Processing $COUNT task(s)..." >> "$LOG"
    echo "$POLL" | python3 scripts/process-tasks.py >> "$LOG" 2>&1
  fi

  sleep 30  # poll every 30 seconds
done
