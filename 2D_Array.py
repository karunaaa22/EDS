import numpy as np

# Get the number of rows and columns from the user
rows, cols = map(int, input().split())
elements = []

# Collect elements for each row
for _ in range(rows):
    elements.extend(map(int, input().split()))

# Convert the list to a NumPy array and reshape it to (rows, cols)
arr = np.array(elements).reshape(rows, cols)

# Print the array and its properties
print(arr)         # The 2D array itself
print(arr.ndim)    # Number of dimensions (will be 2)
print(arr.shape)   # Shape of the array (rows, cols)
print(arr.size)    # Total number of elements (rows * cols)
