# 6. Conditional Execution
"""Conditionals allow execution of code based on conditions.
    Syntax:
        if condition:
            # code to execute if condition is true
        elif another_condition:
            # code if another_condition is true
        else:
            # code if no condition is met
"""
age = 22

# used logical 'and' to check 2 comditions at once.
if age >= 13 and age <= 17:
    print("Teenager")
elif age >= 18:
    print("Adult")
else:
    print("Minor")