# Step 1: Install Required Libraries
# Run this command in terminal if not installed: pip install pandas numpy matplotlib seaborn

# Step 2: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 3: Generate Sample Sales Data
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture']
data = {
    'Date': np.random.choice(dates, 200),
    'Category': np.random.choice(categories, 200),
    'Sales_Amount': np.random.randint(100, 1000, 200),
    'Units_Sold': np.random.randint(1, 20, 200)
}
df = pd.DataFrame(data)

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Summary Statistics
print("Summary Statistics:")
print(df.describe())

# Step 4: Visualizations

# Sales Trend Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df.groupby('Date')['Sales_Amount'].sum().reset_index(), x='Date', y='Sales_Amount')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Sales by Category
plt.figure(figsize=(10, 5))
sns.barplot(data=df.groupby('Category', as_index=False)['Sales_Amount'].sum(), x='Category', y='Sales_Amount', palette='viridis')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales Amount')
plt.show()

# Distribution of Sales Amounts
plt.figure(figsize=(10, 5))
sns.histplot(df['Sales_Amount'], bins=20, kde=True, color='blue')
plt.title('Distribution of Sales Amounts')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Scatter Plot: Sales Amount vs. Units Sold
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='Units_Sold', y='Sales_Amount', hue='Category', palette='coolwarm')
plt.title('Sales Amount vs. Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Sales Amount')
plt.grid(True)
plt.show()
