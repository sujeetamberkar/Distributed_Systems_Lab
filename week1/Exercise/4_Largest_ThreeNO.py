import numpy as np
x = -np.inf
a = int(input("Enter 1st Number\t"))
b = int(input("Enter 2nd Number\t"))
c = int(input("Enter 3rd Number\t"))

if a > b and b > c:
    x=a
elif b > a and b >c:
    x = b
else :
    x =c

print("The Largest Number is ",x)