/* Write your T-SQL query statement below */
SELECT
C.id
, C.movie
, C.description
, ROUND(C.rating,1) as rating
FROM Cinema C
WHERE 
C.description NOT LIKE '%boring%'
AND C.id % 2 <> 0
ORDER BY 4 DESC 