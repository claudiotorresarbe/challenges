SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
Select ROUND(LONG_W,4) from STATION WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345);
exit;