import math
import os

MAX_BYTES = 30 * 1024 * 1024  # 30 MB

input_file = input("Enter the path to the CSV file: ").strip().strip('"')

if not os.path.isfile(input_file):
    print(f"File not found: {input_file}")
    exit(1)

file_size = os.path.getsize(input_file)
file_size_mb = file_size / (1024 * 1024)
print(f"File size: {file_size_mb:.2f} MB")

num_splits = math.ceil(file_size / MAX_BYTES)
print(f"Splitting into {num_splits} file(s) to keep each under 30 MB...")

base_name = os.path.splitext(os.path.basename(input_file))[0]
output_dir = os.path.dirname(input_file)

with open(input_file, 'r', encoding='utf-8', newline='') as f:
    total_rows = sum(1 for _ in f) - 1

rows_per_file = math.ceil(total_rows / num_splits)

with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    header = infile.readline()

    file_count = 1
    row_count = 0

    out_path = os.path.join(output_dir, f"{base_name}_split_{file_count}.csv")
    outfile = open(out_path, 'w', encoding='utf-8', newline='')
    outfile.write(header)

    for line in infile:
        if row_count >= rows_per_file and file_count < num_splits:
            outfile.close()
            file_count += 1
            out_path = os.path.join(output_dir, f"{base_name}_split_{file_count}.csv")
            outfile = open(out_path, 'w', encoding='utf-8', newline='')
            outfile.write(header)
            row_count = 0

        outfile.write(line)
        row_count += 1

    outfile.close()

print(f"Done. Created {file_count} file(s) in: {output_dir}")
