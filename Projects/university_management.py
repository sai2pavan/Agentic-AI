import random
import re
from datetime import datetime

email_pattern = r'^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$'


def get_valid_email(prompt="Enter email: "):
    """Validate correct email"""
    while True:
        email = input(prompt).strip()
        if re.match(email_pattern, email):
            return email
        print("Invalid email format. Please try again (e.g. name@example.com).")


class Student:
    """Base Student class"""
    def __init__(self, name, email):
        if not re.match(email_pattern, email):
            print(f"'{email}' is not a valid email.")
            email = get_valid_email(f"Enter a valid email for {name}: ")
        self.name = name
        self.roll_no = None
        self.email = email
        self.course = None
        self._grades = {}

    def attend_exam(self, exam):
        if exam.subject.name in self._grades:
            print("Exam Already Completed")
        else:
            grade = exam.generate_grade()
            self._grades[exam.subject.name] = grade

    def view_schedule(self):
        for subject in self.course.subjects:
            print("Subject:", subject.name)
            print("Faculty:", subject.faculty.name)
            print("Time:", subject.time)
            print("Exam:", subject.exam.name)
            print()

    def view_grades(self):
        print(self._grades)


class UndergraduateStudent(Student):
    """Undergraduate student inherits from Student"""
    def __init__(self, name, email):
        super().__init__(name, email)
        self.level = "Undergraduate"

    def view_schedule(self):
        print(f"Schedule for {self.name}")
        super().view_schedule()


class GraduateStudent(Student):
    """Graduate student inherits from Student"""
    def __init__(self, name, email):
        super().__init__(name, email)
        self.level = "Graduate"

    def view_schedule(self):
        print(f"Schedule for {self.name}")
        super().view_schedule()


class Course:
    """Course class"""
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
        subject.course = self

    def get_roster(self, university):
        """Data abstraction: simplified view of enrolled students"""
        return [
            {"name": s.name, "roll_no": s.roll_no}
            for s in university.students if s.course is self
        ]


class Subject:
    """Subject class"""
    def __init__(self, name):
        hour = random.randint(8, 16)
        minute = random.choice([0, 30])
        time = datetime.strptime(f"{hour}:{minute:02d}", "%H:%M")
        self.time = time.strftime("%I:%M %p")

        self.name = name
        self.exam = None
        self.faculty = None
        self.course = None

    def assign_faculty(self, faculty):
        self.faculty = faculty
        faculty.subject = self
        faculty.course = self.course

    def assign_exam(self, exam):
        self.exam = exam
        exam.subject = self


class Exam:
    """Exam class"""
    def __init__(self, name):
        self.name = name
        self.subject = None

    def generate_grade(self):
        return random.choice(['A', 'B', 'C', 'D', 'E', 'F'])


class Faculty:
    """Faculty class"""
    def __init__(self, name, teacher_id, email):
        if not re.match(email_pattern, email):
            print(f"'{email}' is not a valid email.")
            email = get_valid_email(f"Enter a valid email for {name}: ")
        self.name = name
        self.teacher_id = teacher_id
        self.email = email
        self.course = None
        self.subject = None

    def view_assignment(self):
        print(f"Faculty: {self.name} | Subject: {self.subject.name} | Course: {self.course.name}")

    def view_roster(self, university):
        subject_name = self.subject.name
        print(f"--- Roster for {subject_name} ---")
        for student in university.students:
            grade = student._grades.get(subject_name, "Not attended")
            print(student.name, grade)


class University:
    """University class"""
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        self.faculty = []
        self.next_roll_number = 1

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student, course):
        if student in self.students:
            print("Student already present")
        else:
            roll_no = f"{self.next_roll_number:04d}"
            student.roll_no = roll_no
            student.course = course
            self.students.append(student)
            self.next_roll_number += 1

    def view_subject_grades(self, faculty):
        subject_name = faculty.subject.name
        for student in self.students:
            if subject_name in student._grades:
                print(student.name, student._grades[subject_name])
            else:
                print(student.name, "Not attended")


class Department(University):
    """Department inherits from University"""
    def __init__(self, name, head_of_department):
        super().__init__(name)
        self.head_of_department = head_of_department


course1 = Course('Agentic-Ai')
subject1 = Subject("Python")
exam1 = Exam("Python Exam")
subject1.assign_exam(exam1)

faculty1 = Faculty('rao', 'F0001', 'rao@faculty.edu')

university1 = University("ABC University")
university1.add_course(course1)
course1.add_subject(subject1)
subject1.assign_faculty(faculty1)

student1 = UndergraduateStudent('Pavan', 'pavan@student.edu')
student2 = GraduateStudent('Srujan', 'srujan@student.edu')

university1.enroll_student(student1, course1)
university1.enroll_student(student2, course1)

subject2 = Subject('Advanced Python')
exam2 = Exam('Advanced Python Exam')
subject2.assign_exam(exam2)
course1.add_subject(subject2)

faculty2 = Faculty('Rakesh', 'F0002', 'rakesh@faculty.edu')
subject2.assign_faculty(faculty2)

student1.attend_exam(exam1)
student1.attend_exam(exam2)
student2.attend_exam(exam1)

print("\n=== Grades ===")
student1.view_grades()
student2.view_grades()

print("\n=== Schedules (polymorphic view_schedule) ===")
for student in university1.students:
    student.view_schedule()

print("=== Faculty roster view ===")
faculty1.view_roster(university1)

print("\n=== Course roster (data abstraction) ===")
print(course1.get_roster(university1))

print("\n=== Department (inherits University) ===")
dept = Department("Computer Science Dept", head_of_department="Dr. Meera")
print(dept.name, "-", dept.head_of_department)