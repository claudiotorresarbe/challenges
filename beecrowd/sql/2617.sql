select a.name, b.name
  from products a
  left join providers b on b.id = a.id_providers
 where b.name = 'Ajax SA'