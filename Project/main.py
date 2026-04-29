from student_functions import add_student,view_students,filter_by_department
from course_functions import add_course,view_courses
from enrollment_functions import enroll_student

def menu():
    while True:
        print("\n1. Add Student")
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
                    print(f"ID:{s['student_id']}, Name:{s['name']}, Age:{s['age']}, Dept:{s['department']}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice=="3":
            try:
                course_id=int(input("Enter Course ID: "))
                name=input("Enter Course Name: ")
                credits = int(input("Enter Credits: "))
                add_course(course_id, name, credits)
                print(f"Course {name} added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice=="4":
            try:
                student_id=int(input("Enter Student ID: "))
                course_id=int(input("Enter Course ID: "))
                enroll_student(student_id,course_id)
                print(f"Student {student_id} enrolled in course {course_id}.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice=="5":
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    menu()