from student_functions import students
from course_functions import courses

enrollments=[]
def enroll_student(student_id,course_id):
    student_exists=any(s["student_id"]==student_id for s in students)
    if not student_exists:
        raise ValueError(f"Student with ID {student_id} does not exist.")
    course_exists=any(c["course_id"]==course_id for c in courses)
    if not course_exists:
        raise ValueError(f"Course with ID {course_id} does not exist.")
    enrollment={
        "student_id":student_id,
        "course_id":course_id
    }
    enrollments.append(enrollment)