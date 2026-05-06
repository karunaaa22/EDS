# Python Program to Calculate Aggregate Percentage

def calculate_aggregate():
    try:
        # number of courses
        num_courses = int(input("Enter the number of courses: "))
        if num_courses <= 0:
            print("Number of courses must be greater than 0.")
            return

        #max marks per course (assuming equal weightage)
        max_marks_per_course = float(input("Enter maximum marks per course: "))
        if max_marks_per_course <= 0:
            print("Maximum marks must be greater than 0.")
            return

        total_obtained = 0
        
        #input of marks by user
        for i in range(1, num_courses + 1):
            mark = float(input(f"Enter marks obtained in course {i}: "))
            if 0 <= mark <= max_marks_per_course:
                total_obtained += mark
            else:
                print(f"Invalid marks. Please enter marks between 0 and {max_marks_per_course}.")
                return

     #Aggregate Percentage
        total_max_marks = num_courses * max_marks_per_course
        percentage = (total_obtained / total_max_marks) * 100

        # 5. Output results
        print(f"Total Courses: {num_courses}")
        print(f"Total Marks Obtained: {total_obtained}/{total_max_marks}")
        print(f"Aggregate Percentage: {percentage:.2f}%")

    except ValueError:
        print("Invalid input! Please enter numerical values.")

# Run the function
calculate_aggregate()
