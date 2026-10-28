-- Write your query below
WITH june AS (
    SELECT o.customer_id
    FROM orders o
    JOIN product p ON o.product_id = p.product_id
    JOIN customers c ON c.customer_id = o.customer_id
    WHERE order_date BETWEEN '2020-06-01' AND '2020-06-30'
    GROUP BY o.customer_id
    HAVING SUM(quantity * price) >= 100
),

july AS (
    SELECT o.customer_id
    FROM orders o
    JOIN product p ON o.product_id = p.product_id
    JOIN customers c ON c.customer_id = o.customer_id
    WHERE order_date BETWEEN '2020-07-01' AND '2020-07-31'
    GROUP BY o.customer_id
    HAVING SUM(quantity * price) >= 100
)

SELECT customer_id, name
FROM customers
WHERE customer_id IN (SELECT * FROM june) 
    AND customer_id IN (SELECT * FROM july);