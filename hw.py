class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}    
        self.average_rating = float() 
    def rate_hw(self, lecturer, course, grade):
     if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
        if course in lecturer.grades:
                lecturer.grades[course] += [grade]
        else:
                lecturer.grades[course] = [grade]
     else:
            return 'Ошибка'
    def __str__(self):
      grades_count = 0
      courses_in_progress_string = ', '.join(self.courses_in_progress)
      finished_courses_string = ', '.join(self.finished_courses)
      for k in self.grades:
          grades_count += len(self.grades[k])
      self.average_rating = sum(map(sum, self.grades.values())) / grades_count
      res = f'\nИмя: {self.name}'\
              f'\nФамилия: {self.surname}'\
              f'\nСредняя оценка за домашнее задание: {self.average_rating}'\
              f'\nКурсы в процессе обучения: {courses_in_progress_string}'\
              f'\nЗавершенные курсы: {finished_courses_string}'
      return res
    def __lt__(self, other):
       if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
       return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname      
class Reviewer(Mentor):
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname   
    self.courses_attached = []
  def __str__(self):
    return f'Имя : {self.name}'\
           f'\nФамилия : {self.surname}'
  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
class Lecturer(Mentor):
  def __init__ (self, name, surname):
    self.name = name
    self.surname = surname
    self.grades = {}
    self.courses_attached = []
    self.average_rating = float()
  def __str__(self):
    grades_count = 0
    for k in self.grades:
        grades_count += len(self.grades[k])
    self.average_rating = sum(map(sum, self.grades.values())) / grades_count
    res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
    return res
  def __lt__(self, other):
    if not isinstance(other, Lecturer):
         print('Такое сравнение некорректно')
         return
    return self.average_rating < other.average_rating

  

#создадим студента        
some_student = Student('Ruoy', 'Eman')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses = ['Введение в программирование']

some_student1 = Student('Anny', 'Way')
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Git']
some_student1.finished_courses = ['Введение в программирование']
#создаем ревьюера
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
#созддаим лектора 
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_lecturer1 = Lecturer('Ilon', 'Mas')
some_lecturer1.courses_attached += ['Python']
#создадим оценки от студента лектору
some_student.rate_hw(some_lecturer,'Python',10)
some_student.rate_hw(some_lecturer1,'Python',7)

some_student1.rate_hw(some_lecturer1,'Python',9)
some_student1.rate_hw(some_lecturer,'Python',9)
#создадим оценки студенту от ревьюера
some_reviewer.rate_hw(some_student, 'Python', 9.7)
some_reviewer.rate_hw(some_student, 'Python', 10.2)

some_reviewer.rate_hw(some_student1,'Python', 8)
some_reviewer.rate_hw(some_student1,'Python', 9)


student_list = [some_student ,some_student1]
def student_rating(student_list, course_name):
  grades_count = 0
  sum_grades = 0 
  for student in student_list:
    if student == student:
      sum_grades = sum(student.grades[course_name])
      grades_count +=1
  return round(sum_grades / grades_count ,2)
  
lecturer_list = [some_lecturer,some_lecturer1]
def lecturer_rating(lecturer_list, course_name):
  grades_count = 0
  sum_grades = 0
  for lecturer in lecturer_list:
    if lecturer == lecturer:
      sum_grades = sum(lecturer.grades[course_name])
      grades_count +=1
  return round(sum_grades / grades_count ,2)    
  

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list,'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list,'Python')}")
print(some_student.average_rating >= some_student1.average_rating)
print(some_student.average_rating < some_student1.average_rating)
print(some_lecturer.average_rating <= some_lecturer1.average_rating )
print(some_lecturer.average_rating < some_lecturer1.average_rating )
print(some_student)
print(some_reviewer)
print(some_lecturer)



