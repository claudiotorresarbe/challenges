/* Write your PL/SQL query statement below */
select
name as results
from(
select
c.name,
count(*) as qtd,
ROW_NUMBER() OVER(ORDER BY COUNT(*) DESC, c.name ASC) AS rank
from MovieRating a
left join Users c on c.user_id = a.user_id
group by c.name
order by qtd desc
)
where 1 = 1
and rank = 1

union all

select
title as results
from
(
SELECT 
    title,
    RANK() OVER (ORDER BY rt DESC, title ASC) as movie_rank
FROM (
    SELECT
        c.title,
        AVG(a.rating) as rt
    FROM MovieRating a
    LEFT JOIN Movies c ON c.movie_id = a.movie_id
    WHERE TO_CHAR(a.created_at, 'YYYY-MM') = '2020-02'
    GROUP BY c.title
) 
)
where movie_rank = 1