from claude_agent_sdk import AgentDefinition

SUBAGENTS: dict[str, AgentDefinition] = {
    "browser-agent": AgentDefinition(
        description=(
            "Automates web browsing via Playwright MCP. Use for fetching URLs, "
            "clicking elements, filling forms, and scraping page content."
        ),
        prompt=(
            "You control a web browser. Use the available browser tools to navigate "
            "URLs, read page content via snapshots, click elements, and fill forms. "
            "Report extracted content clearly and concisely. "
            "Do not follow links unless explicitly asked to do so."
        ),
        tools=["Bash"],
        model="claude-sonnet-4-6",
    ),
    "research-agent": AgentDefinition(
        description=(
            "Searches the web and synthesizes information. Use for factual lookups, "
            "topic summaries, comparisons, and current events."
        ),
        prompt=(
            "You research topics thoroughly. Use the browser-agent subagent to visit "
            "URLs and fetch page content when needed. "
            "Synthesize your findings into a clear, structured response. "
            "Always cite your sources with URL and page title."
        ),
        tools=["Agent"],
        model="claude-sonnet-4-6",
    ),
    "code-agent": AgentDefinition(
        description=(
            "Writes, executes, and debugs Python code. Use for calculations, "
            "data processing, script generation, and computational tasks."
        ),
        prompt=(
            "You write and run Python code to accomplish tasks. "
            "Show the code before running it. "
            "Use the Bash tool to execute scripts. "
            "Report stdout and stderr output faithfully. "
            "If execution fails, debug and retry with a fixed version."
        ),
        tools=["Bash", "Read", "Write", "Edit"],
        model="claude-sonnet-4-6",
    ),
    "file-agent": AgentDefinition(
        description=(
            "Reads, writes, and manages files and directories. Use for creating files, "
            "reading documents, searching file content, and directory inspection."
        ),
        prompt=(
            "You manage files and directories. "
            "Use Read/Write/Edit for file content operations. "
            "Use Glob to find files by pattern and Grep to search content. "
            "Use Bash only for directory listing (ls) or creating directories (mkdir). "
            "Never delete files without explicit confirmation from the user."
        ),
        tools=["Read", "Write", "Edit", "Glob", "Grep", "Bash"],
        model="claude-sonnet-4-6",
    ),
}
