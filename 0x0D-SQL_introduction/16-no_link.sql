-- Lists all records from the `second_table` table in your MySQL server where the name is not empty.
-- The records are ordered by the score column in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
