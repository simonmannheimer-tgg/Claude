#!/usr/bin/env bash
# SessionStart hook for Claude Code on the web.
# Bootstraps the workspace so MCPs declared in .claude/settings.json
# can find their binaries and credentials.
#
# Configured under "hooks": { "SessionStart": [...] } in .claude/settings.json.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LOG_FILE="$REPO_ROOT/.claude/session_start.log"

{
  echo ""
  echo "=== SessionStart $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  bash "$REPO_ROOT/.devcontainer/setup.sh"
  echo "=== SessionStart complete ==="
} >> "$LOG_FILE" 2>&1 || true

# Always exit 0 — never block the session on setup failure.
exit 0
