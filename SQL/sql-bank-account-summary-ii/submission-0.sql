-- Write your query below
SELECT name, SUM(amount) AS balance
FROM transactions t
JOIN users u ON t.account = u.account
GROUP BY u.account, u.name
HAVING SUM(amount) > 10000;