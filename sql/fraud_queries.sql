-- Total flagged vs unflagged transactions
SELECT flagged_fraud, COUNT(*) AS count
FROM transactions
GROUP BY flagged_fraud;

-- Fraud rate by flagged status
SELECT flagged_fraud,
       ROUND(SUM(is_fraud)*1.0/COUNT(*), 3) AS fraud_rate
FROM transactions
GROUP BY flagged_fraud;

-- Top 5 users with most frauds
SELECT user_id, COUNT(*) AS fraud_count
FROM transactions
WHERE is_fraud = 1
GROUP BY user_id
ORDER BY fraud_count DESC
LIMIT 5;

-- Fraud count by location
SELECT location, COUNT(*) AS frauds
FROM transactions
WHERE is_fraud = 1
GROUP BY location
ORDER BY frauds DESC
LIMIT 10;

-- Average amount of flagged vs unflagged
SELECT flagged_fraud, ROUND(AVG(amount), 2) AS avg_amount
FROM transactions
GROUP BY flagged_fraud;