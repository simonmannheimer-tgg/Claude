---
title: CSV URL status checker output location (medium)
parent: Chat/Light/2026-04-21-csv-url-status-checker-output-location-f02941
uuid: f02941b3-b5c0-4071-afdc-678791c2134c
---

#chat/medium #project/main #status/completed

# CSV URL status checker output location — Key User Messages

→ Light view: [[Chat/Light/2026-04-21-csv-url-status-checker-output-location-f02941]]
→ Full transcript: [[Chat/Full/2026-04-21-csv-url-status-checker-output-location-f02941]]

**Total user messages:** 1

---

### Message 1 — 2026-04-21T06:28

```python
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
        print("Error: CSV must have at least

[truncated — see full transcript]
