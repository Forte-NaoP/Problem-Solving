WITH RATIO AS (
    SELECT
        CASE 
            WHEN AVG(SCORE) >= 96 THEN 0.2
            WHEN AVG(SCORE) >= 90 THEN 0.15
            WHEN AVG(SCORE) >= 80 THEN 0.1
            ELSE 0
        END AS R,
        CASE 
            WHEN AVG(SCORE) >= 96 THEN "S"
            WHEN AVG(SCORE) >= 90 THEN "A"
            WHEN AVG(SCORE) >= 80 THEN "B"
            ELSE "C"
        END AS GRADE,
        EMP_NO
    FROM
        HR_GRADE
    GROUP BY
        EMP_NO
)

SELECT
    E.EMP_NO,
    E.EMP_NAME,
    R.GRADE,
    E.SAL * R.R AS BONUS
FROM 
    HR_EMPLOYEES E
JOIN 
    RATIO R
ON 
    R.EMP_NO = E.EMP_NO
ORDER BY
    E.EMP_NO
    

