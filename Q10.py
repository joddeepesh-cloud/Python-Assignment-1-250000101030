# Question 10: Write a program to swap two variables without using a temporary variable.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
a = 50
b = 100

print(f"Before swapping: a = {a}, b = {b}")

# Swapping using Python tuple packing/unpacking
a, b = b, a

print(f"After swapping:  a = {a}, b = {b}")
