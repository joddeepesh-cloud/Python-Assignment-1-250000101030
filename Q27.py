# Question 27: Write a program to demonstrate the use of int(), float() and str() functions.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
val = "125"

# Using int()
as_int = int(val)
# Using float()
as_float = float(val)
# Using str()
as_str = str(as_int + 50)

print(f"Original value: '{val}'")
print(f"Using int()   : {as_int} (Type: {type(as_int).__name__})")
print(f"Using float() : {as_float} (Type: {type(as_float).__name__})")
print(f"Using str()   : '{as_str}' (Type: {type(as_str).__name__})")
