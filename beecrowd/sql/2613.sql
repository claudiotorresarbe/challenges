select a.id,a.name
from movies a
left join prices b on b.id = id_prices
where value < 2.00