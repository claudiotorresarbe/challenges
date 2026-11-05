select
a.firstname,
a.lastname,
b.city,
b.state
from person a
left join address b on b.personid = a.personid