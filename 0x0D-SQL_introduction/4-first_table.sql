-- creates a table called first_table in the current database
USE mysql;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);