

#HOW TO USE
# python "C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\VSCode (new)\MHTML_Parser.py" [Your copied file path here]

#!/usr/bin/env python3
"""
MHTML to Readable Format Converter
Extracts HTML, CSS, JS, images, and other assets from .mhtml/.mht files
into an organized folder structure or a single consolidated HTML file.
"""

import email
import base64
import quopri
import os
import re
import sys
import argparse
from pathlib import Path
from urllib.parse import unquote, urlparse


def decode_part(part):
    """Decode a MIME part's payload based on its Content-Transfer-Encoding."""
    encoding = part.get("Content-Transfer-Encoding", "").lower()
    payload = part.get_payload(decode=False)

    if encoding == "base64":
        try:
            return base64.b64decode(payload)
        except Exception:
            return payload.encode("utf-8", errors="replace") if isinstance(payload, str) else payload
    elif encoding == "quoted-printable":
        raw = payload.encode("utf-8", errors="replace") if isinstance(payload, str) else payload
        return quopri.decodestring(raw)
    elif encoding in ("7bit", "8bit", "binary", ""):
        return payload.encode("utf-8", errors="replace") if isinstance(payload, str) else payload
    else:
        return payload.encode("utf-8", errors="replace") if isinstance(payload, str) else payload


def get_content_location(part):
    """Extract the content location/URL identifier for a MIME part."""
    location = part.get("Content-Location", "")
    if not location:
        content_id = part.get("Content-ID", "")
        if content_id:
            location = content_id.strip("<>")
    return location.strip()


def sanitize_filename(name, max_len=100):
    """Create a safe filename from a URL or string."""
    name = unquote(name)
    name = urlparse(name).path if "://" in name else name
    name = name.split("/")[-1] or "index"
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name)
    return name[:max_len] if name else "unnamed"


def classify_content(content_type):
    """Classify content type into a subfolder category."""
    ct = content_type.lower()
    if "html" in ct:
        return "html"
    elif "css" in ct:
        return "css"
    elif "javascript" in ct or "ecmascript" in ct:
        return "js"
    elif "image" in ct:
        return "images"
    elif "font" in ct or "woff" in ct or "ttf" in ct:
        return "fonts"
    elif "json" in ct or "xml" in ct:
        return "data"
    else:
        return "other"


def parse_mhtml(mhtml_path):
    """Parse the MHTML file and return a list of extracted parts."""
    with open(mhtml_path, "rb") as f:
        raw = f.read()

    msg = email.message_from_bytes(raw)
    parts = []

    if msg.is_multipart():
        for i, part in enumerate(msg.walk()):
            if part.get_content_type() == "multipart/related":
                continue
            content_type = part.get_content_type()
            location = get_content_location(part)
            decoded = decode_part(part)
            parts.append({
                "index": i,
                "content_type": content_type,
                "location": location,
                "data": decoded,
                "category": classify_content(content_type),
                "charset": part.get_content_charset() or "utf-8",
            })
    else:
        # Single-part MHTML (rare but possible)
        decoded = decode_part(msg)
        parts.append({
            "index": 0,
            "content_type": msg.get_content_type(),
            "location": get_content_location(msg),
            "data": decoded,
            "category": classify_content(msg.get_content_type()),
            "charset": msg.get_content_charset() or "utf-8",
        })

    return parts


# ──────────────────────────────────────────────
#  MODE 1: Extract to folder structure
# ──────────────────────────────────────────────
def extract_to_folder(parts, output_dir):
    """Extract all MHTML parts into an organized folder."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest_lines = []
    seen_filenames = {}

    for part in parts:
        category = part["category"]
        sub_dir = output_dir / category
        sub_dir.mkdir(exist_ok=True)

        filename = sanitize_filename(part["location"]) if part["location"] else f"part_{part['index']}"

        # Add extension if missing
        if "." not in filename:
            ext_map = {
                "html": ".html", "css": ".css", "js": ".js",
                "images": ".png", "fonts": ".woff", "data": ".json",
            }
            filename += ext_map.get(category, ".bin")

        # Handle duplicate filenames
        if filename in seen_filenames:
            seen_filenames[filename] += 1
            stem, ext = os.path.splitext(filename)
            filename = f"{stem}_{seen_filenames[filename]}{ext}"
        else:
            seen_filenames[filename] = 0

        file_path = sub_dir / filename
        mode = "wb"
        file_path.write_bytes(part["data"] if isinstance(part["data"], bytes) else part["data"].encode("utf-8"))

        manifest_lines.append(
            f"[{category.upper():>6}]  {file_path.relative_to(output_dir)}  ←  {part['location'] or '(no URL)'}"
        )
        print(f"  ✅  {file_path.relative_to(output_dir)}")

    # Write manifest / index
    manifest_path = output_dir / "_manifest.txt"
    manifest_path.write_text(
        f"MHTML Extraction Manifest\n{'=' * 50}\n\n" + "\n".join(manifest_lines),
        encoding="utf-8",
    )
    print(f"\n📄 Manifest written to {manifest_path}")


# ──────────────────────────────────────────────
#  MODE 2: Consolidate into single readable HTML
# ──────────────────────────────────────────────
def consolidate_to_html(parts, output_path):
    """Merge all parts into one self-contained HTML file with inlined CSS/JS."""
    main_html = None
    css_blocks = []
    js_blocks = []
    other_info = []

    # URL → data mapping for image inlining
    image_map = {}

    for part in parts:
        text = None
        if part["category"] in ("html", "css", "js", "data"):
            try:
                text = part["data"].decode(part["charset"], errors="replace") if isinstance(part["data"], bytes) else part["data"]
            except Exception:
                text = part["data"].decode("utf-8", errors="replace") if isinstance(part["data"], bytes) else str(part["data"])

        if part["category"] == "html" and main_html is None:
            main_html = text
        elif part["category"] == "css":
            css_blocks.append(f"/* Source: {part['location']} */\n{text}")
        elif part["category"] == "js":
            js_blocks.append(f"// Source: {part['location']}\n{text}")
        elif part["category"] == "images":
            b64 = base64.b64encode(part["data"] if isinstance(part["data"], bytes) else part["data"].encode()).decode()
            data_uri = f"data:{part['content_type']};base64,{b64}"
            if part["location"]:
                image_map[part["location"]] = data_uri
        else:
            other_info.append(f"<!-- Embedded asset: {part['location']} ({part['content_type']}) -->")

    if not main_html:
        main_html = "<html><body><p>No HTML part found in MHTML.</p></body></html>"

    # Inline images by replacing URLs in the HTML
    for url, data_uri in image_map.items():
        main_html = main_html.replace(url, data_uri)

    # Inject consolidated CSS into <head>
    if css_blocks:
        combined_css = "\n\n".join(css_blocks)
        style_tag = f"\n<style>\n{combined_css}\n</style>\n"
        if "</head>" in main_html:
            main_html = main_html.replace("</head>", style_tag + "</head>")
        else:
            main_html = style_tag + main_html

    # Inject consolidated JS before </body>
    if js_blocks:
        combined_js = "\n\n".join(js_blocks)
        script_tag = f"\n<script>\n{combined_js}\n</script>\n"
        if "</body>" in main_html:
            main_html = main_html.replace("</body>", script_tag + "</body>")
        else:
            main_html += script_tag

    Path(output_path).write_text(main_html, encoding="utf-8")
    print(f"  ✅  Consolidated HTML written to {output_path}")


# ──────────────────────────────────────────────
#  CLI
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Convert MHTML to readable file(s).",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("input", help="Path to the .mhtml / .mht file")
    parser.add_argument(
        "-m", "--mode",
        choices=["folder", "html"],
        default="html",
        help=(
            "Output mode:\n"
            "  folder  →  Extract into organized subfolders\n"
            "  html    →  Consolidate into a single self-contained HTML file (default)"
        ),
    )
    parser.add_argument("-o", "--output", help="Output folder or file path (auto-generated if omitted)")

    args = parser.parse_args()
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"❌ File not found: {input_path}")
        sys.exit(1)

    print(f"\n🔍 Parsing {input_path.name} …")
    parts = parse_mhtml(str(input_path))
    print(f"   Found {len(parts)} part(s)\n")

    # Print summary
    categories = {}
    for p in parts:
        categories[p["category"]] = categories.get(p["category"], 0) + 1
    for cat, count in sorted(categories.items()):
        print(f"   📦 {cat}: {count} file(s)")
    print()

    if args.mode == "folder":
        output_dir = args.output or str(input_path.with_suffix("")) + "_extracted"
        print(f"📂 Extracting to: {output_dir}\n")
        extract_to_folder(parts, output_dir)
    else:
        output_file = args.output or str(input_path.with_suffix("")) + ".html"
        print(f"📄 Consolidating to: {output_file}\n")
        consolidate_to_html(parts, output_file)

    print("\n✅ Done!")


if __name__ == "__main__":
    main()