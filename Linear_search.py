
def liner_search(list,n):
#for loop for finding
    for i in list:
        if i == n:
            return i
        
    

list=[55,77,78,98,95] #creating list
n = int(input("Enter no. to be searched: "))#input by user

result = liner_search(list,n)
print(result)
if result != n :
    print("Element Not Found")




        
        
