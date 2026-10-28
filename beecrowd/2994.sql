select b.name,
round( sum((a.hours * 150) + ( (a.hours * 150) * (c.bonus / 100) )) ,1) as salary
from attendances a
left join doctors b on b.id = a.id_doctor
left join work_shifts c on c.id = a.id_work_shift
group by b.name
order by 2 desc