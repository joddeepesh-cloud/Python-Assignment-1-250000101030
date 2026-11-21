# Question 48: Write a program to demonstrate the use of print() with multiple variables and formatted output.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
name = "DEEPESH JOSHI"
roll_no = 250000101030
percentage = 94.75

# Demonstration of sep and end parameters
print("Name:", name, "Roll:", roll_no, sep=" | ")
print("Formatted using f-string: Roll No: %d, Percentage: %.2f%%" % (roll_no, percentage))
print(f"Student: {name} scored {percentage:.2f}% in CSE.")
