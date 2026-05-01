#!/usr/bin/env python3
"""
extract_competitors.py — fetch and parse competitor pages for a target keyword.

Searches for the keyword on each competitor domain using their site search or
falls back to a Google site: query via Semrush organic data. Fetches the
top-ranking page and extracts H1/H2/H3 structure plus body text.

Usage:
    python3 .claude/skills/tgg-ce-competitor-extract/scripts/extract_competitors.py \
        --keyword "heat pump dryer" \
        --competitors jbhifi.com.au,harveynorman.com.au,appliancesonline.com.au \
        --output runs/<run-id>/competitor-raw.json

Environment:
    SEMRUSH_API_KEY — used to find top-ranking competitor URLs (optional)

Outputs JSON list of competitor page extracts with keys:
    domain, url, status, headings, body_text_excerpt
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

TIMEOUT = 20
USER_AGENT = (
    "Mozilla/5.0 (compatible; TGGResearchBot/1.0; +https://thegoodguys.com.au)"
)


class HeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings: list[dict] = []
        self.body_chunks: list[str] = []
        self._current_tag: str = ""
        self._current_text: list[str] = []
        self._in_body_tag = False
        self._skip_tags = {"script", "style", "nav", "header", "footer"}
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in self._skip_tags:
            self._skip_depth += 1
        if self._skip_depth:
            return
        if tag in ("h1", "h2", "h3"):
            self._current_tag = tag
            self._current_text = []
        elif tag in ("p", "li"):
            self._in_body_tag = True
            self._current_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag in self._skip_tags and self._skip_depth:
            self._skip_depth -= 1
            return
        if tag in ("h1", "h2", "h3") and self._current_tag == tag:
            text = " ".join(self._current_text).strip()
            if text:
                self.headings.append({"level": tag.upper(), "text": text})
            self._current_tag = ""
            self._current_text = []
        elif tag in ("p", "li") and self._in_body_tag:
            text = " ".join(self._current_text).strip()
            if len(text) > 40:
                self.body_chunks.append(text)
            self._in_body_tag = False
            self._current_text = []

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if self._current_tag or self._in_body_tag:
            cleaned = re.sub(r"\s+", " ", data).strip()
            if cleaned:
                self._current_text.append(cleaned)


def fetch_page(url: str) -> tuple[str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            charset = "utf-8"
            content_type = resp.headers.get("Content-Type", "")
            if "charset=" in content_type:
                charset = content_type.split("charset=")[-1].split(";")[0].strip()
            html = resp.read().decode(charset, errors="replace")
            return html, resp.geturl()
    except Exception as exc:
        raise RuntimeError(str(exc)) from exc


def find_competitor_url(keyword: str, domain: str) -> str:
    # Try Semrush organic data first; fall back to a direct site search URL
    import os
    api_key = os.environ.get("SEMRUSH_API_KEY")
    if api_key:
        try:
            params = urllib.parse.urlencode({
                "key": api_key,
                "action": "phrase_organic",
                "phrase": keyword,
                "database": "au",
                "display_limit": "20",
                "export_columns": "Dn,Ur,Po",
            })
            with urllib.request.urlopen(
                f"https://api.semrush.com/?{params}", timeout=15
            ) as resp:
                raw = resp.read().decode("utf-8").strip()
            for line in raw.splitlines()[1:]:
                parts = line.split(";")
                if len(parts) >= 2 and domain in parts[0]:
                    return parts[1]
        except Exception:
            pass

    # Fallback: guess the search URL for common competitor patterns
    slug = keyword.lower().replace(" ", "-")
    fallbacks = {
        "jbhifi.com.au": f"https://www.jbhifi.com.au/search?q={urllib.parse.quote(keyword)}",
        "harveynorman.com.au": f"https://www.harveynorman.com.au/search?q={urllib.parse.quote(keyword)}",
        "appliancesonline.com.au": f"https://www.appliancesonline.com.au/search?q={urllib.parse.quote(keyword)}",
    }
    return fallbacks.get(domain, f"https://www.{domain}/search?q={urllib.parse.quote(keyword)}")


def extract(keyword: str, domain: str) -> dict:
    result: dict = {"domain": domain, "url": "", "status": "", "headings": [], "body_text_excerpt": ""}
    try:
        url = find_competitor_url(keyword, domain)
        result["url"] = url
        html, final_url = fetch_page(url)
        result["url"] = final_url
        parser = HeadingParser()
        parser.feed(html)
        result["headings"] = parser.headings[:30]
        result["body_text_excerpt"] = " ".join(parser.body_chunks[:10])
        result["status"] = "fetched"
    except Exception as exc:
        result["status"] = f"failed — {exc}"
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch and parse competitor pages.")
    parser.add_argument("--keyword", required=True)
    parser.add_argument("--competitors", required=True, help="Comma-separated domains")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    domains = [d.strip() for d in args.competitors.split(",") if d.strip()]
    results = []
    errors = 0

    for domain in domains:
        print(f"Fetching {domain}...", file=sys.stderr)
        extract_result = extract(args.keyword, domain)
        results.append(extract_result)
        if "failed" in extract_result["status"]:
            errors += 1
            print(f"  {extract_result['status']}", file=sys.stderr)
        else:
            heading_count = len(extract_result["headings"])
            print(f"  OK — {heading_count} headings extracted", file=sys.stderr)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    print(f"\nResults written to {out_path} ({errors} failures)")
    if errors == len(domains):
        sys.exit(1)


if __name__ == "__main__":
    main()
