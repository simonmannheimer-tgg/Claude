import csv
import os
from urllib.parse import urlsplit

input_file = r"C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\outlinks.csv"
output_file = r"C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\outlinks_filtered.csv"

def strip_params(url):
    p = urlsplit(url)
    return p._replace(query="", fragment="").geturl()

seen = set()
written = 0

with open(input_file, 'r', encoding='utf-8', newline='') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=["From", "To"])
    writer.writeheader()

    for i, row in enumerate(reader, 1):
        frm = strip_params(row["From"])
        to  = strip_params(row["To"])
        pair = (frm, to)
        if pair not in seen:
            seen.add(pair)
            writer.writerow({"From": frm, "To": to})
            written += 1
        if i % 500_000 == 0:
            print(f"  {i:,} rows processed, {written:,} unique pairs so far...")

size_mb = os.path.getsize(output_file) / (1024 * 1024)
print(f"Done. {written:,} unique page-to-page links.")
print(f"Output: {output_file}  ({size_mb:.2f} MB)")
