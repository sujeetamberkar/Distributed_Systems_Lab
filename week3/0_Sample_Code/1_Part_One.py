import numpy as np
# Array Creation


print("#################################################################################")
A = np.array([1,2,3])
print(A)
print(A.dtype)

print("#################################################################################")
B = np.array([2.4,4,12.6])
print(B.dtype)
print(B)

print("#################################################################################")
# Creating a 2 - D Array 
A = np.array([(2,3,4),(1,2,6)])
Z = np.zeros((2,4)) # Create a matrix of dimenion 2 x 4   Rows x Column 
print(A)
print(A.dtype)
print("#################################################################################")
print(Z)
print(Z.dtype)

print("#################################################################################")
# Create Sequence of Data 
S = np.arange(10,30,5) # Upper Limit, Lower Limit, Increment 
print(S)
print("#################################################################################")



# LineSpace 
s1 = np.linspace(0,2,9) 
print(s1)