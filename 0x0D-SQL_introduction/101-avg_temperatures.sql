-- display avg temperature in fahrenheit order by tempmin desc
SELECT city, AVG(value) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
