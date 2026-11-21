# Question 09: Write a program to swap two variables using a temporary variable.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
x = 15
y = 30

print(f"Before swapping: x = {x}, y = {y}")

# Swapping using a temporary variable
temp = x
x = y
y = temp

print(f"After swapping:  x = {x}, y = {y}")
