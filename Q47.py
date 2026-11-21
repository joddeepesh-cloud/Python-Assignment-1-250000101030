# Question 47: Write a program to demonstrate the use of list(), tuple() and dict() constructors.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Using constructors
sample_str = "UTU"
sample_pairs = [("name", "Deepesh"), ("roll", 250000101030)]

constructed_list = list(sample_str)
constructed_tuple = tuple(sample_str)
constructed_dict = dict(sample_pairs)

print("list('UTU')               :", constructed_list, "Type:", type(constructed_list))
print("tuple('UTU')              :", constructed_tuple, "Type:", type(constructed_tuple))
print("dict([('name', ...), ...]):", constructed_dict, "Type:", type(constructed_dict))
