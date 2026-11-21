# Question 33: Write a program to create a list containing different data types.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
mixed_list = ["Deepesh", 250000101030, 9.45, True, [1, 2, 3]]

print("Mixed Data Type List:")
print(mixed_list)

for idx, item in enumerate(mixed_list):
    print(f"Index {idx}: Value = {item!r:<18} Type = {type(item).__name__}")
