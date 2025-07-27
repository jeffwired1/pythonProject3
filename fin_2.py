import csv

with open("input.csv", newline="") as f:
    lines = f.readlines()

# Split into two header blocks
split_index = None
for i, line in enumerate(lines):
    if line.strip() == "":  # blank line separator
        split_index = i
        break

section1 = lines[:split_index]
section2 = lines[split_index + 1:]  # skip the blank line

# Process Section 1
reader1 = csv.DictReader(section1)
data1 = [row for row in reader1]

# Process Section 2
reader2 = csv.DictReader(section2)
data2 = [row for row in reader2]

print("Section 1:", data1)
print("Section 2:", data2)