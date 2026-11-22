-- Write your query below
SELECT employee_id
FROM employees
WHERE employee_id != 1 AND (
    manager_id = 1 OR manager_id IN (
        SELECT employee_id
        FROM employees
        WHERE manager_id = 1
    ) OR (
        manager_id IN (
            SELECT employee_id
            FROM employees
            WHERE manager_id IN (
                SELECT employee_id
                FROM employees
                WHERE manager_id = 1
            )
        )
    )
);