-- Save this SQL script in a file named 'average_temperature.sql'

SELECT city, AVG(temperature) AS avg_temp
FROM temperature_table
GROUP BY city
ORDER BY average_temperature DESC;