BLOCKED_BASH_PATTERNS = [
    "rm -rf",
    "sudo",
    "chmod 777",
    "> /dev/",
    ":(){ :|:& };:",  # fork bomb
    "curl | bash",
    "curl|bash",
    "wget | sh",
    "wget|sh",
    "dd if=",
    "mkfs",
    "> /etc/",
]


def make_pre_tool_hook():
    """Return a PreToolUse hook function that blocks dangerous Bash commands."""

    async def pre_tool_use(input_data: dict, tool_use_id: str, context: dict) -> dict:
        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})

        if tool_name == "Bash":
            command = tool_input.get("command", "")
            for pattern in BLOCKED_BASH_PATTERNS:
                if pattern in command:
                    return {
                        "hookSpecificOutput": {
                            "permissionDecision": "deny",
                            "permissionDecisionReason": (
                                f"Blocked dangerous command pattern: {pattern!r}"
                            ),
                        }
                    }
        return {}

    return pre_tool_use
