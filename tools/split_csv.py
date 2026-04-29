import math

input_file = r"C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\outlinks.csv"
output_prefix = "split_half"

# Count total rows (excluding header)
with open(input_file, 'r', encoding='utf-8', newline='') as f:
    total_rows = sum(1 for _ in f) - 1  # minus header

rows_per_file = math.ceil(total_rows / 2)

with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    header = infile.readline()

    file_count = 1
    row_count = 0

    outfile = open(f"{output_prefix}_{file_count}.csv", 'w', encoding='utf-8', newline='')
    outfile.write(header)

    for line in infile:
        if row_count >= rows_per_file:
            outfile.close()
            file_count += 1
            outfile = open(f"{output_prefix}_{file_count}.csv", 'w', encoding='utf-8', newline='')
            outfile.write(header)
            row_count = 0

        outfile.write(line)
        row_count += 1

    outfile.close()

print(f"Done. Created {file_count} files.")