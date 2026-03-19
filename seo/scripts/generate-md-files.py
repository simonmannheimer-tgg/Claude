#!/usr/bin/env python3
"""
Generate final batch MD files from the merged all-batches CSV.
Produces plp-batch-2, plp-batch-3, plp-batch-4 MD files.
"""
import csv, os
from collections import defaultdict

INPUT_CSV = "/home/user/Claude/seo/outputs/plp-all-batches-2026-03-19.csv"
OUTPUT_DIR = "/home/user/Claude/seo/outputs"
DATE = "2026-03-19"

with open(INPUT_CSV, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

# Group by batch
batches = defaultdict(list)
for row in rows:
    batches[row['batch']].append(row)

# QA stats helper
def qa_stats(batch_rows):
    chars = [int(r['chars']) for r in batch_rows]
    in_range = sum(1 for c in chars if 220 <= c <= 250)
    out_range = [r for r in batch_rows if not (220 <= int(r['chars']) <= 250)]
    return {
        'total': len(batch_rows),
        'in_range': in_range,
        'min': min(chars),
        'max': max(chars),
        'out_range': out_range,
    }

def url_to_path(url):
    return url.replace('https://www.thegoodguys.com.au', '')

BATCH_NUMS = {'Batch 2': 2, 'Batch 3': 3, 'Batch 4': 4}

for batch_name, batch_rows in sorted(batches.items()):
    batch_num = BATCH_NUMS.get(batch_name)
    if batch_num is None:
        continue

    stats = qa_stats(batch_rows)
    out_file = os.path.join(OUTPUT_DIR, f"plp-batch-{batch_num}-{DATE}.md")

    lines = []
    lines.append(f"# PLP Intro Copy — Batch {batch_num}")
    lines.append(f"**Date:** {DATE}")
    lines.append(f"**Source:** TGG - SEO WIP _ SM - PLP Intro (Brand Cat).csv")
    lines.append(f"**Batch:** {batch_name} ({len(batch_rows)} URLs)")
    lines.append(f"**Process:** 01-plp-intros.md (220–250 chars, 2 sentences, Australian English)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## QA Summary")
    lines.append("")
    lines.append(f"- **Total URLs processed:** {stats['total']}")
    lines.append(f"- **In range (220–250 chars):** {stats['in_range']} / {stats['total']}")
    lines.append(f"- **Char range:** {stats['min']}–{stats['max']}")
    if stats['out_range']:
        lines.append(f"- **Out of range:** {len(stats['out_range'])} rows")
        for r in stats['out_range']:
            lines.append(f"  - {url_to_path(r['url'])} ({r['chars']} chars)")
    else:
        lines.append(f"- **All char counts:** 220–250 ✓")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Output")
    lines.append("")
    lines.append("| URL | Type | Pri | Copy | Chars |")
    lines.append("|-----|------|-----|------|-------|")

    for r in batch_rows:
        path = url_to_path(r['url'])
        page_type = r['page_type']
        pri = r['priority']
        copy = r['copy'].replace('|', '\\|')
        chars = r['chars']
        lines.append(f"| {path} | {page_type} | {pri} | {copy} | {chars} |")

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print(f"Written: {out_file} ({len(batch_rows)} rows, chars {stats['min']}–{stats['max']})")

print("\nAll MD files generated.")
