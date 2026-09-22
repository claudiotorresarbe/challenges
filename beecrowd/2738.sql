select
a.name,
round(((math*2)+(specific*3)+(project_plan*5))/10,2) as avg
from candidate a
left join score b on b.candidate_id  = a.id
order by 2 desc