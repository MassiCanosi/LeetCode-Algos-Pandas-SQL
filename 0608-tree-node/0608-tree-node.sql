/* Write your T-SQL query statement below */
SELECT 
id
, CASE
    WHEN p_id IS NULL THEN 'Root'
    WHEN p_id IS NOT NULL AND id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
    WHEN p_id IS NOT NULL AND id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
    END AS type
FROM Tree