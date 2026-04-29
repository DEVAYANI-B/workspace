courses=[]
def add_course(course_id,name,credits):
    if course_id is None or str(course_id).strip()=="":
        raise ValueError("Course ID cannot be empty.")
    if not name or str(name).strip()=="":
        raise ValueError("Course name cannot be empty.")
    
    if credits is None or not isinstance(credits,int) or credits<=0:
        raise ValueError("Credits must be a positive integer.")
    
    course={
        "course_id":course_id,
        "name": name.strip(),
        "credits":credits
    }
    
    courses.append(course)
def view_courses():
    return courses.copy()
    