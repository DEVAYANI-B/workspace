courses=[]
def add_course(course_id,name,credits):
    if course_id is None or str(course_id).strip()="":
        raise ValueError("Course ID cannot be empty.")