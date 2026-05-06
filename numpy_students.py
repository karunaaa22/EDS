import numpy as np

# Matrix A representing marks
A = np.array([
    [85, 90, 78],
    [70, 85, 68],
    [88, 78, 80]
])

# Matrix B representing marks
B = np.array([
    [95, 90, 88],
    [70, 65, 98],
    [78, 98, 80]
])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition of matrices
total = A + B
print("Total Marks:\n", total)

# Subtraction of matrices
improve = B - A
print("Improvement:\n", improve)

# Element-wise multiplication
consistency = A * B
print("Consistency Analysis:\n", consistency)

print("Matrix B", B)

total = A + B
print("Total Marks:\n", total)

improve = B - A
print("Improvement:\n", improve)

consistency = A * B
print("Consistency Analysis:\n", consistency)

performance = np.dot(A, B)
print("Matrix Multiplication:\n", performance)

subject_A = A.T  # Returns the inverse of matrix A
print("Subject wise:\n", subject_A)
