students=[]

def add student(student_id,name,age,department):
    if student_id is None or str(student_id).strip()=="":
        raise ValueError("Student ID cannot be empty.")
    if not name or str(name).strip()="":
        raise ValueError("Name cannot be empty.")
    if age is None:
        raise ValueError("Age ")