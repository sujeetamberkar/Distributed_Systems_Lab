import numpy as np

# Define two sample matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Element-wise product
elementwise_product = matrix1 * matrix2

# Print the original matrices and the products
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nElement-wise Product (Matrix 1 * Matrix 2):")
print(elementwise_product)

