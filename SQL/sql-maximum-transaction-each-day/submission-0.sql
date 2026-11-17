-- Write your query below
SELECT transaction_id
FROM transactions t
WHERE amount = (
    SELECT MAX(amount)
    FROM transactions
    WHERE DATE(day) = DATE(t.day)
)
ORDER BY transaction_id;