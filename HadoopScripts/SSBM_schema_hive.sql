# Author: Ronaldlee Ejalu
# Hadoop queries

create table part (
  p_partkey     int,
  p_name        varchar(22),
  p_mfgr        varchar(6),
  p_category    varchar(7),
  p_brand1      varchar(9),
  p_color       varchar(11),
  p_type        varchar(25),
  p_size        int,
  p_container   varchar(10)    
) ROW FORMAT DELIMITED FIELDS
TERMINATED BY '|' STORED AS TEXTFILE;

# Load the data using:
LOAD DATA LOCAL INPATH '/home/ec2‐user/part.tbl'
OVERWRITE INTO TABLE part;



CREATE TABLE partswapped
(
  p_partkey     int,
  p_name        varchar(22),
  p_mfgr        varchar(6),
  p_category    varchar(7),
  p_brand1      varchar(9),
  p_color       varchar(11),
  p_type        varchar(25),
  p_size        int,
  p_container   varchar(10) 
)
ROW FORMAT DELIMITED FIELDS
TERMINATED BY '\t';
add FILE partSwampedTransform.py;
INSERT OVERWRITE Table partswapped
SELECT TRANSFORM (p_partkey, p_name, p_mfgr, p_category, p_brand1, p_color, p_type, p_size, p_container)
USING 'python partSwampedTransform.py'
AS (p_partkey, p_name, p_mfgr, p_category, p_brand1, p_color, p_type, p_size, p_container) FROM part;

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
/*This is for loading the data*/
LOAD DATA LOCAL INPATH '/home/ec2‐user/lineorder.tbl'
OVERWRITE INTO TABLE lineorder;