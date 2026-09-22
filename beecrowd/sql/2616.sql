select a.id,a.name
from customers a
where a.id not in(select id_customers from locations)