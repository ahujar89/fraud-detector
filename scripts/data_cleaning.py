import pandas as pd

# Step 1: Load the messy dataset
df = pd.read_csv('../data/synthetic_fraud_transactions.csv')

# Step 2: Remove duplicate rows
initial_rows = df.shape[0]
df = df.drop_duplicates()
final_rows = df.shape[0]
print(f"Removed {initial_rows - final_rows} duplicate rows.")

# Step 3: Convert 'timestamp' to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Step 4: Convert 'is_fraud' to integer
df['is_fraud'] = df['is_fraud'].fillna(0).astype(int)

# Step 5: Handle missing values
# Drop rows with critical nulls in transaction_id, user_id, amount, timestamp
critical_cols = ['transaction_id', 'user_id', 'amount', 'timestamp']
df = df.dropna(subset=critical_cols)

# Fill other nulls with placeholders
df['merchant'] = df['merchant'].fillna('Unknown')
df['location'] = df['location'].fillna('Unknown')
df['device_id'] = df['device_id'].fillna('N/A')

# Step 6: Save the cleaned dataset
df.to_csv('../data/cleaned_transactions.csv', index=False)
print("Cleaned data saved to 'cleaned_transactions.csv'")