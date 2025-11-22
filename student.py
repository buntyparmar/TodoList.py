# Student Grade Tracker

def calculate_average(marks):  #Finds the average marks
    
    return sum(marks) / len(marks)


def grade_system(avg):    #Gives grade from average
    
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


students = {}  # Dictionary to store student name and marks

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []

    for j in range(3):  # taking 3 subjects
        mark = float(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)

    avg = calculate_average(marks)
    grade = grade_system(avg)
    students[name] = {"Marks": marks, "Average": avg, "Grade": grade}

# Save results to a file
with open("student_grades.txt", "w") as f:    # w is creates a new file or overwrites an old one , as f is file short name for using in block
    for name, info in students.items():
        f.write(f"{name}: {info}\n")

print("\n Grades Saved to 'student_grades.txt' file successfully!\n")

# Display all student details
for name, info in students.items():
    print(f"{name} → Marks: {info['Marks']}, Average: {info['Average']:.2f}, Grade: {info['Grade']}")
