-- Write your query below
WITH dates AS (
    SELECT 
        'succeeded' AS period_state,
        success_date AS event_date
    FROM succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION ALL 
    SELECT 
        'failed' AS period_state,
        fail_date AS event_date
    FROM failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
),
ranks AS (
    SELECT
        event_date,
        period_state,
        ROW_NUMBER() OVER (ORDER BY event_date) AS row,
        ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY event_date) AS state_row
    FROM dates
),
grps AS (
    SELECT
        event_date,
        period_state,
        row - state_row AS grp
    FROM ranks
)

SELECT
    period_state,
    MIN(event_date) AS start_date,
    MAX(event_date) AS end_date
FROM grps
GROUP BY period_state, grp
ORDER BY start_date;