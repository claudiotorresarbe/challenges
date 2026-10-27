SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;

select b.continent
     , round(avg(a.population)-0.5)
  from city a
  join country b on b.code = a.countrycode
 group by b.continent;
exit;