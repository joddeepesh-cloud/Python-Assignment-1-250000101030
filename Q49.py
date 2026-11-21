# Question 49: Write a program to demonstrate the difference between integer and floating-point values.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
int_val = 15
float_val = 15.0

print(f"Integer Value     : {int_val} (Type: {type(int_val).__name__})")
print(f"Float Value       : {float_val} (Type: {type(float_val).__name__})")

print("\nDivision comparison:")
print("15 / 2  (Float division) :", 15 / 2, "Type:", type(15 / 2).__name__)
print("15 // 2 (Floor division) :", 15 // 2, "Type:", type(15 // 2).__name__)
