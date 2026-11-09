-- Write your query below
WITH counts AS (
    SELECT player_id,
        player_name,
        year,
        CASE
            WHEN wimbledon = player_id THEN 1
            ELSE 0
        END AS wimbledon,
        CASE
            WHEN fr_open = player_id THEN 1
            ELSE 0
        END AS fr_open,
        CASE
            WHEN us_open = player_id THEN 1
            ELSE 0
        END AS us_open,
        CASE 
            WHEN au_open = player_id THEN 1
            ELSE 0
        END AS au_open
FROM players
CROSS JOIN championships
)

SELECT player_id, 
        player_name,
        SUM(wimbledon + fr_open + us_open + au_open) AS grand_slams_count
FROM counts
GROUP BY player_id, player_name
HAVING SUM(wimbledon + fr_open + us_open + au_open) > 0;