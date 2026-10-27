SET FEEDBACK OFF;

select * from (select name || '('||substr(occupation,0,1)||')' from OCCUPATIONS order by name)
 union all
 select * from (
 select 'There are a total of '||count(*)||' '||lower(occupation)||'s.' 
   from OCCUPATIONS 
  group by occupation
  order by count(*) asc, occupation asc);
 
exit;