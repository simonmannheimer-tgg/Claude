#!/usr/bin/env python3
"""Claude Code Chat UI — claude.ai-style interface for Claude Code + GitHub + SEO agents."""

import json
import os
import subprocess
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import urllib.request
import urllib.error

PORT = int(os.environ.get("CHAT_PORT", 7860))
REPO = os.environ.get("GITHUB_REPO", "simonmannheimer-tgg/Claude")

# In-memory state
sessions: dict[str, list] = {}   # session_id -> [{"role", "content"}]
session_names: dict[str, str] = {}  # session_id -> display name

SYSTEM_PROMPTS = {
    "general": (
        "You are Claude, running inside a Claude Code session for thegoodguys.com.au. "
        "You have access to code editing, GitHub, and SEO tools. Be concise. Use markdown."
    ),
    "seo": (
        "You are the SEO Team Lead for thegoodguys.com.au. "
        "Coordinate PLP copy, metadata, FAQs, keyword research, competitor analysis. "
        "Target domain: thegoodguys.com.au. Competitors: jbhifi.com.au, harveynorman.com.au. "
        "Structure responses clearly with headings. Use markdown."
    ),
    "github": (
        "You are Claude managing GitHub issues for the thegoodguys.com.au SEO project. "
        f"The repo is: {REPO}. Help create, review, and respond to issues. Use markdown."
    ),
    "code": (
        "You are Claude Code, an expert software engineer. "
        "You can read, write, and modify code files. Be precise. Explain what you do. Use markdown."
    ),
}

AGENT_LABELS = {
    "general": "General",
    "seo": "SEO Team Lead",
    "github": "GitHub",
    "code": "Code",
}


def github_api(path: str, method: str = "GET", body: dict | None = None) -> dict | list | None:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        return None
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if body:
        data = json.dumps(body).encode()
        req.add_header("Content-Type", "application/json")
        req.data = data
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def run_claude(prompt: str, system: str) -> str:
    full_prompt = f"{system}\n\n---\n\n{prompt}"
    try:
        proc = subprocess.run(
            ["claude", "--print"],
            input=full_prompt,
            capture_output=True, text=True, timeout=120
        )
        return proc.stdout.strip() or proc.stderr.strip() or "(no response)"
    except Exception as e:
        return f"Error running claude: {e}"


def format_history(messages: list, agent: str, new_message: str) -> str:
    system = SYSTEM_PROMPTS.get(agent, SYSTEM_PROMPTS["general"])
    parts = []
    for m in messages:
        role = "User" if m["role"] == "user" else "Assistant"
        parts.append(f"{role}: {m['content']}")
    parts.append(f"User: {new_message}")
    conversation = "\n\n".join(parts)
    return run_claude(conversation, system)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # suppress default logging

    def send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def send_sse_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def sse_event(self, data: str):
        payload = f"data: {json.dumps(data)}\n\n"
        self.wfile.write(payload.encode())
        self.wfile.flush()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if path == "/":
            self.serve_html()
        elif path == "/api/sessions":
            result = [
                {"id": sid, "name": session_names.get(sid, f"Chat {i+1}"), "count": len(msgs)}
                for i, (sid, msgs) in enumerate(sessions.items())
            ]
            self.send_json(result)
        elif path == "/api/issues":
            issues = github_api(f"/repos/{REPO}/issues?state=open&per_page=30")
            if issues is None:
                self.send_json({"error": "GITHUB_TOKEN not set or API error"}, 401)
            else:
                self.send_json([{"number": i["number"], "title": i["title"], "url": i["html_url"]} for i in issues])
        elif path == "/stream":
            self.handle_stream(qs)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        if parsed.path == "/api/sessions":
            sid = str(uuid.uuid4())[:8]
            sessions[sid] = []
            session_names[sid] = body.get("name", "New chat")
            self.send_json({"id": sid})
        elif parsed.path == "/api/issues/comment":
            num = body.get("number")
            text = body.get("body", "")
            result = github_api(f"/repos/{REPO}/issues/{num}/comments", "POST", {"body": text})
            if result:
                self.send_json({"url": result.get("html_url", "")})
            else:
                self.send_json({"error": "Failed to post comment"}, 500)
        elif parsed.path == "/api/issues/create":
            result = github_api(f"/repos/{REPO}/issues", "POST", {
                "title": body.get("title", "New task"),
                "body": body.get("body", ""),
                "labels": body.get("labels", []),
            })
            if result:
                self.send_json({"number": result["number"], "url": result["html_url"]})
            else:
                self.send_json({"error": "Failed to create issue"}, 500)
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/sessions/"):
            sid = parsed.path.split("/")[-1]
            sessions.pop(sid, None)
            session_names.pop(sid, None)
            self.send_json({"ok": True})
        else:
            self.send_response(404)
            self.end_headers()

    def handle_stream(self, qs):
        sid = qs.get("session", [""])[0]
        message = qs.get("msg", [""])[0]
        agent = qs.get("agent", ["general"])[0]

        if not message or not sid:
            self.send_json({"error": "Missing msg or session"}, 400)
            return

        self.send_sse_headers()

        # Auto-name the session from first message
        if sid in sessions and len(sessions[sid]) == 0:
            session_names[sid] = (message[:40] + "…") if len(message) > 40 else message

        history = sessions.get(sid, [])

        def do_work():
            try:
                response = format_history(history, agent, message)
                return response
            except Exception as e:
                return f"Error: {e}"

        result_holder = [None]
        t = threading.Thread(target=lambda: result_holder.__setitem__(0, do_work()))
        t.start()

        # While waiting, send keep-alive pings
        while t.is_alive():
            try:
                self.sse_event({"type": "ping"})
            except Exception:
                return
            time.sleep(2)
        t.join()

        response = result_holder[0] or "(empty response)"

        # Stream response character by character (simulate typing)
        CHARS_PER_SEC = 800
        delay = 1.0 / CHARS_PER_SEC
        chunk_size = 4

        try:
            for i in range(0, len(response), chunk_size):
                chunk = response[i:i + chunk_size]
                self.sse_event({"type": "token", "text": chunk})
                if i % 80 == 0:
                    time.sleep(delay * chunk_size)
        except Exception:
            pass

        # Save to history
        if sid not in sessions:
            sessions[sid] = []
        sessions[sid].append({"role": "user", "content": message})
        sessions[sid].append({"role": "assistant", "content": response})

        try:
            self.sse_event({"type": "done"})
        except Exception:
            pass

    def serve_html(self):
        html = build_html()
        body = html.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def build_html() -> str:
    agents_json = json.dumps(AGENT_LABELS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Claude Code Chat</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js"></script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#0f0f11;--sidebar:#17171b;--surface:#1c1c20;--surface2:#242428;
  --border:#2a2a30;--text:#e8e8ea;--muted:#888;--accent:#d97706;
  --user-bg:#1e3a5f;--code-bg:#111118;--radius:12px;
  --font:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
}}
html,body{{height:100%;background:var(--bg);color:var(--text);font-family:var(--font);font-size:15px}}
a{{color:var(--accent);text-decoration:none}}
/* Layout */
#app{{display:flex;height:100vh;overflow:hidden}}
/* Sidebar */
#sidebar{{width:260px;min-width:260px;background:var(--sidebar);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}}
#sidebar-header{{padding:16px;font-weight:700;font-size:16px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:8px}}
#sidebar-header span{{color:var(--accent)}}
#sidebar-sections{{flex:1;overflow-y:auto;padding:8px}}
.section-label{{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);padding:12px 8px 4px}}
.new-btn{{display:flex;align-items:center;gap:6px;padding:8px 10px;border-radius:8px;cursor:pointer;font-size:13px;color:var(--muted);transition:background .15s;margin:2px 0}}
.new-btn:hover{{background:var(--surface2);color:var(--text)}}
.new-btn svg{{flex-shrink:0}}
.chat-item{{display:flex;align-items:center;gap:6px;padding:8px 10px;border-radius:8px;cursor:pointer;font-size:13px;transition:background .15s;margin:2px 0;color:var(--muted)}}
.chat-item:hover,.chat-item.active{{background:var(--surface2);color:var(--text)}}
.chat-item .del{{margin-left:auto;opacity:0;font-size:11px;color:var(--muted);padding:2px 4px;border-radius:4px}}
.chat-item:hover .del{{opacity:1}}
.chat-item .del:hover{{background:var(--border);color:#e55}}
.issue-item{{display:flex;align-items:flex-start;gap:8px;padding:8px 10px;border-radius:8px;cursor:pointer;font-size:13px;transition:background .15s;margin:2px 0;color:var(--muted)}}
.issue-item:hover{{background:var(--surface2);color:var(--text)}}
.issue-item .num{{color:var(--accent);font-size:11px;font-weight:600;flex-shrink:0;padding-top:1px}}
.issue-item .title{{line-height:1.3}}
#github-status{{padding:8px 10px;font-size:12px;color:var(--muted)}}
/* Main */
#main{{flex:1;display:flex;flex-direction:column;overflow:hidden}}
/* Top bar */
#topbar{{padding:12px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px;background:var(--bg)}}
#topbar h1{{font-size:15px;font-weight:600;flex:1}}
#agent-select{{background:var(--surface);border:1px solid var(--border);color:var(--text);padding:6px 10px;border-radius:8px;font-size:13px;cursor:pointer;outline:none}}
#agent-select:focus{{border-color:var(--accent)}}
/* Messages */
#messages{{flex:1;overflow-y:auto;padding:24px 0}}
#messages-inner{{max-width:780px;margin:0 auto;padding:0 24px}}
.msg{{margin-bottom:24px;animation:fadeIn .2s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
.msg-user{{display:flex;justify-content:flex-end}}
.msg-user .bubble{{background:var(--user-bg);border-radius:var(--radius) var(--radius) 4px var(--radius);padding:12px 16px;max-width:85%;line-height:1.6}}
.msg-assistant{{display:flex;gap:12px;align-items:flex-start}}
.avatar{{width:28px;height:28px;border-radius:50%;background:var(--accent);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0;margin-top:2px}}
.msg-content{{flex:1;line-height:1.7;max-width:100%}}
.msg-content h1,.msg-content h2,.msg-content h3{{margin:16px 0 8px;font-weight:600}}
.msg-content h1{{font-size:1.3em}}.msg-content h2{{font-size:1.15em}}.msg-content h3{{font-size:1em}}
.msg-content p{{margin-bottom:10px}}
.msg-content ul,.msg-content ol{{margin:8px 0 10px 20px}}
.msg-content li{{margin-bottom:4px}}
.msg-content code{{background:var(--code-bg);border:1px solid var(--border);border-radius:4px;padding:1px 5px;font-size:13px;font-family:'JetBrains Mono','Fira Code',monospace}}
.msg-content pre{{background:var(--code-bg);border:1px solid var(--border);border-radius:8px;padding:14px 16px;overflow-x:auto;margin:10px 0;position:relative}}
.msg-content pre code{{background:none;border:none;padding:0;font-size:13px;line-height:1.6}}
.copy-btn{{position:absolute;top:8px;right:8px;background:var(--surface2);border:1px solid var(--border);color:var(--muted);padding:3px 8px;border-radius:5px;font-size:11px;cursor:pointer;transition:all .15s}}
.copy-btn:hover{{background:var(--border);color:var(--text)}}
.msg-content a{{color:var(--accent)}}
.msg-content blockquote{{border-left:3px solid var(--accent);padding-left:12px;color:var(--muted);margin:8px 0}}
.msg-content table{{border-collapse:collapse;width:100%;margin:10px 0}}
.msg-content th,.msg-content td{{border:1px solid var(--border);padding:8px 12px;text-align:left}}
.msg-content th{{background:var(--surface)}}
.cursor{{display:inline-block;width:2px;height:1em;background:var(--accent);margin-left:1px;animation:blink .7s infinite;vertical-align:middle}}
@keyframes blink{{0%,50%{{opacity:1}}51%,100%{{opacity:0}}}}
#empty-state{{text-align:center;padding:80px 24px;color:var(--muted)}}
#empty-state h2{{font-size:22px;font-weight:600;color:var(--text);margin-bottom:8px}}
#empty-state p{{font-size:14px;line-height:1.6;max-width:400px;margin:0 auto 24px}}
.suggestion-chips{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}}
.chip{{background:var(--surface);border:1px solid var(--border);padding:8px 14px;border-radius:20px;font-size:13px;cursor:pointer;transition:all .15s;color:var(--text)}}
.chip:hover{{background:var(--surface2);border-color:var(--accent)}}
/* Input */
#input-area{{border-top:1px solid var(--border);padding:16px 24px;background:var(--bg)}}
#input-wrap{{max-width:780px;margin:0 auto;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);display:flex;align-items:flex-end;gap:8px;padding:10px 12px;transition:border-color .2s}}
#input-wrap:focus-within{{border-color:var(--accent)}}
#msg-input{{flex:1;background:none;border:none;outline:none;color:var(--text);font-size:15px;font-family:var(--font);resize:none;min-height:24px;max-height:180px;line-height:1.5}}
#msg-input::placeholder{{color:var(--muted)}}
#send-btn{{background:var(--accent);border:none;color:#fff;width:32px;height:32px;border-radius:8px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:opacity .15s;font-size:16px}}
#send-btn:disabled{{opacity:.4;cursor:not-allowed}}
#input-hint{{text-align:center;font-size:11px;color:var(--muted);margin-top:8px;max-width:780px;margin:8px auto 0}}
/* Thinking indicator */
.thinking{{display:flex;align-items:center;gap:8px;color:var(--muted);font-size:14px}}
.dots span{{animation:dot 1.2s infinite;display:inline-block}}
.dots span:nth-child(2){{animation-delay:.2s}}
.dots span:nth-child(3){{animation-delay:.4s}}
@keyframes dot{{0%,60%,100%{{opacity:.3}}30%{{opacity:1}}}}
/* Scrollbar */
::-webkit-scrollbar{{width:6px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:var(--border);border-radius:3px}}
/* Issue modal */
#modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:100;align-items:center;justify-content:center}}
#modal.open{{display:flex}}
#modal-box{{background:var(--sidebar);border:1px solid var(--border);border-radius:var(--radius);padding:24px;width:520px;max-width:90vw}}
#modal-box h3{{margin-bottom:16px;font-size:16px}}
#modal-box input,#modal-box textarea{{width:100%;background:var(--surface);border:1px solid var(--border);color:var(--text);padding:10px 12px;border-radius:8px;font-size:14px;outline:none;margin-bottom:12px;font-family:var(--font)}}
#modal-box textarea{{min-height:100px;resize:vertical}}
#modal-box input:focus,#modal-box textarea:focus{{border-color:var(--accent)}}
.modal-actions{{display:flex;gap:8px;justify-content:flex-end;margin-top:4px}}
.btn{{padding:8px 16px;border-radius:8px;border:none;cursor:pointer;font-size:14px;font-family:var(--font)}}
.btn-primary{{background:var(--accent);color:#fff}}.btn-secondary{{background:var(--surface2);color:var(--text)}}
.btn:hover{{opacity:.85}}
</style>
</head>
<body>
<div id="app">
  <!-- Sidebar -->
  <div id="sidebar">
    <div id="sidebar-header">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l2 2"/></svg>
      <span>Claude</span> Code Chat
    </div>
    <div id="sidebar-sections">
      <div class="section-label">Chats</div>
      <div class="new-btn" onclick="newChat()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        New chat
      </div>
      <div id="chat-list"></div>
      <div class="section-label">GitHub Issues</div>
      <div class="new-btn" onclick="openNewIssueModal()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        New issue
      </div>
      <div id="issue-list"><div id="github-status">Loading…</div></div>
    </div>
  </div>
  <!-- Main -->
  <div id="main">
    <div id="topbar">
      <h1 id="chat-title">Claude Code Chat</h1>
      <select id="agent-select" onchange="agentChanged()">
        <option value="general">General</option>
        <option value="seo">SEO Team Lead</option>
        <option value="github">GitHub</option>
        <option value="code">Code</option>
      </select>
    </div>
    <div id="messages">
      <div id="messages-inner">
        <div id="empty-state">
          <h2>What can I help with?</h2>
          <p>Chat with Claude Code — with SEO agents, GitHub integration, and coding skills.</p>
          <div class="suggestion-chips">
            <div class="chip" onclick="send('Write PLP intro copy for /air-fryers')">Write PLP copy for /air-fryers</div>
            <div class="chip" onclick="send('Check GitHub for pending @claude tasks')">Check GitHub tasks</div>
            <div class="chip" onclick="send('What are the top SEO opportunities for thegoodguys.com.au?')">SEO opportunities</div>
            <div class="chip" onclick="send('Write 5 FAQ questions for washing machines')">FAQs for washing machines</div>
          </div>
        </div>
      </div>
    </div>
    <div id="input-area">
      <div id="input-wrap">
        <textarea id="msg-input" placeholder="Message Claude…" rows="1" onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
        <button id="send-btn" onclick="send()" title="Send (Enter)">↑</button>
      </div>
      <div id="input-hint">Enter to send · Shift+Enter for new line · <a href="https://github.com/{REPO}" target="_blank">{REPO}</a></div>
    </div>
  </div>
</div>

<!-- New Issue Modal -->
<div id="modal">
  <div id="modal-box">
    <h3>Create GitHub Issue</h3>
    <input id="issue-title" placeholder="Issue title" />
    <textarea id="issue-body" placeholder="Describe the task… (include @claude to trigger auto-processing)"></textarea>
    <div class="modal-actions">
      <button class="btn btn-secondary" onclick="closeModal()">Cancel</button>
      <button class="btn btn-primary" onclick="createIssue()">Create Issue</button>
    </div>
  </div>
</div>

<script>
const AGENTS = {agents_json};
let currentSession = null;
let streaming = false;

// ── Sessions ──
async function loadSessions() {{
  const res = await fetch('/api/sessions');
  const list = await res.json();
  const el = document.getElementById('chat-list');
  el.innerHTML = '';
  list.forEach(s => {{
    const d = document.createElement('div');
    d.className = 'chat-item' + (s.id === currentSession ? ' active' : '');
    d.dataset.id = s.id;
    d.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      <span style="flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${{escHtml(s.name)}}</span>
      <span class="del" onclick="deleteSession(event,'${{s.id}}')">✕</span>`;
    d.onclick = (e) => {{ if (!e.target.classList.contains('del')) switchSession(s.id, s.name); }};
    el.appendChild(d);
  }});
}}

async function newChat() {{
  const res = await fetch('/api/sessions', {{method:'POST', headers:{{'Content-Type':'application/json'}}, body: JSON.stringify({{name:'New chat'}})}});
  const data = await res.json();
  currentSession = data.id;
  clearMessages();
  await loadSessions();
}}

async function switchSession(id, name) {{
  currentSession = id;
  document.getElementById('chat-title').textContent = name;
  clearMessages();
  await loadSessions();
}}

async function deleteSession(e, id) {{
  e.stopPropagation();
  await fetch('/api/sessions/' + id, {{method:'DELETE'}});
  if (currentSession === id) {{
    currentSession = null;
    clearMessages();
  }}
  await loadSessions();
}}

function clearMessages() {{
  const inner = document.getElementById('messages-inner');
  inner.innerHTML = `<div id="empty-state">
    <h2>What can I help with?</h2>
    <p>Chat with Claude Code — with SEO agents, GitHub integration, and coding skills.</p>
    <div class="suggestion-chips">
      <div class="chip" onclick="send('Write PLP intro copy for /air-fryers')">Write PLP copy for /air-fryers</div>
      <div class="chip" onclick="send('Check GitHub for pending @claude tasks')">Check GitHub tasks</div>
      <div class="chip" onclick="send('What are the top SEO opportunities for thegoodguys.com.au?')">SEO opportunities</div>
      <div class="chip" onclick="send('Write 5 FAQ questions for washing machines')">FAQs for washing machines</div>
    </div>
  </div>`;
}}

// ── GitHub Issues ──
async function loadIssues() {{
  const el = document.getElementById('issue-list');
  const statusEl = document.getElementById('github-status');
  try {{
    const res = await fetch('/api/issues');
    if (!res.ok) {{
      el.innerHTML = '<div id="github-status" style="font-size:12px;padding:8px 10px;color:var(--muted)">Set GITHUB_TOKEN to see issues</div>';
      return;
    }}
    const issues = await res.json();
    el.innerHTML = '';
    if (issues.length === 0) {{
      el.innerHTML = '<div style="padding:8px 10px;font-size:12px;color:var(--muted)">No open issues</div>';
      return;
    }}
    issues.slice(0, 15).forEach(issue => {{
      const d = document.createElement('div');
      d.className = 'issue-item';
      d.innerHTML = `<span class="num">#${{issue.number}}</span><span class="title">${{escHtml(issue.title)}}</span>`;
      d.onclick = () => loadIssueIntoChat(issue);
      el.appendChild(d);
    }});
  }} catch(e) {{
    el.innerHTML = '<div style="padding:8px 10px;font-size:12px;color:var(--muted)">Could not load issues</div>';
  }}
}}

async function loadIssueIntoChat(issue) {{
  if (!currentSession) await newChat();
  document.getElementById('msg-input').value = `Tell me about GitHub issue #${{issue.number}}: "${{issue.title}}" and suggest what work needs to be done.`;
  document.getElementById('agent-select').value = 'github';
  document.getElementById('msg-input').focus();
}}

// ── New Issue Modal ──
function openNewIssueModal() {{
  document.getElementById('modal').classList.add('open');
  document.getElementById('issue-title').focus();
}}
function closeModal() {{
  document.getElementById('modal').classList.remove('open');
  document.getElementById('issue-title').value = '';
  document.getElementById('issue-body').value = '';
}}
async function createIssue() {{
  const title = document.getElementById('issue-title').value.trim();
  const body = document.getElementById('issue-body').value.trim();
  if (!title) return;
  const res = await fetch('/api/issues/create', {{
    method: 'POST',
    headers: {{'Content-Type':'application/json'}},
    body: JSON.stringify({{title, body}})
  }});
  const data = await res.json();
  closeModal();
  if (data.url) {{
    appendMessage('assistant', `✓ Created issue [#${{data.number}}](${{data.url}}): **${{title}}**`);
    loadIssues();
  }} else {{
    appendMessage('assistant', '❌ Failed to create issue. Is GITHUB_TOKEN set?');
  }}
}}

// ── Chat ──
async function send(presetMsg) {{
  if (streaming) return;
  const input = document.getElementById('msg-input');
  const msg = (presetMsg || input.value).trim();
  if (!msg) return;

  if (!currentSession) await newChat();

  // Hide empty state
  const empty = document.getElementById('empty-state');
  if (empty) empty.remove();

  input.value = '';
  autoResize(input);
  appendMessage('user', msg);
  document.getElementById('send-btn').disabled = true;
  streaming = true;

  const agent = document.getElementById('agent-select').value;
  const thinkingId = appendThinking();
  const assistantId = 'msg-' + Date.now();
  let buffer = '';

  const url = `/stream?msg=${{encodeURIComponent(msg)}}&session=${{currentSession}}&agent=${{agent}}`;
  const es = new EventSource(url);

  es.onmessage = (e) => {{
    const data = JSON.parse(e.data);
    if (data.type === 'ping') return;
    if (data.type === 'token') {{
      removeThinking(thinkingId);
      buffer += data.text;
      renderAssistant(assistantId, buffer);
      scrollToBottom();
    }}
    if (data.type === 'done') {{
      es.close();
      streaming = false;
      document.getElementById('send-btn').disabled = false;
      removeThinking(thinkingId);
      renderAssistant(assistantId, buffer, true);
      loadSessions();
      scrollToBottom();
    }}
  }};

  es.onerror = () => {{
    es.close();
    streaming = false;
    document.getElementById('send-btn').disabled = false;
    removeThinking(thinkingId);
    if (!buffer) appendMessage('assistant', '⚠ Connection error. Try again.');
    else renderAssistant(assistantId, buffer, true);
  }};
}}

function appendMessage(role, content) {{
  const inner = document.getElementById('messages-inner');
  const div = document.createElement('div');
  if (role === 'user') {{
    div.className = 'msg msg-user';
    div.innerHTML = `<div class="bubble">${{escHtml(content)}}</div>`;
  }} else {{
    div.className = 'msg msg-assistant';
    div.innerHTML = `<div class="avatar">C</div><div class="msg-content">${{renderMd(content)}}</div>`;
    addCopyButtons(div);
  }}
  inner.appendChild(div);
  scrollToBottom();
  return div;
}}

function appendThinking(id) {{
  const tid = 'thinking-' + Date.now();
  const inner = document.getElementById('messages-inner');
  const div = document.createElement('div');
  div.id = tid;
  div.className = 'msg msg-assistant';
  div.innerHTML = `<div class="avatar">C</div><div class="msg-content thinking">Thinking<div class="dots"><span>.</span><span>.</span><span>.</span></div></div>`;
  inner.appendChild(div);
  scrollToBottom();
  return tid;
}}

function removeThinking(tid) {{
  const el = document.getElementById(tid);
  if (el) el.remove();
}}

function renderAssistant(id, content, final = false) {{
  const inner = document.getElementById('messages-inner');
  let el = document.getElementById(id);
  if (!el) {{
    el = document.createElement('div');
    el.id = id;
    el.className = 'msg msg-assistant';
    inner.appendChild(el);
  }}
  el.innerHTML = `<div class="avatar">C</div><div class="msg-content">${{renderMd(content)}}${{final ? '' : '<span class="cursor"></span>'}}</div>`;
  if (final) addCopyButtons(el);
}}

function renderMd(text) {{
  return DOMPurify.sanitize(marked.parse(text));
}}

function addCopyButtons(container) {{
  container.querySelectorAll('pre').forEach(pre => {{
    if (pre.querySelector('.copy-btn')) return;
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = 'Copy';
    btn.onclick = () => {{
      const code = pre.querySelector('code');
      navigator.clipboard.writeText(code ? code.textContent : pre.textContent);
      btn.textContent = 'Copied!';
      setTimeout(() => btn.textContent = 'Copy', 2000);
    }};
    pre.style.position = 'relative';
    pre.appendChild(btn);
  }});
}}

function scrollToBottom() {{
  const el = document.getElementById('messages');
  el.scrollTop = el.scrollHeight;
}}

function handleKey(e) {{
  if (e.key === 'Enter' && !e.shiftKey) {{
    e.preventDefault();
    send();
  }}
}}

function autoResize(el) {{
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 180) + 'px';
}}

function agentChanged() {{
  const agent = document.getElementById('agent-select').value;
  const labels = {{ general:'General', seo:'SEO Team Lead', github:'GitHub', code:'Code' }};
  document.getElementById('chat-title').textContent = labels[agent] || 'Claude Code Chat';
}}

function escHtml(s) {{
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}}

// Close modal on backdrop click
document.getElementById('modal').onclick = (e) => {{ if (e.target === document.getElementById('modal')) closeModal(); }};

// Init
(async () => {{
  await newChat();
  await loadIssues();
}})();
</script>
</body>
</html>"""


def main():
    print(f"Claude Code Chat UI")
    print(f"Open: http://localhost:{PORT}")
    if not os.environ.get("GITHUB_TOKEN"):
        print("Tip: set GITHUB_TOKEN=<pat> to enable GitHub integration")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
