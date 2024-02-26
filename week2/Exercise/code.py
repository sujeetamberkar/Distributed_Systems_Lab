def matrix_multiply(A, B):
    # Number of rows in A
    rows_A = len(A)
    # Number of cols in A / Rows in B
    cols_A = len(A[0])
    # Number of cols in B
    cols_B = len(B[0])

    # Initialize result matrix C with zeros
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Example usage:
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

result = matrix_multiply(A, B)
print("Resultant Matrix:")
for row in result:
    print(row)
