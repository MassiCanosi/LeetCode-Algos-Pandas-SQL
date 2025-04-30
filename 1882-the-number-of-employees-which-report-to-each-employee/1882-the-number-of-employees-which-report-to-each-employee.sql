/* Write your T-SQL query statement below */
WITH CTE AS (SELECT * FROM Employees)
, CTE1 AS (SELECT 
e1.employee_id
, e1.name
, COUNT(DISTINCT CTE.employee_id) AS reports_count
, ROUND(AVG(CAST(CTE.age AS FLOAT)),0) AS average_age
FROM Employees e1
JOIN CTE
    ON e1.employee_id = CTE.reports_to
GROUP BY 
e1.employee_id
, e1.name
)
SELECT * FROM CTE1 WHERE reports_count > 0 ORDER BY 1
