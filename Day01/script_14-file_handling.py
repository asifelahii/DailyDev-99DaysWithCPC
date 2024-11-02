# 14. Data Processing (File Handling)
"""File handling allows reading from and writing to files.
    Syntax:
        open("filename", "mode") as file:
            file operations
"""
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, File Handling!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)