class Student:
    def __init__(self, name, surname, average_grade):
        self.name = name
        self.surname = surname
        self.average_grade = average_grade

    def __str__(self):
        return f"Student: {self.name}{self.surname}, Average Grade: {self.average_grade}"


class StudentGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return


StudentGroupIterator(self.students)


class StudentGroupIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self
