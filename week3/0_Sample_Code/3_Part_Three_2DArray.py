# Arrange will create a 1 D array from 0 to upper Limit and then rearrange 
import numpy as np 
a = np.arange(15).reshape(3,5)
print(a)

print(a.size) # Total Number of elements 
print(a.shape) # Dimension of array 
print(a.T) # Transpose 

# 3 D dimensions 
c = np.arange(24).reshape(2,3,4)
print(c)

# Array Operations 
a = np.array([20,30,40,50])
b = np.arange(4)
print(a)
print(b)

# Subtarct ith term of a and b respectively and store it as ith term of C 
c = a-b
print(c)

# Square each element of b and store it in b
b=b**2
print(b)
print(10*np.sin(b))
print(np.sin(1.57079632679)) # Angle is an radian 

print(a<45) # Creates an array after considering the condition


