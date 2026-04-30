#!/usr/bin/env python3
"""
Read pending @claude tasks from stdin (JSON from github-poll.sh),
call claude CLI for each via seo-team-lead, write outputs to seo/outputs/,
commit, then post replies to the GitHub Issue.
"""
import json, os, subprocess, sys
from datetime import date

ROOT = "/home/user/Claude"
TOKEN = os.environ.get("PAT_TOKEN_GH", "")

poll = json.load(sys.stdin)
pending = poll.get("pending", [])

if not pending:
    sys.exit(0)

today = date.today().isoformat()

for task in pending:
    task_id      = task["id"]
    issue_number = str(task["number"])
    task_text    = task["task"].strip()

    print(f"[task] {task_id}: {task_text[:80]}")

    prompt = f"""Use the seo-team-lead to action the following task for thegoodguys.com.au:

{task_text}

Instructions:
- Route through seo-team-lead — do not do SEO work directly
- Target domain: thegoodguys.com.au | Competitors: jbhifi.com.au, harveynorman.com.au, officeworks.com.au | Database: au
- Write all outputs to seo/outputs/ with today's date ({today}) in the filename
- After writing files: git add seo/outputs/ && git commit -m "feat(outputs): {task_text[:60]}" && git push -u origin HEAD
- Return a concise markdown summary of what was produced, including the file path(s) written
- End your reply with: _— Claude Code_
- Do NOT include the text @claude anywhere in your response
"""

    env = os.environ.copy()
    env["CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"] = "1"

    result = subprocess.run(
        ["claude", "--print", "--dangerously-skip-permissions"],
        input=prompt,
        capture_output=True, text=True, timeout=600,
        cwd=ROOT, env=env
    )
    response = (result.stdout or result.stderr or "(no response)").strip()
    if not response:
        response = "Sorry, I couldn't process that request. Please try again."

    env["BODY"]         = response
    env["TASK_ID"]      = task_id
    env["ISSUE_NUMBER"] = issue_number

    post = subprocess.run(
        ["bash", "scripts/github-post-comment.sh"],
        env=env, cwd=ROOT, capture_output=True, text=True, timeout=30
    )
    print(post.stdout.strip() or post.stderr.strip())
