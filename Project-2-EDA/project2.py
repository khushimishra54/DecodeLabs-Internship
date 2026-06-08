import pandas as pd

# Load dataset
df = pd.read_excel("Dataset for Data Analytics (1).xlsx")

# Basic Information
print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean(numeric_only=True))

# Median
print("\nMedian:")
print(df.median(numeric_only=True))

# Count
print("\nCount:")
print(df.count())

# -------------------------
# Outlier Detection
# -------------------------

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower_bound) |
    (df["TotalPrice"] > upper_bound)
]

print("\nNumber of Outliers:", len(outliers))