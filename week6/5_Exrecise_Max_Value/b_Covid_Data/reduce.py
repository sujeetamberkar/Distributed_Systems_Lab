# reduce.py
import sys

def reduce_function():
    max_age = -1  # Initialize max_age with a value that will be lower than any age
    for line in sys.stdin:
        age = int(line.strip())  # Convert age from string to integer
        if age > max_age:
            max_age = age
    print(f"Maximum age: {max_age}")

if __name__ == "__main__":
    reduce_function()
