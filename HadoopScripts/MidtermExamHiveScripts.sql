
create table dwdate (
  d_datekey            int,
  d_date               varchar(19),
  d_dayofweek          varchar(10),
  d_month              varchar(10),
  d_year               int,
  d_yearmonthnum       int,
  d_yearmonth          varchar(8),
  d_daynuminweek       int,
  d_daynuminmonth      int,
  d_daynuminyear       int,
  d_monthnuminyear     int,
  d_weeknuminyear      int,
  d_sellingseason      varchar(13),
  d_lastdayinweekfl    varchar(1),
  d_lastdayinmonthfl   varchar(1),
  d_holidayfl          varchar(1),
  d_weekdayfl          varchar(1)     
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY '|' STORED AS TEXTFILE;


LOAD DATA LOCAL INPATH '/user/ec2-user/dwdate.tbl' 
OVERWRITE INTO TABLE dwdate;



create table lineorder (
  lo_orderkey          int,
  lo_linenumber        int,
  lo_custkey           int,
  lo_partkey           int,
  lo_suppkey           int,
  lo_orderdate         int,
  lo_orderpriority     varchar(15),
  lo_shippriority      varchar(1),
  lo_quantity          int,
  lo_extendedprice     int,
  lo_ordertotalprice   int,
  lo_discount          int,
  lo_revenue           int,
  lo_supplycost        int,
  lo_tax               int,
  lo_commitdate         int,
  lo_shipmode          varchar(10)    
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY '|' STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/home/ec2-user/lineorder.tbl' 
OVERWRITE INTO TABLE lineorder;

create table dwdate (
  d_datekey            int, --0           --1
  d_date               varchar(19), --1    --2
  d_dayofweek          varchar(10), --2    --3
  d_month              varchar(10), --3    --4
  d_year               int, --4            --5
  d_yearmonthnum       int, --5            --6
  d_yearmonth          varchar(8), --6     --7
--   d_daynuminweek       int,--7
--   d_daynuminmonth      int,--8
--   d_daynuminyear       int, --9
  d_monthnuminyear     int,--10            --9
  d_weeknuminyear      int, -- 11 --no
  d_sellingseason      varchar(13), --12    --10
  d_lastdayinweekfl    varchar(1), --13     --11
  d_lastdayinmonthfl   varchar(1),-- 14--no
  d_holidayfl          varchar(1), --15      ---12
  d_weekdayfl          varchar(1)     --16    --13
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY '|' STORED AS TEXTFILE;


LOAD DATA LOCAL INPATH '/home/ec2-user/dwdate.tbl' 
OVERWRITE INTO TABLE dwdate;

create table dwdate_new (
  d_datekey            int,
  d_date               varchar(19),
  d_dayofweek          varchar(10),
  d_month              varchar(10),
  d_year               int,
  d_yearmonthnum       int,
  d_yearmonth           varchar(8),
  d_monthnuminyear     int,
  d_sellingseason      varchar(13),
  d_lastdayinweekfl    varchar(1),
  d_holidayfl          varchar(1),
  d_weekdayfl          varchar(1),
  d_daysinwkmonthyr varchar(50)
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY '\t';

add FILE dwdateTransform.py;

INSERT OVERWRITE TABLE dwdate_new
SELECT TRANSFORM (d_datekey, d_date, d_dayofweek, d_month, d_year, d_yearmonthnum, d_yearmonth, d_monthnuminyear, d_sellingseason, d_lastdayinweekfl, d_holidayfl, d_weekdayfl, d_daynuminweek, d_daynuminmonth, d_daynuminyear)
USING 'python dwdateTransform.py'
AS (d_datekey, d_date, d_dayofweek, d_month, d_year, d_yearmonthnum, d_yearmonth, d_monthnuminyear, d_sellingseason, d_lastdayinweekfl, d_holidayfl, d_weekdayfl, d_daysinwkmonthyr)
FROM dwdate;
