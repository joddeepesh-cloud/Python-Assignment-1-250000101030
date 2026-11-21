# Question 26: Write a program to accept a number as a string and convert it into an integer.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Accepting a number as string from user
user_input = input("Enter a number as a string: ")

# Converting string to integer using int()
converted_int = int(user_input)

print("Original String Value :", repr(user_input), "| Data Type:", type(user_input).__name__)
print("Converted Integer Value:", converted_int, "| Data Type:", type(converted_int).__name__)
print("Demonstration (Double) :", converted_int * 2)
