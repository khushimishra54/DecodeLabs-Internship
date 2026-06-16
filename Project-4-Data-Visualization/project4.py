import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Dataset for Data Analytics (6).xlsx")

# 1. Bar Chart - Order Status
plt.figure(figsize=(8,5))
df["OrderStatus"].value_counts().plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.show()

# 2. Pie Chart - Payment Method
plt.figure(figsize=(6,6))
df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

# 3. Line Chart - Monthly Sales Trend
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["TotalPrice"].sum()

monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(8,5)
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()