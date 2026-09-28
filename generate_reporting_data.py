import pandas as pd
import numpy as np

np.random.seed(42)

N = 20000

products = ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard", "Mouse", "Printer", "Headphones"]
cities = ["Lucknow", "Delhi", "Mumbai", "Bangalore", "Pune", "Chennai", "Hyderabad", "Kolkata"]
regions = ["North", "South", "East", "West"]

df = pd.DataFrame({
    "Order_ID": [f"O{i:06d}" for i in range(1, N + 1)],
    "Order_Date": pd.date_range("2024-01-01", "2025-12-31", periods=N),
    "Customer_ID": [f"C{np.random.randint(1, 5001):05d}" for _ in range(N)],
    "Product": np.random.choice(products, N),
    "Category": np.random.choice(
        ["Electronics", "Accessories", "Office"],
        N,
        p=[0.45, 0.35, 0.20]
    ),
    "City": np.random.choice(cities, N),
    "Region": np.random.choice(regions, N),
    "Quantity": np.random.randint(1, 6, N),
    "Unit_Price": np.round(np.random.uniform(500, 100000, N), 2),
    "Discount_Percent": np.random.randint(0, 31, N),
    "Payment_Method": np.random.choice(
        ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash"],
        N
    ),
    "Order_Status": np.random.choice(
        ["Delivered", "Cancelled", "Returned"],
        N,
        p=[0.88, 0.07, 0.05]
    )
})

df["Gross_Sales"] = np.round(
    df["Quantity"] * df["Unit_Price"], 2
)

df["Discount_Amount"] = np.round(
    df["Gross_Sales"] * df["Discount_Percent"] / 100, 2
)

df["Net_Sales"] = np.round(
    df["Gross_Sales"] - df["Discount_Amount"], 2
)

df["Profit"] = np.round(
    df["Net_Sales"] * np.random.uniform(0.08, 0.30, N), 2
)

# Intentional missing values
for column in ["City", "Payment_Method", "Discount_Percent"]:
    indexes = np.random.choice(df.index, 100, replace=False)
    df.loc[indexes, column] = np.nan

# Intentional duplicate records
duplicates = df.sample(15, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

df.to_csv("sales_reporting_data_20000.csv", index=False)

print("Sales reporting dataset created successfully!")
print(f"Raw rows: {len(df):,}")
print(f"Unique orders: {df['Order_ID'].nunique():,}")
print(f"Columns: {len(df.columns)}")
print("File: sales_reporting_data_20000.csv")
