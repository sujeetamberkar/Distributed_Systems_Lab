import numpy as np

my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Find the sum of rows (along axis 1)
row_sums = np.sum(my_array, axis=1)

# Find the sum of columns (along axis 0)
column_sums = np.sum(my_array, axis=0)

print("Sum of rows:", row_sums)
print("Sum of columns:", column_sums)
