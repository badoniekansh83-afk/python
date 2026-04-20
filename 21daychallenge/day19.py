

#                   Python Challenge Day 19


#Create a Student Management System in Python using OOP. Define a Student class with attributes name and marks, 
# and methods to display details and update marks. Also, create a StudentManager class to add, delete, and display all
#  students. Implement a simple menu-driven program to perform these operations.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks updated for {self.name}")


class StudentManager:
    def __init__(self):
        self.students = []

    # Add student
    def add_student(self, name, marks):
        student = Student(name, marks)
        self.students.append(student)
        print(f"Student {name} added.")


    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} deleted.")
                return
        print("Student not found.")


    def display_all(self):
        if not self.students:
            print("No students available.")
        else:
            print("\nStudent List:")
            for student in self.students:
                student.display()

    def update_student(self, name, new_marks):
        for student in self.students:
            if student.name == name:
                student.update_marks(new_marks)
                return
        print("Student not found.")



def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Display All Students")
        print("4. Update Marks")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            manager.add_student(name, marks)

        elif choice == '2':
            name = input("Enter name to delete: ")
            manager.delete_student(name)

        elif choice == '3':
            manager.display_all()

        elif choice == '4':
            name = input("Enter name to update: ")
            marks = int(input("Enter new marks: "))
            manager.update_student(name, marks)

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()