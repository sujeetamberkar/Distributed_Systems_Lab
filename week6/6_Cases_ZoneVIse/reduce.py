# reduce.py
import sys

def reduce_function():
    current_max = 0
    current_country = None
    for line in sys.stdin:
        # Split the line into country/region and confirmed cases
        country, confirmed = line.strip().split('\t')
        confirmed = int(confirmed)  # Convert confirmed cases to integer
        # If this is the same country as the previous one
        if country == current_country:
            # Update the max if this entry has more confirmed cases
            if confirmed > current_max:
                current_max = confirmed
        else:
            # If this is a new country, print the previous country's max confirmed cases
            if current_country is not None:
                print(f"{current_country}\t{current_max}")
            current_country = country
            current_max = confirmed
    # Don't forget to print the last country's max confirmed cases
    print(f"{current_country}\t{current_max}")

if __name__ == "__main__":
    reduce_function()
