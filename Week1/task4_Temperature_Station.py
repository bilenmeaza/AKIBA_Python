# TASK 4 — Temperature Station
# Goal
# Practice mathematical expressions and unit conversion.
# Create a temperature conversion program.
# The user enters a temperature in Celsius.
# Convert it to Fahrenheit.

# Formula:
# F = (C × 9/5) + 32
# Then display both temperatures.
# Example
# Temperature: 25°C

# Celsius: 25°C
# Fahrenheit: 77°F
# Bonus
# Also convert Fahrenheit → Celsius.
# Concepts
# float() • arithmetic • formatted output


temInCelsius = float(input("Enter the value of the temprature in degree celsius: "))

fahrenheit = (temInCelsius * 9 / 5) + 32

print(f"The temprature is {temInCelsius} in degree celsius and has a value of {fahrenheit} in degree fahrenheit")