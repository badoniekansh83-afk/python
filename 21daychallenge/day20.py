


                            ## Python Challenge Day 20

#### Q. Write a Python program to store student names and marks using a dictionary. 
# Calculate the average, highest, and lowest marks, and display students scoring above 75.


student = {"Aman": 85, "Riya":72, "Rahul":90, "Senha":81, "Karan":78}

marks = list(student.values())

average = sum(marks)/ len(marks)

maximum = max(marks)
minimum = min(marks)

a = sum((x - average) **2 for x in marks) / len(marks)
std_dev = a **0.5

high_score = [name for name, m in student.items() if m >75]

print("Students:",student)
print("Average Marks:", average)
print("Maximum:",maximum)
print("Minimum:", minimum)
print("Standard Deviation:",round(std_dev))
print("Student with marks >75:",high_score)

