-- Write your query below
SELECT product_name, o.product_id, order_id, order_date
FROM products p
JOIN orders o ON p.product_id = o.product_id
WHERE order_date = (
    SELECT MAX(order_date)
    FROM orders
    WHERE product_id = o.product_id
)
ORDER BY product_name, o.product_id, o.order_id;