-- Write your query below
WITH order_counts AS (SELECT customer_number, COUNT(*) AS num_orders
FROM orders
GROUP BY customer_number
ORDER BY num_orders DESC)

SELECT customer_number
FROM order_counts
LIMIT 1;