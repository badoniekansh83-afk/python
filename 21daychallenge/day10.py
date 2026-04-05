students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!\n")


def search_student():
    roll = input("Enter Roll Number to search: ")
    
    if roll in students:
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found!")
    print()


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")
    print()


def display_students():
    if not students:
        print("No records found.\n")
    else:
        print("Student Records:")
        for roll, data in students.items():
            print("Roll:", roll, "| Name:", data["name"], "| Marks:", data["marks"])
        print()


# Menu-driven program
while True:
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        display_students()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")