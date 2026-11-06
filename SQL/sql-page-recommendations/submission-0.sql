-- Write your query below
SELECT DISTINCT page_id AS recommended_page
FROM likes
WHERE user_id IN (
    SELECT user1_id AS uid
    FROM friendship
    WHERE user2_id = 1
    UNION
    SELECT user2_id AS uid
    FROM friendship
    WHERE user1_id = 1
) AND page_id NOT IN (
    SELECT page_id
    FROM likes
    WHERE user_id = 1
);