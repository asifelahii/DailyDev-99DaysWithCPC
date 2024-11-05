import pandas as pd

# Load dataset
file_path = "CAERS_ASCII_2004_2017Q2.csv"
df = pd.read_csv(file_path)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Check for any remaining duplicates
print("Duplicates remaining:", df.duplicated().sum())

# Standardize column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
print("Cleaned Column Names:\n", df.columns)
