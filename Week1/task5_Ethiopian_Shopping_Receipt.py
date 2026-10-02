# TASK 5 — Ethiopian Shopping Receipt
# Goal
# Practice variables, quantities, arithmetic, and formatted output.
# Create a simple shopping receipt.
# Ask for:
# Customer name
# Product name
# Price
# Quantity
# Calculate the total price.
# Display a receipt.
# Example
# ========================================
#               RECEIPT
# ========================================

# Customer: Ahmed

# Product        Price       Qty
# ----------------------------------------
# Notebook       100 ETB      3

# Total:         300 ETB

# Thank you for shopping!
# ========================================

# Bonus
# Add a second product.
# Concepts
# Numbers • multiplication • strings • formatted output

name = input ("Enter you first name: ")
productName = input ("Enter the name of the product ")
price = float(input("Enter the price of the product "))
quantity = int(input("Enter the number of product"))

totalPrice = (price * quantity)

print(f"=========================")
print(f"       Receipt           ")
print(f"=========================")
print(f"customer: {name}")
print(f"Product      Price      Qty    ")
print(f"==========================")
print(f"{productName}       {price} ETB     {quantity}")
print(f"                           ")
print(f"Total:       {totalPrice}")
print("Thank you for shopping!")
print(f"=========================")
