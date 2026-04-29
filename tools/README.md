# Tools

Local Python scripts for Windows/PowerShell or macOS. Not run in GitHub Actions.

## Usage

Run from repo root:
```powershell
python tools/tgg_plp_auditor.py
python tools/check_status.py input.csv
```

## Scripts

| Script | What it does |
|--------|-------------|
| `tgg_plp_auditor.py` | Audits live TGG PLP pages — checks intro copy against 220–250 char rule, banned words, and sentence structure |
| `tgg_transcript_scraper.py` | Extracts YouTube transcripts in bulk from a hardcoded video list |
| `mhtml_parser.py` | Parses browser-saved .mhtml files, extracts text for Claude ingestion |
| `mhtml_transformer.py` | Converts .mhtml → self-contained .ai.html with embedded JSON for AI reading |
| `check_status.py` | Checks HTTP status codes for URLs from a CSV input |
| `merge_and_split.py` | Merges folder of CSVs and splits by count (used for Semrush exports) |
| `split_csv.py` | Splits a large CSV into two halves |

## Note on hardcoded paths

Some scripts have Windows paths hardcoded (e.g. `C:\Users\simonma\OneDrive...`). Update the path variables at the top of each script for your machine. These will be moved to `.env` in a future pass.
