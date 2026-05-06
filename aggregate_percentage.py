def cal(marks, total_courses):
    if any(mark < 40 for mark in marks):
        return "Fail"
    
    total_marks = sum(marks)
    aggregate_percentage = (total_marks / (total_courses * 100)) * 100
    
    if aggregate_percentage > 75:
        grade = "Distinction"
    elif aggregate_percentage >= 60:
        grade = "First Division"
    elif aggregate_percentage >= 50:
        grade = "Second Division"
    elif aggregate_percentage >= 40:
        grade = "Third Division"
    
    return aggregate_percentage, grade


total_courses = int(input())
marks = list(map(int, input().split()))

result = cal(marks, total_courses)

if result == "Fail":
    print("Fail")
else:
    percentage, grade = result
    print(f"{percentage:.2f}")
    print(grade)
