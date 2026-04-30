#!/usr/bin/env python3
"""
PLP Intro Copy — QA Audit Script
Run on any plp-all-batches-*.csv output to check for violations.

Usage:
    python3 seo/scripts/plp-qa-audit.py seo/outputs/plp-all-batches-2026-03-19-fixed.csv

Outputs:
    - Summary table to stdout
    - Detailed violation rows to seo/outputs/plp-qa-violations-YYYY-MM-DD.csv
"""

import csv
import sys
import re
from datetime import date
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────

CHAR_FLOOR = 220
CHAR_CEILING = 250

HARD_BANS = [
    'sale', 'sales', 'discount', 'exclusive deal', 'exclusive offer',
    'amazing', 'stunning', 'wonderful',
    "australia's trusted choice",
    'quality brands',
    'get great value',
    'perfect for all needs',
    'busy homes', 'hearty meals', 'sleek design',
    'save money', 'save on ', 'save with price beat',
]

# Only on brand pages (page_type B, C, B1, B2, B3)
BRAND_BANS = ['trusted', 'reliable', 'enjoy', 'features']

# S1 openers to flag as overused (check across batch)
WEAK_S1_OPENERS = ['discover ', 'explore ', 'shop ']

# Generic S1 phrases that indicate no entity anchor
GENERIC_PHRASES = [
    'flexible storage',
    'precise temperature control',
    'generous capacities',
    'powerful purification',
    'smart sensors',
    'stable connections',
    'fast data transfer',
    'gentle fabric care',
    'efficient cycles',
    'strong suction',
    'cordless convenience',
    'clear audio',
    'long battery life',
    'vivid display',
    'ample storage',
    'great features',
    'wide range of options',
    'advanced technology',
    'superior performance',
]


# ── Utilities ────────────────────────────────────────────────────────────────

def is_brand_page(page_type: str) -> bool:
    pt = page_type.strip().upper()
    return pt in ('B', 'C', 'B1', 'B2', 'B3')


def count_sentences(text: str) -> int:
    """Count sentences by full stops not inside abbreviations."""
    # Simple: count terminal full stops
    sentences = re.split(r'(?<=[a-zA-Z0-9\'\"])\.\s+', text)
    # Also check if text ends with a full stop
    if text.strip().endswith('.'):
        return len(sentences)
    return len(sentences) - 1 if len(sentences) > 1 else 0


def ends_with_full_stop(text: str) -> bool:
    return text.strip().endswith('.')


def has_truncation(text: str) -> bool:
    """Detect copy that ends mid-sentence (comma, no full stop)."""
    stripped = text.strip()
    if not stripped:
        return False
    last_char = stripped[-1]
    return last_char in (',', ';', '-', '–', '…', 'and', 'or', 'to', 'with', 'for')


def count_tgg(text: str) -> int:
    return text.lower().count('the good guys')


def check_hard_bans(text: str) -> list:
    """Return list of hard-banned phrases found."""
    lower = text.lower()
    found = []
    for ban in HARD_BANS:
        if ban in lower:
            found.append(ban)
    return found


def check_brand_bans(text: str) -> list:
    """Return list of brand-page-banned phrases found."""
    lower = text.lower()
    found = []
    for ban in BRAND_BANS:
        # Check as whole word
        if re.search(r'\b' + re.escape(ban) + r'\b', lower):
            found.append(ban)
    return found


def check_generic_phrases(text: str) -> list:
    """Return list of generic phrases with no entity value."""
    lower = text.lower()
    found = []
    for phrase in GENERIC_PHRASES:
        if phrase in lower:
            found.append(phrase)
    return found


def get_s1(text: str) -> str:
    """Extract S1 (first sentence)."""
    match = re.split(r'(?<=[a-zA-Z0-9\'\"])\.\s+', text)
    return match[0] if match else text


def get_s2(text: str) -> str:
    """Extract S2 (second sentence)."""
    match = re.split(r'(?<=[a-zA-Z0-9\'\"])\.\s+', text)
    return match[1] if len(match) > 1 else ''


# ── Main audit ───────────────────────────────────────────────────────────────

def audit(input_file: str) -> dict:
    results = {
        'total': 0,
        'pass': 0,
        'fail': 0,
        'violations': [],
        'char_stats': {'min': 999, 'max': 0, 'sum': 0},
        'flag_counts': {},
        'opener_counts': {},
    }

    with open(input_file, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        results['total'] += 1
        url = row.get('URL', row.get('url', ''))
        page_type = row.get('Page_Type', row.get('page_type', ''))
        copy = row.get('Copy', row.get('copy', ''))
        chars_str = row.get('Chars', row.get('chars', ''))

        flags = []

        # Skip already-failed rows if Status column present
        # (we still count them in total but don't double-flag)

        # 1. Character count
        try:
            chars = int(chars_str) if chars_str else len(copy)
        except ValueError:
            chars = len(copy)

        results['char_stats']['sum'] += chars
        results['char_stats']['min'] = min(results['char_stats']['min'], chars)
        results['char_stats']['max'] = max(results['char_stats']['max'], chars)

        if chars < CHAR_FLOOR:
            flags.append(f'chars_low:{chars}')
        elif chars > CHAR_CEILING:
            flags.append(f'chars_high:{chars}')

        # 2. Sentence count
        sentence_count = count_sentences(copy)
        if sentence_count != 2:
            flags.append(f'sentence_count:{sentence_count}')

        # 3. Full stop check
        if not ends_with_full_stop(copy):
            flags.append('missing_terminal_full_stop')

        # 4. Truncation check
        if has_truncation(copy):
            flags.append('truncated_copy')

        # 5. TGG count
        tgg_count = count_tgg(copy)
        if tgg_count == 0:
            flags.append('missing_tgg')
        elif tgg_count > 1:
            flags.append(f'tgg_repeated:{tgg_count}')

        # 6. Hard bans
        hard_ban_hits = check_hard_bans(copy)
        for hit in hard_ban_hits:
            flags.append(f'hard_ban:{hit}')

        # 7. Brand bans (only for brand pages)
        if is_brand_page(page_type):
            brand_ban_hits = check_brand_bans(copy)
            for hit in brand_ban_hits:
                flags.append(f'brand_ban:{hit}')

        # 8. S1 opener check
        s1 = get_s1(copy).lower().strip()
        for opener in WEAK_S1_OPENERS:
            if s1.startswith(opener):
                flags.append(f's1_opener:{opener.strip()}')

        # 9. Generic phrase check (entity depth signal)
        generic_hits = check_generic_phrases(copy)
        if generic_hits:
            flags.append(f'generic_s1:{"|".join(generic_hits[:2])}')

        # 10. S2 length check (S2 should be shorter than S1)
        s2 = get_s2(copy)
        if s1 and s2 and len(s2) > len(s1):
            flags.append('s2_longer_than_s1')

        # Compile result
        if flags:
            results['fail'] += 1
            results['violations'].append({
                'url': url,
                'page_type': page_type,
                'copy': copy,
                'chars': chars,
                'flags': '|'.join(flags),
            })
            for flag in flags:
                flag_key = flag.split(':')[0]
                results['flag_counts'][flag_key] = results['flag_counts'].get(flag_key, 0) + 1
        else:
            results['pass'] += 1

        # Track S1 opener distribution
        words = s1.split()
        if words:
            opener_word = words[0].rstrip(',.:;')
            results['opener_counts'][opener_word] = results['opener_counts'].get(opener_word, 0) + 1

    if results['total'] > 0:
        results['char_stats']['mean'] = results['char_stats']['sum'] / results['total']

    return results


# ── Output ───────────────────────────────────────────────────────────────────

def print_summary(results: dict, input_file: str):
    total = results['total']
    passed = results['pass']
    failed = results['fail']
    char_stats = results['char_stats']

    print(f"\n{'='*60}")
    print(f"PLP QA Audit — {input_file}")
    print(f"{'='*60}")
    print(f"Total rows:   {total}")
    print(f"PASS:         {passed} ({passed/total*100:.1f}%)" if total else "PASS: 0")
    print(f"FAIL:         {failed} ({failed/total*100:.1f}%)" if total else "FAIL: 0")
    print(f"\nChar range:   {char_stats['min']}–{char_stats['max']} (mean: {char_stats.get('mean', 0):.1f})")
    print(f"In range:     {CHAR_FLOOR}–{CHAR_CEILING}")

    if results['flag_counts']:
        print(f"\nViolation breakdown:")
        for flag, count in sorted(results['flag_counts'].items(), key=lambda x: -x[1]):
            print(f"  {flag:<35} {count}")

    # Top S1 openers
    openers = results['opener_counts']
    if openers:
        print(f"\nTop S1 openers:")
        for word, count in sorted(openers.items(), key=lambda x: -x[1])[:10]:
            pct = count / total * 100
            print(f"  {word:<20} {count:>4}  ({pct:.1f}%)")
            if pct > 20:
                print(f"  ⚠️  '{word}' exceeds 20% — variation needed")

    print(f"\n{'='*60}\n")


def write_violations(results: dict, input_file: str):
    if not results['violations']:
        print("No violations to write.")
        return

    today = date.today().strftime('%Y-%m-%d')
    out_path = Path(input_file).parent / f"plp-qa-violations-{today}.csv"

    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['url', 'page_type', 'chars', 'flags', 'copy'])
        writer.writeheader()
        writer.writerows(results['violations'])

    print(f"Violations written to: {out_path}")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 plp-qa-audit.py <input_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not Path(input_file).exists():
        print(f"File not found: {input_file}")
        sys.exit(1)

    results = audit(input_file)
    print_summary(results, input_file)
    write_violations(results, input_file)
