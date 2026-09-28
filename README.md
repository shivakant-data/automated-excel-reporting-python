@'
# Automated Excel Reporting with Python 📊⚙️

An end-to-end Python automation project that transforms raw sales data into a structured Excel business report with automated KPIs, summary tables, and interactive Excel charts.

## 📌 Project Overview

This project demonstrates how Python can automate repetitive Excel reporting workflows.

The pipeline takes raw sales data, cleans and validates it, calculates business KPIs, creates analytical summary tables, and generates a professional Excel report with a centralized dashboard.

### Workflow

Raw Sales Data
↓
Data Cleaning
↓
KPI Calculation
↓
Business Summaries
↓
Excel Report Generation
↓
Automated Dashboard
↓
Business Insights

## 📊 Dataset

The project uses a synthetic sales dataset containing:

- 20,015 raw records
- 20,000 unique orders
- 15 intentional duplicate records
- 16 columns
- 2 years of order data
- Multiple products
- Multiple cities and regions
- Multiple payment methods
- Intentional missing values for data-cleaning practice

## 📈 Key Business KPIs

| KPI | Result |
|---|---:|
| Total Orders | 20,000 |
| Total Sales | ₹2,561,879,965.55 |
| Total Profit | ₹489,525,232.39 |
| Average Order Value | ₹128,094.00 |
| Profit Margin | 19.11% |

## 📊 Automated Dashboard

The generated Excel dashboard contains:

- Total Orders
- Total Sales
- Total Profit
- Average Order Value
- Profit Margin
- Monthly Sales Trend
- Sales by Product

![Automated Sales Dashboard](screenshots/automated_sales_dashboard.png)

## 📑 Excel Report Sheets

The automated workbook contains:

- Dashboard
- Raw Data
- Monthly Summary
- Product Summary
- City Summary
- Payment Summary
- Category Summary

## 🧹 Data Cleaning

The Python automation performs:

- Duplicate order removal
- Missing-value handling
- Date conversion
- Monthly feature creation
- Data aggregation
- KPI calculation
- Business summary generation

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- OpenPyXL
- Matplotlib
- Seaborn
- Excel

## 💡 Skills Demonstrated

### Python & Data Analysis
- Data cleaning
- Data transformation
- GroupBy analysis
- KPI calculation
- Feature engineering

### Excel Automation
- Automated workbook creation
- Multiple worksheet generation
- Excel formatting
- Freeze panes
- Automatic column sizing
- Excel charts

### Business Analytics
- Sales analysis
- Profit analysis
- Product performance
- City performance
- Payment-method analysis
- Monthly sales trends

## 📂 Project Structure

```text
automated-excel-reporting-python/
│
├── README.md
├── requirements.txt
├── generate_reporting_data.py
├── automated_excel_report.py
├── build_dashboard.py
├── sales_reporting_data_20000.csv
├── Automated_Sales_Report.xlsx
│
└── screenshots/
    └── automated_sales_dashboard.
    
▶️ How to Run
1. Clone the repository
git clone https://github.com/shivakant-data/automated-excel-reporting-python.git
cd automated-excel-reporting-python
2. Install dependencies
pip install -r requirements.txt
3. Generate the dataset
python generate_reporting_data.py
4. Generate the Excel report
python automated_excel_report.py
5. Build the dashboard
python build_dashboard.py

The final file will be:

Automated_Sales_Report.xlsx
🔄 Analytical Workflow
Raw Data
   ↓
Duplicate Removal
   ↓
Missing Value Handling
   ↓
Date Processing
   ↓
KPI Calculation
   ↓
Business Aggregation
   ↓
Excel Workbook
   ↓
Dashboard & Charts
🎯 Project Highlights
20,000+ business records
Automated Excel report generation
Automated KPI calculation
Automated summary tables
Automated Excel charts
Data-cleaning workflow
Reusable Python scripts
Portfolio-ready business reporting workflow
🚀 Future Improvements
Automated email delivery of reports
Scheduled daily/weekly reporting
Excel conditional formatting
More advanced dashboard controls
Power BI integration
Automated PDF report generation
Database integration
👤 Author

Shivakant

Data Analyst | Python | Pandas | Advanced SQL | Power BI | Excel | Data Visualization

GitHub: https://github.com/shivakant-data

📌 Project Purpose

This project demonstrates practical Python-based Excel automation for business reporting and data analyst workflows.

It is designed to show how repetitive manual Excel reporting tasks can be converted into a reproducible and automated Python pipeline.    