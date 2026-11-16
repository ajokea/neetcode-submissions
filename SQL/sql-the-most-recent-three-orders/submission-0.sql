-- Write your query below
SELECT name AS customer_name,
       c.customer_id,
       order_id,
       order_date
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE (
    SELECT COUNT(*)
    FROM orders o2
    WHERE o.customer_id = o2.customer_id
    AND o2.order_date > o.order_date
) < 3
ORDER BY customer_name, customer_id, order_date DESC;