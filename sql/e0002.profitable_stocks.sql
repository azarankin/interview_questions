SELECT 
    t1.stock_code
FROM 
    price_today t1
JOIN 
    price_tomorrow t2 ON t1.stock_code = t2.stock_code
WHERE 
    t2.price > t1.price
ORDER BY 
    t1.stock_code ASC;




#another version:

SELECT 
    t1.stock_code
FROM 
    price_today t1
CROSS JOIN 
    price_tomorrow t2
WHERE 
    t1.stock_code = t2.stock_code 
    AND t2.price > t1.price
ORDER BY 
    t1.stock_code ASC;
