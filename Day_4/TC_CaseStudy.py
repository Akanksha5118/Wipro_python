import json
import csv
from abc import ABC, abstractmethod

# ================== DESCRIPTORS ==================

class MarksDescriptor:
    def __set__(self, instance, value):
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Invalid Marks\nError: Marks should be between 0 and 100")
        instance.__dict__['_marks'] = value


class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Unauthorized Salary Access\nAccess Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance.__dict__['_salary'] = value


# ================== DECORATORS ==================

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


# ================== ABSTRACT BASE ==================

class Person(ABC):
    def __init__(self, pid, name, dept):
        self.id = pid
        self.name = name
        self.department = dept

    @abstractmethod
    def get_details(self):
        pass


# ================== STUDENT ==================

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, dept, sem, marks):
        super().__init__(sid, name, dept)
        self.semester = sem
        self.marks = marks
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @log_execution
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        print("Student Performance Report")
        print("--------------------------------")
        print(f"Student Name : {self.name}")
        print(f"Marks        : {self.marks}")
        print(f"Average      : {avg}")
        print(f"Grade        : {grade}")
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


# ================== FACULTY ==================

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")


# ================== COURSE ==================

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


# ================== STORAGE ==================

students = {}
faculty = {}
courses = {}

# ================== MENU ==================

while True:
    try:
        choice = int(input())

        if choice == 1:
            sid = input()
            if sid in students:
                print("Error: Student ID already exists")
                continue
            name = input()
            dept = input()
            sem = int(input())
            marks = list(map(int, input().split()))

            s = Student(sid, name, dept, sem, marks)
            students[sid] = s

            print("Student Created Successfully")
            print("--------------------------------")
            print(f"ID        : {sid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")
            print(f"Semester  : {sem}")

        elif choice == 2:
            fid = input()
            name = input()
            dept = input()
            sal = int(input())

            f = Faculty(fid, name, dept, sal)
            faculty[fid] = f

            print("Faculty Created Successfully")
            print("--------------------------------")
            print(f"ID        : {fid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")

        elif choice == 3:
            code = input()
            cname = input()
            credits = int(input())
            fid = input()

            c = Course(code, cname, credits, faculty[fid])
            courses[code] = c

            print("Course Added Successfully")
            print("--------------------------------")
            print(f"Course Code : {code}")
            print(f"Course Name : {cname}")
            print(f"Credits     : {credits}")
            print(f"Faculty     : {faculty[fid].name}")

        elif choice == 4:
            sid = input()
            code = input()

            students[sid].enroll(courses[code])

            print("Enrollment Successful")
            print("--------------------------------")
            print(f"Student Name : {students[sid].name}")
            print(f"Course       : {courses[code].name}")

        elif choice == 5:
            sid = input()
            students[sid].calculate_performance()

        elif choice == 6:
            s1 = students[input()]
            s2 = students[input()]

            print("Compare Two Students (> operator)")
            print("Comparing Students Performance")
            print("--------------------------------")
            print(f"{s1.name} > {s2.name} : {s1 > s2}")

        elif choice == 7:
            with open("students_report.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
                for s in students.values():
                    avg, grade = s.calculate_performance()
                    writer.writerow([s.id, s.name, s.department, avg, grade])

            with open("students.json", "w") as f:
                json.dump(
                    [{"id": s.id, "name": s.name, "department": s.department} for s in students.values()],
                    f
                )

            print("CSV Report (students_report.csv)")
            print("Student data successfully saved to students.json")

        elif choice == 8:
            print("Thank you for using Smart University Management System")
            break

    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nThank you for using Smart University Management System")
        break
