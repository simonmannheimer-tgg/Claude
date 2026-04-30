import os
import math

folder = r"C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\SEMRush Mobile Keyword Exports"

base_file = "thegoodguys.com.au-organic.Positions-mobile-au-20230315-2026-03-27T08_31_04Z.csv"

merged_output = "merged_all.csv"

# -------------------------
# STEP 1: MERGE FILES
# -------------------------

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

# ensure base file is first, then others
files.remove(base_file)
files = [base_file] + files

base_path = os.path.join(folder, base_file)

with open(base_path, "r", encoding="utf-8", newline="") as f:
    header = f.readline()

with open(os.path.join(folder, merged_output), "w", encoding="utf-8", newline="") as out:
    out.write(header)

    for file in files:
        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8", newline="") as f:
            next(f)  # skip header
            for line in f:
                out.write(line)

print("Merged file created:", merged_output)

# -------------------------
# STEP 2: SPLIT MERGED FILE
# -------------------------

merged_path = os.path.join(folder, merged_output)

with open(merged_path, "r", encoding="utf-8", newline="") as f:
    total_rows = sum(1 for _ in f) - 1

half = math.ceil(total_rows / 2)

def split_file(output_name, start_row, end_row):
    with open(merged_path, "r", encoding="utf-8", newline="") as f:
        header = f.readline()

        with open(os.path.join(folder, output_name), "w", encoding="utf-8", newline="") as out:
            out.write(header)

            for i, line in enumerate(f):
                if start_row <= i < end_row:
                    out.write(line)

# first half
split_file("split_1.csv", 0, half)

# second half
split_file("split_2.csv", half, total_rows)

print("Split files created: split_1.csv, split_2.csv")