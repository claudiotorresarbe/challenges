select
a.id
,a.name
from movies a
left join genres b on b.id = a.id_genres 
where b.description = 'Action'