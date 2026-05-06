def employee_bonus():
    sal=int(input("Enter Salary of Employee: "))
    exp=int(input("Enter Experience of Employee: "))
    per_rat=float(input("Enter Performance Rating of Employee: "))
    if sal>50000 and exp>5 and per_rat>4:
        print("ELIGIBLE FOR 20% BONUS")
        bonus=sal*0.2
        print("Bonus= ", bonus,"\nTOTAL SALARY= ",bonus+sal)
    elif sal> 35000 and exp>3 and per_rat>3:
        print("ELIGIBLE FOR 10% BONUS")
        bonus=sal*0.1
        print("Bonus= ", bonus,"\nTOTAL SALARY= ",bonus+sal)
    else:
        print("NOT ELIGIBLE FOR BONUS")

employee_bonus()
