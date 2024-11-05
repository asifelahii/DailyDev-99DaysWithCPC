import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "CAERS_ASCII_2004_2017Q2.csv"
df = pd.read_csv(file_path)

# Bar plot of outcomes
plt.figure(figsize=(10, 6))
df['aec_one_row_outcomes'].value_counts().plot(kind='bar')
plt.title("Outcome Distribution")
plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.show()

# Box plot of age to detect outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['ci_age_at_adverse_event'].dropna().astype(float))
plt.title("Age Distribution (Box Plot)")
plt.xlabel("Age")
plt.show()