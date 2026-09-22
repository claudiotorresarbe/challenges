select
a.name,
b.name,
a.price
from products a
left join providers b on b.id = a.id_providers
left join categories c on c.id = id_categories
where c.name = 'Super Luxury'
  and a.price > 1000