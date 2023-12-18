# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def sayname(self):
#     return f"My name is {self.name}"
#   def sayage(self):
#     return f"I'm {self.age} years old"
  
# p1 = person("Mistre", "21")
# print(p1.sayname())
# print(p1.sayage()
# )


# class Circle:
#   def __init__(self,radius):
#     self.radius = radius

#   def calculate_area(self):
#     return 3.14 * self.radius * self.radius
  
# my_circle = Circle(5)

# area = my_circle.calculate_area()

# print(area)


# class Rectangle:
#   def __init__(self, length, width):
#     self.length = length
#     self.width = width

#   def area(self):
#     return self.length * self.width
#   def perimeter(self):
#     return (2*(self.length + self.width))
  
# r1 = Rectangle(2,4)
# r2 = Rectangle(3,7)

# print(f"The area and permeter of rectangle 1 is {r1.area()} and {r1.perimeter()}")
# print(f"The area and permeter of rectangle 2 is {r2.area()} and {r2.perimeter()}")



# class Shape:
#   def __init__(self, color):
#     pass

#   def get_color(self):
#     pass
  
#   def area(self):
#     pass


# class Rectangle(Shape):
#   def __init__(self,color,length, width):
#     self.color = color
#     self.length = length
#     self.width = width

#   def get_color(self):
#     return self.color
#   def area(self):
#     return self.length * self.width


# class Circle(Shape):
#   def __init__(self, color, radius):
#     self.color = color
#     self.radius = radius

#   def get_color(self):
#     return self.color
#   def area(self):
#     return 3.14 * self.radius * self.radius
  


# circle = Circle("Blue", 10)
# rectangle = Rectangle("Red", 5,6)

# print(f"The Color of the Circle is {circle.get_color()} and its area is {circle.area()}")
# print(f"The Color of the Rectangle is {rectangle.get_color()} and its area is {rectangle.area()}")






## Online session
#Exercise 1
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

















