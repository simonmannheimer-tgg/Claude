"""
Build competitor corpus for AEO content similarity analysis.

Crawls competitor category/guide pages, chunks text into 256-token passages,
encodes with BGE-M3 (or all-MiniLM fallback), and upserts into Qdrant local store.

Run monthly or when competitors update their content strategy.

Usage:
    python build_competitor_corpus.py
    python build_competitor_corpus.py --dry-run     # crawl but don't upsert
    python build_competitor_corpus.py --domains jbhifi.com.au,harveynorman.com.au

Requires:
    pip install playwright httpx beautifulsoup4 qdrant-client FlagEmbedding
    playwright install chromium --with-deps
"""

import argparse
import json
import re
import sys
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

DEFAULT_DOMAIN_PATHS = {
    "jbhifi.com.au": [
        "/collections/tvs",
        "/collections/air-conditioners",
        "/collections/washing-machines",
        "/collections/laptops",
        "/blogs/news",
    ],
    "harveynorman.com.au": [
        "/tv-blu-ray-home-theatre/tvs-by-screen-size/all-tvs",
        "/washing-machines-dryers/washing-machines",
        "/air-conditioners-fans/air-conditioners",
        "/computers/laptops",
        "/buying-guides/security-camera-buying-guide",
    ],
    "appliancesonline.com.au": [
        "/category/refrigeration/fridges/",
        "/category/washing-machines/front-loaders/",
        "/category/air-conditioning/split-systems/",
        "/article/refrigerator-size-guide/",
    ],
}

DEFAULT_DOMAINS = list(DEFAULT_DOMAIN_PATHS.keys())

CHUNK_TOKENS = 256
OVERLAP_TOKENS = 32


# ── Embedding ──────────────────────────────────────────────────────────────────

def _get_encoder():
    try:
        from FlagEmbedding import BGEM3FlagModel
        import numpy as np
        model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)
        def encode(texts):
            out = model.encode(texts, return_dense=True, return_sparse=False, return_colbert_vecs=False)
            vecs = out["dense_vecs"]
            norms = np.linalg.norm(vecs, axis=1, keepdims=True)
            return (vecs / np.where(norms == 0, 1, norms)).tolist()
        print("  Encoder: BGE-M3")
        return encode
    except ImportError:
        pass
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
        def encode(texts):
            return model.encode(texts, normalize_embeddings=True).tolist()
        print("  Encoder: all-MiniLM-L6-v2 (BGE-M3 not installed)")
        return encode
    except ImportError:
        print("ERROR: No embedding model available. pip install FlagEmbedding or sentence-transformers",
              file=sys.stderr)
        sys.exit(1)


# ── Text chunking ──────────────────────────────────────────────────────────────

def _chunk_text(text: str, chunk_tokens: int = CHUNK_TOKENS, overlap: int = OVERLAP_TOKENS) -> list[str]:
    """Split text into overlapping chunks approximately chunk_tokens words each."""
    words = text.split()
    if not words:
        return []
    chunks = []
    step = chunk_tokens - overlap
    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_tokens])
        if len(chunk.split()) >= 30:  # skip tiny fragments
            chunks.append(chunk)
    return chunks


def _extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    # Remove nav/header/footer/script/style
    for tag in soup.find_all(["nav", "header", "footer", "script", "style", "noscript"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body
    if main:
        return main.get_text(separator=" ", strip=True)
    return soup.get_text(separator=" ", strip=True)


def _classify_url(url: str) -> str:
    if "/buying-guide" in url or "/guide" in url:
        return "guide"
    if re.search(r'-\d{5,}|/p/', url):
        return "product"
    return "category"


# ── Crawler ────────────────────────────────────────────────────────────────────

def _playwright_fetch(url: str) -> str:
    """Fetch a Cloudflare-protected page via headless Chromium. Returns raw HTML or ''."""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            ctx = browser.new_context(user_agent=BROWSER_UA)
            page = ctx.new_page()
            page.goto(url, timeout=30000, wait_until="networkidle")
            html = page.content()
            browser.close()
            return html
    except Exception as e:
        print(f"    (playwright error: {e})")
        return ""


def crawl_domain(domain: str, paths: list[str]) -> list[dict]:
    """Returns list of {"url", "text", "page_type"} dicts."""
    base = f"https://www.{domain}"
    results = []
    for path in paths:
        url = base + path
        try:
            resp = httpx.get(url, timeout=20, follow_redirects=True,
                             headers={"User-Agent": BROWSER_UA})
            if resp.status_code != 200:
                print(f"  ✗ {url} — HTTP {resp.status_code}")
                continue
            html = resp.text
            text = _extract_text(html)
            word_count = len(text.split())
            if word_count < 200:
                print(f"  ⚠ {url} — only {word_count} words via httpx, retrying with Playwright...")
                html = _playwright_fetch(url)
                text = _extract_text(html)
                word_count = len(text.split())
            if word_count < 200:
                print(f"  ✗ {url} — only {word_count} words after Playwright (blocked)")
                continue
            page_type = _classify_url(url)
            results.append({"url": url, "text": text, "page_type": page_type, "domain": domain})
            print(f"  ✓ {url} — {word_count} words [{page_type}]")
        except Exception as e:
            print(f"  ✗ {url} — {e}")
    return results


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Build Qdrant competitor corpus")
    parser.add_argument("--domains", type=str, default="",
                        help="Comma-separated domains (default: jbhifi, harveynorman, appliancesonline)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Crawl and chunk but don't upsert into Qdrant")
    parser.add_argument("--qdrant-path", type=str, default="./qdrant_data",
                        help="Qdrant local storage path (default: ./qdrant_data)")
    args = parser.parse_args()

    domains = [d.strip() for d in args.domains.split(",") if d.strip()] or DEFAULT_DOMAINS
    encode = _get_encoder()

    all_pages = []
    for domain in domains:
        print(f"\nCrawling {domain}...")
        paths = DEFAULT_DOMAIN_PATHS.get(domain, ["/"])
        pages = crawl_domain(domain, paths)
        all_pages.extend(pages)

    if not all_pages:
        print("No pages crawled — all competitor URLs returned 404 or were blocked. Check DEFAULT_DOMAIN_PATHS.", file=sys.stderr)
        sys.exit(0)

    # Chunk and encode
    print(f"\nChunking {len(all_pages)} pages...")
    all_passages = []
    for page in all_pages:
        chunks = _chunk_text(page["text"])
        for chunk in chunks:
            all_passages.append({
                "text": chunk,
                "url": page["url"],
                "domain": page["domain"],
                "page_type": page["page_type"],
            })
    print(f"  {len(all_passages)} chunks across {len(all_pages)} pages")

    # Encode in batches
    print("Encoding...")
    batch_size = 32
    vectors = []
    for i in range(0, len(all_passages), batch_size):
        batch = [p["text"] for p in all_passages[i:i+batch_size]]
        batch_vecs = encode(batch)
        vectors.extend(batch_vecs)
        print(f"  Encoded {min(i+batch_size, len(all_passages))}/{len(all_passages)}")

    manifest_path = Path("seo/outputs/aeo/corpus-manifest.json")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print("\nDry run — skipping Qdrant upsert")
        manifest_path.write_text(json.dumps({
            "dry_run": True,
            "domains": domains,
            "pages_crawled": len(all_pages),
            "passages": len(all_passages),
            "vector_dim": len(vectors[0]) if vectors else 0,
        }, indent=2))
        print(f"Manifest: {manifest_path}")
        return

    # Upsert to Qdrant
    try:
        from shared.qdrant_client import get_client, upsert_passages, get_collection_info
        client = get_client(args.qdrant_path)
        points = [
            {"id": i, "vector": vectors[i], "payload": all_passages[i]}
            for i in range(len(all_passages))
        ]
        vector_size = len(vectors[0]) if vectors else 384
        print(f"\nUpserting {len(points)} passages to Qdrant (dim={vector_size})...")
        upsert_passages(client, points, vector_size)
        info = get_collection_info(client)
        print(f"  Qdrant collection: {info['vectors_count']} vectors")
        manifest_path.write_text(json.dumps({
            "domains": domains,
            "pages_crawled": len(all_pages),
            "passages": len(all_passages),
            "qdrant_path": args.qdrant_path,
            "vector_dim": len(vectors[0]) if vectors else 0,
            "collection_count": info["vectors_count"],
        }, indent=2))
    except ImportError:
        print("qdrant-client not installed — skipping upsert (pip install qdrant-client)")
        manifest_path.write_text(json.dumps({
            "qdrant_available": False,
            "passages": len(all_passages),
        }, indent=2))

    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
