"""
Qdrant local vector store client for AEO competitor corpus.

Used by build_competitor_corpus.py (write) and run_content_aeo.py (read).

Install: pip install qdrant-client
"""

from pathlib import Path

COLLECTION = "aeo_competitor_corpus"
DEFAULT_PATH = str(Path(__file__).parent.parent / "qdrant_data")


def get_client(path: str = DEFAULT_PATH):
    from qdrant_client import QdrantClient
    return QdrantClient(path=path)


def ensure_collection(client, vector_size: int) -> None:
    """Create collection if missing; recreate if vector size changed (e.g. BGE-M3→MiniLM)."""
    from qdrant_client.models import Distance, VectorParams
    existing = [c.name for c in client.get_collections().collections]
    if COLLECTION in existing:
        info = client.get_collection(COLLECTION)
        existing_size = info.config.params.vectors.size
        if existing_size != vector_size:
            print(f"  ⚠ Collection dim mismatch ({existing_size} → {vector_size}) — recreating")
            client.delete_collection(COLLECTION)
        else:
            return
    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
    )


def upsert_passages(client, passages: list[dict], vector_size: int) -> None:
    """
    passages: list of {"id": int, "vector": list[float], "payload": {...}}
    payload should include: {"text": str, "url": str, "domain": str, "page_type": str}
    """
    from qdrant_client.models import PointStruct
    ensure_collection(client, vector_size)
    points = [
        PointStruct(id=p["id"], vector=p["vector"], payload=p.get("payload", {}))
        for p in passages
    ]
    client.upsert(collection_name=COLLECTION, points=points)


def search_similar(client, query_vector: list[float], top_k: int = 5) -> list[dict]:
    """Returns top-k similar passages with scores and payloads."""
    hits = client.search(
        collection_name=COLLECTION,
        query_vector=query_vector,
        limit=top_k,
        with_payload=True,
    )
    return [
        {"score": h.score, "text": h.payload.get("text", ""), "url": h.payload.get("url", ""),
         "domain": h.payload.get("domain", ""), "page_type": h.payload.get("page_type", "")}
        for h in hits
    ]


def get_collection_info(client) -> dict:
    try:
        info = client.get_collection(COLLECTION)
        # qdrant-client ≥1.7 may return None for vectors_count until indexing completes;
        # points_count is always available immediately after upsert.
        count = info.points_count
        if count is None:
            count = getattr(info, "vectors_count", None) or 0
        return {"vectors_count": count, "exists": True}
    except Exception:
        return {"vectors_count": 0, "exists": False}
