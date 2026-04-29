#!/usr/bin/env bash
# Shared setup script — used by Codespaces (postCreateCommand) and the
# Claude Code on the web SessionStart hook. Idempotent: re-runs are safe.
#
# Installs:
#   - Python deps via uv sync
#   - GSC MCP (npm package mcp-gsc)
#   - Google Workspace MCP (pip package google-workspace-mcp)
#   - Filesystem MCP (npx-resolved at runtime; warm cache here)
#   - Claude Code CLI (if missing) + claude-seo plugin via marketplace
#   - Materialises GSC + GWS credentials JSONs from base64 secrets if present

set -euo pipefail

log() { printf '[setup] %s\n' "$*"; }

log "starting Claude Code workspace setup"

# 1. Python deps
if [ -f pyproject.toml ]; then
  log "running uv sync"
  uv sync --quiet || log "uv sync failed (continuing)"
fi

# 2. Node MCPs — installed globally so npx -y is fast
log "installing Node-based MCP servers"
npm install -g \
  mcp-gsc \
  @modelcontextprotocol/server-filesystem \
  semrush-mcp \
  firecrawl-mcp \
  @domdomegg/airtable-mcp-server 2>/dev/null || log "npm install partial (will fall back to npx -y at runtime)"

# 3. Python MCPs
log "installing Python MCP servers"
pip install --quiet --upgrade google-workspace-mcp 2>/dev/null || log "google-workspace-mcp pip install skipped"

# 4. Claude Code + claude-seo plugin
if ! command -v claude >/dev/null 2>&1; then
  log "installing Claude Code CLI"
  npm install -g @anthropic-ai/claude-code 2>/dev/null || log "Claude Code CLI install skipped"
fi
if command -v claude >/dev/null 2>&1; then
  log "ensuring claude-seo plugin is installed"
  claude plugin marketplace add AgriciDaniel/claude-seo 2>/dev/null || true
  claude plugin install claude-seo 2>/dev/null || true
fi

# 5. Materialise OAuth credentials from base64 secrets
mkdir -p /tmp/creds
if [ -n "${GSC_CREDENTIALS_JSON:-}" ]; then
  log "writing GSC credentials"
  printf '%s' "$GSC_CREDENTIALS_JSON" | base64 -d > /tmp/creds/gsc.json
  chmod 600 /tmp/creds/gsc.json
fi
if [ -n "${GOOGLE_WORKSPACE_CREDENTIALS_JSON:-}" ]; then
  log "writing Google Workspace credentials"
  printf '%s' "$GOOGLE_WORKSPACE_CREDENTIALS_JSON" | base64 -d > /tmp/creds/gws.json
  chmod 600 /tmp/creds/gws.json
fi

log "setup complete"
