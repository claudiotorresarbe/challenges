/* Write your PL/SQL query statement below */
select a.name as "Employee"
from employee a
left join employee b on b.id = a.managerid
where 1 = 1
and a.managerid is not null
and a.salary > b.salary