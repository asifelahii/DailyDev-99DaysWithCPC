# Script 1 - Series

"""Series is like a column in table.
    It is on-dimensional array holding data of any type.
    Syntax:
        series_name = [ val_1, val_2, val_3, ...]
        here,
            val_1 is at index 0,
            val_2 is at index 1,
            val_3 is at index 2, and so on.
"""
import pandas as pd

a = [7, 8, 9]
print(a) # [7, 8, 9]

# Creating a series from list
my_series = pd.Series(a)
print(my_series)
"""expected output:
    0    7
    1    8
    2    9
"""

