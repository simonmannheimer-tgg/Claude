#!/usr/bin/env python3

import sys
import csv
import urllib.request
import urllib.error
from pathlib import Path

def check_status(url, timeout=10):
    """Check HTTP status code for URL. Returns status or 'ERROR'."""
    if not url or url.strip() == 'Loading...':
        return 'N/A'
    
    url = url.strip().strip('"')
    
    try:
        request = urllib.request.Request(url, method='HEAD')
        response = urllib.request.urlopen(request, timeout=timeout)
        return response.status
    except urllib.error.HTTPError as e:
        return e.code
    except (urllib.error.URLError, TimeoutError, Exception):
        return 'ERROR'

def main():
    if len(sys.argv) < 2:
        print("Usage: python check-status.py <csv_file_path>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    if not Path(csv_file).exists():
        print(f"Error: File not found: {csv_file}")
        sys.exit(1)
    
    print(f"Reading: {csv_file}")
    
    rows = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)
    
    if len(rows) < 2:
        print("Error: CSV must have header + at least 1 data row")
        sys.exit(1)
    
    header = rows[0]
    print(f"Columns: {header}\n")
    
    # Ensure we have at least 4 columns (A, B, C, D)
    if len(header) < 2:
        print("Error: CSV must have at least 2 columns (A, B)")
        sys.exit(1)
    
    # Pad header to 4 columns if needed
    while len(header) < 4:
        header.append(f'Column {chr(65 + len(header))}')
    
    # Update header if columns C and D don't exist
    if len(header) > 2:
        header[2] = f'{header[0]} Status'
    if len(header) > 3:
        header[3] = f'{header[1]} Status'
    
    # Process rows
    total = len(rows) - 1
    for idx, row in enumerate(rows[1:], 1):
        # Ensure row has at least 4 columns
        while len(row) < 4:
            row.append('')
        
        url_a = row[0]
        url_b = row[1] if len(row) > 1 else ''
        
        # Check status for column A
        if url_a and url_a.strip() != 'Loading...':
            status_a = check_status(url_a)
            row[2] = status_a
            print(f"[{idx}/{total}] Col A: {url_a[:70]:<70} → {status_a}")
        else:
            row[2] = 'N/A'
        
        # Check status for column B
        if url_b and url_b.strip() != 'Loading...':
            status_b = check_status(url_b)
            row[3] = status_b
            print(f"[{idx}/{total}] Col B: {url_b[:70]:<70} → {status_b}")
        else:
            row[3] = 'N/A'
    
    # Update first row with new header
    rows[0] = header
    
    # Write output
    output_file = csv_file.replace('.csv', '_with_status.csv')
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"\n✓ Complete. Output saved to:\n  {output_file}")
    except Exception as e:
        print(f"Error writing output: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
