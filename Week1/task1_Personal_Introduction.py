# TASK 1 — Personal Introduction
# Goal
# Practice variables, strings, and user input.
# Create a program that asks the user for:
# Full name
# Age
# City
# University
# Department
# Favorite programming language
# One programming goal
# Display the information as a professional introduction.
# Example
# ========================================
#         STUDENT INTRODUCTION
# ========================================

# My name is Ahmed Ali.
# I am 21 years old.
# I live in Addis Ababa.
# I study Software Engineering at Jimma University.
# My favorite programming language is Python.

# My programming goal:
# Become a professional backend developer.

# ========================================

# Concepts
# input() • variables • strings • print() • formatted output
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
university = input("Enter your university: ")
department = input("Enter your department: ")
favorite_language = input("Enter your favorite programming language: ")
programming_goal = input("Enter your programming goal: ")

print("\n========================================")
print("        STUDENT INTRODUCTION")
print("========================================\n")
print(f"My name is {first_name} {last_name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I study {department} at {university}.")
print(f"My favorite programming language is {favorite_language}.\n")
print(f"My programming goal: {programming_goal}")
print("\n========================================")

