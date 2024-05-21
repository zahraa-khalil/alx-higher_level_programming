-- A script that lists all records with non-empty names in second_table ordered by score
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
