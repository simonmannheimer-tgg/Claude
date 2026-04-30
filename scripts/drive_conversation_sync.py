"""
drive_conversation_sync.py

Pulls the latest Anthropic conversation export ZIP from Google Drive,
extracts it, and runs build_logseq_chat_index.py to update the vault.

Usage:
    python3 scripts/drive_conversation_sync.py [--dry-run] [--file-id ID]

Requirements:
    - Google Drive MCP must be available (local sessions only)
    - Run from repo root

Export naming convention on Drive:
    claude-export_YYYYMMDD.zip   (preferred)
    Any zip containing 'conversations.json' at root level is also accepted.

The script picks the most recently modified matching ZIP. To force a specific
file, pass --file-id with the Drive file ID.
"""

import argparse
import base64
import io
import json
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

EXTRACT_DIR = Path("/tmp/chat-export")
REPO_ROOT = Path(__file__).parent.parent
BUILD_SCRIPT = REPO_ROOT / "scripts" / "build_logseq_chat_index.py"

# Drive search patterns (checked in order, first match wins)
SEARCH_PATTERNS = [
    "title contains 'claude-export'",
    "title contains 'conversation export'",
    "title contains 'conversations.json'",
]


def find_export_on_drive() -> list[dict]:
    """
    Placeholder: returns candidate ZIPs from Drive.

    In a live Claude Code session with Google Drive MCP active, this function
    is replaced by direct MCP tool calls. The script prints instructions for
    the MCP-assisted path below.
    """
    return []


def extract_zip_blob(b64_blob: str, dest: Path) -> bool:
    """Decode a base64 ZIP blob and extract to dest directory."""
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    raw = base64.b64decode(b64_blob)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        # Validate it looks like a conversation export
        names = z.namelist()
        has_conversations = any("conversations.json" in n for n in names)
        if not has_conversations:
            print("ERROR: ZIP does not contain conversations.json — wrong file?")
            return False

        z.extractall(dest)

        # If everything is nested in a subdirectory, hoist it up
        top_dirs = {Path(n).parts[0] for n in names if n}
        if len(top_dirs) == 1:
            subdir = dest / list(top_dirs)[0]
            if subdir.is_dir() and (subdir / "conversations.json").exists():
                for item in subdir.iterdir():
                    shutil.move(str(item), dest / item.name)
                subdir.rmdir()

    return (dest / "conversations.json").exists()


def run_build_script(dry_run: bool = False) -> int:
    """Run build_logseq_chat_index.py and return exit code."""
    cmd = [sys.executable, str(BUILD_SCRIPT), str(EXTRACT_DIR), str(REPO_ROOT / "vault")]
    if dry_run:
        print(f"DRY RUN — would run: {' '.join(cmd)}")
        return 0
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    return result.returncode


def print_mcp_instructions(pattern: str):
    """Print instructions for the MCP-assisted drive search."""
    print()
    print("=" * 60)
    print("DRIVE MCP REQUIRED")
    print("=" * 60)
    print()
    print("This script cannot call Drive MCP tools directly.")
    print("In a Claude Code session, run this instead:")
    print()
    print(f'  Search Drive: {pattern}')
    print()
    print("Then pass the file ID:")
    print("  python3 scripts/drive_conversation_sync.py --file-id <ID>")
    print()
    print("Or use the Claude Code session to:")
    print("  1. Search Drive for the export ZIP")
    print("  2. Download it with download_file_content")
    print("  3. Pass the base64 blob via stdin:")
    print("     python3 scripts/drive_conversation_sync.py --from-stdin")
    print()


def main():
    parser = argparse.ArgumentParser(description="Sync conversation export from Drive to vault")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen, don't write")
    parser.add_argument("--file-id", help="Drive file ID to download directly (requires MCP in session)")
    parser.add_argument("--from-stdin", action="store_true", help="Read base64 ZIP blob from stdin")
    parser.add_argument("--from-file", help="Path to a local ZIP file to use directly")
    args = parser.parse_args()

    print(f"drive_conversation_sync — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print()

    # --- Path 1: local ZIP file ---
    if args.from_file:
        src = Path(args.from_file)
        if not src.exists():
            print(f"ERROR: File not found: {src}")
            sys.exit(1)
        print(f"Using local file: {src}")
        if EXTRACT_DIR.exists():
            shutil.rmtree(EXTRACT_DIR)
        EXTRACT_DIR.mkdir(parents=True)
        with zipfile.ZipFile(src) as z:
            z.extractall(EXTRACT_DIR)
            names = z.namelist()
            top_dirs = {Path(n).parts[0] for n in names if n}
            if len(top_dirs) == 1:
                subdir = EXTRACT_DIR / list(top_dirs)[0]
                if subdir.is_dir() and (subdir / "conversations.json").exists():
                    for item in subdir.iterdir():
                        shutil.move(str(item), EXTRACT_DIR / item.name)
                    subdir.rmdir()

    # --- Path 2: base64 blob from stdin ---
    elif args.from_stdin:
        print("Reading base64 ZIP blob from stdin...")
        blob = sys.stdin.read().strip()
        if not blob:
            print("ERROR: No data received on stdin")
            sys.exit(1)
        ok = extract_zip_blob(blob, EXTRACT_DIR)
        if not ok:
            sys.exit(1)
        print(f"Extracted to {EXTRACT_DIR}")

    # --- Path 3: file ID (MCP needed in session) ---
    elif args.file_id:
        print(f"File ID provided: {args.file_id}")
        print()
        print("To download this file, run the following in a Claude Code session")
        print("that has the Google Drive MCP active:")
        print()
        print(f"  Use mcp__drive__download_file_content with fileId='{args.file_id}'")
        print("  Then pipe the blob to: python3 scripts/drive_conversation_sync.py --from-stdin")
        print()
        sys.exit(0)

    # --- Path 4: no args — print instructions ---
    else:
        print("No input provided. Options:")
        print()
        print("  1. Upload export to Drive as 'claude-export_YYYYMMDD.zip' then run:")
        print("     skill-zip-sync  (or trigger drive-skill-sync workflow)")
        print()
        print("  2. Use a local export ZIP:")
        print("     python3 scripts/drive_conversation_sync.py --from-file /path/to/export.zip")
        print()
        print("  3. In a Claude Code session with Drive MCP:")
        print_mcp_instructions("title contains 'claude-export'")
        sys.exit(0)

    # --- Run the build script ---
    conversations_file = EXTRACT_DIR / "conversations.json"
    if not conversations_file.exists():
        print(f"ERROR: conversations.json not found in {EXTRACT_DIR}")
        print("Check that the ZIP is a valid Anthropic conversation export.")
        sys.exit(1)

    try:
        with open(conversations_file) as f:
            data = json.load(f)
        count = len(data) if isinstance(data, list) else "?"
        print(f"Found {count} conversations in export.")
    except Exception as e:
        print(f"WARNING: Could not read conversations.json: {e}")

    print(f"Running build script...")
    rc = run_build_script(dry_run=args.dry_run)
    if rc != 0:
        print(f"ERROR: Build script exited with code {rc}")
        sys.exit(rc)

    if not args.dry_run:
        vault_pages = REPO_ROOT / "vault" / "pages"
        page_count = len(list(vault_pages.glob("*.md"))) if vault_pages.exists() else 0
        print()
        print(f"Vault updated — {page_count} pages in vault/pages/")
        print("Run 'git add vault/ && git commit' to save changes.")
        print("Or wait for vault-autocommit.yml (runs daily at 13:15 UTC).")


if __name__ == "__main__":
    main()
