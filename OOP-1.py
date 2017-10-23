"""
Задача №1
Попробуйте перенести в ОО-код следующий пример из реального мира:
- есть курсы, учителя и ученики
- у каждого курса есть свой учитель
- у каждого учителя есть своя группа учеников
- у каждого ученика есть свой учитель
и т.д.

Определите какие объекты есть в этом примере, какие у них свойства и какие методы, как эти объекты будут между собой взаимодействовать, например, к курсу можно добавить учителя.

Создайте все необходимые классы и приведите пример их использования.
"""

class EnrollmentException(Exception):
    pass

class Person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_info(self):
        print('{} {}'.format(self.fname, self.lname))

class Teacher(Person):
    def __init__(self, fname, lname, courses):
        super().__init__(fname, lname)
        self.courses = sorted(c.get_course_name() for c in courses)

    def print_info(self):
        super().print_info()
        print('Leads following courses: {}'.format(', '.join(self.courses)))
        #print(type(self.courses))

    # def get_students_list(self):
    #     pass

        
class Student(Person):
    all_students = []

    def __init__(self, fname, lname, courses):
        super().__init__(fname, lname)
        self.courses = courses
        self.course_ids = list(c.get_course_id() for c in courses)
        self.course_names = sorted(c.get_course_name() for c in courses)
        self.on_course = False
        self.all_students.append(self)

    def print_info(self):
        super().print_info()
        print('Attends following courses: {}'.format(', '.join(sorted(c.get_course_name() for c in self.courses))))
        #print('Attends: ', self.courses)

    def get_all_students(self):
        return self.all_students

    def enroll_on_course(self, course):
        if not isinstance(course, Course):
            raise EnrollmentException(
                '''No such course found 
                ("{}" is {} type, not "Course")'''.format(course, type(course))
                )
        self.courses.append(course)
        course.enroll_student(self)
        return self.courses

    def send_down_from_course(self, course):
        if not isinstance(course, Course):
            raise EnrollmentException(
                '''No such course found 
                ("{}" is {} type, not "Course")'''.format(course, type(course))
                )
        if not self.is_on_course(course):
            raise EnrollmentException(
                'This student has not been enrolled on course "{}"'.format(course.get_course_name())
                )
        self.courses.remove(course)
        self.on_course = False

    def is_on_course(self, course):
        if course in self.courses:
            self.on_course = True
        else:                   # w/o 'else' block self.on_course keeps True value after the first is_on_course call  
            self.on_course = False # with an argument leading to 'return self.on_course = True'. 
        return self.on_course


class Course(object):
    stud = Student('', '', '')
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students_list = []

    def get_course_id(self):
        return self.course_id

    def get_course_name(self):
        return self.course_name

    def enroll_student(self, student):
        if not isinstance(student, Student):
            raise EnrollmentException(
                '''No such student found 
                ("{}" is {} type, not "Student")'''.format(student, type(student))
                )
        self.students_list.append(student)

    def get_students_list(self):
        for s in self.stud.get_all_students():
            if s.is_on_course(self):
                self.students_list.append(s)
        return self.students_list






course1 = Course(1, 'Anatomy')
course2 = Course(2, 'Chemistry')
course3 = Course(3, 'Calculus')
course4 = Course(4, 'Economics')

tch1 = Teacher('Aaron', 'Chumakeiro', [course3, course4])
stud1 = Student('Olivia', 'Santos', [course2, course3])
stud2 = Student('Araminta', 'Ditch', [course3, course4])



#tch1.print_info()
#stud1.print_info()

stud1.enroll_on_course(course1)
#stud1.print_info()

stud1.send_down_from_course(course1)
stud1.enroll_on_course(course1)
#stud1.send_down_from_course(course2)
stud1.print_info()

print(stud1.is_on_course(course1), stud1.is_on_course(course2), stud1.is_on_course(course4), stud1.is_on_course(course3))

#print(course3.get_course_name())

# course2.enroll_student(stud2)
# print(course3.get_students_list())