import pandas as pd

# Load flagged data
df = pd.read_csv("../data/flagged_transactions.csv")

# Q1: How many transactions were flagged?
flagged_count = df['flagged_fraud'].sum()
total = len(df)
print(f"Flagged transactions: {flagged_count}/{total} ({round(100 * flagged_count/total, 2)}%)")

# Q2: How many of those flagged were actually frauds?
correct_flags = df[(df['flagged_fraud'] == 1) & (df['is_fraud'] == 1)].shape[0]
total_frauds = df[df['is_fraud'] == 1].shape[0]
print(f"Correctly flagged frauds: {correct_flags}/{total_frauds} ({round(100 * correct_flags/total_frauds, 2)}%)")

# Q3: Top 5 users by number of flagged transactions
print("\nTop 5 users by flagged transactions:")
print(df[df['flagged_fraud'] == 1]['user_id'].value_counts().head())

# Q4: Top 5 merchants with most fraud
print("\nTop 5 merchants with actual fraud:")
print(df[df['is_fraud'] == 1]['merchant'].value_counts().head())

# Q5: Average amount: fraud vs non-fraud
print("\nAverage amount for fraud vs non-fraud:")
print(df.groupby('is_fraud')['amount'].mean())

# Q6: Average amount for flagged vs not flagged
print("\nAverage amount for flagged vs not flagged:")
print(df.groupby('flagged_fraud')['amount'].mean())