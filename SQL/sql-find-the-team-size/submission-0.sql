-- Write your query below
WITH sizes AS (
    SELECT team_id, COUNT(team_id) AS team_size
    FROM employee
    GROUP BY team_id)

SELECT employee_id, team_size
FROM employee e
JOIN sizes s
ON e.team_id = s.team_id;