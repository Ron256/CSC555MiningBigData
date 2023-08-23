-- Author: Ronaldlee Ejalu
-- CSC 555 Mining Big Data
-- MidTerm Exam
-- Script two


/*
SELECT lo_quantity, SUM(lo_revenue)
FROM lineorder
WHERE lo_discount > 8 AND lo_quantity > 33
GROUP BY lo_quantity;
*/

/*
To run this script at the command line shell:

bin/pig -f lineorderpart2.pig
*/

U_lineorder = LOAD '/user/ec2-user/lineorder.tbl' USING PigStorage('|')
 AS (lo_quantity:int, lo_revenue:int, lo_discount:int);
 lo_discount_qty = FILTER U_lineorder BY lo_discount > 8 AND lo_quantity > 33;
 lineorder_grps = GROUP lo_discount_qty BY lo_quantity;
 uLineOrderAgg = FOREACH lineorder_grps GENERATE lo_discount_qty.lo_quantity, SUM(lo_discount_qty.lo_revenue);
 STORE uLineOrderAgg INTO 'out_u_lineorder' USING PigStorage('|');
--DUMP uLineOrderAgg;