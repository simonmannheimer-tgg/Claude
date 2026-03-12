#!/usr/bin/env python3
"""Entry point for the autonomous AI agent."""

import argparse
import sys

import anyio

from agent.orchestrator import run_task


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Autonomous AI agent powered by Claude",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            '  python cli.py "List all markdown files in the current directory"\n'
            '  python cli.py --max-turns 20 "Calculate the prime factors of 1234567"\n'
            '  echo "What is 2+2?" | python cli.py'
        ),
    )
    parser.add_argument(
        "task",
        nargs="?",
        help="Task for the agent to complete (or pipe via stdin)",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=50,
        help="Maximum agent turns before stopping (default: 50)",
    )
    parser.add_argument(
        "--max-budget",
        type=float,
        default=5.0,
        help="Maximum spend in USD before stopping (default: 5.0)",
    )
    parser.add_argument(
        "--cwd",
        type=str,
        default=None,
        help="Working directory for file operations (default: current directory)",
    )
    args = parser.parse_args()

    if args.task:
        task = args.task
    elif not sys.stdin.isatty():
        task = sys.stdin.read().strip()
    else:
        parser.print_help()
        sys.exit(1)

    if not task:
        print("Error: task cannot be empty.", file=sys.stderr)
        sys.exit(1)

    result = anyio.run(run_task, task, args.max_turns, args.max_budget, args.cwd)

    print("\n=== RESULT ===")
    print(result)


if __name__ == "__main__":
    main()
