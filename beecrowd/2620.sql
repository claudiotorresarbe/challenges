select
a.name,
b.id
from customers a
left join orders b on b.id_customers = a.id 
where b.orders_date between '2016-01-01' and '2016-06-30'