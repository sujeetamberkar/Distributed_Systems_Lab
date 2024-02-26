import csv
import sys

# Assuming the 'age' column is at a specific index, e.g., first column index 0
age_index = 0

for row in csv.reader(sys.stdin):
    if len(row) > age_index:
        age = row[age_index]
        # Output the age and a count of 1 for each occurrence
        print(f"{age}\t1")
