/* Write your T-SQL query statement below */
SELECT 
class 
FROM Courses C
GROUP BY 
class
HAVING COUNT(DISTINCT STUDENT) >= 5