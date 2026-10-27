SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;

select listagg(prime_number,'&') within group(order by prime_number)
  from
(
select l as prime_number
 from (select level l from dual connect by level <= 1000)
   , (select level m from dual connect by level <= 1000)
   where m<=l
   group by l
   having count(case l/m when trunc(l/m) then 'Y' end) = 2
    order by l
);
exit;