import os

student_db = {}

def add_student():
  """A function that adds student information to the databse"""

  name = input("Enter name of the Student: ")
  id_no = input("Enter ID.no of the Student: ")
  sex = input("Enter sex of Student: ")
  age = input("Enter age of Student: ")
  student_db[name] = {"Name":name, "ID_no":id_no, "Sex":sex, "Age":age}
  print(f"Student {name} has been added to the database")
  
def view_student(name):
  """A function that list the information of a single student"""
  if name in student_db:
    for key, value in student_db[name].items():
      print(key, ":", value)
  else:
    print("No such student found.")

def list_students():
  """A function to list all the students with their information"""
  print("{:<10} {:<15} {:<10} {:<10}".format('ID_NO', 'NAME', 'SEX', 'AGE'))
  for student_info in student_db.values():
    id_no, name, sex, age = student_info["ID_no"], student_info["Name"], student_info["Sex"], student_info["Age"], 
    print("{:<10} {:<15} {:<10} {:<10}".format(id_no, name, sex, age))

def update_info(name):
    """Function to update info of a student"""
    if name in student_db:
        info_update = input(f"Which data of {name} you want to update (Name/ID_no/Sex/Age): ").lower()
        if info_update == "name":
            new_name = input("New Name: ")
            student_db[new_name] = student_db.pop(name)
            student_db[new_name]['Name'] = new_name
            print(f"Student {name}'s name has been updated to {new_name}.")
        elif info_update == "id_no":
            new_id_no = input("New ID_no: ")
            student_db[name][new_id_no] = student_db[name].pop('ID_no')
            print(f"Student {name}'s ID_no has been updated to {new_id_no}.")
        elif info_update == "sex":
            new_sex = input("New Sex: ")
            student_db[name]['Sex'] = new_sex
            print(f"Student {name}'s sex has been updated to {new_sex}.")
        elif info_update == "age":
            new_age = input("New Age: ")
            student_db[name]['Age'] = new_age
            print(f"Student {name}'s age has been updated to {new_age}.")
        else:
            print("Invalid field. Please choose Name, ID_no, Sex, or Age.")
    else:
        print("No such student found.")

def delete_info(name):
  """Function to delete info of a student"""
  if name in student_db:
    del student_db[name]
  else:
    print("No such student found.")

def menu():
  os.system('cls')
  print("Welcome to the Student Database")
  
  while True:
    print("\n1. Add a new student.")
    print("2. Search for a student by name.")
    print("3. Display all student in the Database.")
    print("4. Update a student's information.")
    print("5. Delete a student from the database.")
    print("6. Exit.\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      add_student()
    elif choice == 2:
      name_view = input("Enter the name of the Student you're searching for: ")
      view_student(name_view)
    elif choice == 3:
      list_students()
    elif choice == 4:
      name_update = input("Enter the name of the Student you want to update: ")
      update_info(name_update)
    elif choice == 5:
      name_delete = input("Enter the name of the Student you want to delete from the Database: ")
      delete_info(name_delete)
    elif choice == 6:
      print("Exited program")
      break
    else:
      print("Invalid input. Please try again")
    
menu()
