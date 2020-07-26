"""
Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
"""
print("User Details")
firstName = input("Enter your first name- ")    # Snehal
lastName = input("Enter your last name- ")      # Thakur
fullName = " ".join([firstName,lastName])       # Snehal Thakur
print("fullName =",fullName)
reverseOrder = fullName[::-1]                   # rukahT lahenS
print("reverseOrder =", reverseOrder)