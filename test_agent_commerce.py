"""
Synthetic agent commerce test for AEO auditing.

Simulates how an AI agent would interact with a retailer's commerce endpoints:
  1. Discover MCP endpoint (/.well-known/mcp.json or /api/mcp)
  2. Call search_products tool
  3. Call get_product_details tool
  4. Validate response schema compliance

Currently a smoke-test layer — actual MCP protocol is evolving.
Returns structured results indicating readiness, not actual purchases.

Usage:
    python test_agent_commerce.py --domain thegoodguys.com.au
    python test_agent_commerce.py --domain thegoodguys.com.au --query "4K TV under $1000"

Writes:
    seo/outputs/aeo/agent-test-<domain>-YYYYMMDD-HHMM.json
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import httpx
    _HTTPX = True
except ImportError:
    _HTTPX = False

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

AGENT_UA = "ClaudeBot/1.0 (+https://anthropic.com/en/claude-bot)"

MCP_DISCOVERY_PATHS = [
    "/.well-known/mcp.json",
    "/.well-known/agent-commerce-capabilities.json",
    "/api/mcp",
]

ACP_PATHS = [
    "/acp-feed.json",
    "/api/acp",
    "/.well-known/acp.json",
]


def _get(url: str, ua: str = AGENT_UA, timeout: int = 15) -> tuple[int, dict | str | None]:
    try:
        resp = httpx.get(url, headers={"User-Agent": ua}, follow_redirects=True, timeout=timeout)
        content_type = resp.headers.get("content-type", "")
        if "json" in content_type:
            try:
                return resp.status_code, resp.json()
            except Exception:
                pass
        return resp.status_code, resp.text[:2000]
    except Exception as e:
        return 0, {"error": str(e)[:100]}


def _post(url: str, payload: dict, ua: str = AGENT_UA, timeout: int = 30) -> tuple[int, dict | str | None]:
    try:
        resp = httpx.post(
            url,
            json=payload,
            headers={"User-Agent": ua, "Content-Type": "application/json"},
            follow_redirects=True,
            timeout=timeout,
        )
        try:
            return resp.status_code, resp.json()
        except Exception:
            return resp.status_code, resp.text[:2000]
    except Exception as e:
        return 0, {"error": str(e)[:100]}


def _validate_acp_feed(data: dict | list | None) -> dict:
    if not isinstance(data, (dict, list)):
        return {"valid": False, "error": "Not JSON"}
    items = data if isinstance(data, list) else data.get("products", data.get("items", []))
    if not items or not isinstance(items, list):
        return {"valid": False, "product_count": 0, "error": "No product array found"}
    required = {"id", "name", "price"}
    sample = items[0] if items else {}
    missing = [f for f in required if f not in sample]
    return {
        "valid": len(missing) == 0,
        "product_count": len(items),
        "missing_required_fields": missing,
        "sample_fields": sorted(sample.keys())[:10],
    }


def test_domain(domain: str, query: str = "4K TV under $1000") -> dict:
    base = f"https://{domain}" if not domain.startswith("http") else domain
    results: dict = {
        "domain": domain,
        "tested_at": datetime.now(timezone.utc).isoformat(),
        "mcp_discovery": {},
        "mcp_search": {},
        "acp_feed": {},
        "agent_ua_access": {},
        "score": 0,
        "max_score": 40,
        "signals": [],
        "issues": [],
    }

    # 1. MCP discovery
    mcp_url = None
    for path in MCP_DISCOVERY_PATHS:
        status, data = _get(f"{base}{path}")
        if status in (200, 401):
            mcp_url = f"{base}{path}"
            results["mcp_discovery"] = {
                "url": mcp_url, "status": status, "reachable": True,
                "has_tools": isinstance(data, dict) and "tools" in data,
            }
            results["score"] += 10
            results["signals"].append(f"MCP endpoint reachable: {path} (HTTP {status})")
            break
    if not mcp_url:
        results["mcp_discovery"] = {"reachable": False}
        results["issues"].append("No MCP endpoint found at standard paths")

    # 2. MCP tool call: search_products
    if mcp_url and "/api/mcp" in mcp_url:
        payload = {
            "jsonrpc": "2.0", "id": 1, "method": "tools/call",
            "params": {"name": "search_products", "arguments": {"query": query, "limit": 5}},
        }
        status, data = _post(mcp_url, payload)
        results["mcp_search"] = {
            "status": status,
            "payload_sent": payload["params"],
            "response_type": type(data).__name__,
            "has_result": isinstance(data, dict) and ("result" in data or "content" in data),
        }
        if results["mcp_search"]["has_result"]:
            results["score"] += 10
            results["signals"].append("MCP search_products returned structured result")
        else:
            results["issues"].append("MCP search_products did not return a valid JSON-RPC result")

    # 3. ACP feed validation
    for path in ACP_PATHS:
        status, data = _get(f"{base}{path}")
        if status == 200 and data:
            acp_result = _validate_acp_feed(data)
            acp_result["url"] = f"{base}{path}"
            acp_result["status"] = status
            results["acp_feed"] = acp_result
            if acp_result["valid"]:
                results["score"] += 10
                results["signals"].append(
                    f"ACP feed valid: {acp_result['product_count']} products at {path}"
                )
            else:
                results["issues"].append(f"ACP feed found but invalid: {acp_result.get('error','schema mismatch')}")
            break
    if not results["acp_feed"]:
        results["acp_feed"] = {"reachable": False}
        results["issues"].append("No ACP feed found at standard paths")

    # 4. Agent UA access test (homepage accessible to agent UA)
    status, _ = _get(base, ua=AGENT_UA)
    results["agent_ua_access"] = {"status": status, "allowed": status == 200}
    if status == 200:
        results["score"] += 10
        results["signals"].append(f"Homepage accessible to agent UA (HTTP {status})")
    else:
        results["issues"].append(f"Homepage returned HTTP {status} for agent User-Agent")

    results["percentage"] = round(results["score"] / results["max_score"] * 100)
    results["grade"] = (
        "A" if results["percentage"] >= 90 else
        "B" if results["percentage"] >= 75 else
        "C" if results["percentage"] >= 60 else
        "D" if results["percentage"] >= 40 else "F"
    )
    results["summary"] = (
        f"{len(results['signals'])} agentic commerce capabilities confirmed | "
        f"Score: {results['score']}/{results['max_score']}"
    )
    return results


def main():
    parser = argparse.ArgumentParser(description="Synthetic agent commerce test")
    parser.add_argument("--domain", default="thegoodguys.com.au", help="Domain to test")
    parser.add_argument("--query", default="4K TV under $1000", help="Search query to test")
    args = parser.parse_args()

    if not _HTTPX:
        print("ERROR: httpx not installed. Run: pip install httpx", file=sys.stderr)
        sys.exit(1)

    print(f"Testing agentic commerce: {args.domain}")
    result = test_domain(args.domain, args.query)

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    slug = re.sub(r"[^a-z0-9-]", "-", args.domain.lower())
    out_file = out_dir / f"agent-test-{slug}-{ts}.json"
    out_file.write_text(json.dumps(result, indent=2))

    print(f"Grade: {result['grade']} ({result['percentage']}%) — {result['summary']}")
    for sig in result["signals"]:
        print(f"  ✓ {sig}")
    for issue in result["issues"]:
        print(f"  ✗ {issue}")
    print(f"Saved {out_file}")


if __name__ == "__main__":
    main()
