"""
Context Mode MCP Server
Indexes large content into SQLite and returns compact structural summaries.
Claude retrieves only the relevant sections via keyword search instead of
getting raw file dumps — reducing context usage by up to 98%.
"""

import asyncio
import re
import sqlite3
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

DB_PATH = Path(__file__).parent / "context_index.db"
CHUNK_SIZE = 100        # max lines per chunk (fixed-size fallback)
CHUNK_OVERLAP = 10      # overlap between fixed-size chunks
MAX_RESULTS = 5         # max chunks returned per search
MAX_PREVIEW_LINES = 60  # max lines shown per chunk in search results


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

def _db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS chunks (
            key        TEXT    NOT NULL,
            chunk_id   INTEGER NOT NULL,
            start_line INTEGER NOT NULL,
            end_line   INTEGER NOT NULL,
            label      TEXT    NOT NULL,
            content    TEXT    NOT NULL,
            PRIMARY KEY (key, chunk_id)
        );
        CREATE TABLE IF NOT EXISTS summaries (
            key         TEXT PRIMARY KEY,
            summary     TEXT NOT NULL,
            total_lines INTEGER NOT NULL,
            file_path   TEXT NOT NULL DEFAULT ''
        );
    """)
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# Chunking strategies
# ---------------------------------------------------------------------------

def _chunk_python(lines: list[str]) -> list[dict]:
    """Split Python source at top-level definitions."""
    chunks, buf, start, label = [], [], 1, "module header"
    top_def = re.compile(r'^(async def |def |class )\S')
    for i, line in enumerate(lines, 1):
        if top_def.match(line) and buf:
            chunks.append({"start": start, "end": i - 1, "label": label, "content": "".join(buf)})
            buf, start = [line], i
            label = line.strip().split("(")[0].replace("async ", "")
        else:
            buf.append(line)
    if buf:
        chunks.append({"start": start, "end": start + len(buf) - 1, "label": label, "content": "".join(buf)})
    return chunks


def _chunk_markdown(lines: list[str]) -> list[dict]:
    """Split Markdown at headings (h1–h3)."""
    chunks, buf, start, label = [], [], 1, "preamble"
    heading = re.compile(r'^#{1,3} ')
    for i, line in enumerate(lines, 1):
        if heading.match(line) and buf:
            chunks.append({"start": start, "end": i - 1, "label": label, "content": "".join(buf)})
            buf, start = [line], i
            label = line.strip().lstrip("#").strip()
        else:
            buf.append(line)
    if buf:
        chunks.append({"start": start, "end": start + len(buf) - 1, "label": label, "content": "".join(buf)})
    return chunks


def _chunk_fixed(lines: list[str]) -> list[dict]:
    """Fixed-size chunks with overlap for unknown file types."""
    chunks = []
    step = max(1, CHUNK_SIZE - CHUNK_OVERLAP)
    for i in range(0, len(lines), step):
        chunk = lines[i:i + CHUNK_SIZE]
        start = i + 1
        end = start + len(chunk) - 1
        chunks.append({"start": start, "end": end, "label": f"lines {start}-{end}", "content": "".join(chunk)})
    return chunks


def _chunk(path_hint: str, content: str) -> list[dict]:
    lines = content.splitlines(keepends=True)
    if path_hint.endswith(".py"):
        return _chunk_python(lines)
    if path_hint.endswith(".md"):
        return _chunk_markdown(lines)
    return _chunk_fixed(lines)


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def _build_summary(key: str, chunks: list[dict], total_lines: int, file_path: str) -> str:
    label = file_path or key
    parts = [f"Indexed: {label} ({total_lines} lines, {len(chunks)} sections)"]
    parts.append("Sections:")
    for c in chunks:
        parts.append(f"  [{c['start']}-{c['end']}] {c['label']}")
    parts.append(f"\nUse ctx_search('{key}', '<topic>') to retrieve specific sections.")
    return "\n".join(parts)


def index_content(key: str, content: str, file_path: str = "") -> str:
    lines = content.splitlines(keepends=True)
    total_lines = len(lines)
    chunks = _chunk(file_path or key, content)

    conn = _db()
    conn.execute("DELETE FROM chunks WHERE key=?", (key,))
    conn.execute("DELETE FROM summaries WHERE key=?", (key,))
    for i, c in enumerate(chunks):
        conn.execute(
            "INSERT INTO chunks VALUES (?,?,?,?,?,?)",
            (key, i, c["start"], c["end"], c["label"], c["content"]),
        )
    summary = _build_summary(key, chunks, total_lines, file_path)
    conn.execute(
        "INSERT OR REPLACE INTO summaries VALUES (?,?,?,?)",
        (key, summary, total_lines, file_path),
    )
    conn.commit()
    conn.close()
    return summary


def search_context(key: str, query: str) -> str:
    conn = _db()
    row = conn.execute("SELECT 1 FROM summaries WHERE key=?", (key,)).fetchone()
    if not row:
        conn.close()
        return f"No indexed content for '{key}'. Use ctx_read_file or ctx_index first."

    rows = conn.execute(
        "SELECT start_line, end_line, label, content FROM chunks WHERE key=? ORDER BY chunk_id",
        (key,),
    ).fetchall()
    conn.close()

    terms = [t.lower() for t in query.split() if t]

    scored = []
    for start, end, label, content in rows:
        text = (label + " " + content).lower()
        score = sum(text.count(t) for t in terms)
        scored.append((score, start, end, label, content))

    scored.sort(reverse=True)
    top = [r for r in scored if r[0] > 0][:MAX_RESULTS] or scored[:1]

    parts = [f"Search: '{query}' in '{key}' — {len(top)} section(s) returned\n"]
    for _, start, end, label, content in top:
        preview_lines = content.splitlines()
        preview = "\n".join(preview_lines[:MAX_PREVIEW_LINES])
        if len(preview_lines) > MAX_PREVIEW_LINES:
            preview += f"\n[...{len(preview_lines) - MAX_PREVIEW_LINES} more lines — refine query to narrow]"
        parts.append(f"--- [{start}-{end}] {label} ---\n{preview}")
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

server = Server("context-mode")

TOOLS = [
    Tool(
        name="ctx_read_file",
        description=(
            "Index a file from disk and return a compact structural summary. "
            "Use this INSTEAD of the Read tool for any file over 50 lines. "
            "Returns section map only — use ctx_search to pull specific content."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Absolute path or path relative to the repo root.",
                },
            },
            "required": ["path"],
        },
    ),
    Tool(
        name="ctx_index",
        description=(
            "Index arbitrary text content under a named key and return a compact summary. "
            "Use for large tool outputs, API responses, or any block of text over 100 lines."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "Unique name for this content."},
                "content": {"type": "string", "description": "The large content to compress and index."},
            },
            "required": ["key", "content"],
        },
    ),
    Tool(
        name="ctx_search",
        description=(
            "Search indexed content and retrieve only the relevant sections. "
            "Always use this after ctx_read_file or ctx_index instead of reading the raw file."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "Key used when indexing."},
                "query": {"type": "string", "description": "Keywords or topic to retrieve."},
            },
            "required": ["key", "query"],
        },
    ),
    Tool(
        name="ctx_list",
        description="List all currently indexed keys with line counts and source paths.",
        inputSchema={"type": "object", "properties": {}, "required": []},
    ),
    Tool(
        name="ctx_drop",
        description="Remove an indexed item by key to free storage. Omit key to clear everything.",
        inputSchema={
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "Key to drop. Omit to clear all."},
            },
            "required": [],
        },
    ),
]


@server.list_tools()
async def list_tools():
    return TOOLS


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "ctx_read_file":
        path_str = arguments["path"]
        path = Path(path_str)
        if not path.is_absolute():
            path = Path(__file__).parent.parent / path_str
        if not path.exists():
            return [TextContent(type="text", text=f"File not found: {path_str}")]
        content = path.read_text(encoding="utf-8", errors="replace")
        key = path.name
        summary = index_content(key, content, file_path=str(path))
        return [TextContent(type="text", text=summary)]

    if name == "ctx_index":
        key = arguments["key"]
        content = arguments["content"]
        summary = index_content(key, content)
        return [TextContent(type="text", text=summary)]

    if name == "ctx_search":
        result = search_context(arguments["key"], arguments["query"])
        return [TextContent(type="text", text=result)]

    if name == "ctx_list":
        conn = _db()
        rows = conn.execute(
            "SELECT key, total_lines, file_path FROM summaries ORDER BY key"
        ).fetchall()
        conn.close()
        if not rows:
            return [TextContent(type="text", text="Context store is empty. Use ctx_read_file or ctx_index to add content.")]
        lines = ["**Context Index**\n"]
        for key, total_lines, file_path in rows:
            fp = f" → {file_path}" if file_path else ""
            lines.append(f"- `{key}` ({total_lines} lines){fp}")
        return [TextContent(type="text", text="\n".join(lines))]

    if name == "ctx_drop":
        key = arguments.get("key")
        conn = _db()
        if key:
            conn.execute("DELETE FROM chunks WHERE key=?", (key,))
            conn.execute("DELETE FROM summaries WHERE key=?", (key,))
            msg = f"Dropped '{key}' from context index."
        else:
            conn.execute("DELETE FROM chunks")
            conn.execute("DELETE FROM summaries")
            msg = "Cleared entire context index."
        conn.commit()
        conn.close()
        return [TextContent(type="text", text=msg)]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
