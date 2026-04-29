from student_functions import add_student,view_students,filter_by_department
from course_functions import add_course,view_courses
from enrollment_functions import enroll_student

def menu():
    while True:
        print(\n1. Add Student)
        print("2. View Studnets by Department")
        print("3. Add Course")
        print("4. Enroll Student")
        print("5. Exit")

        choice=input("Enter your choice: ").strip()
        if choice=="1":
            try:
                student_id=int(input("Enter Student ID: "))
                name=input("Enter Name: ")
                age=int(input("Enter Age: "))
                department=input("Enter Department: ")
                add_student(student_id,name,age,department)
                print(f"Student {name} added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice=="2":
            try:
                dept=input("Enter Department name: ")
                result=filter_by_department(dept)
                for s in result:
                    