# Question 42: Write a program to demonstrate the use of the id() function for different variables.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
x = 100
y = 100
z = 200

print(f"Value of x = {x}, Memory Address id(x) = {id(x)}")
print(f"Value of y = {y}, Memory Address id(y) = {id(y)}")
print(f"Value of z = {z}, Memory Address id(z) = {id(z)}")

# In Python, small integers share identical memory locations (integer interning)
print("Does id(x) == id(y)?", id(x) == id(y))
