-- Write your query below
SELECT c.name AS country
FROM calls
JOIN person p ON id = caller_id OR id = callee_id
JOIN country c ON country_code = SUBSTRING(phone_number, 1, 3)
GROUP BY country_code
HAVING AVG(duration) > (
    SELECT AVG(duration)
    FROM calls
);