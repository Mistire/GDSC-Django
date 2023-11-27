import os

student_db = {}

def add_student():
  name = input("Enter name of the Student: ")
  id_no = input("Enter ID.no of the Student: ")
  sex = input("Enter sex of Student: ")
  age = input("Enter age of Student: ")
  student_db[name] = {"Name":name, "ID_no":id_no, "Sex":sex, "Age":age}
  print(f"Student {name} has been added to the database")
  

def view_student(name):
  if name in student_db:
    for key, value in student_db[name].items():
      print(key, ":", value)
  else:
    print("No such student found.")
def list_students():
  print("{:<10} {:<15} {:<10} {:<10}".format('ID_NO', 'NAME', 'SEX', 'AGE'))
  for student_info in student_db.values():
    id_no, name, sex, age = student_info["ID_no"], student_info["Name"], student_info["Sex"], student_info["Age"], 
    print("{:<10} {:<15} {:<10} {:<10}".format(id_no, name, sex, age))
# def update_info():
#   name = input()
def delete_info(name):
  if name in student_db:
    del student_db[name]
  else:
    print("No such student found.")

def menu():
  print("Welcome to the Student Database")
  while True:
    print("\n1. Add a new student.")
    print("2. Search for a student by name.")
    print("3. Display all student in the Database.")
    print("4. Update a student's information.")
    print("5. Delete a student from the database.")
    print("6. Exit.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      add_student()
    elif choice == 2:
      name_view = input("Enter the name of the Student you're searching for: ")
      view_student(name_view)
    elif choice == 3:
      list_students()
    # elif choice == 4:
    #   update_info()
    elif choice == 5:
      name_delete = input("Enter the name of the Student you want to delete from the Database: ")
      delete_info(name_delete)
    elif choice == 6:
      print("Exited program")
      break
    else:
      print("Invalid input. Please try again")
    # os.system('cls')
menu()
