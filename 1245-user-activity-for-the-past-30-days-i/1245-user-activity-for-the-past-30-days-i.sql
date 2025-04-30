/* Write your T-SQL query statement below */

-- This table may have duplicate rows.
-- each session belongs to exactly one user.
SELECT 
activity_date as DAY
, COUNT(DISTINCT user_id) AS active_users
FROM Activity A
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27' 
GROUP BY
activity_date