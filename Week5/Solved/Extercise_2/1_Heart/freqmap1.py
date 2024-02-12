from __future__ import print_function
import sys
import csv

# input comes from STDIN (standard input)
reader = csv.reader(sys.stdin)
headers = next(reader)  # Assume the first row is headers

for row in reader:
    for header, value in zip(headers, row):
        # Output column name and value with a count of 1
        print('%s:%s\t%d' % (header, value, 1))
