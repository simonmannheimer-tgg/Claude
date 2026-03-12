from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    AssistantMessage,
    ResultMessage,
    HookMatcher,
)

from .subagents import SUBAGENTS
from .hooks import make_pre_tool_hook
from .progress import log

SYSTEM_PROMPT = """\
You are a capable autonomous agent. Your job is to break down the user's task,
decide which subagents to use, coordinate them, and produce a complete result.

Available subagents (invoke with the Agent tool):
- browser-agent: Navigate URLs, scrape pages, fill forms via browser automation
- research-agent: Web research and synthesis (uses browser-agent internally)
- code-agent: Write and execute Python code for calculations and data processing
- file-agent: Read, write, and search files and directories

Steps:
1. Analyse the task and identify which subagents are needed.
2. Delegate sub-tasks to the appropriate agents using the Agent tool.
3. Synthesise the results and provide a clear, complete final answer.
"""


async def run_task(
    task: str,
    max_turns: int = 50,
    max_budget: float = 5.0,
    cwd: str | None = None,
) -> str:
    """Run an autonomous agent task and return the final result string."""

    options = ClaudeAgentOptions(
        model="claude-opus-4-6",
        allowed_tools=["Read", "Write", "Edit", "Bash", "Grep", "Glob", "Agent"],
        agents=SUBAGENTS,
        max_turns=max_turns,
        max_budget_usd=max_budget,
        system_prompt=SYSTEM_PROMPT,
        mcp_servers={
            "playwright": {"command": "npx", "args": ["@playwright/mcp@latest"]}
        },
        hooks={
            "PreToolUse": [
                HookMatcher(matcher="Bash", hooks=[make_pre_tool_hook()])
            ]
        },
        **({"cwd": cwd} if cwd else {}),
    )

    log("START", task[:120])
    result = ""

    async for message in query(prompt=task, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text") and block.text:
                    log("THINK", block.text[:200])
        elif isinstance(message, ResultMessage):
            result = message.result or ""
            log("DONE", result[:200])

    return result
