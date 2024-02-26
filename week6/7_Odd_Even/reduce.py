# reduce.py
import sys

def reduce_function():
    current_count = 0
    current_key = None
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        if key != current_key:
            if current_key:
                print(f"{current_key}\t{current_count}")
            current_key = key
            current_count = 1
        else:
            current_count += int(value)
    # Don't forget to print the last key
    if current_key:
        print(f"{current_key}\t{current_count}")

if __name__ == "__main__":
    reduce_function()
