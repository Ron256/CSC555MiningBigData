/* Part 1
select c_nation, AVG(lo_extendedprice) as AVGL
from customer, lineorder
where lo_custkey = c_custkey
  and c_region = 'AFRICA' 
  and lo_discount = 6 OR lo_discount > 8
group by c_nation
order by AVGL;

*/


Customer = LOAD '/data/customer.tbl' using PigStorage('|') AS (c_custkey: int, c_name: chararray, c_address: chararray, c_city: chararray
, c_nation: chararray, c_region: chararray, c_phone: chararray, c_mktsegment: chararray);

Lineorder = LOAD '/data/lineorder.tbl.sample' using PigStorage('|') AS (lo_orderkey: int, lo_linenumber: int, lo_custkey: int, lo_partkey: int, 
lo_suppkey: int, lo_orderdate: int, lo_orderpriority: chararray, lo_shippriority: chararray, lo_quantity: int, lo_extendedprice: int, 
  lo_ordertotalprice: int, lo_discount: int,lo_revenue: int, lo_supplycost: int, 
  lo_tax: int, lo_commitdate: int, lo_shipmode: chararray );
CustFilt = FILTER Customer BY c_region == 'AFRICA';
LineorderFilt = FILTER Lineorder BY lo_discount == 6 OR lo_discount > 8;
CLJoin = JOIN CustFilt BY c_custkey, LineorderFilt BY lo_custkey;
GBycNation = Group CLJoin BY c_nation;
AggExtendedPrice = FOREACH GBycNation GENERATE group, AVG(CLJoin.lo_extendedprice);
SAggExtendedPrice = ORDER AggExtendedPrice BY $1;
STORE SAggExtendedPrice INTO 'out_u_customerlineorder' USING PigStorage('|');


 c_custkey: int, c_name: chararray,c_address: chararray, c_city: chararray,c_nation: chararray,c_region: chararray,c_phone: chararray,c_mktsegment: chararray

 