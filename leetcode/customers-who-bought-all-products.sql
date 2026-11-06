/* Write your PL/SQL query statement below */
select 
a.customer_id
from Customer a
group by a.customer_id
having count(distinct a.product_key) = (select count(*) from Product)