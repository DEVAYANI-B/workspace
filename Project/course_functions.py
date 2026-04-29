courses=[]
def add_course(course_id,name,credits):
    if course_id is None or str(course_id).strip()=="":
        raise ValueError("Course ID cannot be empty.")
    if not name or str(name).strip()=="":
        raise ValueError("Course name cannot be empty.")
    
    if credits is None or not isinstance(credits,int) or credits<=0:
        raise ValueError("Credits must be a positive integer.")
    if any(c["course_id"]==course_id for c in courses):
        raise ValueError(f"Course with ID {course_id} already exists.")
    
    course={
        "course_id":course_id,
        "name": name.strip(),
        "credits":credits
    }
    
    courses.append(course)
def view_courses():
    return courses.copy()
    