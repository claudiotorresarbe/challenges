/* Write your PL/SQL query statement below */
select 
id,
movie,
description,
to_number(rating) as rating
from Cinema a
where 1 = 1
and mod(id,2) = 1
and description not in('boring')
order by to_number(rating) desc