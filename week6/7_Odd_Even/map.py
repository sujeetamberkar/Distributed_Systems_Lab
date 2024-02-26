# map.py
import sys

def map_function():
    for line in sys.stdin:
        number = int(line.strip())
        if number % 2 == 0:
            print('Even\t1')
        else:
            print('Odd\t1')

if __name__ == "__main__":
    map_function()
