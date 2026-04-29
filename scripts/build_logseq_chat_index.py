#!/usr/bin/env python3
"""Build Logseq vault pages from Anthropic conversation export.

Generates 3-tier markdown (light/medium/full) per conversation with full
tag taxonomy: #project/*, #status/*, #topic/*, #skill/*.

Usage:
    python3 scripts/build_logseq_chat_index.py [export_dir] [vault_dir]

Defaults to /tmp/chat-export and ./vault.
"""
import json
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

EXPORT_DIR = Path(sys.argv[1] if len(sys.argv) > 1 else '/tmp/chat-export')
VAULT_DIR = Path(sys.argv[2] if len(sys.argv) > 2 else 'vault')
PAGES_DIR = VAULT_DIR / 'pages'
INDEX_DOC = Path('seo/outputs/drive-backup/raw/TGG_Claude_Session_Index_FULL.md')

NOW = datetime.now(timezone.utc)

TOPIC_KEYWORDS = {
    'schema': r'\bschema(\.org)?\b|\bjson-?ld\b|\bstructured data\b',
    'feed': r'\bgmc\b|merchant\s*center|product\s+feed|shopify\s+feed',
    'blog': r'\bblog\b|whats?-new|buying\s+guide|\barticle\b',
    'eofy': r'\beofy\b|end\s+of\s+financial\s+year',
    'bfcm': r'\bbfcm\b|black\s+friday|cyber\s+monday',
    '404': r'\b404\b|broken\s+link',
    'contentful': r'\bcontentful\b',
    'shopify': r'\bshopify\b',
    'screaming-frog': r'screaming\s*frog|\bsf\s+crawl\b',
    'semrush': r'\bsemrush\b',
    'profound': r'\bprofound\b',
    'airtable': r'\bairtable\b',
    'aeo': r'\baeo\b|answer\s+engine|\bgeo\b|ai\s+overview',
    'inlink': r'inlink|internal\s+link',
    'plp': r'\bplp\b|product\s+listing\s+page|category\s+page',
    'pdp': r'\bpdp\b|product\s+detail\s+page|product\s+page',
    'redirect': r'\bredirect\b|\b301\b',
    'sitemap': r'sitemap',
    'crawl': r'\bcrawl\b|crawling',
    'meta': r'meta\s+title|meta\s+description|meta\s+tag',
    'copy': r'copywriting|copy\s+production|intro\s+copy|category\s+copy',
    'keyword': r'\bkeyword',
    'gsc': r'\bgsc\b|search\s+console',
    'ga4': r'\bga4\b|google\s+analytics',
    'regex': r'regex|regular\s+expression',
    'youtube': r'youtube|video\s+transcript',
    'deals': r'/deals/|deals\s+page',
    'agent': r'\bsub-?agent\b|claude\s+code\s+agent',
    'mcp': r'\bmcp\b|model\s+context\s+protocol',
    'jira': r'\bjira\b',
    'monday': r'\bmonday\.com\b',
}
TOPIC_RE = {tag: re.compile(p, re.I) for tag, p in TOPIC_KEYWORDS.items()}

KNOWN_SKILLS = [
    'tgg-prompt-architect', 'tgg-copywriting', 'tgg-seo-specialist',
    'tgg-content-strategist', 'tgg-humanizer', 'tgg-pptx-style',
    'tgg-chart-creator', 'tgg-monthly-seo-report', 'tgg-marketing-analyst',
    'tgg-template-generator', 'tgg-repo-manager', 'tgg-contentful-linker',
    'tgg-conversation-indexer', 'tgg-session-anchor',
    'mhtml-reader', 'verification-gate-protocol', 'docx-human-style',
]
SKILL_RE = re.compile(r'\b(' + '|'.join(re.escape(s) for s in KNOWN_SKILLS) + r')\b', re.I)

DELIVERABLE_RE = re.compile(
    r'\.(xlsx|docx|pptx|csv|md|html|json|txt|py|js|sql|zip|pdf)\b|```|\bdeliver(ed|able)',
    re.I,
)
PROJECT_KW_RE = re.compile(
    r'\b(schema|feed|blog|eofy|gmc|404|contentful|shopify|screaming|semrush|profound'
    r'|airtable|aeo|inlink|plp|pdp|redirect|sitemap|crawl|meta|copy|keyword|gsc|ga4'
    r'|merchant)\b',
    re.I,
)
LASTING_RE = re.compile(r'\b(skill|process|memory|rule|standard|decision|brief)\b', re.I)
NAMED_TGG_RE = re.compile(r'\b(eofy|bfcm|tgg|good\s*guys|monthly\s+seo)\b', re.I)


def slugify(s, maxlen=60):
    s = re.sub(r'[^\w\s-]', '', (s or '').lower()).strip()
    s = re.sub(r'[\s_-]+', '-', s)
    return s[:maxlen].rstrip('-') or 'untitled'


SECRET_PATTERNS = [
    # Airtable PAT
    (re.compile(r'pat[A-Za-z0-9]{14}\.[a-f0-9]{50,}'), '[REDACTED-AIRTABLE-PAT]'),
    # OpenAI / Anthropic API keys
    (re.compile(r'sk-ant-[A-Za-z0-9_-]{20,}'), '[REDACTED-ANTHROPIC-KEY]'),
    (re.compile(r'sk-[A-Za-z0-9]{20,}'), '[REDACTED-OPENAI-KEY]'),
    # GitHub tokens
    (re.compile(r'ghp_[A-Za-z0-9]{36}'), '[REDACTED-GITHUB-PAT]'),
    (re.compile(r'github_pat_[A-Za-z0-9_]{50,}'), '[REDACTED-GITHUB-PAT]'),
    # AWS access key
    (re.compile(r'AKIA[0-9A-Z]{16}'), '[REDACTED-AWS-KEY]'),
    # Slack bot token
    (re.compile(r'xox[baprs]-[A-Za-z0-9-]{20,}'), '[REDACTED-SLACK-TOKEN]'),
    # Firecrawl
    (re.compile(r'fc-[a-z0-9]{32,}'), '[REDACTED-FIRECRAWL-KEY]'),
    # Semrush
    (re.compile(r'semrush[_-]?api[_-]?key[\s:=]+["\']?([a-z0-9]{32})', re.I), 'semrush_api_key=[REDACTED]'),
]


def redact_secrets(text):
    for pattern, replacement in SECRET_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def extract_text(msg):
    parts = []
    if msg.get('text'):
        parts.append(msg['text'])
    for block in msg.get('content') or []:
        if block.get('type') == 'text' and block.get('text'):
            parts.append(block['text'])
    return redact_secrets('\n'.join(parts))


def parse_index_mappings(text):
    """uuid -> {project, section, status} mappings from the master index.

    The master index uses backslash-escaped markdown (\\#\\#\\#, \\*\\*).

    Status is derived from which top-level (## ) section the chat appears
    under: ACTIVE PROJECTS → active; COMPLETED DELIVERABLES → completed;
    CLOSED / TACTICAL → tactical.
    """
    out = {}
    if not text:
        return out
    clean = text.replace('\\#', '#').replace('\\*', '*').replace('\\-', '-').replace('\\.', '.')
    chat_re = re.compile(r'claude\.ai/chat/([0-9a-f-]{36})')
    project_re = re.compile(r'\*\*Project:\*\*\s*([^\n|*]+)', re.I)

    # Split into top-level sections (## H2 headings) to determine status
    h2_blocks = re.split(r'\n##\s+(?!#)', clean)
    for block in h2_blocks:
        head_line = block.split('\n', 1)[0].strip(' #').upper()
        if 'ACTIVE PROJECT' in head_line:
            block_status = 'active'
        elif 'COMPLETED DELIVERABLE' in head_line:
            block_status = 'completed'
        elif 'CLOSED' in head_line or 'TACTICAL' in head_line:
            block_status = 'tactical'
        else:
            block_status = None

        # Within block, find ### subsections and chat uuids
        subsections = re.split(r'\n###\s+', block)
        for sec in subsections:
            section_head = sec.split('\n', 1)[0].strip(' #')[:80]
            proj_m = project_re.search(sec)
            proj = proj_m.group(1).strip() if proj_m else None
            if proj:
                proj = re.sub(r'\s*\((?:claude project[s]?)\)\s*$', '', proj, flags=re.I).strip()
                proj = proj.split('/')[0].strip()
            for m in chat_re.finditer(sec):
                uuid = m.group(1)
                if uuid not in out:
                    out[uuid] = {
                        'project': proj,
                        'section': section_head,
                        'status': block_status,
                    }
                else:
                    # If already mapped, prefer non-tactical status
                    existing = out[uuid]
                    if existing.get('status') is None and block_status:
                        existing['status'] = block_status
                    if not existing.get('project') and proj:
                        existing['project'] = proj
    return out


def score_and_classify(conv, full_text):
    score = 0
    reasons = []
    if DELIVERABLE_RE.search(full_text):
        score += 1; reasons.append('deliverable')
    if NAMED_TGG_RE.search(full_text):
        score += 1; reasons.append('named-tgg')
    if len(conv.get('chat_messages') or []) >= 5:
        score += 1; reasons.append('5+turns')
    if PROJECT_KW_RE.search(full_text):
        score += 1; reasons.append('project-keyword')
    if LASTING_RE.search(full_text):
        score += 1; reasons.append('lasting-effect')
    return score, reasons


COMPLETION_RE = re.compile(
    r'\b(thank|thanks|perfect|great|nice|excellent|amazing|legend|brilliant|'
    r'looks good|all good|nailed it|that.?s it|done|sorted|final|approved|ship it|'
    r'go ahead|locked in|good to go)\b',
    re.I,
)


QUESTION_RE = re.compile(r'\?\s*$|^(can you|could you|please|how do|why|what|where|when|fix|update|change|redo|try again|but )', re.I)


def classify_status(conv, score):
    if score <= 1:
        return 'tactical'
    updated = datetime.fromisoformat(conv['updated_at'].replace('Z', '+00:00'))
    days = (NOW - updated).days
    msgs = conv.get('chat_messages') or []
    last_msg = msgs[-1] if msgs else None
    last_user = next((m for m in reversed(msgs) if m.get('sender') == 'human'), None)

    # Recent (< 7 days) → active unless explicit closing signal
    if days < 7:
        if last_user:
            text = extract_text(last_user).strip()
            if len(text) < 300 and COMPLETION_RE.search(text):
                return 'completed'
        return 'active'

    # Old chats (>= 7 days). Default lean: completed.
    # Override to 'abandoned' only when the last message is from human and looks
    # like an unanswered question or open task (i.e., the conversation broke off
    # mid-flow).
    if last_msg and last_msg.get('sender') == 'human':
        last_text = extract_text(last_msg).strip()
        # Short closing thanks → completed
        if len(last_text) < 300 and COMPLETION_RE.search(last_text):
            return 'completed'
        # Unanswered question or request → abandoned
        if QUESTION_RE.search(last_text[:200]):
            return 'abandoned'
        # Long human message with no assistant response → likely abandoned
        if len(last_text) > 500:
            return 'abandoned'

    return 'completed'


def detect_topics(text):
    return sorted(t for t, r in TOPIC_RE.items() if r.search(text))


def detect_skills(text):
    return sorted({m.group(1).lower() for m in SKILL_RE.finditer(text)})


def render_light(meta):
    chat_url = f'https://claude.ai/chat/{meta["uuid"]}'
    tags = ['#chat/light', f'#project/{meta["project_slug"]}', f'#status/{meta["status"]}']
    tags += [f'#topic/{t}' for t in meta['topics']]
    tags += [f'#skill/{s}' for s in meta['skills']]
    return f"""---
title: {meta['title']}
date: {meta['date']}
project: {meta['project']}
status: {meta['status']}
score: {meta['score']}/5
uuid: {meta['uuid']}
---

{' '.join(tags)}

# {meta['title']}

- **Date:** [[{meta['date']}]]
- **Project:** [[Projects/{meta['project']}]]
- **Status:** #status/{meta['status']} (score {meta['score']}/5: {', '.join(meta['reasons']) or 'n/a'})
- **Messages:** {meta['msg_count']}
- **Chat URL:** {chat_url}
- **Medium view:** [[Chat/Medium/{meta['slug']}]]
- **Full transcript:** [[Chat/Full/{meta['slug']}]]

## Summary

{meta['summary']}

## First user message

> {meta['first_user']}

## Topics

{', '.join(f'[[topic/{t}]]' for t in meta['topics']) or 'none detected'}

## Skills referenced

{', '.join(f'[[skill/{s}]]' for s in meta['skills']) or 'none detected'}
"""


def render_medium(meta, user_messages):
    msg_blocks = []
    for i, (ts, txt) in enumerate(user_messages, 1):
        ts_short = ts[:16] if ts else ''
        excerpt = txt.strip()
        if len(excerpt) > 1500:
            excerpt = excerpt[:1500] + '\n\n[truncated — see full transcript]'
        msg_blocks.append(f'### Message {i} — {ts_short}\n\n{excerpt}')
    body = '\n\n'.join(msg_blocks) or '_No user messages._'
    return f"""---
title: {meta['title']} (medium)
parent: Chat/Light/{meta['slug']}
uuid: {meta['uuid']}
---

#chat/medium #project/{meta['project_slug']} #status/{meta['status']}

# {meta['title']} — Key User Messages

→ Light view: [[Chat/Light/{meta['slug']}]]
→ Full transcript: [[Chat/Full/{meta['slug']}]]

**Total user messages:** {len(user_messages)}

---

{body}
"""


def render_full(meta, all_messages):
    blocks = []
    for i, (sender, ts, txt) in enumerate(all_messages, 1):
        ts_short = ts[:16] if ts else ''
        sender_label = '**Human**' if sender == 'human' else '**Claude**'
        # Don't truncate — full is full
        blocks.append(f'### {i}. {sender_label} — {ts_short}\n\n{txt.strip()}')
    body = '\n\n---\n\n'.join(blocks) or '_No messages._'
    return f"""---
title: {meta['title']} (full)
parent: Chat/Light/{meta['slug']}
uuid: {meta['uuid']}
---

#chat/full #project/{meta['project_slug']} #status/{meta['status']}

# {meta['title']} — Full Transcript

→ Light view: [[Chat/Light/{meta['slug']}]]
→ Medium view: [[Chat/Medium/{meta['slug']}]]

**Messages:** {meta['msg_count']} | **Date:** {meta['date']}

---

{body}
"""


def main():
    print(f'Loading export from {EXPORT_DIR}...')
    with (EXPORT_DIR / 'conversations.json').open() as f:
        convs = json.load(f)
    with (EXPORT_DIR / 'projects.json').open() as f:
        projects = json.load(f)

    project_lookup = {p['uuid']: p['name'] for p in projects}
    project_names = {p['name'] for p in projects}

    index_text = INDEX_DOC.read_text() if INDEX_DOC.exists() else ''
    uuid_to_project = parse_index_mappings(index_text)
    print(f'Loaded {len(convs)} conversations, {len(projects)} projects, {len(uuid_to_project)} known uuid->project mappings')

    if PAGES_DIR.exists():
        for p in PAGES_DIR.glob('Chat___*.md'):
            p.unlink()
        for p in PAGES_DIR.glob('Projects___*.md'):
            p.unlink()
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    project_chats = defaultdict(list)
    status_chats = defaultdict(list)
    topic_chats = defaultdict(list)
    written = 0
    skipped = 0

    for conv in convs:
        msgs = conv.get('chat_messages') or []
        if not msgs:
            skipped += 1
            continue

        full_text = '\n'.join(extract_text(m) for m in msgs)
        score, reasons = score_and_classify(conv, full_text)

        # Status: prefer mapping from existing master index; fall back to heuristic.
        proj_info = uuid_to_project.get(conv['uuid'])
        mapped_status = proj_info.get('status') if proj_info else None
        if mapped_status:
            status = mapped_status
            # Override active → abandoned if stale (≥14 days inactive)
            if status == 'active':
                updated_dt = datetime.fromisoformat(conv['updated_at'].replace('Z', '+00:00'))
                if (NOW - updated_dt).days >= 14:
                    status = 'abandoned'
        else:
            status = classify_status(conv, score)

        # project assignment (proj_info already fetched above)
        if proj_info and proj_info.get('project'):
            project = proj_info['project'].strip()
        else:
            # heuristic: match longest distinctive project name first
            haystack = (conv.get('name') or '').lower() + ' ' + full_text[:5000].lower()
            project = 'main'
            # Sort by name length desc so 'EOFY V2' beats 'EOFY'
            for pname in sorted(project_names, key=lambda n: -len(n)):
                pl = pname.lower()
                if len(pname) <= 3:
                    continue
                # Word-boundary match to avoid false positives ('main' in 'maintenance')
                if re.search(rf'\b{re.escape(pl)}\b', haystack):
                    project = pname.strip()
                    break

        topics = detect_topics(full_text)
        skills = detect_skills(full_text)

        title = (conv.get('name') or 'Untitled').strip() or 'Untitled'
        date = (conv.get('updated_at') or conv.get('created_at') or '')[:10]
        # uuid-suffix prevents same-day, same-title slug collisions
        slug = f'{date}-{slugify(title)}-{conv["uuid"][:6]}'

        first_user = next(
            (extract_text(m) for m in msgs if m.get('sender') == 'human'),
            '',
        )
        first_user_excerpt = first_user.strip().replace('\n', ' ')[:400]
        if not first_user_excerpt:
            first_user_excerpt = '_(no user message)_'

        summary = (conv.get('summary') or '').strip()
        if not summary:
            # auto: first 240 chars of first user message
            summary = first_user.strip().replace('\n', ' ')[:240] or '_no summary_'

        meta = {
            'uuid': conv['uuid'],
            'title': title,
            'date': date,
            'slug': slug,
            'project': project,
            'project_slug': slugify(project, 40),
            'status': status,
            'score': score,
            'reasons': reasons,
            'msg_count': len(msgs),
            'topics': topics,
            'skills': skills,
            'summary': summary,
            'first_user': first_user_excerpt,
        }

        # write 3 pages
        (PAGES_DIR / f'Chat___Light___{slug}.md').write_text(render_light(meta))

        user_msgs = [
            (m.get('created_at', ''), extract_text(m))
            for m in msgs if m.get('sender') == 'human'
        ]
        (PAGES_DIR / f'Chat___Medium___{slug}.md').write_text(render_medium(meta, user_msgs))

        all_msgs = [
            (m.get('sender', '?'), m.get('created_at', ''), extract_text(m))
            for m in msgs
        ]
        (PAGES_DIR / f'Chat___Full___{slug}.md').write_text(render_full(meta, all_msgs))

        project_chats[project].append(meta)
        status_chats[status].append(meta)
        for t in topics:
            topic_chats[t].append(meta)

        written += 1

    # Project MOC pages
    for project, chats in sorted(project_chats.items()):
        chats_sorted = sorted(chats, key=lambda c: c['date'], reverse=True)
        rows = []
        for c in chats_sorted:
            rows.append(
                f'- [[Chat/Light/{c["slug"]}]] — {c["date"]} — '
                f'#status/{c["status"]} ({c["msg_count"]} msgs)'
            )
        body = '\n'.join(rows)
        proj_slug = slugify(project, 40)
        (PAGES_DIR / f'Projects___{proj_slug}.md').write_text(f"""---
title: Projects/{project}
type: project-moc
chat-count: {len(chats)}
---

#project/{proj_slug} #moc

# Projects/{project}

**Total chats:** {len(chats)}
**Status breakdown:** {', '.join(f'{s}={sum(1 for c in chats if c["status"]==s)}' for s in ['active','completed','abandoned','tactical'])}

## Chats (newest first)

{body}
""")

    # Master index page
    master_lines = ['---', 'title: Conversations Master Index', '---', '', '# Conversations Master Index', '']
    master_lines.append(f'**Generated:** {NOW.strftime("%Y-%m-%d %H:%M UTC")}')
    master_lines.append(f'**Total indexed:** {written} (skipped {skipped} empty conversations)')
    master_lines.append('')
    master_lines.append('## By status\n')
    for status in ['active', 'completed', 'abandoned', 'tactical']:
        master_lines.append(f'- #status/{status} — {len(status_chats[status])} chats')
    master_lines.append('')
    master_lines.append('## By project\n')
    for project, chats in sorted(project_chats.items(), key=lambda kv: -len(kv[1])):
        master_lines.append(f'- [[Projects/{project}]] — {len(chats)} chats')
    master_lines.append('')
    master_lines.append('## Top topics\n')
    for topic, chats in sorted(topic_chats.items(), key=lambda kv: -len(kv[1]))[:25]:
        master_lines.append(f'- #topic/{topic} — {len(chats)} chats')
    master_lines.append('')
    master_lines.append('## All active projects (status=active)\n')
    for c in sorted(status_chats['active'], key=lambda c: c['date'], reverse=True):
        master_lines.append(f'- [[Chat/Light/{c["slug"]}]] — {c["date"]} — {c["title"][:80]}')
    (PAGES_DIR / 'Conversations Master Index.md').write_text('\n'.join(master_lines))

    print(f'\nWrote {written} conversations × 3 tiers = {written * 3} chat pages')
    print(f'Wrote {len(project_chats)} project MOC pages')
    print(f'Wrote 1 master index')
    print(f'Skipped {skipped} empty conversations')
    print(f'\nStatus breakdown:')
    for status, chats in sorted(status_chats.items(), key=lambda kv: -len(kv[1])):
        print(f'  {status:12} {len(chats)}')
    print(f'\nTop projects:')
    for project, chats in sorted(project_chats.items(), key=lambda kv: -len(kv[1]))[:10]:
        print(f'  {project[:40]:40} {len(chats)}')


if __name__ == '__main__':
    main()
