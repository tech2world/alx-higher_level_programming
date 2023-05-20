-- display max temperature of each state
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
