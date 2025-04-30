/* Write your T-SQL query statement below */
SELECT 
U.user_id AS buyer_id
, U.join_date
, ISNULL(COUNT(DISTINCT O.order_id), 0) AS orders_in_2019
FROM Users U
LEFT JOIN Orders O
    ON U.user_id = buyer_id
    AND YEAR(O.order_date) = 2019
GROUP BY
U.user_id
, U.join_date
ORDER BY 1 ASC