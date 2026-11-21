# Question 37: Write a program to create a dictionary containing five countries and their capitals.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
countries_capitals = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris",
    "United Kingdom": "London",
    "Australia": "Canberra"
}

print("Countries and their Capitals:")
for country, capital in countries_capitals.items():
    print(f"{country:<16} -> {capital}")
