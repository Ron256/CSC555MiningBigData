

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

Load the data using:
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
add FILE partSwapTransform.py;
INSERT OVERWRITE TABLE partswapped
SELECT TRANSFORM (p_partkey, p_name, p_mfgr, p_category, p_brand1, p_color, p_type, p_size, p_container)
USING 'python partSwapTransform.py'
AS (p_partkey, p_name, p_mfgr, p_category, p_brand1, p_color, p_type, p_size, p_container) FROM part;

#Pig Scripts

INSERT OVERWRITE DIRECTORY 'ThreeColExtract' 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT barrels08, city08, charge120
FROM VehicleData;
#############################################################################################
VehicleDataThreeCols = LOAD '/user/ec2-user/ThreeColExtract/000000_0' USING PigStorage(',') 
AS (barrels08:FLOAT, city08:FLOAT, charge120:FLOAT);

ThreeColsExtract = FOREACH VehicleDataThreeCols GENERATE barrels08, city08, charge120;
STORE ThreeColsExtract INTO 'out_threeColsExtract' USING PigStorage('|');

##############################################################################################
 