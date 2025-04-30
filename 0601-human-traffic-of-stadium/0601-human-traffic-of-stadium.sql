/* Write your T-SQL query statement below */
WITH CTE AS (
SELECT
visit_date
, id
, LAG(id) OVER(ORDER BY visit_date ASC) AS lag_1
, LAG(id, 2) OVER(ORDER BY visit_date ASC) AS lag_2
, LEAD(id) OVER(ORDER BY visit_date ASC) AS lead_1
, LEAD(id, 2) OVER(ORDER BY visit_date ASC) AS lead_2
, people
FROM Stadium 
WHERE people >= 100
) 
SELECT 
id
, visit_date
, people
FROM CTE
WHERE 
(
    (id - lag_1 = 1 AND id - lag_2 = 2)
    OR 
    (lead_1 - id = 1 AND lead_2 - id = 2)
    OR 
    (id - lag_1 = 1 AND lead_1 - id = 1)
)
ORDER BY 1 ASC, 2 ASC