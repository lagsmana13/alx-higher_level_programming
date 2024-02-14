-- Retrieves the count of records with the same score from the `second_table` table in your MySQL server.
-- The records are ordered by the count of records in descending order.
SELECT `score`, COUNT(*) AS `record_count`
FROM `second_table`
GROUP BY `score`
ORDER BY `record_count` DESC;
