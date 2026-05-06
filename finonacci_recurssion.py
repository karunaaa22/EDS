def fibonacci(n):
    if n <= 0:
        return "Number of terms must be positive"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
