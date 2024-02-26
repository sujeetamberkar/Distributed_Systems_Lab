# code.py
import random

def generate_numbers(n=1000):
    for _ in range(n):
        print(random.randint(1, 10000))  # Generate a random number between 1 and 10000

if __name__ == "__main__":
    generate_numbers()
