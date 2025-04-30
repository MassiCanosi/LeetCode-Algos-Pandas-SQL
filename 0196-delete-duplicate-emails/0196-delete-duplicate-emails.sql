/* Write your T-SQL query statement below */
DELETE a FROM (
    SELECT 
    id
    , email
    , ROW_NUMBER() OVER(PARTITION BY email ORDER BY id ASC) RN
    from Person
) a
WHERE a.RN > 1