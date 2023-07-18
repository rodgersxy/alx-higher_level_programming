-- script should display the number of records for
-- this score with the label number
SELECT `score`, count( * ) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
