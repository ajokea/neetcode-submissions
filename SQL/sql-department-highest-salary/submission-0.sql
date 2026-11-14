-- Write your query below
SELECT d.name AS department, e.name AS employee, salary
FROM employee e
JOIN department d ON department_id = d.id
WHERE (department_id, salary) IN (
    SELECT department_id, MAX(salary)
    FROM employee
    GROUP BY department_id
);