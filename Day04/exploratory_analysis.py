import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "CAERS_ASCII_2004_2017Q2.csv"
df = pd.read_csv(file_path)

# Example: Distribution of a categorical column
plt.figure(figsize=(10, 6))
df['ci_gender'].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Example: Age distribution histogram
plt.figure(figsize=(10, 6))
df['ci_age_at_adverse_event'].dropna().astype(float).hist(bins=30)
plt.title("Age at Adverse Event Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
