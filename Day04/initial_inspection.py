import pandas as pd

# Load dataset
file_path = "CAERS_ASCII_2004_2017Q2.csv"
df = pd.read_csv(file_path)

# Initial data inspection
print("First 5 rows of the dataset:\n", df.head())
print("\nColumn names:\n", df.columns)
print("\nData Types:\n", df.dtypes)
print("\nSummary Statistics:\n", df.describe())
print("\nMissing Values per column:\n", df.isnull().sum())