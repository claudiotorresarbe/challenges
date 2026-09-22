select a.name, b.name, c.name
  from products a
  left join providers b on b.id = id_providers
  left join categories c on c.id = id_categories
  where b.name = 'Sansul SA'
  and c.name = 'Imported'