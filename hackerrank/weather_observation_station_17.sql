SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;

select round(long_w,4)
  from station
 where round(lat_n,4) = (select round(min(lat_n),4) from station where lat_n > 38.7780);
exit;