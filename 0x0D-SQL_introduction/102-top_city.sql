-- display top 3 cities in 'temperatures.sql' during july and august
-- order by temp DESC
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
