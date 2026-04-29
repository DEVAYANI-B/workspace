import pyodbc

CONNECTION_STRING=(
'DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=localhost,1433;'
'DATABASE = appdb;'
'UID=sa;'
'PWD=examlyMssql@123'
)

def get_connection():
    conn=pyodbc.connect(CONNECTION_STRING)
    _initialize_schema(conn)
    return conn
def _initialize_schema(conn):
    cursor=conn.cursor()
    cursor.execute("""
    IF NOT EXISTS(
    SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='students')
    CREATE TABLE students (
        student_id INT PRIMARY KEY,
        name NVARCHAR(100),
        age INT,
        department NVARCHAR(50)
    )""")
    cursor.execute("""
    IF NOT EXISTS(
    SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='courses')
    CREATE TABLE courses (
        course_id INT PRIMARY KEY,
        name NVARCHAR(100),
        credits INT
    )""")
    cursor.execute("""
    IF NOT EXISTS(
    SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='enrollments')
    CREATE TABLE enrollments (
        student_id INT,
        course_id INT,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id)

    )""")
    conn.commit()
    cursor.close()
def insert_student(student_id,name,age,department):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            "INSERT INTO students(student_id,name,age,department) VALUES (?,?,?,?)",
            (student_id,name,age,department)

        )
        conn.commit()
        cursor.close()
        conn.close()
        except pyodbc.Error as e:
            print(f"Database error: {e}")

def update_student(student_id,name=None,age=None,department=None):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        fields=[]
        values=[]
        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if age is not None:
            fields.append("age = ?")
            values.append(age)
        if department is not None:
            fields.append("department = ?")
            values.append(department)
        if not fields:
            return
        values.append(student_id)
        sql=f"UPDATE students SET {', '.join(fields)} WHERE student_id = ?"
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
    except pyodbc.Error as e:
        print(f"Database error: {e}")
def delete_student(student_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id=?",(student_id,))
        conn.commit()
        cursor.close()
        conn.close()
    except pyodbc.Error as e:
        print(f"Database error: {e}")
def fetch_student(student_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT student_id,name,age,department FROM students WHERE student_id=?",(student_id,))
        row=cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return{
                "student_id": row[0],
                "name": row[1],
                "age": row[2],
                "department" : row[3]

            }
        return None
    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return None