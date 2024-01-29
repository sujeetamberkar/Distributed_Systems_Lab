import numpy as np

# Define a sample matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Transpose the matrix using numpy.transpose()
transposed_matrix_1 = np.transpose(matrix)

# Transpose the matrix using the .T attribute
transposed_matrix_2 = matrix.T

# Print the original and transposed matrices
print("Original Matrix:")
print(matrix)

print("\nTransposed Matrix (Method 1):")
print(transposed_matrix_1)

print("\nTransposed Matrix (Method 2):")
print(transposed_matrix_2)
