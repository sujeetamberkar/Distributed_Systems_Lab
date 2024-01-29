import numpy as np 
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
c = A * B 

print(c) # Multiplication  element wise 
print()


c = A.dot(B) # Dot Product 
print(c)
print()


c = np.cross(A,B) # Cross Product 
print(c)
print()


# Sum 
b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0)) # Entire Coumn 
print(b.sum(axis=1)) # Entire Row 