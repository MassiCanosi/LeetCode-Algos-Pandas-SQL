/* Write your T-SQL query statement below */
SELECT 
query_name
, ROUND(AVG(CAST(rating AS FLOAT)/CAST (position AS FLOAT)),2) AS quality
, ROUND(100*(SUM(CASE WHEN rating < 3 THEN 1.0 ELSE 0.0 END) / COUNT(query_name)),2) AS poor_query_percentage
FROM Queries 
WHERE 
query_name is not null
GROUP BY 
query_name