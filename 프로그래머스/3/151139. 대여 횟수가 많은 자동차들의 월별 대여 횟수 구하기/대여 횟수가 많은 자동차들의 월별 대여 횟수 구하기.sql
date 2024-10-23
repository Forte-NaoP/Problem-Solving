SELECT 
    MONTH(RH.START_DATE) AS MONTH,
    RH.CAR_ID AS CAR_ID,
    COUNT(1) AS RECORDS
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY RH
JOIN (
    SELECT
        CAR_ID
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE
        EXTRACT(YEAR_MONTH FROM START_DATE) BETWEEN "202208" AND "202210"
    GROUP BY
        CAR_ID
    HAVING
        COUNT(1) >= 5) AS PR
ON 
    RH.CAR_ID = PR.CAR_ID
WHERE
    EXTRACT(YEAR_MONTH FROM START_DATE) BETWEEN "202208" AND "202210"
GROUP BY
    RH.CAR_ID,
    EXTRACT(YEAR_MONTH FROM RH.START_DATE)
HAVING 
    RECORDS > 0
ORDER BY
    MONTH(RH.START_DATE) ASC,
    RH.CAR_ID DESC;

    
    
    