select a.id, a.name 
from products a
left join categories b on b.id = a.id_categories
where b.name like 'super%'