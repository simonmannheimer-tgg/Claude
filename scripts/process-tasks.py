#!/usr/bin/env python3
"""
Read pending @claude tasks from stdin (JSON from github-poll.sh),
call claude CLI for each, post replies to the GitHub Issue.
"""
import json, os, subprocess, sys

ROOT = "/home/user/Claude"
TOKEN = os.environ.get("PAT_TOKEN_GH", "")

poll = json.load(sys.stdin)
pending = poll.get("pending", [])

if not pending:
    sys.exit(0)

for task in pending:
    task_id      = task["id"]
    issue_number = str(task["number"])
    task_text    = task["task"].strip()

    print(f"[task] {task_id}: {task_text[:80]}")

    prompt = f"""You are the SEO team lead for thegoodguys.com.au.
Target domain: thegoodguys.com.au | Competitors: jbhifi.com.au, harveynorman.com.au

Task: {task_text}

Instructions:
- Be thorough but concise
- Use markdown (headings, bullets, tables, code blocks as needed)
- Include all key outputs inline (copy text, keyword lists, FAQs, etc.)
- End your reply with: _— Claude Code_
- Do NOT include the text @claude anywhere in your response
"""

    result = subprocess.run(
        ["claude", "--print"],
        input=prompt,
        capture_output=True, text=True, timeout=180,
        cwd=ROOT
    )
    response = (result.stdout or result.stderr or "(no response)").strip()
    if not response:
        response = "Sorry, I couldn't process that request. Please try again."

    env = os.environ.copy()
    env["PAT_TOKEN_GH"]  = TOKEN
    env["BODY"]          = response
    env["TASK_ID"]       = task_id
    env["ISSUE_NUMBER"]  = issue_number

    post = subprocess.run(
        ["bash", "scripts/github-post-comment.sh"],
        env=env, cwd=ROOT, capture_output=True, text=True, timeout=30
    )
    print(post.stdout.strip() or post.stderr.strip())
