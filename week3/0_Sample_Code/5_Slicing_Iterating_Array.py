import numpy as np 
# Indexing, Slicing & Iterating Array

a = np.arange(10)**3
print(a) # Print a
    
print(a[2:5]) # Print 2nd ,3rd ,4th ,5th 

print(a[0:6:2]) # Print (2n)th element
# i = 0,2,4

b = np.array([[ 0, 1, 2, 3],[10, 11, 12, 13],[20, 21, 22, 23],[30, 31, 32, 33],[40, 41, 42, 43]])
print(b)
print(b[2,3]) # (Row,Column)

# Print Entire Column 
print(b[0:5,3])
print(b[-1,:]) # will fetch last row
print(b[:,-1]) # will fetch last col


for element in b.flat:
    print(element) # Will show the element in 1-D Array 

b= b.ravel() # Returns a flatened Array
print(b)

B1 = b.reshape(4,5)
print(B1)


print("Stacking Array together")
#Stacking together different arrays
A1=np.array([(3,4,5),(12,6,1)])
A2=np.array([(1,2,6),(-4,3,8)])
D1=np.vstack((A1,A2))
D2=np.hstack((A1,A2))
print("A1\n",A1)
print("A2\n",A2)
print("D1\n",D1)

# Stacking 1-D array into 2-D array (column wise)
a = np.array([4,2])
b = np.array([3,8])
var = np.column_stack((a,b)) # returns a 2D array
var2 = np.hstack((a,b))
var3 = np.hstack((a[:, np.newaxis], b[:, np.newaxis]))

# Print the result
print(var)
print(var2)
print(var3)
