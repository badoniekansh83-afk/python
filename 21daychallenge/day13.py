

#                   Python Challenge Day 13.....

# Write a program to Manage books using CSV file.
#  Tasks: 
# Add book (title, author) 
# Issue/return book 
# Display all books


import csv
import os

file_name = "Books.csv"

if not os.path.exists(file_name):
    with open(file_name, "w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Author", "Status"])

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter author name: ")

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, author, "Available"])
    print("Book added successfully!\n")

def display_books():
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        print("\n Library Books: ")
        for row in reader:
            print(row)
        print()

def issue_book():
    title = input("Enter Book to Issue: ")
    rows=[]

    with open(file_name,"r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for row in rows:
        if row[0] == title and row[2]=="Available":
            row[2] = "Issued"
            print("Book Issued Successfully\n")
            break
        else:
            print("Book not available")
        
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(rows)
        print()

def return_book():
    title = input("Enter Books to return:  ")
    rows= []

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for row in rows:
        if row[0] == title and row[2] == "Issued":
            row[2] = "Available"
            print("Book return successfully!\n")
            break
        else:
            print("Book not found ")

    with open(file_name, "w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(rows)
    print()


while True:
    print("1. Add Book")
    print("2. Display Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Choice:")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        break
    else:
        print("Invalid Choice\n")

        