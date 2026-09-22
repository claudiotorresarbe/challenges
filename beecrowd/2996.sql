select
a.year,
b.name as sender,
c.name as receiver
from packages a
left join users b on b.id = a.id_user_sender 
left join users c on c.id = a.id_user_receiver 
where (a.year = 2015 or color = 'blue')
  and b.address != 'Taiwan'
  and c.address != 'Taiwan'
order by a.year desc