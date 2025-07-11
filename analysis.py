import os

print("Current Directory:", os.getcwd())
print("File Exists:", os.path.isfile('smartphone_sales.csv'))

# Import libraries
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(r"C:\Users\DELL\Smartphone Sales Data Analysis\smartphone_sales.csv")

# Preview data
print("Initial Data:\n", df.head())

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Add a new column: Revenue
df['Revenue'] = df['Units_Sold'] * df['Price_per_Unit']

# 1. Total revenue
total_revenue = df['Revenue'].sum()
print(f"\n📈 Total Revenue: ${total_revenue}")

# 2. Total units sold per brand
brand_units = df.groupby('Brand')['Units_Sold'].sum()
print("\n📦 Units Sold by Brand:\n", brand_units)

# 3. Monthly Sales Trend
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Revenue'].sum()
print("\n📅 Monthly Revenue Trend:\n", monthly_sales)

# 4. Region-wise Performance
region_perf = df.groupby('Region')['Revenue'].sum()
print("\n🌍 Region-wise Revenue:\n", region_perf)

# 5. Best-selling model
best_model = df.groupby('Model')['Units_Sold'].sum().idxmax()
print(f"\n🏆 Best-Selling Model: {best_model}")

# 6. Using NumPy - Average selling price
avg_price = np.mean(df['Price_per_Unit'])
print(f"\n💵 Average Selling Price: ${avg_price:.2f}")
