-- 코드를 입력하세요
SELECT fh.FLAVOR 
FROM FIRST_HALF as fh
LEFT JOIN ICECREAM_INFO as ii
USING (FLAVOR)
WHERE fh.TOTAL_ORDER > 3000 and ii.INGREDIENT_TYPE = "fruit_based"
ORDER BY fh.TOTAL_ORDER DESC;