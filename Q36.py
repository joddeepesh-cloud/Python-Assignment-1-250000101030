# Question 36: Write a program to create a dictionary containing student details such as roll number, name and marks.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
student = {
    "roll_no": 250000101030,
    "name": "DEEPESH JOSHI",
    "branch": "CSE",
    "marks": 95.5
}

print("Student Details Dictionary:")
for key, value in student.items():
    print(f"{key:<10}: {value}")
