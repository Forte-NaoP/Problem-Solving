SELECT CONCAT(MAX(LENGTH), "cm") AS MAX_LENGTH 
FROM FISH_INFO 
WHERE LENGTH IS NOT NULL