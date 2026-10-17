-- Write your query below
SELECT name, COALESCE(SUM(distance),0) AS travelled_distance
FROM users
LEFT JOIN rides ON users.id = user_id
GROUP BY name
ORDER BY travelled_distance DESC, name;