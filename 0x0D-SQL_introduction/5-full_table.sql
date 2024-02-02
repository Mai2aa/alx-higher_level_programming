-- prints  full description of a table
USE hbtn_0c_0
SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'first_table';