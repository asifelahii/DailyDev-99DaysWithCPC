# 7. Loops
"""Loops allow repeated execution of code.
    Types:
    - For Loop
        Syntax: 
            for i in range(n): // initially i = 0 (if not initialized)
                # code block
    - While Loop
        Syntax:
            while condition:
                # code block
                # iteration count ++
"""
# For loop 
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1