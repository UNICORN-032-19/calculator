from datetime import datetime


class Person(object):
    last_name = ""
    birthdate = False
    faculty = ""

    def __init__(self, last_name, birthdate, faculty):
        self.last_name = last_name
        self.birthdate = birthdate
        self.faculty = faculty
        self.convert_birthdate()

    def convert_birthdate(self):
        self.birthdate = datetime.strptime(self.birthdate, "%d/%m/%Y")

    @property
    def age(self):
        return int(str((datetime.utcnow() - self.birthdate).days / 365).split(".")[0])


class Matriculant(Person):
    def __str__(self):
        return f"Абитуриент(Фамилия: {self.last_name}, Возраст: {self.age})"

    def __repr__(self):
        return f"Matriculant(Фамилия: {self.last_name}, Возраст: {self.age})"


class Student(Person):
    course = ""

    def __init__(self, last_name, birthdate, faculty, course):
        super().__init__(last_name, birthdate, faculty)
        self.course = course

    def __str__(self):
        return f"Студент({self.last_name}, {self.age}, {self.course})"

    def __repr__(self):
        return f"Student({self.last_name}, {self.age}, {self.course})"

class Teacher(Person):
    position = ""
    experience = ""

    def __init__(self, last_name, birthdate, faculty, position, experience):
        super().__init__(last_name, birthdate, faculty)
        self.position = position
        self.experience = experience

    def __str__(self):
        return f"Преподаватель({self.last_name}, {self.age}, {self.position}, {self.experience})"

    def __repr__(self):
        return f"Teacher({self.last_name}, {self.age}, {self.position}, {self.experience})"

persons = [
    Matriculant("Шепилов", "01/01/1999", "ФИТУ"),
    Matriculant("Иванов", "01/01/1999", "ФИТУ"),
    Student("Петров", "02/11/1996", "ФИТУ", "2"),
    Student("Сидоров", "02/11/1997", "ФИТУ", "2"),
    Student("Антонов", "02/11/1995", "ФИТУ", "2"),
    Teacher("Ульянов", "22/05/1965", "ФИТУ", "КТН", "20"),
]
print(persons)
import pdb; pdb.set_trace()