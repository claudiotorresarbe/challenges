select a.name
     , b.name
 from products a
 left join providers b on b.id =  id_providers
 where a.id_categories = 6