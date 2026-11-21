# Question 05: Write a program to demonstrate the use of valid and invalid Python identifiers.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("--- Demonstrating Valid Python Identifiers ---")

# Valid Identifiers
student_name = "Deepesh Joshi"
rollNumber = 250000101030
_branch = "CSE"
age2026 = 18
TOTAL_MARKS = 475

print("student_name :", student_name)
print("rollNumber   :", rollNumber)
print("_branch      :", _branch)
print("age2026      :", age2026)
print("TOTAL_MARKS  :", TOTAL_MARKS)

print("\n--- Rules and Examples of Invalid Identifiers (Explained Safely) ---")
# 1. Cannot start with a digit: e.g. 1student (SyntaxError)
# 2. Cannot contain special characters or spaces: e.g. student-name, roll no, student@id
# 3. Cannot be a reserved keyword: e.g. class, for, while, def, if

invalid_examples = [
    ("1student", "Cannot start with a digit"),
    ("student-name", "Hyphen (-) is an operator, not allowed in identifiers"),
    ("roll no", "Identifiers cannot contain spaces"),
    ("class", "'class' is a reserved Python keyword"),
    ("total$marks", "Special character '$' is not allowed")
]

for identifier, reason in invalid_examples:
    print(f"Invalid: {identifier:<15} -> Reason: {reason}")
