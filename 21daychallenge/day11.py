

#                   Python Challenge Day 10.....


# Write a Python program to store and manage employee data in a CSV file.
## The program should allow adding employees (ID, name, salary), displaying all records, finding the highest salary, and 
# deleting an employee.


import csv
import os

file_name = "employees.csv"

# Create file with header if not exists
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Salary"])


def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")
    
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, name, salary])
    
    print("Employee added!\n")


def display_employees():
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        print("\nEmployee Records:")
        for row in reader:
            print(row)
    print()


def highest_salary():
    max_salary = -1
    max_emp = None
    
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            salary = int(row["Salary"])
            if salary > max_salary:
                max_salary = salary
                max_emp = row
    
    if max_emp:
        print("Highest Salary Employee:")
        print(max_emp)
    else:
        print("No data found!")
    print()


def delete_employee():
    emp_id = input("Enter ID to delete: ")
    rows = []
    
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row[0] != emp_id:
                writer.writerow(row)
    
    print("Employee deleted (if existed).\n")

while True:
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Highest Salary")
    print("4. Delete Employee")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        highest_salary()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        break
    else:
        print("Invalid choice!\n")