-- list all the tables of a database in your MySQL server
SELECT Tables_in_mysql
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'mysql'