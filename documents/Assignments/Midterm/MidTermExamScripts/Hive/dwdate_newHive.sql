

create table dwdate_new (
  dn_datekey            int,
  dn_date               varchar(19),
  dn_dayofweek          varchar(10),
  dn_month              varchar(10),
  dn_year               int,
  dn_yearmonthnum       int,
  dn_yearmonth           varchar(8),
  dn_daysinwkmonthyr varchar(50),
  dn_monthnuminyear int,
  dn_sellingseason      varchar(13),
  dn_lastdayinweekfl    varchar(1),
  dn_Holidayfl          varchar(1),
  dn_weekdayfl          varchar(1)
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY '\t' STORED AS TEXTFILE;

add FILE dwdateTransform.py;

INSERT OVERWRITE TABLE dwdate_new
SELECT TRANSFORM (d_datekey, d_date, d_dayofweek, d_month, d_year, d_yearmonthnum, d_yearmonth, d_daynuminweek, d_daynuminmonth, d_daynuminyear, d_monthnuminyear, d_sellingseason, d_lastdayinweekfl, d_holidayfl, d_weekdayfl)
USING 'python dwdateTransform.py'
AS (dn_datekey, dn_date, dn_dayofweek, dn_month, dn_year, dn_yearmonthnum, dn_yearmonth
, dn_daysinwkmonthyr, dn_monthnuminyear, dn_sellingseason
, dn_lastdayinweekfl, dn_Holidayfl, dn_weekdayfl)
FROM dwdate;















, 



   


