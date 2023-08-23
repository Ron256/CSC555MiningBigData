-- Author: Ronaldlee Ejalu
-- CSC 555 Mining Big Data
-- MidTerm Exam
-- Script 0ne

/* SELECT lo_discount, AVG(lo_extendedprice)
FROM lineorder
GROUP BY lo_discount;
*/

/*
To run this script at the command line shell:

bin/pig -f lineorderpart1.pig
*/


Ulineorder = LOAD '/user/ec2-user/lineorder.tbl' USING PigStorage('|')
 AS (lo_discount:int, lo_extendedprice:int);
 lineorder_groups = GROUP Ulineorder BY lo_discount;
 lineorder_avgs = FOREACH lineorder_groups GENERATE Ulineorder.lo_discount,  AVG(Ulineorder.lo_extendedprice);
 DUMP lineorder_avgs;
