-- Write your query below
SELECT project_id, p.employee_id
FROM project p
JOIN employee e ON p.employee_id = e.employee_id
WHERE experience_years = (
    SELECT MAX(experience_years)
    FROM employee e2
    JOIN project p2 ON e2.employee_id = p2.employee_id
    WHERE p.project_id = p2.project_id
);