SET FEEDBACK OFF;

select distinct city 
  from station 
 where upper(substr(city,0,1)) in('A','E','I','O','U');
exit;