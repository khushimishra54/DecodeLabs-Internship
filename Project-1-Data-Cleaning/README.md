# Project 1: Data Cleaning and Preparation

## Objective

The objective of this project is to clean and prepare raw data for analysis by identifying missing values, checking duplicates, and improving data quality.

## Dataset Information

* Total Records: 1200
* Total Columns: 14

## Data Cleaning Tasks Performed

### 1. Missing Value Detection

The dataset was checked for missing values using Pandas.

Result:

* CouponCode column contained 309 missing values.
* All other columns were complete.

### 2. Missing Value Handling

Missing values in the CouponCode column were replaced with:

```python
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
```

### 3. Duplicate Record Check

Duplicate records were identified using:

```python
df.duplicated().sum()
```

Result:

* No duplicate records were found.

### 4. Data Validation

* Dataset structure was verified.
* Column information was reviewed.
* Data was prepared for further analysis.

## Output

A cleaned dataset was generated and saved as:

```text
Cleaned_Dataset.xlsx
```

## Conclusion

The dataset was successfully cleaned by handling missing values and validating data quality. No duplicate records were found. The cleaned dataset is ready for exploratory data analysis and further business intelligence tasks.
