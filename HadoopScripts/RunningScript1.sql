
create table dwdate_new (
  d_datekey            int,
  d_date               varchar(19),
  d_dayofweek          varchar(10),
  d_month              varchar(10),
  d_year               int,
  d_yearmonthnum       int,
  d_yearmonth           varchar(8),
  d_daysinwkmonthyr varchar(50),
  d_monthnuminyear int,
  d_sellingseason      varchar(13),
  d_lastdayinweekfl    varchar(1),
  d_holidayfl          varchar(10),
  d_weekdayfl          varchar(1)
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY '\t';

add FILE transform_qa.py;

INSERT OVERWRITE TABLE dwdate_new
SELECT TRANSFORM (d_datekey, d_date, d_dayofweek, d_month, d_year, d_yearmonthnum, d_yearmonth, d_daynuminweek, d_daynuminmonth, d_daynuminyear, d_monthnuminyear, d_sellingseason, d_lastdayinweekfl, d_holidayfl, d_weekdayfl)
USING 'python transform_qa.py'
AS (d_datekey, d_date, d_dayofweek, d_month, d_year, d_yearmonthnum, d_yearmonth, d_daysinwkmonthyr, d_monthnuminyear, d_sellingseason, d_lastdayinweekfl, d_holidayfl, d_weekdayfl)
FROM dwdate;



