"""
Generate actionable AEO recommendations from Phase 3 ecommerce audit results.

Usage:
    python generate_recommendations.py seo/outputs/aeo/ecommerce-latest-tgg--ecommerce-.json
    python generate_recommendations.py  # auto-detects latest file

Reads:
    Phase 3 JSON output (ecommerce-aeo-*.json or ecommerce-latest-*.json)

Writes:
    seo/outputs/aeo/recommendations-<label>-YYYYMMDD-HHMM.json
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# ── JSON-LD snippet templates ─────────────────────────────────────────────────

JSONLD_ITEMLIST = """{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "{category_name}",
  "url": "{url}",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Product 1", "url": "{url}/product-1"},
    {"@type": "ListItem", "position": 2, "name": "Product 2", "url": "{url}/product-2"}
  ]
}"""

JSONLD_BREADCRUMB = """{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "url": "https://www.thegoodguys.com.au"},
    {"@type": "ListItem", "position": 2, "name": "{category_name}", "url": "{url}"}
  ]
}"""

JSONLD_PRODUCT = """{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{product_name}",
  "brand": {"@type": "Brand", "name": "{brand}"},
  "offers": {
    "@type": "Offer",
    "price": "{price}",
    "priceCurrency": "AUD",
    "availability": "https://schema.org/InStock",
    "url": "{url}",
    "seller": {"@type": "Organization", "name": "The Good Guys"}
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "120"
  }
}"""

JSONLD_ARTICLE = """{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "author": {"@type": "Organization", "name": "The Good Guys"},
  "datePublished": "{date}",
  "dateModified": "{date}",
  "publisher": {
    "@type": "Organization",
    "name": "The Good Guys",
    "logo": {"@type": "ImageObject", "url": "https://www.thegoodguys.com.au/logo.png"}
  }
}"""

JSONLD_FAQPAGE = """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the best {category}?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The best {category} depends on your needs. Consider..."
      }
    }
  ]
}"""

JSONLD_WEBSITE = """{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "The Good Guys",
  "url": "https://www.thegoodguys.com.au",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.thegoodguys.com.au/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}"""

JSONLD_ORGANIZATION = """{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "The Good Guys",
  "url": "https://www.thegoodguys.com.au",
  "logo": "https://www.thegoodguys.com.au/logo.png",
  "sameAs": [
    "https://www.facebook.com/TheGoodGuysAustralia",
    "https://www.instagram.com/thegoodguysau",
    "https://twitter.com/thegoodguysau"
  ],
  "contactPoint": {"@type": "ContactPoint", "telephone": "1300-942-765", "contactType": "customer service"}
}"""

LLMS_TXT_TEMPLATE = """# The Good Guys

> Australia's leading appliance and electronics retailer, with 100+ stores nationwide.
> Shop TVs, fridges, washing machines, laptops, small appliances, and more.

## Product Catalogue

The Good Guys sells 10,000+ products across major appliance and electronics categories.
Key categories: Televisions, Refrigerators, Washing Machines, Dryers, Dishwashers,
Air Conditioners, Laptops, Computers, Tablets, Cameras, Audio, Small Kitchen Appliances.

Top brands: Samsung, LG, Sony, Panasonic, Hisense, TCL, Bosch, Fisher & Paykel,
Dyson, Breville, De'Longhi, Tefal, Apple, Microsoft, HP, Lenovo.

## Pricing and Offers

- Price Guarantee: The Good Guys will beat any competitor's price
- Regular sales events: Good Guys Club member exclusives
- Buy Now Pay Later: Zip, humm, Latitude Pay available at checkout
- Delivery: Same-day delivery in metro areas, free delivery over threshold

## Buying Guides

Expert advice for all major product categories at /buying-guide/.
Topics include: how to choose a TV size, refrigerator capacity guide, air conditioner
sizing, washing machine load capacity, laptop buying guide.

## Store Finder

100+ stores across Australia. Find your nearest: /store-finder
Store services: in-store demo, price match, installation, extended warranty

## Customer Service

- Phone: 1300 942 765
- Online chat: thegoodguys.com.au
- Returns: 30-day change of mind returns in-store
- Warranty: manufacturer warranty + Good Guys product protection plans
"""


# ── Recommendation generators ─────────────────────────────────────────────────

def recommend_schema(page: dict, page_type: str) -> list[dict]:
    fixes = []
    missing = page.get("missing", [])
    url = page.get("file", "").replace(".html", "").replace("--", "/")

    schema_map = {
        "ItemList":             ("category", JSONLD_ITEMLIST, "Add ItemList schema so AI agents see your product range as a structured list"),
        "BreadcrumbList":       ("category,guide,product", JSONLD_BREADCRUMB, "Add BreadcrumbList schema for navigation context in AI-generated answers"),
        "Product":              ("product", JSONLD_PRODUCT, "Add Product schema with Offer and AggregateRating for product pages"),
        "Offer":                ("product", JSONLD_PRODUCT, "Add Offer schema with price, currency, and availability"),
        "AggregateRating":      ("product", JSONLD_PRODUCT, "Add AggregateRating so AI models can cite review scores"),
        "Article":              ("guide", JSONLD_ARTICLE, "Add Article schema to buying guides — required for Google AI Overviews"),
        "FAQPage":              ("guide", JSONLD_FAQPAGE, "Add FAQPage schema to enable direct FAQ citations in AI answers"),
        "WebSite":              ("home", JSONLD_WEBSITE, "Add WebSite schema with SearchAction for sitelinks search box"),
        "Organization":         ("home", JSONLD_ORGANIZATION, "Add Organization schema with sameAs links for knowledge graph entity"),
        "SiteLinksSearchBox":   ("home", JSONLD_WEBSITE, "Add SiteLinksSearchBox via WebSite potentialAction"),
    }

    for schema_type in missing:
        if schema_type in schema_map:
            relevant_types, snippet, description = schema_map[schema_type]
            fixes.append({
                "check": "schema",
                "schema_type": schema_type,
                "issue": f"Missing {schema_type} schema on {page_type} page",
                "fix": description,
                "snippet": f'<script type="application/ld+json">\n{snippet}\n</script>',
                "effort": "low",
                "impact": "high" if schema_type in ("Product", "ItemList", "Article", "FAQPage") else "medium",
            })

    return fixes


def recommend_hidden_content(page: dict) -> list[dict]:
    hidden_pct = page.get("hidden_pct", 0)
    if hidden_pct < 10:
        return []
    top_hidden = page.get("top_hidden", [])
    worst = top_hidden[0] if top_hidden else {}
    return [{
        "check": "hidden_content",
        "issue": f"{hidden_pct}% of content is hidden from AI crawlers (display:none, aria-hidden, collapsed)",
        "fix": (
            f"Review hidden elements — worst offender: <{worst.get('tag','?')}> "
            f"class='{worst.get('class','')}' ({worst.get('words',0)} words). "
            "Consider moving key product descriptions and specs outside collapsed accordions, "
            "or duplicating them in a server-rendered summary for AI crawlers."
        ),
        "effort": "medium",
        "impact": "high" if hidden_pct >= 30 else "medium",
    }]


def recommend_ai_signals(page: dict) -> list[dict]:
    missing = page.get("missing", [])
    found = page.get("found", [])
    fixes = []

    signal_fixes = {
        "direct_answer_paragraph": (
            "Add a direct-answer paragraph in the first 200 words — start with a clear "
            "declarative sentence: '[Category] at The Good Guys includes [types]. "
            "Key features to consider are [A], [B], [C].' "
            "AI models prioritise concise, factual openers for citation."
        ),
        "numbered_list": (
            "Add an <ol> list summarising top choices or key considerations — "
            "numbered lists are heavily weighted by AI answer engines for citations."
        ),
        "definition_heading": (
            "Add a 'What is [category]?' H2 heading followed by a 1-2 sentence definition. "
            "This matches the query pattern AI models answer most."
        ),
    }

    for sig in missing:
        if sig in signal_fixes:
            fixes.append({
                "check": "ai_signals",
                "issue": f"Missing AI content signal: {sig}",
                "fix": signal_fixes[sig],
                "effort": "low",
                "impact": "medium",
            })

    if "faq_block" not in found:
        fixes.append({
            "check": "ai_signals",
            "issue": "No FAQ block detected — AI models frequently cite FAQ sections",
            "fix": (
                "Add a structured FAQ section with 3-5 Q&A pairs using <details>/<summary> "
                "or a styled accordion. Ensure FAQPage JSON-LD matches the visible questions."
            ),
            "effort": "medium",
            "impact": "high",
        })

    return fixes


def recommend_au_signals(page: dict) -> list[dict]:
    """AU content signals — language attr, currency, spelling, ACCC pricing."""
    fixes = []
    lang = page.get("lang", "")
    if "en-au" not in lang.lower():
        fixes.append({
            "check": "au_signals",
            "issue": f'<html> lang attribute is "{lang or "missing"}" — should be "en-AU"',
            "fix": (
                'Set lang="en-AU" on the <html> tag. AI agents and Google AI Overviews '
                'use this signal to scope answers to the Australian market and serve AUD pricing.'
            ),
            "snippet": '<html lang="en-AU">',
            "effort": "low",
            "impact": "high",
        })
    us_count = page.get("us_spelling_count", 0)
    au_count = page.get("au_spelling_count", 0)
    if us_count > au_count and us_count > 0:
        fixes.append({
            "check": "au_signals",
            "issue": f"US spelling drift detected ({us_count} US terms vs {au_count} AU terms)",
            "fix": (
                "Audit the page text for US spellings (color, optimize, organize, defense) "
                "and replace with AU equivalents (colour, optimise, organise, defence). "
                "Spelling consistency reinforces locale signal for AI ranking."
            ),
            "effort": "low",
            "impact": "medium",
        })
    issue = page.get("issue", "")
    if "ACCC" in issue or "Was/Save" in issue:
        fixes.append({
            "check": "au_signals",
            "issue": "No Was/Save/RRP comparative pricing detected",
            "fix": (
                "Add visible Was/Save/RRP price comparisons to product and category pages. "
                "ACCC requires comparison prices to remain on display long enough to be substantiated. "
                "Markup comparison pricing in Offer schema with priceSpecification and ListPrice."
            ),
            "effort": "medium",
            "impact": "medium",
        })
    return fixes


def recommend_content_freshness(page: dict) -> list[dict]:
    """dateModified / Last-Modified age."""
    if not page.get("stale"):
        return []
    age = page.get("age_days")
    age_str = f"{age} days old" if age is not None else "missing date"
    return [{
        "check": "content_freshness",
        "issue": f"Content {age_str} — AI crawlers deprioritise content older than 90 days",
        "fix": (
            "Update the schema dateModified and ensure server returns Last-Modified HTTP header. "
            "Even minor copy refresh + new dateModified signals freshness to AI agents and Googlebot. "
            "For evergreen pages, schedule quarterly review-and-republish."
        ),
        "snippet": '"dateModified": "2026-05-02T00:00:00+10:00"',
        "effort": "low",
        "impact": "medium" if (age and age > 180) else "low",
    }]


def recommend_review_accessibility(page: dict) -> list[dict]:
    """Reviews JS-gated and invisible to AI crawlers."""
    if not page.get("js_gated"):
        return []
    rendered = page.get("rendered_review_count", 0)
    return [{
        "check": "review_accessibility",
        "issue": f"Review content is JS-gated — {rendered} reviews visible in browser, 0 in raw HTML",
        "fix": (
            "Server-render the first 5-10 review snippets directly in the page HTML "
            "(or duplicate them in a <noscript> block). AI crawlers use httpx, not a JS engine, "
            "so JS-loaded reviews are invisible to ChatGPT, Claude, and Perplexity."
        ),
        "effort": "high",
        "impact": "high",
    }]


def recommend_gtin_coverage(gtin_data: dict) -> list[dict]:
    """Site-wide GTIN gap recommendation."""
    total = gtin_data.get("total_product_pages", 0)
    with_g = gtin_data.get("with_gtin", 0)
    if total == 0 or with_g == total:
        return []
    pct = round(with_g / total * 100) if total else 0
    by_cat = gtin_data.get("by_category", {})
    worst = sorted(
        by_cat.items(),
        key=lambda kv: kv[1].get("with_gtin", 0) / max(kv[1].get("total", 1), 1),
    )[:3]
    worst_str = ", ".join(f"{c} ({s.get('with_gtin',0)}/{s.get('total',0)})" for c, s in worst)
    return [{
        "check": "gtin_coverage",
        "issue": f"Only {pct}% of product pages expose a GTIN ({with_g}/{total}). Worst: {worst_str}",
        "fix": (
            "Populate Product.gtin13 (or gtin14) in JSON-LD on every product page. "
            "GTIN is required for Google Merchant Center eligibility, Google Shopping AI listings, "
            "and Shopify Agentic / ACP feeds. Source GTINs from your GMC feed or supplier data."
        ),
        "snippet": '"gtin13": "4901234567890"',
        "effort": "high",
        "impact": "high",
    }]


def recommend_agentic_commerce(ag_data: dict) -> list[dict]:
    """Site-wide agentic endpoint recommendation."""
    if not ag_data:
        return []
    score = ag_data.get("score", 0)
    if score >= ag_data.get("maxScore", 30):
        return []
    fixes = []
    eps = ag_data.get("checks", {})
    if not eps.get("storefront_mcp", {}).get("reachable") and not eps.get("mcp_api", {}).get("reachable"):
        fixes.append({
            "check": "agentic_commerce",
            "issue": "No Storefront MCP endpoint detected (/.well-known/mcp.json or /api/mcp)",
            "fix": (
                "If on Shopify, enable Agentic Storefronts in admin to publish /.well-known/mcp.json. "
                "Otherwise, expose a Model Context Protocol server describing product search and cart "
                "tool calls. ChatGPT Operator, Claude Computer Use, and Perplexity Shopping all use MCP."
            ),
            "effort": "high",
            "impact": "medium",
        })
    if not eps.get("acp_feed", {}).get("reachable"):
        fixes.append({
            "check": "agentic_commerce",
            "issue": "No ACP (Agentic Commerce Protocol) feed found",
            "fix": (
                "Publish an ACP-compliant product feed at /acp-feed.json with id, name, price, "
                "currency, available, and url for each product. ACP is the emerging standard for "
                "AI agents to discover and transact with retailers."
            ),
            "effort": "high",
            "impact": "medium",
        })
    if not eps.get("agent_link_tag", {}).get("found"):
        fixes.append({
            "check": "agentic_commerce",
            "issue": "<link rel=\"agent-endpoint\"> missing from <head>",
            "fix": "Add a discovery link tag in every page <head> pointing to your MCP endpoint.",
            "snippet": '<link rel="agent-endpoint" href="https://www.thegoodguys.com.au/.well-known/mcp.json">',
            "effort": "low",
            "impact": "low",
        })
    return fixes


def recommend_gmc_feed(gmc_data: dict) -> list[dict]:
    """Site-wide GMC feed completeness recommendation."""
    if not gmc_data or gmc_data.get("skipped") or "error" in gmc_data:
        return []
    req_pct = gmc_data.get("required_completeness_pct", 100)
    missing = gmc_data.get("missing_fields", {})
    if req_pct == 100 and not missing:
        return []
    worst = sorted(missing.items(), key=lambda kv: -kv[1])[:5]
    worst_str = ", ".join(f"{f}: {n}" for f, n in worst)
    return [{
        "check": "gmc_feed",
        "issue": f"GMC feed required-field completeness is {req_pct}%. Top gaps: {worst_str}",
        "fix": (
            "Backfill missing required fields in the merchant feed. Priority order: gtin, brand, "
            "mpn, google_product_category. Missing required fields cause GMC item disapprovals "
            "and exclude products from Shopping ads + AI shopping surfaces."
        ),
        "effort": "high",
        "impact": "high",
    }]


def recommend_robots(robots_data: dict) -> list[str]:
    additions = []
    bot_rules = robots_data.get("robots", {})
    llms = robots_data.get("llms_txt", {})

    blocked_bots = [
        name for name, rules in bot_rules.items()
        if rules.get("blocked") and name != "Googlebot"
    ]
    if blocked_bots:
        for bot in blocked_bots:
            additions.append(
                f"# Allow {bot} to crawl product and category pages\n"
                f"User-agent: {bot}\nAllow: /\n"
            )

    if not llms.get("exists"):
        additions.append(
            "# Create /llms.txt to give AI agents a structured site overview\n"
            "# See: https://llmstxt.org for the specification"
        )

    return additions


def prioritise(fixes: list[dict]) -> str:
    if not fixes:
        return "low"
    impacts = [f.get("impact", "low") for f in fixes]
    if "high" in impacts:
        return "critical" if len([i for i in impacts if i == "high"]) >= 3 else "high"
    if "medium" in impacts:
        return "medium"
    return "low"


# ── Main ─────────────────────────────────────────────────────────────────────

def load_phase3(path: str) -> dict:
    return json.loads(Path(path).read_text())


def generate(input_path: str) -> dict:
    data = load_phase3(input_path)
    label = data.get("label", "unknown")
    checks = data.get("checks", {})

    schema_check     = checks.get("schema", {})
    hidden_check     = checks.get("hidden_content", {})
    signals_check    = checks.get("ai_signals", {})
    robots_check     = checks.get("robots_content", {})
    au_check         = checks.get("au_signals", {})
    freshness_check  = checks.get("content_freshness", {})
    review_check     = checks.get("review_accessibility", {})
    gtin_check       = checks.get("gtin_coverage", {})
    agentic_check    = checks.get("agentic_commerce", {})
    gmc_check        = checks.get("gmc_feed", {})

    page_fixes = []

    schema_pages    = {p["file"]: p for p in schema_check.get("pages", [])}
    hidden_pages    = {p["file"]: p for p in hidden_check.get("pages", [])}
    signals_pages   = {p["file"]: p for p in signals_check.get("pages", [])}
    au_pages        = {p["file"]: p for p in au_check.get("pages", [])}
    freshness_pages = {p["file"]: p for p in freshness_check.get("pages", [])}
    review_pages    = {p["file"]: p for p in review_check.get("pages", [])}

    all_files = sorted(
        set(schema_pages) | set(hidden_pages) | set(signals_pages)
        | set(au_pages) | set(freshness_pages) | set(review_pages)
    )

    for fname in all_files:
        sp   = schema_pages.get(fname, {})
        hp   = hidden_pages.get(fname, {})
        sigp = signals_pages.get(fname, {})
        aup  = au_pages.get(fname, {})
        fp   = freshness_pages.get(fname, {})
        rp   = review_pages.get(fname, {})
        page_type = sp.get("page_type") or sigp.get("page_type") or fp.get("page_type", "category")

        fixes = []
        fixes.extend(recommend_schema(sp, page_type))
        fixes.extend(recommend_hidden_content(hp))
        fixes.extend(recommend_ai_signals(sigp))
        fixes.extend(recommend_au_signals(aup))
        fixes.extend(recommend_content_freshness(fp))
        fixes.extend(recommend_review_accessibility(rp))

        if fixes:
            page_fixes.append({
                "file": fname,
                "page_type": page_type,
                "priority": prioritise(fixes),
                "fix_count": len(fixes),
                "fixes": fixes,
            })

    # Site-wide fixes (not tied to a specific page)
    site_fixes: list[dict] = []
    site_fixes.extend(recommend_gtin_coverage(gtin_check))
    site_fixes.extend(recommend_agentic_commerce(agentic_check))
    site_fixes.extend(recommend_gmc_feed(gmc_check))

    robots_additions = recommend_robots(robots_check) if robots_check else []

    output = {
        "label": label,
        "source": str(input_path),
        "generated": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "pages_with_fixes": len(page_fixes),
            "total_page_fixes": sum(p["fix_count"] for p in page_fixes),
            "site_wide_fixes": len(site_fixes),
            "total_fixes": sum(p["fix_count"] for p in page_fixes) + len(site_fixes),
            "critical_pages": sum(1 for p in page_fixes if p["priority"] == "critical"),
            "high_pages": sum(1 for p in page_fixes if p["priority"] == "high"),
        },
        "pages": sorted(
            page_fixes,
            key=lambda p: {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(p["priority"], 4),
        ),
        "site_wide_fixes": site_fixes,
        "robots_additions": robots_additions,
        "llms_txt_template": LLMS_TXT_TEMPLATE,
        "global_fixes": [
            f"Create /llms.txt — currently {'missing' if not robots_check.get('llms_txt', {}).get('exists') else 'present but review needed'}",
            "Add AI bot section to robots.txt (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot)",
            "Add BreadcrumbList schema to every page type",
            "Add FAQPage schema to all buying guides and category pages with FAQ blocks",
            "Ensure schema is server-rendered (not JS-injected) — AI bots do not execute JS",
            "Add lang=\"en-AU\" to <html> tag on all pages",
        ],
    }

    return output


def main():
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        out_dir = Path("seo/outputs/aeo")
        candidates = sorted(out_dir.glob("ecommerce-*.json"))
        if not candidates:
            print("ERROR: No Phase 3 JSON found. Pass a path or run Phase 3 first.", file=sys.stderr)
            sys.exit(1)
        input_path = str(candidates[-1])
        print(f"Auto-detected: {input_path}")

    result = generate(input_path)

    out_dir = Path("seo/outputs/aeo")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    slug = re.sub(r"[^a-z0-9-]", "-", result["label"].lower())
    out_file = out_dir / f"recommendations-{slug}-{ts}.json"
    out_file.write_text(json.dumps(result, indent=2))
    print(f"Saved {out_file}")
    print(f"  {result['summary']['pages_with_fixes']} pages need fixes")
    print(f"  {result['summary']['total_fixes']} total recommended fixes")
    print(f"  {result['summary']['critical_pages']} critical, {result['summary']['high_pages']} high priority")


if __name__ == "__main__":
    main()
