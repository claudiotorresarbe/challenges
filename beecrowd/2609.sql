select b.name,sum(amount)
  from products a
  left join categories b on b.id = a.id_categories
  group by b.name