class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade_hw(self):
        for course, grades in self.grades.items():
            return f'{round(sum(grades) / len(grades), 1)}'

    def __lt__(self, other):
        return self.avg_grade_hw() < other.avg_grade_hw()

    def __str__(self):
        finished_courses = ', '.join(self.finished_courses)
        courses_in_progress = ', '.join(self.courses_in_progress)
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade_hw()} \nКурсы в процессе изучения: {courses_in_progress} \nЗавершенные курсы: {finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        for course, grades in self.grades.items():
            return f'{round(sum(grades) / len(grades), 1)}'

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

student1 = Student('Jim', 'Carrey', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Какой-то курс']

student2 = Student('Jack', 'Nicholson', 'male')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Какой-то курс']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'Git']

lecturer1 = Lecturer('Kelly', 'Brown')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Jack', 'Black')
lecturer2.courses_attached += ['Python', 'Git']

rev1 = Reviewer('John', 'Smith')
rev1.courses_attached += ['Python', 'Git']

rev2 = Reviewer('Jane', 'Doe')
rev2.courses_attached += ['Python', 'Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

rev1.rate_hw(student1, 'Python', 10)
rev1.rate_hw(student1, 'Python', 7)
rev1.rate_hw(student1, 'Python', 8)

rev2.rate_hw(student2, 'Python', 9)
rev2.rate_hw(student2, 'Python', 9)
rev2.rate_hw(student2, 'Python', 9)

best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 6)
student1.rate_lecturer(lecturer1, 'Python', 8)

student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)

print(cool_mentor)
print(best_student)
print(cool_lecturer)
print(student2 > student1)
print(lecturer1 < lecturer2)
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(rev1)
print(rev2)

students_list = [student1, student2, best_student]


def avg_grade_all_stud(students_list, course):
    for student in students_list:
        if course in student.grades:
            return f'{round(sum(student.grades[course]) / len(student.grades[course]), 1)}'
        else:
            return 'Ошибка'


print(avg_grade_all_stud(students_list, 'Python'))

lecturers_list = [cool_lecturer, lecturer1, lecturer2]


def avg_grade_all_lect(lecturers_list, course):
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            return f'{round(sum(lecturer.grades[course]) / len(lecturer.grades[course]), 1)}'
        else:
            return 'Ошибка'

print(avg_grade_all_lect(lecturers_list, 'Python'))