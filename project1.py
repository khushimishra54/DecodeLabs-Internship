import pandas as pd

# Load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Missing values check
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Check again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nDataset cleaned and saved successfully!")