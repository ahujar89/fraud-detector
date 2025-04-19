# Step 1: Import pandas
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv('data/synthetic_fraud_transactions.csv')

# Step 3: Print the first few rows
print("First 5 records:")
print(df.head())

# Step 4: Print column names and data types
print("\n Column names and types:")
print(df.dtypes)

# Step 5: Check shape (rows, columns)
print("\n Dataset shape (rows, columns):")
print(df.shape)

# Step 6: Count null values per column
print("\n Null values per column:")
print(df.isnull().sum())

# Step 7: Count duplicate rows
print("\n Number of duplicate rows:")
print(df.duplicated().sum())