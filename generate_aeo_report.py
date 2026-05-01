"""
AEO Audit Report Generator

Reads JSON outputs from all audit phases and generates a rich HTML report
with embedded Chart.js charts, score cards, competitor comparison, and issue tables.

Usage:
    python generate_aeo_report.py
    AEO_OUTPUT_DIR=seo/outputs/aeo python generate_aeo_report.py

Writes:
    seo/outputs/aeo/report-YYYYMMDD-HHMM.html  — self-contained HTML (no external deps)
    seo/outputs/aeo/report-latest.html           — copy for easy access
    Committed to repo via GitHub API
"""

import base64
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

# ── Helpers ────────────────────────────────────────────────────────────────────

GRADE_COLOR = {"A": "#22c55e", "B": "#4ade80", "C": "#eab308", "D": "#f97316", "F": "#ef4444"}
GRADE_BG    = {"A": "#dcfce7", "B": "#dcfce7", "C": "#fef9c3", "D": "#fff7ed", "F": "#fee2e2"}
GRADE_EMOJI = {"A": "🟢", "B": "🟢", "C": "🟡", "D": "🟠", "F": "🔴"}

# Checks produced by run_aeo_crawl.py
CRAWL_CHECKS = [
    ("robots_ai",  "Robots (AI bots)",  30),
    ("llms_txt",   "llms.txt",          20),
    ("http_access","HTTP Access",        10),
    ("meta_tags",  "Meta Tags",          20),
    ("headings",   "Headings",           20),
    ("schema_type","Schema / JSON-LD",   20),
    ("content",    "Content Signals",    20),
    ("js_depend",  "JS Dependency",      20),
]
CRAWL_MAX = 160

PHASE3_CATS = [
    ("schema",            "Schema / Structured Data",     30),
    ("schema_validity",   "Schema Validity",              15),
    ("render_diff",       "Render Diff",                  20),
    ("user_agents",       "User Agent Behaviour",         20),
    ("hidden_content",    "Hidden Content",               20),
    ("ai_signals",        "AI Content Signals",           10),
    ("dom_structure",     "DOM Structure",                25),
    ("robots_content",    "Robots.txt & llms.txt",        50),
    ("sitemap_coverage",  "Sitemap Coverage",             40),
    ("competitor_schema", "Competitor Schema Comparison", 45),
    ("au_signals",        "AU Content Signals",           20),
    ("agentic_commerce",  "Agentic Commerce Readiness",   30),
    ("gtin_coverage",     "GTIN Coverage",                20),
    ("gmc_feed",          "GMC Feed Completeness",        30),
]

PHASE4_CATS = [
    ("boilerplate_ratio",  "Boilerplate Ratio",              20),
    ("content_chunking",   "Content Chunking",               25),
    ("entity_signals",     "Entity Signals",                 25),
    ("knowledge_graph",    "Knowledge Graph",                20),
    ("semantic_structure", "Semantic Structure",             30),
    ("anchor_quality",     "Anchor Text Quality",            20),
    ("content_similarity", "Content Similarity",             20),
    ("entity_gap",         "Entity Gap vs Competitors",      25),
    ("llm_quality",        "LLM Quality Judge",              25),
]


def load_latest(*patterns: str) -> dict | list | None:
    """Load the most recent file matching any of the given glob patterns."""
    files = []
    for p in patterns:
        files.extend(glob.glob(p))
    files = sorted(files)
    if not files:
        return None
    try:
        return json.loads(Path(files[-1]).read_text())
    except Exception:
        return None


def pct_bar_color(pct: int) -> str:
    if pct >= 75: return "#22c55e"
    if pct >= 50: return "#eab308"
    if pct >= 25: return "#f97316"
    return "#ef4444"


def grade_badge(grade: str, pct: int) -> str:
    color = GRADE_COLOR.get(grade, "#94a3b8")
    bg    = GRADE_BG.get(grade, "#f1f5f9")
    return (
        f'<span style="display:inline-block;padding:4px 14px;border-radius:20px;'
        f'background:{bg};color:{color};font-weight:700;font-size:1.1em;border:2px solid {color}">'
        f'{grade} · {pct}%</span>'
    )


def _grade(pct: int) -> str:
    if pct >= 80: return "A"
    if pct >= 65: return "B"
    if pct >= 50: return "C"
    if pct >= 35: return "D"
    return "F"


# ── Data Loading ───────────────────────────────────────────────────────────────

def load_all_data(out_dir: str) -> dict:
    d = out_dir.rstrip("/")
    return {
        "crawl":           load_latest(f"{d}/crawl-*.json"),
        "phase3":          load_latest(f"{d}/ecommerce-aeo-*.json", f"{d}/ecommerce-latest-*.json"),
        "phase4":          load_latest(f"{d}/content-aeo-*.json",  f"{d}/content-latest-*.json"),
        "recommendations": load_latest(f"{d}/recommendations-*.json"),
        "run_id":          os.getenv("GITHUB_RUN_ID", "local"),
        "run_number":      os.getenv("GITHUB_RUN_NUMBER", "?"),
        "ref":             os.getenv("GITHUB_REF_NAME", "main"),
        "ts":              datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


# ── Hero cards ─────────────────────────────────────────────────────────────────

def _tgg_crawl_grade(crawl: list) -> tuple[str, int]:
    """Average grade across TGG pages only."""
    tgg_pages = [r for r in crawl if "thegoodguys" in r.get("domain", "")]
    if not tgg_pages:
        return "?", 0
    avg = round(sum(p["percentage"] for p in tgg_pages) / len(tgg_pages))
    return _grade(avg), avg


def section_hero(data: dict) -> str:
    crawl = data.get("crawl") or []
    p3    = data["phase3"]
    p4    = data.get("phase4")

    crawl_grade, crawl_pct = _tgg_crawl_grade(crawl) if crawl else ("?", 0)

    p3_grade = p3.get("grade", "?") if p3 else "?"
    p3_pct   = p3.get("percentage", 0) if p3 else 0
    p4_grade = p4.get("grade", "?") if p4 else "?"
    p4_pct   = p4.get("percentage", 0) if p4 else 0

    # Competitor average for the 4th card
    if crawl:
        comp_pages = [r for r in crawl if "thegoodguys" not in r.get("domain", "")]
        comp_avg = round(sum(p["percentage"] for p in comp_pages) / len(comp_pages)) if comp_pages else 0
        comp_grade = _grade(comp_avg)
        comp_sub = f"{len(set(r['domain'] for r in comp_pages))} competitors benchmarked"
    else:
        comp_grade, comp_avg, comp_sub = "?", 0, "No crawl data"

    cards = [
        ("AEO Crawl · TGG",       crawl_grade, crawl_pct,   "robots, llms.txt, schema, JS, meta"),
        ("Ecommerce AEO",          p3_grade,    p3_pct,      "schema, render diff, UA, signals"),
        ("Content Intelligence",   p4_grade,    p4_pct,      "entities, chunking, semantics"),
        ("Competitor Avg",         comp_grade,  comp_avg,    comp_sub),
    ]

    html = '<div class="hero-cards">'
    for title, g, pct, sub in cards:
        c = GRADE_COLOR.get(g, "#94a3b8")
        bg = GRADE_BG.get(g, "#f8fafc")
        html += f"""
        <div class="hero-card" style="border-top:4px solid {c};background:{bg}">
            <div class="hero-grade" style="color:{c}">{g}</div>
            <div class="hero-pct" style="color:{c}">{pct}%</div>
            <div class="hero-title">{title}</div>
            <div class="hero-sub">{sub}</div>
        </div>"""
    html += "</div>"
    return html


# ── AEO Crawl section ──────────────────────────────────────────────────────────

def _check_icon(c: dict | None) -> str:
    if not c or c.get("score") is None:
        return "–"
    p = c.get("percentage", 0)
    return "✅" if p >= 80 else "⚠️" if p >= 50 else "❌"


def section_crawl(crawl: list) -> str:
    if not crawl:
        return "<p class='empty'>No AEO Crawl data found. Run the workflow with AEO Crawl enabled.</p>"

    # ── Domain-level summary ─────────────────────────────────────────────────
    by_domain: dict[str, list] = {}
    for r in crawl:
        by_domain.setdefault(r["domain"], []).append(r)

    domain_rows = ""
    for domain, pages in sorted(by_domain.items()):
        avg = round(sum(p["percentage"] for p in pages) / len(pages))
        g   = _grade(avg)
        c   = GRADE_COLOR.get(g, "#94a3b8")
        is_tgg = "thegoodguys" in domain
        domain_rows += f"""<tr style="{'background:#f0fdf4' if is_tgg else ''}">
            <td><strong>{'⭐ ' if is_tgg else ''}{domain}</strong></td>
            <td><span style="color:{c};font-weight:700">{g}</span></td>
            <td><div class="pct-bar"><div style="width:{avg}%;background:{pct_bar_color(avg)}"></div></div><span>{avg}%</span></td>
            <td style="color:#64748b">{len(pages)} pages</td>
        </tr>"""

    html = f"""
    <h3>Domain Comparison</h3>
    <table class="data-table" style="margin-bottom:24px">
        <thead><tr><th>Domain</th><th>Grade</th><th>Avg Score</th><th>Pages</th></tr></thead>
        <tbody>{domain_rows}</tbody>
    </table>"""

    # ── Per-URL check table ──────────────────────────────────────────────────
    check_headers = "".join(
        f'<th title="{name} (max {mx} pts)">{name.split("/")[0].strip()}<br><small>/{mx}</small></th>'
        for _, name, mx in CRAWL_CHECKS
    )

    url_rows = ""
    for r in crawl:
        g    = r.get("grade", "?")
        pct  = r.get("percentage", 0)
        c    = GRADE_COLOR.get(g, "#94a3b8")
        ch   = r.get("checks", {})
        is_tgg = "thegoodguys" in r.get("domain", "")
        icons = "".join(f"<td style='text-align:center'>{_check_icon(ch.get(k))}</td>" for k, _, _ in CRAWL_CHECKS)
        short_label = r["label"].split(" · ", 1)[-1] if " · " in r["label"] else r["label"]
        domain_tag = r["domain"].replace("thegoodguys.com.au", "TGG").replace("jbhifi.com.au", "JB").replace("harveynorman.com.au", "HN").replace("appliancesonline.com.au", "AO")
        url_rows += f"""<tr style="{'background:#f0fdf4' if is_tgg else ''}">
            <td style="white-space:nowrap"><small style="color:#94a3b8">{domain_tag}</small><br><a href="{r['url']}" target="_blank" style="color:#1d4ed8;text-decoration:none;font-size:0.9em">{short_label}</a></td>
            <td style="text-align:center"><span style="color:{c};font-weight:700">{g}</span></td>
            <td style="text-align:center">{pct}%</td>
            {icons}
        </tr>"""

    html += f"""
    <h3>Per-URL Check Results</h3>
    <p style="font-size:0.82em;color:#64748b;margin-top:-8px">✅ ≥80% &nbsp; ⚠️ 50–79% &nbsp; ❌ &lt;50% &nbsp; – Not scored (no snapshot)</p>
    <div style="overflow-x:auto">
    <table class="data-table">
        <thead><tr>
            <th>Page</th><th>Grade</th><th>%</th>
            {check_headers}
        </tr></thead>
        <tbody>{url_rows}</tbody>
    </table>
    </div>"""

    # ── Issue list ───────────────────────────────────────────────────────────
    all_issues = [
        (r["label"], i["check"], i["issue"])
        for r in crawl
        if "thegoodguys" in r.get("domain", "")
        for i in r.get("issues", [])
    ]
    if all_issues:
        issue_rows = "".join(
            f'<tr><td style="white-space:nowrap;font-size:0.85em">{lbl}</td>'
            f'<td><code>{chk}</code></td><td>{issue}</td></tr>'
            for lbl, chk, issue in all_issues[:30]
        )
        html += f"""
        <h3>TGG Issues</h3>
        <table class="issues-table">
            <thead><tr><th>Page</th><th>Check</th><th>Issue</th></tr></thead>
            <tbody>{issue_rows}</tbody>
        </table>"""

    # ── Render diff visual (if crawl has js_depend data) ────────────────────
    js_pages = [r for r in crawl if r.get("checks", {}).get("js_depend", {}).get("rendered_words") is not None]
    if js_pages:
        max_rend = max((r["checks"]["js_depend"].get("rendered_words", 0) or 0) for r in js_pages) or 1
        rd_rows = ""
        for r in js_pages:
            jd = r["checks"]["js_depend"]
            raw_w   = jd.get("raw_words", 0) or 0
            rend_w  = jd.get("rendered_words", 0) or 0
            pct_acc = jd.get("pct_accessible", 0) or 0
            bar_c   = pct_bar_color(pct_acc)
            raw_bar = round(raw_w  / max_rend * 100)
            label   = r["label"].split(" · ", 1)[-1] if " · " in r["label"] else r["label"]
            rd_rows += f"""<tr>
                <td style="font-size:0.85em"><code>{label}</code></td>
                <td>
                  <div title="Raw (no JS): {raw_w:,} words" style="margin-bottom:3px">
                    <span style="font-size:0.75em;color:#94a3b8;display:inline-block;width:60px">No JS</span>
                    <div style="display:inline-block;width:{raw_bar}%;max-width:180px;height:10px;background:#f59e0b;border-radius:3px;vertical-align:middle"></div>
                    <span style="font-size:0.75em;margin-left:4px">{raw_w:,}</span>
                  </div>
                  <div title="Rendered (JS): {rend_w:,} words">
                    <span style="font-size:0.75em;color:#94a3b8;display:inline-block;width:60px">With JS</span>
                    <div style="display:inline-block;width:100%;max-width:180px;height:10px;background:#3b82f6;border-radius:3px;vertical-align:middle"></div>
                    <span style="font-size:0.75em;margin-left:4px">{rend_w:,}</span>
                  </div>
                </td>
                <td style="text-align:center;color:{bar_c};font-weight:600">{pct_acc}%</td>
            </tr>"""
        html += f"""
        <h3>JS Dependency — Raw vs Rendered Word Counts</h3>
        <p style="font-size:0.85em;color:#64748b;margin-top:-8px">
          🟡 No JS = what AI bots see via httpx &nbsp;|&nbsp; 🔵 With JS = Playwright render &nbsp;|&nbsp;
          % = share of content accessible without JS
        </p>
        <table class="data-table">
            <thead><tr><th>Page</th><th>Word counts</th><th>% accessible</th></tr></thead>
            <tbody>{rd_rows}</tbody>
        </table>"""

    return html


def section_phase3(phase3: dict) -> str:
    if not phase3:
        return "<p class='empty'>No Phase 3 data found.</p>"

    checks = phase3.get("checks", {})
    rows = ""
    all_issues = []

    for key, name, _ in PHASE3_CATS:
        c = checks.get(key, {})
        if not c:
            continue
        if c.get("skipped"):
            rows += f'<tr><td>{name}</td><td colspan="3" style="color:#94a3b8;font-style:italic">⏭ Skipped — set {key.upper()}_URL env var to enable</td></tr>'
            continue
        if "error" in c:
            rows += f'<tr><td>{name}</td><td colspan="3" class="error">✗ {c["error"][:80]}</td></tr>'
            continue
        pct = c.get("percentage", 0)
        score = c.get("score", 0)
        max_s = c.get("maxScore", 0)
        bar_c = pct_bar_color(pct)
        rows += f"""<tr>
            <td>{name}</td>
            <td><div class="pct-bar"><div style="width:{pct}%;background:{bar_c}"></div></div></td>
            <td style="color:{bar_c};font-weight:600">{score}/{max_s}</td>
            <td>{pct}%</td>
        </tr>"""
        for e in c.get("errors", []):
            issue = e.get("issue") or e.get("error") or ""
            ident = e.get("url") or e.get("file") or ""
            if issue:
                all_issues.append((name, ident, issue))

    issue_rows = ""
    for check_name, ident, issue in all_issues[:25]:
        issue_rows += f'<tr><td class="sev-error">{check_name}</td><td><code>{ident}</code></td><td>{issue}</td></tr>'

    html = f"""
    <table class="data-table">
        <thead><tr><th>Check</th><th>Progress</th><th>Score</th><th>%</th></tr></thead>
        <tbody>{rows}</tbody>
    </table>"""

    if issue_rows:
        html += f"""
        <h3>Ecommerce Issues</h3>
        <table class="issues-table">
            <thead><tr><th>Check</th><th>Page / URL</th><th>Issue</th></tr></thead>
            <tbody>{issue_rows}</tbody>
        </table>"""

    # Render diff visual from Phase 3 render_diff check
    rd = checks.get("render_diff", {})
    if rd and "pages" in rd:
        rd_rows = ""
        for p in rd.get("pages", []):
            if "error" in p:
                continue
            raw_w    = p.get("raw_words", 0)
            rend_w   = p.get("rendered_words", 0)
            pct_acc  = p.get("pct_accessible", 0)
            ssr_sc   = p.get("ssr_schema_count", 0)
            csr_sc   = p.get("csr_schema_count", 0)
            raw_pr   = p.get("price_elements_ssr", 0)
            rend_pr  = p.get("price_elements_rendered", 0)
            csr_flag = p.get("schema_injected_csr", False)
            bar_c    = pct_bar_color(pct_acc)
            label    = p.get("url", "").replace("https://www.thegoodguys.com.au", "")
            csr_badge = '<span style="background:#ef4444;color:#fff;font-size:0.75em;padding:1px 5px;border-radius:3px;margin-left:4px">CSR schema</span>' if csr_flag else ''
            max_w = max(rend_w, 1)
            raw_bar_w = round(raw_w / max_w * 100)
            rd_rows += f"""<tr>
                <td style="font-size:0.85em"><code>{label or '/'}</code>{csr_badge}</td>
                <td>
                  <div title="Raw (no JS): {raw_w:,} words" style="margin-bottom:3px">
                    <span style="font-size:0.75em;color:#94a3b8;display:inline-block;width:60px">No JS</span>
                    <div style="display:inline-block;width:{raw_bar_w}%;max-width:180px;height:10px;background:#f59e0b;border-radius:3px;vertical-align:middle"></div>
                    <span style="font-size:0.75em;margin-left:4px">{raw_w:,}</span>
                  </div>
                  <div title="Rendered (JS): {rend_w:,} words">
                    <span style="font-size:0.75em;color:#94a3b8;display:inline-block;width:60px">With JS</span>
                    <div style="display:inline-block;width:100%;max-width:180px;height:10px;background:#3b82f6;border-radius:3px;vertical-align:middle"></div>
                    <span style="font-size:0.75em;margin-left:4px">{rend_w:,}</span>
                  </div>
                </td>
                <td style="text-align:center;color:{bar_c};font-weight:600">{pct_acc}%</td>
                <td style="text-align:center;font-size:0.85em">
                  {"🟠 " if csr_flag else "🟢 "}{ssr_sc} raw / {csr_sc} rendered
                </td>
                <td style="text-align:center;font-size:0.85em">
                  {"🔴 " if raw_pr == 0 and rend_pr > 0 else "🟢 "}{raw_pr} raw / {rend_pr} rendered
                </td>
            </tr>"""
        if rd_rows:
            html += f"""
            <h3>Render Diff — Pre JS vs Post JS</h3>
            <p style="font-size:0.85em;color:#64748b;margin-top:-8px">
              🟡 No JS = what AI bots (httpx) see &nbsp;|&nbsp; 🔵 With JS = Playwright render &nbsp;|&nbsp;
              % = content accessible without JS &nbsp;|&nbsp; Schema: JSON-LD blocks &nbsp;|&nbsp; Price elements
            </p>
            <table class="data-table">
                <thead><tr><th>Page</th><th>Word counts</th><th>% accessible</th><th>Schema blocks</th><th>Price els</th></tr></thead>
                <tbody>{rd_rows}</tbody>
            </table>"""

    # Schema detail
    schema_data = checks.get("schema", {})
    if schema_data and "pages" in schema_data:
        schema_rows = ""
        for p in schema_data["pages"]:
            missing = ", ".join(p.get("missing", [])) or "—"
            found = ", ".join(p.get("found_types", [])[:6]) or "None"
            bonus = ", ".join(p.get("bonus", [])) or "—"
            page_pct = round(p.get("score", 0) / p.get("maxScore", 1) * 100) if p.get("maxScore") else 0
            bar_c = pct_bar_color(page_pct)
            schema_rows += f"""<tr>
                <td><code>{p.get("file","")}</code></td>
                <td>{p.get("page_type","")}</td>
                <td style="color:{bar_c};font-weight:600">{p.get("score",0)}/{p.get("maxScore",0)}</td>
                <td style="color:#64748b;font-size:0.85em">{found}</td>
                <td style="color:#ef4444;font-size:0.85em">{missing}</td>
                <td style="color:#22c55e;font-size:0.85em">{bonus}</td>
            </tr>"""
        html += f"""
        <h3>Schema Detail by Page</h3>
        <table class="data-table">
            <thead><tr><th>Page</th><th>Type</th><th>Score</th><th>Schema Found</th><th>Missing</th><th>Bonus</th></tr></thead>
            <tbody>{schema_rows}</tbody>
        </table>"""

    return html


def section_phase4(phase4: dict) -> str:
    if not phase4:
        return "<p class='empty'>No Phase 4 data found.</p>"

    checks = phase4.get("checks", {})
    rows = ""
    all_issues = []

    for key, name, _ in PHASE4_CATS:
        c = checks.get(key, {})
        if not c:
            continue
        if c.get("skipped"):
            rows += f'<tr><td>{name}</td><td colspan="3" style="color:#94a3b8;font-style:italic">⏭ Skipped — self-hosted runner required</td></tr>'
            continue
        if "error" in c:
            rows += f'<tr><td>{name}</td><td colspan="3" class="error">✗ {c["error"][:80]}</td></tr>'
            continue
        pct = c.get("percentage", 0)
        score = c.get("score", 0)
        max_s = c.get("maxScore", 0)
        bar_c = pct_bar_color(pct)
        rows += f"""<tr>
            <td>{name}</td>
            <td><div class="pct-bar"><div style="width:{pct}%;background:{bar_c}"></div></div></td>
            <td style="color:{bar_c};font-weight:600">{score}/{max_s}</td>
            <td>{pct}%</td>
        </tr>"""
        for e in c.get("errors", []):
            issue = e.get("issue") or e.get("error") or ""
            ident = e.get("file") or e.get("url") or ""
            if issue:
                all_issues.append((name, ident, issue))

    issue_rows = "".join(
        f'<tr><td class="sev-error">{n}</td><td><code>{i}</code></td><td>{issue}</td></tr>'
        for n, i, issue in all_issues[:20]
    )

    html = f"""
    <table class="data-table">
        <thead><tr><th>Check</th><th>Progress</th><th>Score</th><th>%</th></tr></thead>
        <tbody>{rows}</tbody>
    </table>"""

    if issue_rows:
        html += f"""
        <h3>Content Intelligence Issues</h3>
        <table class="issues-table">
            <thead><tr><th>Check</th><th>Page</th><th>Issue</th></tr></thead>
            <tbody>{issue_rows}</tbody>
        </table>"""

    # Entity detail
    entity_data = checks.get("entity_signals", {})
    if entity_data and "pages" in entity_data:
        ent_rows = ""
        for p in entity_data["pages"][:8]:
            top = ", ".join(e["entity"] for e in p.get("top_entities", [])[:5]) or "—"
            hi  = ", ".join(p.get("heading_entities", [])[:3]) or "—"
            bar_c = pct_bar_color(round(p.get("score", 0) / max(p.get("maxScore", 1), 1) * 100))
            ent_rows += f"""<tr>
                <td><code>{p.get("file","")}</code></td>
                <td style="color:{bar_c};font-weight:600">{p.get("entity_count",0)} entities</td>
                <td style="font-size:0.82em;color:#475569">{top}</td>
                <td style="font-size:0.82em;color:#6366f1">{hi}</td>
            </tr>"""
        html += f"""
        <h3>Entity Signal Detail</h3>
        <table class="data-table">
            <thead><tr><th>Page</th><th>Entities</th><th>Top Entities</th><th>In Headings</th></tr></thead>
            <tbody>{ent_rows}</tbody>
        </table>"""

    return html


# ── Chart.js Snippets ──────────────────────────────────────────────────────────

def charts_js(data: dict) -> str:
    crawl  = data.get("crawl") or []
    phase3 = data["phase3"]
    phase4 = data.get("phase4")

    # ── Crawl: domain-level bar chart ────────────────────────────────────────
    by_domain: dict[str, list] = {}
    for r in crawl:
        by_domain.setdefault(r["domain"], []).append(r)
    domain_labels = list(by_domain.keys())
    domain_avgs   = [round(sum(p["percentage"] for p in pages) / len(pages)) for pages in by_domain.values()]
    crawl_labels_js = json.dumps(domain_labels)
    crawl_avgs_js   = json.dumps(domain_avgs)

    # ── Crawl: per-check radar for TGG only ─────────────────────────────────
    tgg_pages = [r for r in crawl if "thegoodguys" in r.get("domain", "")]
    if tgg_pages:
        check_names = [name for _, name, _ in CRAWL_CHECKS]
        check_avgs  = []
        for key, _, mx in CRAWL_CHECKS:
            scores = [r.get("checks", {}).get(key, {}).get("score") or 0 for r in tgg_pages]
            avg_pct = round(sum(scores) / len(scores) / mx * 100) if mx else 0
            check_avgs.append(avg_pct)
        crawl_check_labels = json.dumps(check_names)
        crawl_check_data   = json.dumps(check_avgs)
    else:
        crawl_check_labels = "[]"
        crawl_check_data   = "[]"

    # ── Phase 3 radar ────────────────────────────────────────────────────────
    if phase3:
        p3_checks = phase3.get("checks", {})
        p3_labels = json.dumps([c[1] for c in PHASE3_CATS])
        p3_data   = json.dumps([p3_checks.get(c[0], {}).get("percentage", 0) for c in PHASE3_CATS])
    else:
        p3_labels = "[]"
        p3_data   = "[]"

    # ── Phase 4 radar ────────────────────────────────────────────────────────
    if phase4:
        p4_checks = phase4.get("checks", {})
        p4_labels = json.dumps([c[1] for c in PHASE4_CATS])
        p4_data   = json.dumps([p4_checks.get(c[0], {}).get("percentage", 0) for c in PHASE4_CATS])
    else:
        p4_labels = "[]"
        p4_data   = "[]"

    return f"""
<script>
// ── Crawl: Domain comparison ─────────────────────────────────────────
new Chart(document.getElementById('chartCrawlDomains'), {{
    type: 'bar',
    data: {{
        labels: {crawl_labels_js},
        datasets: [{{
            label: 'Avg AEO Score %',
            data: {crawl_avgs_js},
            backgroundColor: {crawl_avgs_js}.map(v => v >= 75 ? '#22c55e' : v >= 50 ? '#eab308' : v >= 25 ? '#f97316' : '#ef4444'),
            borderRadius: 6,
        }}]
    }},
    options: {{
        indexAxis: 'y',
        responsive: true,
        scales: {{
            x: {{ min: 0, max: 100, ticks: {{ callback: v => v + '%' }} }},
            y: {{ ticks: {{ font: {{ size: 13 }} }} }}
        }},
        plugins: {{ legend: {{ display: false }}, title: {{ display: true, text: 'AEO Score by Domain', font: {{ size: 15 }} }} }}
    }}
}});

// ── Crawl: TGG check radar ────────────────────────────────────────────
new Chart(document.getElementById('chartCrawlChecks'), {{
    type: 'radar',
    data: {{
        labels: {crawl_check_labels},
        datasets: [{{
            label: 'TGG AEO Crawl',
            data: {crawl_check_data},
            backgroundColor: 'rgba(99,102,241,0.2)',
            borderColor: '#6366f1',
            pointBackgroundColor: '#6366f1',
            pointRadius: 4,
        }}]
    }},
    options: {{
        responsive: true,
        scales: {{ r: {{ min: 0, max: 100, ticks: {{ stepSize: 25 }} }} }},
        plugins: {{ title: {{ display: true, text: 'TGG — AEO Check Scores', font: {{ size: 15 }} }} }}
    }}
}});

// ── Phase 3 Radar ─────────────────────────────────────────────────────
new Chart(document.getElementById('chartP3'), {{
    type: 'radar',
    data: {{
        labels: {p3_labels},
        datasets: [{{
            label: 'TGG Ecommerce AEO',
            data: {p3_data},
            backgroundColor: 'rgba(34,197,94,0.2)',
            borderColor: '#22c55e',
            pointBackgroundColor: '#22c55e',
            pointRadius: 5,
        }}]
    }},
    options: {{
        responsive: true,
        scales: {{ r: {{ min: 0, max: 100, ticks: {{ stepSize: 25 }} }} }},
        plugins: {{ title: {{ display: true, text: 'Ecommerce AEO Checks — Phase 3 (TGG)', font: {{ size: 15 }} }} }}
    }}
}});

// ── Phase 4 Radar — Content Intelligence ─────────────────────────────
new Chart(document.getElementById('chartP4'), {{
    type: 'radar',
    data: {{
        labels: {p4_labels},
        datasets: [{{
            label: 'TGG Content Intelligence',
            data: {p4_data},
            backgroundColor: 'rgba(249,115,22,0.2)',
            borderColor: '#f97316',
            pointBackgroundColor: '#f97316',
            pointRadius: 5,
        }}]
    }},
    options: {{
        responsive: true,
        scales: {{ r: {{ min: 0, max: 100, ticks: {{ stepSize: 25 }} }} }},
        plugins: {{ title: {{ display: true, text: 'Content Intelligence — Phase 4 (TGG)', font: {{ size: 15 }} }} }}
    }}
}});
</script>"""


# ── Recommendations ────────────────────────────────────────────────────────────

def section_recommendations(recs: dict | None) -> str:
    if not recs:
        return "<p class='empty'>No recommendations data found. Run generate_recommendations.py after Phase 3.</p>"

    summary = recs.get("summary", {})
    pages = recs.get("pages", [])
    global_fixes = recs.get("global_fixes", [])
    robots_additions = recs.get("robots_additions", [])

    priority_color = {"critical": "#dc2626", "high": "#f97316", "medium": "#eab308", "low": "#22c55e"}

    html = f"""
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px">
        <div style="background:#fee2e2;padding:16px;border-radius:8px;text-align:center">
            <div style="font-size:2em;font-weight:800;color:#dc2626">{summary.get('critical_pages',0)}</div>
            <div style="font-size:0.85em;color:#9a3412">Critical pages</div>
        </div>
        <div style="background:#fff7ed;padding:16px;border-radius:8px;text-align:center">
            <div style="font-size:2em;font-weight:800;color:#f97316">{summary.get('high_pages',0)}</div>
            <div style="font-size:0.85em;color:#9a3412">High priority</div>
        </div>
        <div style="background:#fef9c3;padding:16px;border-radius:8px;text-align:center">
            <div style="font-size:2em;font-weight:800;color:#ca8a04">{summary.get('pages_with_fixes',0)}</div>
            <div style="font-size:0.85em;color:#713f12">Pages needing fixes</div>
        </div>
        <div style="background:#dcfce7;padding:16px;border-radius:8px;text-align:center">
            <div style="font-size:2em;font-weight:800;color:#16a34a">{summary.get('total_fixes',0)}</div>
            <div style="font-size:0.85em;color:#14532d">Total fixes</div>
        </div>
    </div>"""

    if global_fixes:
        html += "<h3>Global Fixes</h3><ul style='margin:0 0 16px 20px'>"
        for fix in global_fixes:
            html += f"<li style='margin-bottom:6px'>{fix}</li>"
        html += "</ul>"

    if pages:
        html += "<h3>Per-Page Fixes</h3>"
        for page in pages[:20]:
            prio = page.get("priority", "medium")
            pcolor = priority_color.get(prio, "#94a3b8")
            html += f"""<details style="margin-bottom:10px;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden">
            <summary style="padding:12px 16px;cursor:pointer;background:#f8fafc;display:flex;align-items:center;gap:12px">
                <span style="background:{pcolor};color:white;padding:2px 10px;border-radius:12px;font-size:0.78em;font-weight:700;text-transform:uppercase">{prio}</span>
                <code style="font-size:0.9em">{page.get('file','')}</code>
                <span style="color:#64748b;font-size:0.85em">({page.get('page_type','')}) — {page.get('fix_count',0)} fix(es)</span>
            </summary>
            <div style="padding:16px">"""
            for fix in page.get("fixes", []):
                impact_badge = f'<span style="background:#dcfce7;color:#166534;padding:1px 8px;border-radius:10px;font-size:0.75em;font-weight:600">{fix.get("impact","").upper()}</span>'
                effort_badge = f'<span style="background:#f1f5f9;color:#475569;padding:1px 8px;border-radius:10px;font-size:0.75em">{fix.get("effort","").upper()} effort</span>'
                html += f"""<div style="margin-bottom:14px;padding:12px;background:#fffbeb;border-left:3px solid {pcolor};border-radius:4px">
                    <div style="font-weight:600;margin-bottom:4px">{fix.get('issue','')} &nbsp;{impact_badge} {effort_badge}</div>
                    <div style="font-size:0.88em;color:#374151;margin-bottom:8px">{fix.get('fix','')}</div>"""
                if fix.get("snippet"):
                    html += f'<details style="margin-top:6px"><summary style="cursor:pointer;font-size:0.82em;color:#6366f1">Show code snippet</summary><pre style="background:#1e293b;color:#e2e8f0;padding:12px;border-radius:6px;overflow-x:auto;font-size:0.82em;margin-top:6px">{fix["snippet"]}</pre></details>'
                html += "</div>"
            html += "</div></details>"

    if robots_additions:
        html += "<h3>robots.txt Additions</h3>"
        for addition in robots_additions:
            html += f'<pre style="background:#1e293b;color:#e2e8f0;padding:12px;border-radius:6px;font-size:0.82em;margin-bottom:8px">{addition}</pre>'

    llms_txt = recs.get("llms_txt_template", "")
    if llms_txt:
        html += f"""<h3>llms.txt Template</h3>
        <details>
            <summary style="cursor:pointer;color:#6366f1;font-weight:600">Show llms.txt template for thegoodguys.com.au</summary>
            <pre style="background:#1e293b;color:#e2e8f0;padding:16px;border-radius:8px;overflow-x:auto;font-size:0.82em;margin-top:8px;white-space:pre-wrap">{llms_txt}</pre>
        </details>"""

    return html


CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; }
.container { max-width: 1200px; margin: 0 auto; padding: 24px 16px; }
.report-header { background: linear-gradient(135deg, #1e293b 0%, #334155 100%); color: white; padding: 32px; border-radius: 12px; margin-bottom: 28px; }
.report-header h1 { font-size: 1.8em; margin-bottom: 4px; }
.report-header .meta { color: #94a3b8; font-size: 0.9em; }
.hero-cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 28px; }
.hero-card { padding: 24px; border-radius: 10px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
.hero-grade { font-size: 3em; font-weight: 800; line-height: 1; }
.hero-pct { font-size: 1.6em; font-weight: 700; margin: 4px 0; }
.hero-title { font-weight: 600; font-size: 1em; margin-top: 8px; color: #374151; }
.hero-sub { font-size: 0.8em; color: #6b7280; margin-top: 2px; }
.section { background: white; border-radius: 10px; padding: 24px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.07); }
.section h2 { font-size: 1.3em; color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 18px; }
.section h3 { font-size: 1.05em; color: #374151; margin: 20px 0 12px; }
.charts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 28px; }
.chart-box { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.07); }
.chart-box-wide { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.07); margin-bottom: 24px; }
.data-table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
.data-table th { background: #f1f5f9; padding: 8px 12px; text-align: left; font-size: 0.82em; color: #475569; text-transform: uppercase; letter-spacing: 0.04em; }
.data-table td { padding: 9px 12px; border-bottom: 1px solid #f1f5f9; vertical-align: middle; }
.data-table tr:hover td { background: #f8fafc; }
.issues-table { width: 100%; border-collapse: collapse; font-size: 0.85em; }
.issues-table th { background: #fff7ed; padding: 8px 12px; text-align: left; font-size: 0.8em; color: #9a3412; text-transform: uppercase; letter-spacing: 0.04em; }
.issues-table td { padding: 8px 12px; border-bottom: 1px solid #fef3c7; vertical-align: top; }
.issues-table tr:hover td { background: #fffbeb; }
.pct-bar { display: inline-block; width: 80px; height: 8px; background: #e2e8f0; border-radius: 4px; vertical-align: middle; margin-right: 6px; overflow: hidden; }
.pct-bar div { height: 100%; border-radius: 4px; }
.sev-error { color: #dc2626; font-weight: 600; white-space: nowrap; }
.sev-warn { color: #d97706; font-weight: 600; white-space: nowrap; }
.fail { color: #dc2626; font-weight: 600; }
.warn { color: #d97706; font-weight: 600; }
.error { color: #dc2626; font-style: italic; }
.empty { color: #94a3b8; font-style: italic; padding: 20px 0; }
.score-summary { margin-bottom: 16px; }
.score-label { color: #64748b; font-size: 1em; }
code { font-family: 'SF Mono', 'Fira Code', monospace; background: #f1f5f9; padding: 1px 5px; border-radius: 3px; font-size: 0.85em; }
.footer { text-align: center; color: #94a3b8; font-size: 0.82em; margin-top: 32px; padding: 16px; }
@media (max-width: 768px) {
    .hero-cards { grid-template-columns: 1fr; }
    .charts-grid { grid-template-columns: 1fr; }
}
"""


def build_html(data: dict) -> str:
    crawl  = data.get("crawl") or []
    p3     = data["phase3"]
    ts     = data["ts"]
    run_num = data["run_number"]
    ref    = data["ref"]

    p3_grade = p3.get("grade", "?") if p3 else "?"
    p3_pct   = p3.get("percentage", 0) if p3 else 0
    p4       = data.get("phase4")
    p4_grade = p4.get("grade", "?") if p4 else "?"
    p4_pct   = p4.get("percentage", 0) if p4 else 0

    crawl_grade, crawl_pct = _tgg_crawl_grade(crawl) if crawl else ("?", 0)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AEO Audit Report — The Good Guys — {ts}</title>
<style>{CSS}</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
</head>
<body>
<div class="container">

  <div class="report-header">
    <h1>AEO Audit Report — The Good Guys</h1>
    <div class="meta">Run #{run_num} &nbsp;·&nbsp; Branch: {ref} &nbsp;·&nbsp; Generated: {ts}</div>
  </div>

  {section_hero(data)}

  <div class="charts-grid">
    <div class="chart-box"><canvas id="chartCrawlDomains" height="220"></canvas></div>
    <div class="chart-box"><canvas id="chartCrawlChecks" height="220"></canvas></div>
    <div class="chart-box"><canvas id="chartP3" height="220"></canvas></div>
    <div class="chart-box"><canvas id="chartP4" height="220"></canvas></div>
  </div>

  <div class="section">
    <h2>AEO Crawl — Per-URL Signal Audit {grade_badge(crawl_grade, crawl_pct)}</h2>
    {section_crawl(crawl)}
  </div>

  <div class="section">
    <h2>Phase 3 — Ecommerce AEO {grade_badge(p3_grade, p3_pct)}</h2>
    {section_phase3(p3)}
  </div>

  <div class="section">
    <h2>Phase 4 — Content Intelligence {grade_badge(p4_grade, p4_pct)}</h2>
    {section_phase4(p4)}
  </div>

  <div class="section">
    <h2>Recommendations — Prioritised Fix List</h2>
    {section_recommendations(data.get('recommendations'))}
  </div>

  <div class="footer">
    AEO Audit · The Good Guys · thegoodguys.com.au · {ts}
  </div>

</div>
{charts_js(data)}
</body>
</html>"""
    return html


# ── Push to Repo ───────────────────────────────────────────────────────────────

def push_to_repo(content: str, path: str) -> None:
    token = os.getenv("GITHUB_TOKEN")
    repo  = os.getenv("GITHUB_REPOSITORY")
    ref   = os.getenv("GITHUB_REF_NAME")
    run_number = os.getenv("GITHUB_RUN_NUMBER", "?")
    if not (token and repo and ref):
        return
    b64 = base64.b64encode(content.encode()).decode()
    api  = "https://api.github.com"
    hdrs = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    existing = httpx.get(f"{api}/repos/{repo}/contents/{path}?ref={ref}", headers=hdrs, timeout=30)
    sha = existing.json().get("sha") if existing.status_code == 200 else None
    payload = {"message": f"AEO report run #{run_number}", "content": b64, "branch": ref}
    if sha:
        payload["sha"] = sha
    resp = httpx.put(f"{api}/repos/{repo}/contents/{path}", headers=hdrs, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"Committed to repo: {path}")
    else:
        print(f"Warning: could not commit report ({resp.status_code})", file=sys.stderr)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    out_dir = os.getenv("AEO_OUTPUT_DIR", "seo/outputs/aeo")
    data = load_all_data(out_dir)

    if not any([data["crawl"], data["phase3"]]):
        print("No AEO output data found. Run the audit first.", file=sys.stderr)
        sys.exit(1)

    html = build_html(data)

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    report_file = out_path / f"report-{ts}.html"
    report_latest = out_path / "report-latest.html"

    report_file.write_text(html, encoding="utf-8")
    report_latest.write_text(html, encoding="utf-8")
    print(f"Report saved: {report_file}")

    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as f:
            f.write(
                f"\n\n---\n\n## 📊 Full Interactive Report\n\n"
                f"🔗 **[View Report → simonmannheimer-tgg.github.io/Claude/aeo/](https://simonmannheimer-tgg.github.io/Claude/aeo/)**\n\n"
                f"Updated automatically after every workflow run. Also in artifact **aeo-results-${{GITHUB_RUN_ID}}** → `{report_file.name}`.\n"
            )

    push_to_repo(html, "seo/outputs/aeo/report-latest.html")


if __name__ == "__main__":
    main()
