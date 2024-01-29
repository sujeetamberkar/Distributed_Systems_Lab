import numpy as np

array_from_list = np.array([1, 2, 3, 4, 5], dtype=float)

array_from_tuple = np.array((1, 2, 3, 4, 5))

zeros_array = np.zeros((3, 4))

sequence_array = np.arange(0, 21, 5)

original_array = np.arange(12).reshape((3, 4))
reshaped_array = original_array.reshape((2, 2, 3))

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# Maximum and minimum element of the entire array
max_element = np.max(array)
min_element = np.min(array)

# Row-wise maximum and minimum
row_max = np.max(array, axis=1)
row_min = np.min(array, axis=1)

# Column-wise maximum and minimum
column_max = np.max(array, axis=0)
column_min = np.min(array, axis=0)

# Sum of all elements in the array
array_sum = np.sum(array)

# Print the results
print("a) Array from list:", array_from_list)
print("b) Array from tuple:", array_from_tuple)
print("c) Zeros array (3x4):", zeros_array)
print("d) Sequence array:", sequence_array)
print("e) Reshaped array (2x2x3):\n", reshaped_array)
print("f) Maximum element:", max_element)
print("f) Minimum element:", min_element)
print("f) Row-wise maximum:", row_max)
print("f) Row-wise minimum:", row_min)
print("f) Column-wise maximum:", column_max)
print("f) Column-wise minimum:", column_min)
print("f) Sum of elements:", array_sum)
