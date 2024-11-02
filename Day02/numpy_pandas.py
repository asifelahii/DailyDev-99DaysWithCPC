import numpy as numpy
import pandas as pd

# creating a dictionary
dic = {
    "Name": ["Asif", "Abdullah", "A.Rahman", "A.Rahim"],
    "Age": [20, 22, 19, 18],
    "City": ["Dhaka", "Rajshahi", "Madina", "Cairo"]
}

# creating a DataFrame from the dictionary
df = pd.DataFrame(dic)
print(df) 

# Export the dataframe
# Save to CSV
df.to_csv('dic_with_indices.csv')
df.to_csv('dic_without_indices.csv', index = False)
#Save to Excel
df.to_excel('dic_with_indices.xlsc')
df.to_excel('dic_without_indices.xlsc', index = False)