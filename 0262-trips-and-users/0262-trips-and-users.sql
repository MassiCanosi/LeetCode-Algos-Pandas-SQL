WITH client_clean AS (
    SELECT 
    T.client_id
    FROM Trips T
    JOIN Users U 
        ON T.client_id = U.users_id
    WHERE 
    U.banned = 'No'
), driver_clean AS (
    SELECT 
    T.driver_id
    FROM Trips T
    JOIN Users U 
        ON T.driver_id = U.users_id
    WHERE 
    U.banned = 'No'
), OTP AS (
SELECT 
request_at AS Day
, COUNT(DISTINCT id) AS [Total Requests]
, COUNT(DISTINCT 
    CASE 
            WHEN status IN ('cancelled_by_driver', 'cancelled_by_client') 
            THEN id 
            END
        ) AS [Cancelled]
FROM Trips
WHERE client_id IN (SELECT * FROM client_clean)
AND driver_id IN (SELECT * FROM driver_clean)
GROUP BY 
request_at
)
SELECT 
Day
, ROUND((1.0*[Cancelled]) / (1.0*[Total requests]), 2) AS [Cancellation Rate]
FROM OTP 
WHERE Day BETWEEN '2013-10-01' AND '2013-10-03'