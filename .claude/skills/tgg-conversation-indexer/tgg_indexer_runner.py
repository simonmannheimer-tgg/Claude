#!/usr/bin/env python3
"""
tgg_indexer_runner.py
Weekly runner for the TGG conversation indexer.

Usage:
  python tgg_indexer_runner.py

Add to crontab for weekly schedule:
  0 8 * * 1 cd /path/to/claude-code-project && python tgg_indexer_runner.py >> logs/indexer.log 2>&1

What this does:
  1. Sends the scheduled trigger prompt to Claude with the tgg-conversation-indexer skill loaded
  2. Claude runs all 7 steps (fetch, score, classify, update index, write todo, update timestamp)
  3. Output is printed to stdout (captured by cron to log file)

Requirements:
  - Claude Code configured with ANTHROPIC_API_KEY
  - tgg-conversation-indexer skill installed in your skills directory
  - /mnt/user-data/outputs/ writable (or adjust OUTPUT_DIR below)
"""

import subprocess
import sys
from datetime import datetime

OUTPUT_DIR = "outputs"  # adjust to your Claude Code project output path

TRIGGER_PROMPT = """Run tgg-conversation-indexer. Scan conversations since last run, score significance, append to index, flag abandoned projects with upside, update todo."""

def run_indexer():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*60}")
    print(f"TGG Conversation Indexer — {timestamp}")
    print(f"{'='*60}\n")

    result = subprocess.run(
        ["claude", "-p", TRIGGER_PROMPT],
        capture_output=False,  # stream output to stdout
        text=True
    )

    if result.returncode != 0:
        print(f"\nIndexer exited with code {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)

    print(f"\nIndexer run complete at {timestamp}")

if __name__ == "__main__":
    run_indexer()
