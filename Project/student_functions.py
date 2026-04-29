import json
from exceptions import DepartmentNotFoundError


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

def view_students():
    return students.copy()
def filter_by_department(dept_name):
    result=[s for s in students if s["department"].lower()==dept_name.lower()]
    if not result:
        raise DepartmentNotFoundError(f"No students found in department: {dept_name}")
    return result
def save_to_file(filename,data):
    pass
def load_from_file(filename):
    pass
    