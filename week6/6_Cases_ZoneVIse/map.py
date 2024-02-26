# map.py
import sys
import csv

def map_function():
    reader = csv.reader(sys.stdin)
    for row in reader:
        if len(row) > 5:  # Ensure the row has enough columns
            country_region = row[3]  # Country/Region column
            confirmed = row[5]  # Confirmed cases column
            print(f"{country_region}\t{confirmed}")

if __name__ == "__main__":
    map_function()
