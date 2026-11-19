-- Write your query below
WITH groups AS (
    SELECT
        log_id,
        log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
    FROM logs
)

SELECT
    MIN(log_id) AS start_id,
    MAX(log_id) AS end_id
FROM groups
GROUP BY grp
ORDER BY start_id;