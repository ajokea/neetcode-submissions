-- Write your query below
WITH RECURSIVE pairs AS (
    SELECT 
        task_id,
        1 AS subtask_id,
        subtasks_count
    FROM tasks
    UNION ALL
    SELECT
        task_id,
        subtask_id + 1,
        subtasks_count
    FROM pairs
    WHERE subtask_id < subtasks_count
)

SELECT 
    p.task_id,
    p.subtask_id
FROM pairs p
LEFT JOIN executed e 
ON p.task_id = e.task_id AND p.subtask_id = e.subtask_id
WHERE e.subtask_id IS NULL;