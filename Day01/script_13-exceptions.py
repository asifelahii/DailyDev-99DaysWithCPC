# 13. Exceptions
"""Exceptions handle runtime errors using try-except blocks.
    Syntax:
        try:
            # code that may raise an error
        except ExceptionType:
            # code to handle the error
"""
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number.")