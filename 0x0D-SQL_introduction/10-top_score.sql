-- Retrieves all records from the `second_table` table.
-- The records are sorted in descending order based on the score column.
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
