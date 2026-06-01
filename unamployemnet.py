import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("dataset.csv")

# First 5 Rows
print(df.head())

# Dataset Information
print(df.info())

# Missing Values
print(df.isnull().sum())

# Basic Statistics
print(df.describe())

# Unemployment Trend Graph
plt.figure(figsize=(10,5))
plt.plot(df.index, df.iloc[:, -1])
plt.title("Unemployment Rate Trend")
plt.xlabel("Records")
plt.ylabel("Unemployment Rate")
plt.grid(True)
plt.show()