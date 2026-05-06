def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter an integer: "))
print("Factorial is:", factorial(num))



n = int(input())
factorial(n)
