# TASK 2 — Student ID Card
# Goal
# Practice storing and formatting different types of data.
# Create a program that generates a simple student ID card.
# Ask for:
# Student name
# Student ID
# Department
# Year
# University
# Phone number
# Display the information in a clean ID-card style.

# Example
# +--------------------------------+
# |       AKIBA STUDENT CARD       |
# +--------------------------------+
# | Name: Ahmed Ali                |
# | ID: AKB-001                    |
# | Department: Software Eng.      |
# | Year: 1                        |
# | University: Jimma University   |
# | Phone: 0912345678              |
# +--------------------------------+

# Concepts
# Variables • strings • integers • formatted output

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
student_id = input("Enter your student ID: ")
department = input("Enter your department: ")
year = int(input("Enter your year: "))
university = input("Enter your university: ")
phone_number = input("Enter your phone number: ")

print("\n+--------------------------------+")
print("|       AKIBA STUDENT CARD       |")
print("+--------------------------------+")
print(f"| Name: {first_name} {last_name:<20}|")
print(f"| ID: {student_id:<28}|")
print(f"| Department: {department:<28}|")
print(f"| Year: {year:<28}|")
print(f"| University: {university:<28}|")
print(f"| Phone: {phone_number:<28}|")
print("+--------------------------------+")