select 
case 
when position <=3 then 'Podium: '||team
when position >= (select max(position) from league)-1 then 'Demoted: '||team
end
from
league
where position <=3
   or position >= (select max(position) from league)-1
order by 
position