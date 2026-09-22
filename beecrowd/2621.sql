SELECT A.NAME FROM products A
JOIN providers B ON B.ID = A.id_providers
 WHERE amount BETWEEN 10 AND 20
 AND B.NAME LIKE 'P%'