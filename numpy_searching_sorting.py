import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# 1. Searching (indices)
indices = np.where(array1 == search_value)[0]
print(indices)

# 2. Counting
count = np.count_nonzero(array1 == count_value)
print(count)

# 3. Broadcasting (addition)
broadcasted_array = array1 + broadcast_value
print(broadcasted_array)

# 4. Sorting
sorted_array = np.sort(array1)
print(sorted_array)
