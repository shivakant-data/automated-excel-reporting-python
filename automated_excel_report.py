import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.utils import get_column_letter

INPUT_FILE = "sales_reporting_data_20000.csv"
OUTPUT_FILE = "Automated_Sales_Report.xlsx"

# -----------------------------
# 1. Load data
# -----------------------------
df = pd.read_csv(INPUT_FILE)

print("=== AUTOMATED EXCEL REPORT ===")
print(f"Raw rows: {len(df):,}")

# -----------------------------
# 2. Clean data
# -----------------------------
df = df.drop_duplicates(subset="Order_ID").copy()

df["City"] = df["City"].fillna("Unknown")
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")
df["Discount_Percent"] = df["Discount_Percent"].fillna(
    df["Discount_Percent"].median()
)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# -----------------------------
# 3. KPI calculations
# -----------------------------
total_orders = len(df)
total_sales = df["Net_Sales"].sum()
total_profit = df["Profit"].sum()
avg_order_value = df["Net_Sales"].mean()
profit_margin = total_profit / total_sales * 100

# -----------------------------
# 4. Summary tables
# -----------------------------
monthly_summary = (
    df.groupby("Month")
    .agg(
        Orders=("Order_ID", "count"),
        Sales=("Net_Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

product_summary = (
    df.groupby("Product")
    .agg(
        Orders=("Order_ID", "count"),
        Sales=("Net_Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
    .sort_values("Sales", ascending=False)
)

city_summary = (
    df.groupby("City")
    .agg(
        Orders=("Order_ID", "count"),
        Sales=("Net_Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values("Sales", ascending=False)
)

payment_summary = (
    df.groupby("Payment_Method")
    .agg(
        Orders=("Order_ID", "count"),
        Sales=("Net_Sales", "sum")
    )
    .reset_index()
)

category_summary = (
    df.groupby("Category")
    .agg(
        Orders=("Order_ID", "count"),
        Sales=("Net_Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

# -----------------------------
# 5. Create Excel workbook
# -----------------------------
with pd.ExcelWriter(
    OUTPUT_FILE,
    engine="openpyxl"
) as writer:

    df.to_excel(writer, sheet_name="Raw Data", index=False)

    kpi_data = pd.DataFrame({
        "KPI": [
            "Total Orders",
            "Total Sales",
            "Total Profit",
            "Average Order Value",
            "Profit Margin"
        ],
        "Value": [
            total_orders,
            total_sales,
            total_profit,
            avg_order_value,
            profit_margin
        ]
    })

    kpi_data.to_excel(writer, sheet_name="Dashboard", index=False)
    monthly_summary.to_excel(writer, sheet_name="Monthly Summary", index=False)
    product_summary.to_excel(writer, sheet_name="Product Summary", index=False)
    city_summary.to_excel(writer, sheet_name="City Summary", index=False)
    payment_summary.to_excel(writer, sheet_name="Payment Summary", index=False)
    category_summary.to_excel(writer, sheet_name="Category Summary", index=False)

# -----------------------------
# 6. Format workbook
# -----------------------------
wb = load_workbook(OUTPUT_FILE)

for ws in wb.worksheets:

    ws.freeze_panes = "A2"

    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

    for column in ws.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)

        for cell in column:
            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        ws.column_dimensions[column_letter].width = min(
            max_length + 2,
            30
        )

# -----------------------------
# 7. Dashboard formatting
# -----------------------------
dashboard = wb["Dashboard"]

for row in range(2, 7):
    dashboard.cell(row=row, column=1).font = Font(bold=True)

dashboard["B3"].number_format = '?#,##0.00'
dashboard["B4"].number_format = '?#,##0.00'
dashboard["B5"].number_format = '?#,##0.00'
dashboard["B6"].number_format = '0.00%'

# -----------------------------
# 8. Monthly sales chart
# -----------------------------
monthly = wb["Monthly Summary"]

chart = LineChart()
chart.title = "Monthly Sales Trend"
chart.y_axis.title = "Sales"
chart.x_axis.title = "Month"

data = Reference(
    monthly,
    min_col=3,
    min_row=1,
    max_row=monthly.max_row
)

categories = Reference(
    monthly,
    min_col=1,
    min_row=2,
    max_row=monthly.max_row
)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
chart.height = 8
chart.width = 15

monthly.add_chart(chart, "F2")

# -----------------------------
# 9. Product sales chart
# -----------------------------
product = wb["Product Summary"]

bar_chart = BarChart()
bar_chart.title = "Sales by Product"
bar_chart.y_axis.title = "Sales"
bar_chart.x_axis.title = "Product"

data = Reference(
    product,
    min_col=3,
    min_row=1,
    max_row=product.max_row
)

categories = Reference(
    product,
    min_col=1,
    min_row=2,
    max_row=product.max_row
)

bar_chart.add_data(data, titles_from_data=True)
bar_chart.set_categories(categories)
bar_chart.height = 8
bar_chart.width = 15

product.add_chart(bar_chart, "F2")

# -----------------------------
# 10. Save
# -----------------------------
wb.save(OUTPUT_FILE)

print(f"Clean orders: {total_orders:,}")
print(f"Total sales: ?{total_sales:,.2f}")
print(f"Total profit: ?{total_profit:,.2f}")
print(f"Average order value: ?{avg_order_value:,.2f}")
print(f"Profit margin: {profit_margin:.2f}%")
print(f"Excel report created: {OUTPUT_FILE}")
