SELECT
    queue,
    "left",
    "right"
FROM (
    SELECT 
        a.queue, 
        CASE 
            WHEN next.available AND a.available THEN a.id 
        END AS "left",
        CASE 
            WHEN next.available AND a.available THEN next.id 
        END AS "right"
    FROM chairs a
    LEFT JOIN chairs next 
        ON next.id = a.id + 1 
       AND next.queue = a.queue
) AS sub
WHERE "left" IS NOT NULL 
  AND "right" IS NOT NULL
ORDER BY queue, "left";