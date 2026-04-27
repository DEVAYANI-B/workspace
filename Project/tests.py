import unittest
import os
from unittest.mock import patch
import builtins


class TestStudentCourseSystem(unittest.TestCase):

    # ---------- Day 1: Add Students ----------
    def test_day1_add_student_case1(self):
        try:
            from student_functions import add_student, students
        except ImportError:
            self.skipTest("Day 1 not implemented yet")
        students.clear()
        add_student(1, "Alice", 20, "CS")
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Alice")

    def test_day1_add_student_case2(self):
        try:
            from student_functions import add_student, students
        except ImportError:
            self.skipTest("Day 1 not implemented yet")
        add_student(2, "Bob", 21, "EE")
        self.assertEqual(len(students), 2)
        self.assertEqual(students[1]['department'], "EE")

    def test_day1_add_student_case3(self):
        try:
            from student_functions import add_student
        except ImportError:
            self.skipTest("Day 1 not implemented yet")
        with self.assertRaises(ValueError):
            add_student(None, "", 18, "ME")  # invalid input

    # ---------- Day 2: View / Filter Students ----------
    def test_day2_view_students_case1(self):
        try:
            from student_functions import filter_by_department
        except ImportError:
            self.skipTest("Day 2 not implemented yet")
        cs_students = filter_by_department("CS")
        self.assertEqual(len(cs_students), 1)
        self.assertEqual(cs_students[0]['name'], "Alice")

    def test_day2_view_students_case2(self):
        try:
            from student_functions import filter_by_department
        except ImportError:
            self.skipTest("Day 2 not implemented yet")
        ee_students = filter_by_department("EE")
        self.assertEqual(len(ee_students), 1)
        self.assertEqual(ee_students[0]['name'], "Bob")


    # ---------- Day 3: Add Courses ----------
    def test_day3_add_course_case1(self):
        try:
            from course_functions import add_course, courses
        except ImportError:
            self.skipTest("Day 3 not implemented yet")
        courses.clear()
        add_course(101, "Maths", 4)
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0]['name'], "Maths")

    def test_day3_add_course_case2(self):
        try:
            from course_functions import add_course, courses
        except ImportError:
            self.skipTest("Day 3 not implemented yet")
        add_course(102, "Physics", 3)
        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[1]['credits'], 3)

    def test_day3_add_course_case3(self):
        try:
            from course_functions import add_course
        except ImportError:
            self.skipTest("Day 3 not implemented yet")
        with self.assertRaises(ValueError):
            add_course(None, "", 0)

    # ---------- Day 4: Enroll Students ----------
    def test_day4_enroll_student_case1(self):
        try:
            from enrollment_functions import enroll_student, enrollments
        except ImportError:
            self.skipTest("Day 4 not implemented yet")
        enrollments.clear()
        enroll_student(1, 101)
        self.assertEqual(len(enrollments), 1)
        self.assertEqual(enrollments[0]['student_id'], 1)

    def test_day4_enroll_student_case2(self):
        try:
            from enrollment_functions import enroll_student, enrollments
        except ImportError:
            self.skipTest("Day 4 not implemented yet")
        enroll_student(2, 102)
        self.assertEqual(len(enrollments), 2)
        self.assertEqual(enrollments[1]['course_id'], 102)

    def test_day4_enroll_student_case3(self):
        try:
            from enrollment_functions import enroll_student
        except ImportError:
            self.skipTest("Day 4 not implemented yet")
        with self.assertRaises(ValueError):
            enroll_student(99, 101)

    # ---------- Day 5: OOP Student & Course Classes ----------
    def test_day5_student_course_objects_case1(self):
        try:
            from models import Student, Course
        except ImportError:
            self.skipTest("Day 5 not implemented yet")
        s = Student(3, "Charlie", 22, "ME")
        c = Course(103, "Chemistry", 4)
        self.assertEqual(s.name, "Charlie")
        self.assertEqual(c.name, "Chemistry")

    def test_day5_student_course_objects_case2(self):
        try:
            from models import Student
        except ImportError:
            self.skipTest("Day 5 not implemented yet")
        s = Student(4, "Daisy", 21, "CS")
        self.assertEqual(s.get_info(), "ID:4, Name:Daisy, Age:21, Department:CS")

    def test_day5_student_course_objects_case3(self):
        try:
            from models import Course
        except ImportError:
            self.skipTest("Day 5 not implemented yet")
        c = Course(104, "Biology", 3)
        self.assertEqual(str(c), "Course(ID:104, Name:Biology, Credits:3)")

    # ---------- Day 6: Enrollment Class ----------
    def test_day6_enrollment_case1(self):
        try:
            from models import Enrollment, Student, Course
        except ImportError:
            self.skipTest("Day 6 not implemented yet")
        s = Student(5, "Eve", 23, "EE")
        c = Course(105, "Electronics", 4)
        e = Enrollment(s, c)
        self.assertEqual(e.student.name, "Eve")
        self.assertEqual(e.course.name, "Electronics")

    def test_day6_enrollment_case2(self):
        try:
            from models import Enrollment, Student, Course
        except ImportError:
            self.skipTest("Day 6 not implemented yet")
        s = Student(6, "Frank", 22, "ME")
        c = Course(106, "Maths", 3)
        e = Enrollment(s, c)
        self.assertEqual(e.get_info(), "Student: Frank, Course: Maths")

    def test_day6_enrollment_case3(self):
        try:
            from models import Enrollment, Student, Course
        except ImportError:
            self.skipTest("Day 6 not implemented yet")
        s = Student(7, "Grace", 21, "CS")
        c = Course(107, "Physics", 4)
        e = Enrollment(s, c)
        self.assertEqual(str(e), "Enrollment(Student: Grace, Course: Physics)")

    # ---------- Day 7: Polymorphism ----------
    def test_day7_polymorphism_case1(self):
        try:
            from models import Student, Course, Enrollment
        except ImportError:
            self.skipTest("Day 7 not implemented yet")
        s = Student(8, "Hank", 20, "EE")
        c = Course(108, "Chemistry", 4)
        e = Enrollment(s, c)
        self.assertEqual(e.get_info(), "Student: Hank, Course: Chemistry")

    def test_day7_polymorphism_case2(self):
        try:
            from models import Student
        except ImportError:
            self.skipTest("Day 7 not implemented yet")
        s = Student(9, "Ivy", 21, "ME")
        self.assertEqual(s.get_info(), "ID:9, Name:Ivy, Age:21, Department:ME")

    def test_day7_polymorphism_case3(self):
        try:
            from models import Course
        except ImportError:
            self.skipTest("Day 7 not implemented yet")
        c = Course(109, "Biology", 3)
        self.assertEqual(c.get_info(), "Course: Biology, Credits:3")


    def test_day8_add_student_flow(self):
        try:
            from main import menu
        except ImportError:
            self.skipTest("Day 8 main.py not implemented yet")

        inputs = ["1", "10", "Jack", "22", "CS", "5"]  # Add student then exit
        with patch.object(builtins, "input", side_effect=inputs):
            with patch("builtins.print") as mocked_print:
                menu()
                # Check success message printed
                mocked_print.assert_any_call("Student Jack added successfully.")

    def test_day8_view_students_flow(self):
        try:
            from main import menu
            from student_functions import add_student, students
        except ImportError:
            self.skipTest("Day 8 main.py not implemented yet")

        students.clear()
        add_student(11, "Jill", 21, "EE")

        inputs = ["2", "EE", "5"]  # View EE students then exit
        with patch.object(builtins, "input", side_effect=inputs):
            with patch("builtins.print") as mocked_print:
                menu()
                mocked_print.assert_any_call("ID:11, Name:Jill, Age:21, Dept:EE")


    def test_day8_exit_menu(self):
        try:
            from main import menu
        except ImportError:
            self.skipTest("Day 8 main.py not implemented yet")

        inputs = ["5"]  # Exit immediately
        with patch.object(builtins, "input", side_effect=inputs):
            with patch("builtins.print") as mocked_print:
                menu()
                mocked_print.assert_any_call("Exiting the menu. Goodbye!")

    def test_day9_add_course_flow(self):
        try:
            from main import menu
        except ImportError:
            self.skipTest("Day 8 main.py not implemented yet")

        inputs = ["3", "201", "Algorithms", "4", "5"]  # Add course then exit
        with patch.object(builtins, "input", side_effect=inputs):
            with patch("builtins.print") as mocked_print:
                menu()
                mocked_print.assert_any_call("Course Algorithms added successfully.")

    def test_day9_enroll_student_flow(self):
        try:
            from main import menu
            from student_functions import add_student, students
            from course_functions import add_course, courses
        except ImportError:
            self.skipTest("Day 8 main.py not implemented yet")

        students.clear()
        courses.clear()
        add_student(12, "Leo", 23, "ME")
        add_course(301, "Physics", 3)

        inputs = ["4", "12", "301", "5"]  # Enroll student then exit
        with patch.object(builtins, "input", side_effect=inputs):
            with patch("builtins.print") as mocked_print:
                menu()
                mocked_print.assert_any_call("Student 12 enrolled in course 301.")




    # ---------- Day 10: Custom Exception for Department ----------

    def test_day10_filter_nonexistent_department(self):
        from student_functions import filter_by_department, students
        from exceptions import DepartmentNotFoundError
        students.clear()
        with self.assertRaises(DepartmentNotFoundError):
            filter_by_department("ME")


    # ---------- Day 11: JSON Persistence ----------
    def test_day11_save_load_case1(self):
        try:
            from student_functions import students, save_to_file, load_from_file
        except ImportError:
            self.skipTest("Day 11 not implemented yet")
        students.clear()
        students.append({'id':1,'name':'Alice','age':20,'department':'CS'})
        save_to_file('students.json', students)
        self.assertTrue(os.path.exists('students.json'))
        loaded = load_from_file('students.json')
        self.assertEqual(loaded[0]['name'], 'Alice')
        os.remove('students.json')

    def test_day11_save_load_case2(self):
        try:
            from student_functions import students, save_to_file, load_from_file
        except ImportError:
            self.skipTest("Day 11 not implemented yet")
        students.clear()
        students.append({'id':2,'name':'Bob','age':21,'department':'EE'})
        save_to_file('students.json', students)
        loaded = load_from_file('students.json')
        self.assertEqual(loaded[0]['department'], 'EE')
        os.remove('students.json')

    def test_day11_save_load_case3(self):
        try:
            from student_functions import save_to_file
        except ImportError:
            self.skipTest("Day 11 not implemented yet")
        with self.assertRaises(TypeError):
            save_to_file('students.json', set())  # cannot serialize set

    def test_day12_db_connection_string(self):
        try:
            from db_functions import get_connection
        except ImportError:
            self.skipTest("Day 12 not implemented yet")

        expected_conn_str = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost,1433;'
            'DATABASE=appdb;'
            'UID=sa;'
            'PWD=examlyMssql@123'
        )

        with patch("pyodbc.connect") as mock_connect:
            get_connection()
            mock_connect.assert_called_once_with(expected_conn_str)

    def test_day12_tables_exist(self):
        try:
            from db_functions import get_connection
        except ImportError:
            self.skipTest("Day 12 not implemented yet")
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check students table
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='students'")
        self.assertIsNotNone(cursor.fetchone())
        
        # Check courses table
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='courses'")
        self.assertIsNotNone(cursor.fetchone())
        
        # Check enrollments table
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='enrollments'")
        self.assertIsNotNone(cursor.fetchone())
        
        conn.close()

    def test_day13_insert_student(self):
        try:
            from db_functions import insert_student, fetch_student, get_connection
        except ImportError:
            self.skipTest("Day 13 not implemented yet")
        
        # Insert student
        insert_student(1001, "Alice", 20, "CS")
        student = fetch_student(1001)
        self.assertIsNotNone(student)
        self.assertEqual(student['name'], "Alice")

    def test_day13_update_student(self):
        try:
            from db_functions import update_student, fetch_student
        except ImportError:
            self.skipTest("Day 13 not implemented yet")
        
        # Update student
        update_student(1001, name="Alicia", age=21)
        student = fetch_student(1001)
        self.assertEqual(student['name'], "Alicia")
        self.assertEqual(student['age'], 21)

    def test_day13_delete_student(self):
        try:
            from db_functions import delete_student, fetch_student
        except ImportError:
            self.skipTest("Day 13 not implemented yet")
        
        # Delete student
        delete_student(1001)
        student = fetch_student(1001)
        self.assertIsNone(student)



if __name__ == "__main__":
    unittest.main()
