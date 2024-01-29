num = int(input("Enter a number: "))
factors = [] # Store

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("Factors of", num, "are:", factors)
