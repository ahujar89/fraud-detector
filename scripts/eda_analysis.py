import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('../data/cleaned_transactions.csv')

# Show basic stats
print("Dataset Overview:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())

# Distribution of transaction amounts
plt.figure(figsize=(8, 4))
sns.histplot(df['amount'], bins=50, kde=True)
plt.title('Transaction Amount Distribution')
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Fraud vs Non-Fraud counts
plt.figure(figsize=(6, 3))
sns.countplot(x='is_fraud', data=df)
plt.title('Fraud vs Non-Fraud Transactions')
plt.xticks([0, 1], ['Not Fraud', 'Fraud'])
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Amounts for Fraud vs Non-Fraud
plt.figure(figsize=(8, 4))
sns.boxplot(x='is_fraud', y='amount', data=df)
plt.title('Transaction Amount by Fraud Type')
plt.xticks([0, 1], ['Not Fraud', 'Fraud'])
plt.tight_layout()
plt.show()

# Fraud rates by location (Top 10 only)
top_locations = df['location'].value_counts().head(10).index
filtered = df[df['location'].isin(top_locations)]

plt.figure(figsize=(10, 5))
sns.countplot(x='location', hue='is_fraud', data=filtered)
plt.title('Fraud Count by Location (Top 10)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()