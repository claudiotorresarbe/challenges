select
name,
investment,
min(month) as month,
min(saldo-investment) as return
from (
  select 
  a.name,
  b.month,
  a.investment,
  b.profit,
  sum(b.profit) over (partition by b.client_id order by b.client_id, b.month) as saldo
  from clients a
  left join operations b on b.client_id = a.id
) as sub
where 1 = 1
and saldo-investment >= 0
group by name,investment
order by 4 desc