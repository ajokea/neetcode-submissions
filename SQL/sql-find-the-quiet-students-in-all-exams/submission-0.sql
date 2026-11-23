-- Write your query below
WITH max_scores AS (
    SELECT
        exam_id,
        MAX(score) AS max_score
    FROM exam
    GROUP BY exam_id
),
min_scores AS (
    SELECT
        exam_id,
        MIN(score) AS min_score
    FROM exam
    GROUP BY exam_id
),
loud_students AS (
    SELECT student_id
    FROM exam e
    JOIN max_scores mxs ON e.exam_id = mxs.exam_id AND e.score = max_score
    UNION 
    SELECT student_id
    FROM exam e
    JOIN min_scores mns ON e.exam_id = mns.exam_id AND e.score = min_score
)

SELECT DISTINCT e.student_id, student_name
FROM exam e
JOIN student s ON e.student_id = s.student_id
WHERE e.student_id NOT IN (
    SELECT student_id
    FROM loud_students
)
ORDER BY e.student_id;