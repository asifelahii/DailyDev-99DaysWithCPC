import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


"""Load the dataset"""
file_path = "CAERS_ASCII_2004_2017Q2.csv"
# Read CSV file into a DataFrame
df = pd.read_csv(file_path)

"""Categorical Analysis:""" 
# Display unique values in a categorical column
# Example: Replace 'column_name' with an actual categorical column name if it exists
if 'column_name' in df.columns:
    print("\nUnique values in 'column_name':")
    print(df['column_name'].value_counts())
    
# Numerical Analysis: Plot distributions of numerical columns
for col in df.select_dtypes(include='number').columns:
    plt.figure()
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.show()