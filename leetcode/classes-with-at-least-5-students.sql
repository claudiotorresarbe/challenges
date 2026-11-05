/* Write your PL/SQL query statement below */
select
class
from Courses a
where 1 = 1
group by class
having count(*) >= 5