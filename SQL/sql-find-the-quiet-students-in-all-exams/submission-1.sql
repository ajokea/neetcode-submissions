-- Write your query below
WITH loud_scores AS (
    SELECT
        exam_id,
        MAX(score) AS max_score,
        MIN(score) AS min_score
    FROM exam
    GROUP BY exam_id
),
loud_students AS (
    SELECT DISTINCT student_id
    FROM exam e
    JOIN loud_scores ls ON e.exam_id = ls.exam_id
    WHERE score = max_score OR score = min_score
)

SELECT student_id, student_name
FROM student
WHERE student_id IN (
    SELECT student_id
    FROM exam) 
    AND student_id NOT IN (
        SELECT student_id
        FROM loud_students)
ORDER BY student_id;