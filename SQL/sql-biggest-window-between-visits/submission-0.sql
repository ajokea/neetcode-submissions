-- Write your query below
SELECT
    user_id,
    MAX(wndw) AS biggest_window
FROM (
    SELECT
        user_id,
        visit_date,
        LEAD(visit_date, 1, DATE('2021-1-1')) OVER (PARTITION BY user_id ORDER BY visit_date) - visit_date AS wndw,
        RANK() OVER (PARTITION BY user_id ORDER BY visit_date) AS rnk
    FROM user_visits)
GROUP BY user_id
ORDER BY user_id;