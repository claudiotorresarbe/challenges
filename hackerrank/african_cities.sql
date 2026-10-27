SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;

select city.name from city, country where country.code = city.countrycode 
and country.continent = 'Africa';
exit;