-- Save this SQL script in a file named 'average_temperature.sql'

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;