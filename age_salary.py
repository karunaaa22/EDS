
exchange_rate = 90.69

#Take input
try:
    age = str(input("Enter your age: "))
    salary = float(input("Enter your salary in rs.: "))

    #Conversion of salary to dollars
    salary_in_dollars = salary / exchange_rate

    #Display result
    print(f"Age: {age}")
    print(f"Salary in local currency: {salary:.2f}")
    print(f"Salary in USD: ${salary_in_dollars:.2f}")

except ValueError:
    print("Please enter valid numerical values for age and salary.")
