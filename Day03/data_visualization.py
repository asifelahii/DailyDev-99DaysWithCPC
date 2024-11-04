import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "CAERS_ASCII_2004_2017Q2.csv"

# Read CSV file into a DataFrame
df = pd.read_csv(file_path)

# visualizing missing values as a heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values in Dataset")
plt.show()