-- Retrieves all records from the `second_table` table in your MySQL server with a score greater than or equal to 10.
-- The records are ordered by the score column in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
