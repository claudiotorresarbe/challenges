SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;

select sum(a.population)
  from city a, country b 
 where b.continent = 'Asia'
  and b.code = a.countrycode;
exit;