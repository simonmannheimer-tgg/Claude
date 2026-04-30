#!/usr/bin/env python3
"""
MHTML Transformer — AI + Human Readable Single-File Output
Converts .mhtml/.mht files into self-contained .ai.html documents
with embedded canonical JSON for deterministic AI ingestion.

Zero external dependencies — uses only Python standard library.

Usage:
    python mhtml_transformer.py                         (interactive prompt)
    python mhtml_transformer.py <file_or_folder>
    python mhtml_transformer.py <file_or_folder> --seo
"""

import sys
import os
import uuid
import json
import hashlib
import re
from html.parser import HTMLParser
from email import policy
from email.parser import BytesParser
from pathlib import Path
from urllib.parse import urlparse, unquote


# ════════════════════════════════════════════════
#  MINI DOM (replaces BeautifulSoup)
# ════════════════════════════════════════════════

class Node:
    """Lightweight DOM node."""

    def __init__(self, tag=None, attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs) if attrs else {}
        self.children = []
        self.parent = parent
        self._text_parts = []

    # ── Attribute access ──

    def get(self, attr, default=None):
        val = self.attrs.get(attr, default)
        if isinstance(val, list):
            return val
        return val

    def has_attr(self, attr):
        return attr in self.attrs

    # ── Class helpers ──

    def get_classes(self):
        c = self.attrs.get("class", [])
        if isinstance(c, str):
            return c.split()
        if isinstance(c, list):
            return c
        return []

    # ── Text ──

    def get_text(self, separator="", strip=False):
        parts = []
        self._collect_text(parts)
        text = separator.join(parts)
        return text.strip() if strip else text

    def _collect_text(self, parts):
        for child in self.children:
            if child.tag is None:
                parts.extend(child._text_parts)
            else:
                child._collect_text(parts)

    # ── Traversal ──

    def find_all(self, tag=None, attrs=None, recursive=True):
        results = []
        self._search(tag, attrs, recursive, results)
        return results

    def find(self, tag=None, attrs=None):
        results = self.find_all(tag, attrs, recursive=True)
        return results[0] if results else None

    def _search(self, tag, attrs, recursive, results):
        for child in self.children:
            if child.tag is None:
                continue
            if self._matches(child, tag, attrs):
                results.append(child)
            if recursive:
                child._search(tag, attrs, recursive, results)

    @staticmethod
    def _matches(node, tag, attrs):
        if tag and node.tag != tag:
            return False
        if attrs:
            for key, val in attrs.items():
                node_val = node.attrs.get(key)
                if node_val is None:
                    return False
                if isinstance(node_val, list):
                    if val not in node_val and val != " ".join(node_val):
                        return False
                elif node_val != val:
                    return False
        return True

    @property
    def name(self):
        return self.tag


class MiniDOMParser(HTMLParser):
    """Build a lightweight DOM tree from HTML using only stdlib."""

    SELF_CLOSING = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node(tag="[root]")
        self.current = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag=tag, attrs=attrs, parent=self.current)
        self.current.children.append(node)
        if tag.lower() not in self.SELF_CLOSING:
            self.current = node

    def handle_endtag(self, tag):
        cursor = self.current
        while cursor and cursor.tag != tag and cursor.parent:
            cursor = cursor.parent
        if cursor and cursor.parent:
            self.current = cursor.parent
        elif self.current.parent:
            self.current = self.current.parent

    def handle_data(self, data):
        text_node = Node(tag=None, parent=self.current)
        text_node._text_parts = [data]
        self.current.children.append(text_node)

    def handle_startendtag(self, tag, attrs):
        node = Node(tag=tag, attrs=attrs, parent=self.current)
        self.current.children.append(node)


def parse_html(html):
    """Parse HTML string into a MiniDOM tree, return root Node."""
    parser = MiniDOMParser()
    try:
        parser.feed(html)
    except Exception:
        pass
    return parser.root


# ════════════════════════════════════════════════
#  CONFIGURATION
# ════════════════════════════════════════════════

SKIP_TAGS = {
    "html", "head", "body", "meta", "link", "br", "hr",
    "noscript", "iframe", "object", "embed", "param",
    "col", "colgroup", "source", "track", "wbr",
}

SEO_ALLOWED_TYPES = {
    "navigation", "heading", "text", "list",
    "table", "media", "container",
}

CONTAINER_TAGS = {
    "div", "section", "article", "aside", "main",
    "header", "footer", "figure", "figcaption",
    "blockquote", "details", "summary",
}

CONTAINER_ROLES = {
    "header": "page_header",
    "footer": "page_footer",
    "main": "main_content",
    "article": "article",
    "aside": "sidebar",
    "section": "section",
    "figure": "figure",
    "figcaption": "figure_caption",
    "blockquote": "quote",
    "details": "expandable",
    "summary": "expandable_title",
    "div": "generic_container",
}


# ════════════════════════════════════════════════
#  UTILITIES
# ════════════════════════════════════════════════

def gen_id():
    return str(uuid.uuid4())[:12]


def clean_text(el):
    """Get clean text from a Node."""
    return el.get_text(strip=True)


def detect_canonical_domain(html):
    """Try to detect the site domain from canonical or og:url."""
    root = parse_html(html)
    for link_node in root.find_all("link"):
        rel = link_node.get("rel")
        if rel and ("canonical" in rel if isinstance(rel, list) else rel == "canonical"):
            href = link_node.get("href")
            if href:
                parsed = urlparse(href)
                if parsed.netloc:
                    return parsed.netloc
    for meta_node in root.find_all("meta"):
        if meta_node.get("property") == "og:url":
            content = meta_node.get("content")
            if content:
                parsed = urlparse(content)
                if parsed.netloc:
                    return parsed.netloc
    return None


# ════════════════════════════════════════════════
#  MHTML EXTRACTION
# ════════════════════════════════════════════════

def is_mhtml(path):
    return path.suffix.lower() in [".mhtml", ".mht"]


def extract_html_from_mhtml(mhtml_path):
    """Extract the first text/html part from an MHTML file."""
    with open(mhtml_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    for part in msg.walk():
        ct = part.get_content_type()
        if ct == "text/html":
            payload = part.get_content()
            if isinstance(payload, bytes):
                charset = part.get_content_charset() or "utf-8"
                return payload.decode(charset, errors="replace")
            return payload
    return ""


# ════════════════════════════════════════════════
#  BREADCRUMB DETECTION
# ════════════════════════════════════════════════

def is_breadcrumb(el):
    """Determine if an element is a breadcrumb nav."""
    classes = " ".join(el.get_classes()).lower()
    el_id = (el.get("id") or "").lower()

    if any(kw in classes for kw in ["breadcrumb", "crumb", "breadcrumbs"]):
        return True
    if any(kw in el_id for kw in ["breadcrumb", "crumb"]):
        return True
    if el.has_attr("itemtype") and "BreadcrumbList" in (el.get("itemtype") or ""):
        return True
    aria = el.get("aria-label") or ""
    if aria.lower() in ["breadcrumb", "breadcrumbs"]:
        return True

    text = el.get_text(" ", strip=True)
    if len(text) < 500:
        sep_count = text.count(">") + text.count("\u00bb") + text.count("\u203a")
        link_count = len(el.find_all("a"))
        if sep_count >= 2 and link_count >= 2:
            return True

    return False


# ════════════════════════════════════════════════
#  LINK CLASSIFICATION
# ════════════════════════════════════════════════

def classify_link(href, canonical_domain=None):
    """Classify a URL as internal or external."""
    if not href or href.startswith("#") or href.startswith("javascript:"):
        return None
    if href.startswith("mailto:") or href.startswith("tel:"):
        return "utility"

    parsed = urlparse(href)
    if not parsed.netloc:
        return "internal"
    if canonical_domain and canonical_domain in parsed.netloc:
        return "internal"
    return "external"


def extract_links(el, canonical_domain=None):
    """Extract and classify all links inside an element."""
    links = []
    for a in el.find_all("a", recursive=True):
        href = a.get("href")
        link_type = classify_link(href, canonical_domain)
        if link_type:
            links.append({
                "href": href,
                "type": link_type,
                "anchor": a.get_text(strip=True),
            })
    return links


# ════════════════════════════════════════════════
#  ELEMENT CLASSIFICATION
# ════════════════════════════════════════════════

def classify_element(el):
    """Deterministic classification of HTML elements into block types and roles."""
    tag = el.tag

    if not tag or tag in SKIP_TAGS:
        return None, None

    if tag == "nav":
        if is_breadcrumb(el):
            return "navigation", "breadcrumb"
        return "navigation", "site_navigation"

    if tag in ["ul", "ol"]:
        parent = el.parent
        if parent and parent.tag == "nav":
            return "list", "nav_list"
        return "list", "content_list"

    if tag == "dl":
        return "list", "definition_list"

    if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        return "heading", "section_title"

    if tag == "p":
        return "text", "body_copy"
    if tag == "span":
        text = clean_text(el)
        if len(text) > 30:
            return "text", "inline_text"
        return None, None

    if tag == "table":
        return "table", "data_table"

    if tag in ["pre", "code"]:
        return "code", "example"

    if tag == "script":
        return "script", "script"

    if tag == "style":
        return "style", "presentation"

    if tag == "form":
        return "form", "interaction"

    if tag == "img":
        return "media", "image"
    if tag == "video":
        return "media", "video"
    if tag == "audio":
        return "media", "audio"
    if tag == "svg":
        return "media", "svg"

    if tag == "a":
        return "link", "hyperlink"

    if tag in CONTAINER_TAGS:
        return "container", CONTAINER_ROLES.get(tag, "generic_container")

    return None, None


# ════════════════════════════════════════════════
#  ELEMENT -> JSON BLOCK
# ════════════════════════════════════════════════

def element_to_block(el, canonical_domain=None, seo_mode=False):
    """Convert a single Node into a classified JSON block."""
    block_type, role = classify_element(el)

    if block_type is None:
        return None

    if seo_mode and block_type not in SEO_ALLOWED_TYPES:
        return None

    block_id = gen_id()

    block = {
        "block_id": block_id,
        "block_type": block_type,
        "html_tag": el.tag,
        "role": role,
        "state": {
            "origin": "original",
            "status": "informational",
        },
        "source": {
            "classes": el.get_classes(),
            "id": el.get("id"),
        },
        "content": {},
        "links": [],
    }

    if block_type == "heading":
        block["content"] = {
            "level": int(el.tag[1]),
            "text": clean_text(el),
        }

    elif block_type == "text":
        block["content"] = {
            "text": clean_text(el),
        }

    elif block_type == "list":
        items = []
        for li in el.find_all("li", recursive=False):
            items.append({
                "text": li.get_text(strip=True),
                "links": extract_links(li, canonical_domain),
            })
        block["content"] = {
            "list_type": "ordered" if el.tag == "ol" else ("definition" if el.tag == "dl" else "unordered"),
            "items": items,
        }

    elif block_type == "navigation":
        items = []
        for a in el.find_all("a"):
            items.append({
                "label": a.get_text(strip=True),
                "url": a.get("href"),
                "type": classify_link(a.get("href"), canonical_domain),
            })
        block["content"] = {
            "items": items,
        }

    elif block_type == "table":
        headers = []
        rows = []
        for i, tr in enumerate(el.find_all("tr")):
            cells = [td.get_text(strip=True) for td in tr.find_all("td") + tr.find_all("th")]
            if i == 0 and tr.find("th"):
                headers = cells
            else:
                rows.append(cells)
        block["content"] = {
            "headers": headers,
            "rows": rows,
        }

    elif block_type == "code":
        classes = el.get_classes()
        block["content"] = {
            "language": classes[0] if classes else "unknown",
            "code": el.get_text(),
        }

    elif block_type == "media":
        block["content"] = {
            "src": el.get("src"),
            "alt": el.get("alt"),
            "width": el.get("width"),
            "height": el.get("height"),
        }

    elif block_type == "form":
        fields = []
        for inp in el.find_all("input") + el.find_all("select") + el.find_all("textarea"):
            fields.append({
                "name": inp.get("name"),
                "type": inp.get("type", "text"),
                "required": inp.has_attr("required"),
            })
        block["content"] = {
            "action": el.get("action"),
            "method": el.get("method", "get"),
            "fields": fields,
        }

    elif block_type == "script":
        src = el.get("src")
        block["content"] = {
            "external": bool(src),
            "src": src,
        }

    elif block_type == "style":
        block["content"] = {
            "rules_count": el.get_text().count("{"),
        }

    elif block_type == "container":
        block["content"] = {
            "text_preview": clean_text(el)[:200],
        }

    elif block_type == "link":
        href = el.get("href")
        block["content"] = {
            "href": href,
            "anchor": clean_text(el),
            "type": classify_link(href, canonical_domain),
        }

    if block_type not in ("navigation", "link", "script", "style"):
        block["links"] = extract_links(el, canonical_domain)

    return block


# ════════════════════════════════════════════════
#  HTML -> STRUCTURED SECTIONS
# ════════════════════════════════════════════════

def _walk_nodes(node):
    """Yield all descendant nodes depth-first."""
    for child in node.children:
        if child.tag is not None:
            yield child
            yield from _walk_nodes(child)


def build_sections(html, canonical_domain=None, seo_mode=False):
    """Parse HTML into sections grouped by headings."""
    root = parse_html(html)

    sections = []
    current_section = {
        "section_id": gen_id(),
        "heading": "Document Start",
        "heading_level": 0,
        "blocks": [],
    }

    for el in _walk_nodes(root):
        if el.tag in SKIP_TAGS:
            continue

        block = element_to_block(el, canonical_domain, seo_mode)
        if not block:
            continue

        if block["block_type"] == "heading":
            if current_section["blocks"]:
                sections.append(current_section)
            current_section = {
                "section_id": gen_id(),
                "heading": block["content"].get("text", "Untitled"),
                "heading_level": block["content"].get("level", 0),
                "blocks": [block],
            }
        else:
            current_section["blocks"].append(block)

    if current_section["blocks"]:
        sections.append(current_section)

    return sections


# ════════════════════════════════════════════════
#  EXTRACT METADATA
# ════════════════════════════════════════════════

def extract_metadata(html):
    """Extract page-level metadata."""
    root = parse_html(html)

    def meta_content(name=None, prop=None):
        for m in root.find_all("meta"):
            if name and m.get("name") == name:
                return m.get("content")
            if prop and m.get("property") == prop:
                return m.get("content")
        return None

    title_node = root.find("title")
    canonical_node = None
    for link_node in root.find_all("link"):
        rel = link_node.get("rel")
        if rel and ("canonical" in rel if isinstance(rel, list) else rel == "canonical"):
            canonical_node = link_node
            break

    html_node = root.find("html")

    return {
        "title": title_node.get_text(strip=True) if title_node else None,
        "description": meta_content(name="description"),
        "canonical_url": canonical_node.get("href") if canonical_node else None,
        "og_title": meta_content(prop="og:title"),
        "og_description": meta_content(prop="og:description"),
        "og_url": meta_content(prop="og:url"),
        "lang": html_node.get("lang") if html_node else None,
        "viewport": meta_content(name="viewport"),
    }


# ════════════════════════════════════════════════
#  LINK SUMMARY
# ════════════════════════════════════════════════

def build_link_summary(sections):
    """Build a deduplicated link summary across the entire document."""
    internal = {}
    external = {}

    for section in sections:
        for block in section["blocks"]:
            for link in block.get("links", []):
                href = link.get("href")
                if not href:
                    continue
                bucket = internal if link["type"] == "internal" else external
                if href not in bucket:
                    bucket[href] = {
                        "href": href,
                        "type": link["type"],
                        "anchors": [],
                        "occurrences": 0,
                    }
                bucket[href]["occurrences"] += 1
                anchor = link.get("anchor", "")
                if anchor and anchor not in bucket[href]["anchors"]:
                    bucket[href]["anchors"].append(anchor)

    return {
        "internal_links": list(internal.values()),
        "external_links": list(external.values()),
        "internal_count": len(internal),
        "external_count": len(external),
    }


# ════════════════════════════════════════════════
#  BUILD CANONICAL JSON
# ════════════════════════════════════════════════

def build_canonical_json(source_file, metadata, sections, link_summary, seo_mode):
    """Build the master canonical JSON document."""
    return {
        "document": {
            "id": gen_id(),
            "type": "html_document",
            "profile": "seo" if seo_mode else "full",
            "source": {
                "format": "mhtml",
                "original_file": source_file,
            },
            "metadata": metadata,
        },
        "link_summary": link_summary,
        "sections_count": len(sections),
        "blocks_count": sum(len(s["blocks"]) for s in sections),
    }


# ════════════════════════════════════════════════
#  BUILD OUTPUT HTML
# ════════════════════════════════════════════════

def build_output_html(original_html, metadata, sections, canonical_json):
    """Produce the final self-contained .ai.html file."""

    title = metadata.get("title") or "Transformed Document"

    # Build section HTML with <details>
    sections_html = []
    for i, section in enumerate(sections):
        is_first = i == 0
        heading = section["heading"]
        level = section.get("heading_level", 0)
        block_count = len(section["blocks"])

        type_counts = {}
        for b in section["blocks"]:
            t = b["block_type"]
            type_counts[t] = type_counts.get(t, 0) + 1
        type_summary = ", ".join(f"{v} {k}" for k, v in sorted(type_counts.items()))

        open_attr = " open" if is_first else ""
        sections_html.append(f"""
        <details class="section" id="{section['section_id']}"{open_attr}>
            <summary>
                <strong>{'#' * max(level, 1)} {heading}</strong>
                <span class="meta">{block_count} blocks ({type_summary})</span>
            </summary>
            <div class="section-content">
        """)

        for block in section["blocks"]:
            bt = block["block_type"]
            role = block["role"]
            bid = block["block_id"]
            content = block.get("content", {})

            if bt == "heading":
                tag = f"h{content.get('level', 2)}"
                sections_html.append(
                    f'<{tag} id="{bid}">{content.get("text", "")}</{tag}>'
                )

            elif bt == "text":
                text = content.get("text", "")
                if text:
                    sections_html.append(f'<p id="{bid}" class="block-text">{text}</p>')

            elif bt == "list":
                list_tag = "ol" if content.get("list_type") == "ordered" else "ul"
                items_html = "".join(
                    f'<li>{item.get("text", "")}</li>'
                    for item in content.get("items", [])
                )
                sections_html.append(f'<{list_tag} id="{bid}">{items_html}</{list_tag}>')

            elif bt == "table":
                headers = content.get("headers", [])
                rows = content.get("rows", [])
                table_html = '<table id="' + bid + '" class="block-table">'
                if headers:
                    table_html += "<thead><tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr></thead>"
                table_html += "<tbody>"
                for row in rows:
                    table_html += "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
                table_html += "</tbody></table>"
                sections_html.append(table_html)

            elif bt == "navigation":
                items = content.get("items", [])
                nav_html = f'<nav id="{bid}" class="block-nav"><ul>'
                for item in items:
                    label = item.get("label", "")
                    url = item.get("url", "#")
                    link_type = item.get("type", "")
                    badge = f' <span class="link-type">[{link_type}]</span>' if link_type else ""
                    nav_html += f'<li><a href="{url}">{label}</a>{badge}</li>'
                nav_html += "</ul></nav>"
                sections_html.append(nav_html)

            elif bt == "code":
                code_text = content.get("code", "")
                lang = content.get("language", "")
                sections_html.append(
                    f'<pre id="{bid}" class="block-code"><code class="{lang}">{code_text[:2000]}</code></pre>'
                )

            elif bt == "media":
                alt = content.get("alt", "")
                src = content.get("src", "")
                sections_html.append(
                    f'<div id="{bid}" class="block-media">[Image: alt="{alt}" src="{src}"]</div>'
                )

            elif bt == "container":
                preview = content.get("text_preview", "")
                if preview:
                    sections_html.append(
                        f'<div id="{bid}" class="block-container"><em>[{role}]</em> {preview}</div>'
                    )

            elif bt == "form":
                fields = content.get("fields", [])
                fields_str = ", ".join(f'{f.get("name", "?")}:{f.get("type", "?")}' for f in fields)
                sections_html.append(
                    f'<div id="{bid}" class="block-form">[Form: action={content.get("action", "?")} fields=({fields_str})]</div>'
                )

            links = block.get("links", [])
            if links:
                int_count = sum(1 for l in links if l["type"] == "internal")
                ext_count = sum(1 for l in links if l["type"] == "external")
                sections_html.append(
                    f'<div class="link-badge">Links: {int_count} internal, {ext_count} external</div>'
                )

        sections_html.append("</div></details>")

    sections_joined = "\n".join(sections_html)

    # Link summary HTML
    link_summary = canonical_json.get("link_summary", {})
    internal_links = link_summary.get("internal_links", [])
    external_links = link_summary.get("external_links", [])

    link_summary_html = f"""
    <details id="link-summary">
        <summary><strong>Link Summary</strong>
            <span class="meta">{link_summary.get('internal_count', 0)} internal, {link_summary.get('external_count', 0)} external</span>
        </summary>
        <details>
            <summary>Internal Links ({link_summary.get('internal_count', 0)})</summary>
            <ul>
                {"".join(f'<li><code>{l["href"]}</code> ({l["occurrences"]}x) anchors: {", ".join(l["anchors"][:5])}</li>' for l in internal_links[:200])}
            </ul>
        </details>
        <details>
            <summary>External Links ({link_summary.get('external_count', 0)})</summary>
            <ul>
                {"".join(f'<li><code>{l["href"]}</code> ({l["occurrences"]}x)</li>' for l in external_links[:100])}
            </ul>
        </details>
    </details>
    """

    # Chunk JSON
    chunk_scripts = []
    for section in sections:
        chunk_json = json.dumps({
            "chunk_id": section["section_id"],
            "chunk_type": "section",
            "heading": section["heading"],
            "heading_level": section["heading_level"],
            "blocks": section["blocks"],
        }, indent=2, ensure_ascii=False)
        chunk_scripts.append(
            f'<script type="application/json" class="ai-chunk" data-section="{section["section_id"]}">\n{chunk_json}\n</script>'
        )

    chunks_joined = "\n".join(chunk_scripts)

    # Master JSON
    master_json = json.dumps(canonical_json, indent=2, ensure_ascii=False)

    # Final HTML
    return f"""<!DOCTYPE html>
<html lang="{metadata.get('lang', 'en')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — AI Readable</title>
<style>
:root {{
    --bg: #fafafa;
    --fg: #1a1a1a;
    --accent: #2563eb;
    --border: #ddd;
    --code-bg: #f0f0f0;
    --section-bg: #fff;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: var(--bg);
    color: var(--fg);
    line-height: 1.6;
    padding: 2rem;
    max-width: 1100px;
    margin: 0 auto;
}}
h1 {{ font-size: 1.6rem; margin-bottom: 1.5rem; border-bottom: 2px solid var(--accent); padding-bottom: 0.5rem; }}
h2 {{ font-size: 1.3rem; margin: 1rem 0 0.5rem; }}
h3 {{ font-size: 1.1rem; margin: 0.8rem 0 0.4rem; }}
.doc-meta {{ background: var(--section-bg); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; margin-bottom: 1.5rem; }}
.doc-meta p {{ margin: 0.2rem 0; font-size: 0.9rem; }}
.doc-meta code {{ background: var(--code-bg); padding: 0.15rem 0.4rem; border-radius: 3px; font-size: 0.85rem; }}
details.section {{
    background: var(--section-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 0.75rem;
    overflow: hidden;
}}
details.section > summary {{
    padding: 0.75rem 1rem;
    cursor: pointer;
    background: #f5f5f5;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
details.section > summary:hover {{ background: #eef; }}
.section-content {{ padding: 0.75rem 1rem; }}
.meta {{ font-size: 0.78rem; color: #888; font-weight: normal; }}
p.block-text {{ margin: 0.4rem 0; }}
ul, ol {{ margin: 0.4rem 0 0.4rem 1.5rem; }}
table.block-table {{ width: 100%; border-collapse: collapse; margin: 0.5rem 0; font-size: 0.88rem; }}
table.block-table th, table.block-table td {{ border: 1px solid var(--border); padding: 0.4rem 0.6rem; text-align: left; }}
table.block-table th {{ background: #f0f0f0; font-weight: 600; }}
pre.block-code {{ background: var(--code-bg); padding: 0.8rem; border-radius: 4px; overflow-x: auto; font-size: 0.82rem; margin: 0.4rem 0; }}
.block-nav ul {{ list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 0.3rem; }}
.block-nav li {{ background: #eef; padding: 0.2rem 0.5rem; border-radius: 3px; font-size: 0.82rem; }}
.block-nav a {{ color: var(--accent); text-decoration: none; }}
.link-type {{ font-size: 0.7rem; color: #999; }}
.block-media {{ background: #f8f8f8; padding: 0.4rem; border-radius: 4px; font-size: 0.82rem; color: #666; margin: 0.3rem 0; }}
.block-container {{ font-size: 0.85rem; padding: 0.3rem 0; color: #555; }}
.block-form {{ background: #fef9e7; padding: 0.4rem; border-radius: 4px; font-size: 0.82rem; margin: 0.3rem 0; }}
.link-badge {{ font-size: 0.75rem; color: var(--accent); margin: 0.2rem 0 0.5rem; }}
#link-summary {{ background: var(--section-bg); border: 1px solid var(--border); border-radius: 8px; padding: 0; margin-bottom: 1rem; }}
#link-summary > summary {{ padding: 0.75rem 1rem; cursor: pointer; background: #f5f5f5; display: flex; justify-content: space-between; }}
#link-summary details {{ padding: 0 1rem 0.5rem; }}
#link-summary ul {{ font-size: 0.82rem; }}
#original-source {{ margin-top: 1.5rem; }}
#original-source > summary {{ padding: 0.75rem 1rem; cursor: pointer; background: #f5f5f5; border: 1px solid var(--border); border-radius: 8px; }}
.original-html {{ max-height: 600px; overflow: auto; border: 1px solid var(--border); padding: 1rem; margin-top: 0.5rem; border-radius: 4px; background: #fff; }}
</style>
</head>
<body>

<h1>{title}</h1>

<div class="doc-meta">
    <p><strong>Source:</strong> <code>{canonical_json["document"]["source"]["original_file"]}</code></p>
    <p><strong>Canonical URL:</strong> <code>{metadata.get("canonical_url") or "not detected"}</code></p>
    <p><strong>Profile:</strong> {canonical_json["document"]["profile"]}</p>
    <p><strong>Sections:</strong> {canonical_json["sections_count"]} | <strong>Blocks:</strong> {canonical_json["blocks_count"]}</p>
</div>

{link_summary_html}

{sections_joined}

<details id="original-source">
    <summary><strong>Original HTML Source</strong></summary>
    <div class="original-html">
        <pre><code>{original_html[:50000].replace("<", "&lt;").replace(">", "&gt;")}</code></pre>
    </div>
</details>

<!-- AI CANONICAL MAP -->
<script type="application/json" id="ai-canonical-map">
{master_json}
</script>

<!-- AI SECTION CHUNKS -->
{chunks_joined}

</body>
</html>"""


# ════════════════════════════════════════════════
#  MAIN PIPELINE
# ════════════════════════════════════════════════

def process_mhtml(mhtml_path, seo_mode=False):
    """Full pipeline: MHTML -> .ai.html"""
    print(f"\n  Parsing: {mhtml_path.name}")

    html = extract_html_from_mhtml(mhtml_path)
    if not html:
        print(f"  [SKIP] No HTML found in {mhtml_path.name}")
        return

    canonical_domain = detect_canonical_domain(html)
    print(f"  Domain: {canonical_domain or 'not detected'}")

    metadata = extract_metadata(html)
    print(f"  Title: {metadata.get('title', 'none')}")

    sections = build_sections(html, canonical_domain, seo_mode)
    total_blocks = sum(len(s["blocks"]) for s in sections)
    print(f"  Sections: {len(sections)} | Blocks: {total_blocks}")

    link_summary = build_link_summary(sections)
    print(f"  Links: {link_summary['internal_count']} internal, {link_summary['external_count']} external")

    canonical_json = build_canonical_json(
        source_file=mhtml_path.name,
        metadata=metadata,
        sections=sections,
        link_summary=link_summary,
        seo_mode=seo_mode,
    )
    canonical_json["link_summary"] = link_summary

    output_html = build_output_html(html, metadata, sections, canonical_json)

    # Output in the SAME directory as the source file
    output_filename = mhtml_path.stem + ".ai.html"
    output_path = mhtml_path.parent / output_filename
    output_path.write_text(output_html, encoding="utf-8")

    size_kb = output_path.stat().st_size / 1024
    print(f"  Saved: {output_path} ({size_kb:.0f} KB)")


def main():
    seo_mode = "--seo" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--seo"]

    # Interactive mode if no path provided
    if not args:
        print("\n=== MHTML Transformer ===\n")
        raw_path = input("Enter file or folder path: ").strip().strip('"').strip("'")
        seo_input = input("SEO mode? (strips scripts/styles) [y/N]: ").strip().lower()
        if seo_input in ("y", "yes"):
            seo_mode = True
        input_path = Path(raw_path)
    else:
        input_path = Path(args[0])

    if seo_mode:
        print("\nSEO mode: scripts and styles will be excluded")

    if input_path.is_file() and is_mhtml(input_path):
        process_mhtml(input_path, seo_mode)

    elif input_path.is_dir():
        mhtml_files = list(input_path.rglob("*.mhtml")) + list(input_path.rglob("*.mht"))
        if not mhtml_files:
            print(f"No .mhtml/.mht files found in {input_path}")
            sys.exit(1)
        print(f"\nFound {len(mhtml_files)} MHTML file(s) in {input_path}")
        for f in mhtml_files:
            process_mhtml(f, seo_mode)

    else:
        print(f"Invalid path or not an MHTML file: {input_path}")
        sys.exit(1)

    print("\nDone!")


if __name__ == "__main__":
    main()
