-- Write your query below
SELECT customer_id, product_id, product_name
FROM (
    SELECT 
       c.customer_id,
       o.product_id,
       p.product_name,
       RANK() OVER (PARTITION BY c.customer_id ORDER BY COUNT(*) DESC) AS rnk
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.customer_id, o.product_id, p.product_name)
WHERE rnk = 1;