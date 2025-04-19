import pandas as pd

# Step 1: Load the cleaned data
df = pd.read_csv('../data/cleaned_transactions.csv')

# Step 2: Initialize flagged column
df['flagged_fraud'] = 0

# Step 3: Rule 1 - High amount + new device
device_counts = df['device_id'].value_counts()
new_devices = device_counts[device_counts == 1].index
df.loc[(df['amount'] > 500) & (df['device_id'].isin(new_devices)), 'flagged_fraud'] = 1

# Step 4: Rule 2 - Amount > $750
df.loc[df['amount'] > 750, 'flagged_fraud'] = 1

# Step 5: Rule 3 - Unknown location
df.loc[df['location'] == 'Unknown', 'flagged_fraud'] = 1

# Step 6: Summary stats
print("Rule-based fraud detection complete.")
print(df['flagged_fraud'].value_counts())

# Step 7: Save to new file
df.to_csv('../data/flagged_transactions.csv', index=False)
print("Flagged transactions saved to 'flagged_transactions.csv'")