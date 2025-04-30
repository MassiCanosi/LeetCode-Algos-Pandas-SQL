/* Write your T-SQL query statement below */
WITH CTE AS (
    SELECT 
    stock_name
    , SUM(CASE WHEN operation = 'Buy' THEN -1.0*Price END) AS Buy
    , SUM(CASE WHEN operation = 'Sell' THEN 1.0*Price END) AS Sell
    FROM Stocks
    GROUP BY 
    stock_name
)
SELECT 
stock_name
, Buy+Sell AS capital_gain_loss
FROM CTE