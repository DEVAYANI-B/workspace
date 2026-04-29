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
