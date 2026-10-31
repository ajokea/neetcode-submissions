-- Write your query below
SELECT DISTINCT title
FROM tv_program t
JOIN content c ON t.content_id = c.content_id
WHERE program_date LIKE '2020-06-%' 
AND kids_content = 'Y'
AND content_type = 'Movies';