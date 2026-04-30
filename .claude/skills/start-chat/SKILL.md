---
name: start-chat
description: "Start the Claude Code Chat UI server on port 7860."
---

# Start Chat

Start the Claude Code Chat UI server on port 7860.

## Steps

1. Check if the server is already running:
   ```bash
   curl -s http://localhost:7860/ > /dev/null 2>&1 && echo "already running" || echo "not running"
   ```
   If already running, tell the user: "Chat UI is already running at http://localhost:7860"

2. If not running, start it in the background:
   ```bash
   CHAT_PORT=7860 python3 chat_ui/server.py &
   echo "PID: $!"
   ```
   Wait 2 seconds, then verify it started:
   ```bash
   curl -s http://localhost:7860/ | head -3
   ```

3. Tell the user:
   - The UI is running at **http://localhost:7860**
   - In Claude Code on the web, use the port-forward button (if available) or open via the preview panel
   - Set `export GITHUB_TOKEN=<pat>` to enable GitHub issue integration
   - Use `/check-github` to manually poll GitHub for @claude tasks
   - The server runs until you stop this session or kill the process
