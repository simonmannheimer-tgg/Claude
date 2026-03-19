#!/usr/bin/env python3
"""
Merge all PLP intro copy output files into a single downloadable CSV.

Usage:
    python3 seo/scripts/merge-plp-outputs.py

Output:
    seo/outputs/plp-all-batches-<date>.csv
"""

import csv, re
from pathlib import Path
from datetime import date
from collections import Counter

ROOT    = Path(__file__).parent.parent.parent
OUT_DIR = ROOT / 'seo' / 'outputs'
TODAY   = date.today().strftime('%Y-%m-%d')

BATCH_FILES = sorted(OUT_DIR.glob('plp-batch-*.md'))


def parse_md_table(path):
    rows = []
    for line in path.read_text().splitlines():
        if not line.startswith('| /'):
            continue
        cells = [c.strip() for c in line.strip('| ').split(' | ')]
        if len(cells) < 5:
            continue
        url, page_type, priority, copy = cells[0], cells[1], cells[2], cells[3]
        chars_raw = cells[4].split()[0]
        try:
            chars = int(re.search(r'\d+', chars_raw).group())
        except (AttributeError, ValueError):
            chars = len(copy)
        m = re.search(r'plp-batch-(\w+)-', path.stem)
        batch = f'Batch {m.group(1)}' if m else path.stem
        rows.append({
            'batch':     batch,
            'url':       f'https://www.thegoodguys.com.au{url}',
            'page_type': page_type,
            'priority':  priority,
            'copy':      copy,
            'chars':     chars,
        })
    return rows


def main():
    all_rows = []
    for f in BATCH_FILES:
        rows = parse_md_table(f)
        print(f'  {f.name}: {len(rows)} rows')
        all_rows.extend(rows)

    if not all_rows:
        print('No rows found. Check that output .md files exist in seo/outputs/.')
        return

    out_path = OUT_DIR / f'plp-all-batches-{TODAY}.csv'
    with open(out_path, 'w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=['batch', 'url', 'page_type', 'priority', 'copy', 'chars'])
        writer.writeheader()
        writer.writerows(all_rows)

    print(f'\nWritten: {out_path}')
    print(f'Total rows: {len(all_rows)}')

    buckets = Counter()
    for r in all_rows:
        c = r['chars']
        if   c < 220:  buckets['<220'] += 1
        elif c <= 229: buckets['220-229'] += 1
        elif c <= 239: buckets['230-239'] += 1
        elif c <= 249: buckets['240-249'] += 1
        else:          buckets['250'] += 1

    print('\nChar distribution:')
    for k in ['<220', '220-229', '230-239', '240-249', '250']:
        v = buckets[k]
        if v:
            print(f'  {k:8s}: {v:4d}  ({v / len(all_rows) * 100:.1f}%)')


if __name__ == '__main__':
    main()
