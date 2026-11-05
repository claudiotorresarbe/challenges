/* Write your PL/SQL query statement below */
select customer_number
from (
select customer_number, count(order_number) as qtd
from Orders
where 1 = 1
group by customer_number
order by 2 desc
)
where rownum = 1