/* Write your PL/SQL query statement below */
select
a.name
from Customer a
where referee_id is null
or referee_id != 2