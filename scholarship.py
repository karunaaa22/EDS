def eligiblity_scholarship():
    marks=int(input("Enter Marks: "))
    attend=int(input("Enter Attendance: "))
    fincome=int(input("Enter Family Income: "))
    if marks>90 and attend>90 and fincome<200000:
        print("FULL SCHOLARSHIP")
    elif marks>75 and attend>75 and fincome<300000:
        print("PARTIAL SCHOLARSHIP")
    else:
        print("NOT ELIGIBLE FOR SCHOLARSHIP")

eligiblity_scholarship()
    
    
