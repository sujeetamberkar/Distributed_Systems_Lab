import sys

age_counts = {}

for line in sys.stdin:
    age, count = line.strip().split("\t")
    count = int(count)
    
    if age in age_counts:
        age_counts[age] += count
    else:
        age_counts[age] = count

for age, count in age_counts.items():
    print(f"{age}\t{count}")
