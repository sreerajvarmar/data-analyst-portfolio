# Student Performance Analyzer
# Author: Sreeraj Varma

def calculate_grade(marks):
    if marks>=90:
        return 'A+'
    elif marks>=80:
        return 'A'
    elif marks>=70:
        return 'B+'
    elif marks>=60:
        return 'B'
    elif marks>50:
        return 'C+'
    elif marks==50:
        return 'C'
    else:
        return 'Fail'

def main():    
    num_students=int(input("Enter the Number of Students: "))
    
    students={}
    
    for i in range(num_students):
        name=input("Enter Student Name: ")
        marks=float(input("Enter Student Marks: "))
        students[name]=marks
    
    total_marks=sum(students.values())
    average_marks=total_marks/num_students
    top_student=max(students,key=students.get)
    
    print('\n--- Student Performance Summary ---\n')
    
    for name,marks in students.items():
        grade = calculate_grade(marks)
        print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
    
    print(f"\nAverage Marks: {average_marks:.2f}")
    print(f"Top Performer: {top_student} ({students[top_student]} marks)")
if __name__ == "__main__":
    main()
