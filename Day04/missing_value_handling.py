import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
file_path = "CAERS_ASCII_2004_2017Q2.csv"
df = pd.read_csv(file_path)

# Check missing values
missing_values = df.isnull().sum()
print("Missing Values per column:\n", missing_values)

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values in Dataset")
plt.show()

# Handle missing values (example strategy)
df.fillna("Unknown", inplace=True)
