-- Write your query below
SELECT c.customer_id, name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN product p ON o.product_id = p.product_id
WHERE order_date BETWEEN '2020-06-01' AND '2020-07-31'
GROUP BY c.customer_id
HAVING 
    SUM(CASE
            WHEN order_date BETWEEN '2020-06-01' AND '2020-06-30'
            THEN price * quantity ELSE 0
        END) >= 100
    AND
    SUM(CASE
            WHEN order_date BETWEEN '2020-07-01' AND '2020-07-31'
            THEN price * quantity ELSE 0
        END) >= 100;