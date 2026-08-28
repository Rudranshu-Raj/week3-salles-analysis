import pandas as pd

df = pd.read_csv("sales_data.csv")

#Displaying first 5 rows
print("===== FIRST 5 ROWS =====")
print(df.head())

#Displaying number of rows and columns
print("\n===== DATASET SHAPE =====")
print(df.shape)

#Displaying Column names
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

#Displaying data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

#Displaying missing values
print("\n===== MISSING VALIUES =====")
print(df.isnull().sum())

#Displaying duplicate rows
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# ======================
# DATA CLEANING
# ======================

# Convert date column to date-time format
df["Date"] = pd.to_datetime(df["Date"])

# Fill missing Price values using the median price
df["Price"] = df["Price"].fillna(df["Price"].median())

# Remove duplicate records
df = df.drop_duplicates()

# Check whether missing values remain
print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

# Check number of duplicates after cleaning
print("\n===== DUPLICATES AFTER CLEANING =====")
print(df.duplicated().sum())

# Display cleaned data
print("\n===== CLEANED DATA =====")
print(df)

# ==========================================
# SALES ANALYSIS
# ==========================================

# Calculate revenue for each sales record
df["Revenue"] = df["Quantity"] * df["Price"]

# 1. Total Revenue
total_revenue = df["Revenue"].sum()

# 2. Total Units Sold
total_units = df["Quantity"].sum()

# 3. Best-Selling Product by Quantity
product_quantity = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_quantity.idxmax()
best_selling_quantity = product_quantity.max()

# 4. Best Product by Revenue
product_revenue = df.groupby("Product")["Revenue"].sum()
highest_revenue_product = product_revenue.idxmax()
highest_product_revenue = product_revenue.max()

# 5. Average Order Value
average_order_value = df["Revenue"].mean()

# 6. Number of Sales Records
number_of_sales = len(df)

# Display results
print("\n==========================================")
print("           SALES ANALYSIS")
print("==========================================")

print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Total Units Sold    : {total_units}")
print(f"Number of Records   : {number_of_sales}")

print(f"\nBest-Selling Product: {best_selling_product}")
print(f"Units Sold          : {best_selling_quantity}")

print(f"\nHighest Revenue Product: {highest_revenue_product}")
print(f"Revenue               : ₹{highest_product_revenue:,.2f}")

print(f"\nAverage Order Value  : ₹{average_order_value:,.2f}")


# ==========================================
# PRODUCT-WISE SUMMARY
# ==========================================

product_summary = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum")
).sort_values("Total_Revenue", ascending=False)

print("\n===== PRODUCT-WISE SUMMARY =====")
print(product_summary)



# ==========================================
# CREATE FINAL REPORT
# ==========================================

report = f"""
==========================================
        SALES DATA ANALYSIS REPORT
==========================================

DATASET SUMMARY
------------------------------------------
Number of Records : {number_of_sales}
Total Units Sold  : {total_units}

SALES METRICS
------------------------------------------
Total Revenue     : ₹{total_revenue:,.2f}
Average Order Value: ₹{average_order_value:,.2f}

PRODUCT PERFORMANCE
------------------------------------------
Best-Selling Product       : {best_selling_product}
Units Sold                 : {best_selling_quantity}

Highest Revenue Product    : {highest_revenue_product}
Revenue Generated          : ₹{highest_product_revenue:,.2f}

PRODUCT-WISE SUMMARY
------------------------------------------
{product_summary.to_string()}

REGION-WISE SUMMARY
------------------------------------------
{region_summary.to_string()}

INSIGHTS
------------------------------------------
1. {best_selling_product} is the best-selling product
   based on total quantity sold.

2. {highest_revenue_product} generates the highest
   revenue among all products.

3. The dataset was cleaned by filling the missing
   price value using the median.

4. Duplicate records were removed before analysis.

==========================================
            END OF REPORT
==========================================
"""

# Save report to a text file
with open("sales_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nReport successfully created: sales_report.txt")