import pandas as pd

file_path = "CAERS_ASCII_2004_2017Q2.csv"

# Read CSV file into a DataFrame
df = pd.read_csv(file_path)

# to view first few rows of the DataFrame
print("First five rows of the dataset:")
print(df.head())
# to view summary information
print("\nDataset Info:")
print(df.info())
# To view statistical summery of numerical colums
print("\nStatistical Summary:")
print(df.describe())
