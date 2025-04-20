import pandas as pd
import sqlite3

# Loading the flagged dataset
df = pd.read_csv("../data/flagged_transactions.csv")

# Connect to SQLite database
conn = sqlite3.connect("../data/fraud_detection.db")

# Loading into SQLite table
df.to_sql("transactions", conn, if_exists="replace", index=False)

print("Data loaded to SQLite as table 'transactions'")
conn.close()