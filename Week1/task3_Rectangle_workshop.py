# TASK 3 — Rectangle Workshop
# Goal
# Practice numeric values and arithmetic operators.
# Imagine you are building a small construction tool.
# Ask the user for:
# Length
# Width
# Calculate:
# Area
# Perimeter
# Then display the results.
# Example
# Length: 10
# Width: 5

# Area: 50 m²
# Perimeter: 30 m

# Concepts
# Numbers • arithmetic operators • input conversion

length = float(input("Enter the length of the rectangle"))
width = float(input ("Enter the width of the rectangle"))

Area = length * width

Perimeter = (2 * length) + (2 * width)

print(f"the area of the rectangle is {Area}")
print(f"the perimeter of the rectangle is {Perimeter}")

