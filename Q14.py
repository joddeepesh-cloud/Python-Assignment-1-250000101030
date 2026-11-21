# Question 14: Write a program to calculate simple interest using principal, rate and time.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
principal = 10000.0  # Principal amount in INR
rate = 7.5           # Annual rate of interest in percentage
time = 3.0           # Time in years

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("Simple Interest Calculation:")
print("Principal Amount :", principal)
print("Rate of Interest :", rate, "%")
print("Time Period      :", time, "years")
print("Simple Interest  :", simple_interest)
print("Total Amount     :", total_amount)
