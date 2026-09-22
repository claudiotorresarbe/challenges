select
a.name,
b.name
from products a
left join categories b on b.id = a.id_categories 
where a.amount > 100
 and b.id in(1,2,3,6,9)
 order by b.id asc