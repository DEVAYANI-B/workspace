class Student:
    def __init__(self,student_id,name,age,department):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.department=department
        def get_info(self):
            return f"ID:{self.student_id}, Name:{self.name}, Age:{self.age}, Department:{self.department}"
        def __str__(self):
        return f"Student(ID:{self.student_id}, Name:{self.name}, Age:{self.age}, Department:{self.department})"

class Course:
    def __init__(self,course_id,name,credits):
        self.course_id=course_id
        self.name=name
        self.credits=credits
    def get_info(self):
        return f"Course: {self.name}, Credits:{self.credits}"
    def __str__(self):
        return f"Course(ID:{self.course_id}, Name:{self.name}, Credits:{self.credits})"
class Enrollment:
    def __init__(self,student,course):
        self.student=student
        self.course=course
    def get_info(self):
        return f"Student: {self.student.name}, Course: {self.course.name}"
    def __str__(self):
        return f"Enrollment(Student: {self.student.name}, Course: {self.course.name})"
        
