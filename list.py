num=[10, 20, 30, 40, 50, 60]
print("original list:", num)

num.append(70)
print("After Append: ", num)

num.remove(30)
print("After Removing: ", num)

num.insert(2,30)
print("After Inserting: ",num)

print("Length of List: ",len(num))

print("Sorted List: ", num.sort())
