-- A script that creates a table called second_table and inserts multiple rows

-- Create the table second_table
CREATE TABLE IF NOT EXISTS second_table (
    id INT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL
);

-- Insert multiple rows into second_table
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
