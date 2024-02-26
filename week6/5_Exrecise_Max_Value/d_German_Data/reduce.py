# reduce.py
import sys

def reduce_function():
    max_var = -1  # Initialize max_age with a value that will be lower than any age
    for line in sys.stdin:
        var = float(line.strip())  # Convert age from string to integer
        if var > max_var:
            max_var = var
    print(f"Maximum Value: {max_var}")

if __name__ == "__main__":
    reduce_function()
