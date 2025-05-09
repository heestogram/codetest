SELECT P.PRODUCT_ID, PRODUCT_NAME, SUM(AMOUNT*PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT P, FOOD_ORDER O
WHERE P.PRODUCT_ID = O.PRODUCT_ID AND PRODUCE_DATE BETWEEN "2022-05-01" AND "2022-05-31"
GROUP BY P.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID;