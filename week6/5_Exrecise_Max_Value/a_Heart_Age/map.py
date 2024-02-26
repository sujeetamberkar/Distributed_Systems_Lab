# map.py
import sys

def map_function():
    # Reading a single line of ages from standard input
    line = sys.stdin.readline()
    unique_ages = set(line.strip().split(' '))  # Convert to set to remove duplicates
    for age in unique_ages:
        print(age)

if __name__ == "__main__":
    map_function()
