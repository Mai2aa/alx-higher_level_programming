-- create a new database and a new table called cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS cities(
    id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT FOREIGN KEY(states.id) NOT NULL,
    name VARCHAR(256) NOT NULL
);