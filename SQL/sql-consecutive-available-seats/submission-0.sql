-- Write your query below
WITH free_seats AS (
    SELECT seat_id
    FROM cinema
    WHERE free = 1
)

SELECT seat_id
FROM cinema
WHERE free = 1 AND (
    seat_id - 1 IN (SELECT seat_id FROM free_seats) 
    OR seat_id + 1 IN (SELECT seat_id FROM free_seats)
)
ORDER BY seat_id;