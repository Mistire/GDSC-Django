class User:
  def __init__(self,name):
    self.name = name


class Student(User):

  list_student = []
  
  def __init__(self, age, grade):
      
    assert type(age) == int, "Age should be only integer"

    self.name = User.name
    self.age = age
    self.grade = grade
    self.courses = []

  def display_data(self):
    return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}rd year student\nCourses: {self.courses}"
  
  def add_course(self, courses):
    self.courses.append(courses)

student = Student("Mistire", 21, 3)

print(student.display_data())




#Course - class, course_name, course_code, course_teacher
class Course(User):
  def __init__(self, course_name, course_code):
    self.course_name = course_name
    self.course_code = course_code
    self.teacher_name = User.name

  def __repr__(self):
    return f"Course name: {self.course_name}\nCourse code: {self.course_code}\nTeacher name: {self.teacher_name}\n"
  
course1 = Course("Maths", 112, "Teshome")
course2 = Course("Civics", 113, "Daniel")
course3 = Course("English", 114, "Ayu")

print(student.add_course(course1))
print(student.add_course(course2))
print(student.add_course(course3))


class Teacher:
  def __init__(self, name, subject):

    # assert Teacher(self.subject) == Course(self.course_name)

    self.name = User.name
    self.subject = subject

  def __repr__(self):
    return f"{self.name} teaches {self.subject}"
  
teacher1 = Teacher("Teshome", "Maths")
teacher2 = Teacher("Daniel", "Civics")
teacher3 = Teacher("Ayu", "English")

print(teacher1)
print(teacher2)
print(teacher3)