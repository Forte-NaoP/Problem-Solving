SELECT 
    T.CAR_TYPE,
    COUNT(1) AS CARS
FROM (
    SELECT 
        CAR_TYPE
    FROM 
        CAR_RENTAL_COMPANY_CAR 
    WHERE
        FIND_IN_SET("가죽시트", OPTIONS) OR
        FIND_IN_SET("열선시트", OPTIONS) OR
        FIND_IN_SET("통풍시트", OPTIONS)
) AS T
GROUP BY
    T.CAR_TYPE
ORDER BY
    T.CAR_TYPE ASC