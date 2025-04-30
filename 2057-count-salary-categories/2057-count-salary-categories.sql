/* Write your T-SQL query statement below */
WITH CTE AS (
SELECT
CASE WHEN income < 20000 THEN 1 ELSE 0 end as low_s
, CASE WHEN income between 20000 and 50000 THEN 1 ELSE 0 end as avg_s
, CASE WHEN income > 50000 THEN 1 ELSE 0 end as high_s
FROM Accounts
)
SELECT 
'Low Salary' AS category
, SUM(CTE.low_s) AS accounts_count
FROM CTE 
UNION ALL
SELECT 
'Average Salary' AS category
, SUM(CTE.avg_s) AS accounts_count
FROM CTE 
UNION ALL
SELECT 
'High Salary' AS category
, SUM(CTE.high_s) AS accounts_count
FROM CTE 
