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
  
  print(student_db[name])
# def list_students():
#   name = input()
# def update_info():
#   name = input()
# def delete_info(name):
#   name = input()

def menu():
  print("Welcome to the Student Database")
  while True:
    print("\n1. Add a new student.")
    print("2. Display all students.")
    print("3. Search for a student by name.")
    print("4. Update a student's information.")
    print("5. Delete a student from the database.")
    print("6. Exit.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      add_student()
    elif choice == 2:
      name_view = input("Enter the name of the Student you're searching for: ")
      view_student(name_view)
    # elif choice == 3:
    #   list_students()
    # elif choice == 4:
    #   update_info()
    # elif choice == 5:
    #   delete_info()
    elif choice == 6:
      print("Exited program")
      break
    else:
      print("Invalid input. Please try again")
    # os.system('cls')
menu()
