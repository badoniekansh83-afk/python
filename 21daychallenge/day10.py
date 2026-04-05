

#                   Python Challenge Day 10.....

#  Write a Python program to create a Student Record System using a dictionary.
#  The program should allow adding, searching, deleting, and displaying student records.
#  Implement it using a menu-driven approach


students={}

def add_student():
    roll =input("Enter Roll Number: ")
    name= input("Enter Name: ")
    marks= input("Enter Marks: ")

    students[roll]= {"name":name, "marks":marks}
    print("Student added successfully!\n")

def search_student():
    roll= input("Enter Roll Number to search: ")

    if roll in students:
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found!!")
    print()

def delete_student():
    roll= input("Enter Roll Number to delete:  ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!!")
    print()

def display_student():
    if not students:
        print("No Record found!\n")
    else:
        print("Student Records:")
        for roll , data in students.items():
            print("Roll:", roll, "| Name:",data["name"], "| Marks:", data["marks"])
        print()

while True:
    print("1.  Add student")
    print("2.  Search student")
    print("3.  Delete student")
    print("4.  Display student")
    print("5.  Exit")

    choice= input("Enter Choice:  ")

    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        display_student()
    elif choice == '5':
        print("Exiting program....")
        break
    else:
        print("Invalid Choice!!!\n")

    