# Question 46: Write a program to accept five subject marks from the user and display their total.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Accepting marks for 5 subjects from user
marks = []
print("Please enter marks for five subjects:")
for i in range(1, 6):
    m = float(input(f"Enter marks for Subject {i}: "))
    marks.append(m)

total_marks = sum(marks)
print("Entered Subject Marks:", marks)
print(f"Total Marks Obtained : {total_marks} out of 500")
