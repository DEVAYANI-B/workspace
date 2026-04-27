import json

students=[]

def add_student(student_id,name,age,department):
    if student_id is None or str(student_id).strip()=="":
        raise ValueError("Student ID cannot be empty.")
    if not name or str(name).strip()="":
        raise ValueError("Name cannot be empty.")
    if age is None:
        raise ValueError("Age cannot be empty.")
    if not isinstance(age,int) or age<=0:
        raise ValueError("Age must be a positive integer.")
    if not department or str(department).strip()=="":
        raise ValueError("Department cannot be empty.")
    student={
        "student_id":student_id,
        "name":name.strip(),
        "age":age,
        "department":department.strip()
    }
    students.append(student)