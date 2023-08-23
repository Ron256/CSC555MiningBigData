--d_sellingseason      varchar(13), --12    --10 -- failing
  --d_lastdayinweekfl    varchar(1), --13     --11 --failing
  --d_holidayfl          varchar(1), --15      ---12 
 -- d_weekdayfl          varchar(1)     --16    --13
go


create table dwdate_new (
  d_datekey            int,
  d_date               varchar(19),
  d_dayofweek          varchar(10),
  d_month              varchar(10),
  d_year               int,
  d_yearmonthnum       int,
  d_yearmonth           varchar(8),
  d_daysinwkmonthyr varchar(50),
  d_monthnuminyear int
)
ROW FORMAT DELIMITED FIELDS 
TERMINATED BY '\t';

add FILE dwdateTransform.py;

INSERT OVERWRITE TABLE dwdate_new
SELECT TRANSFORM (d_datekey, d_date, d_dayofweek, d_month, d_year, d_yearmonthnum, d_yearmonth, d_daynuminweek, d_daynuminmonth, d_daynuminyear, d_monthnuminyear)
USING 'python dwdateTransform.py'
AS (d_datekey, d_date, d_dayofweek, d_month, d_year, d_yearmonthnum, d_yearmonth, d_daysinwkmonthyr, d_monthnuminyear)
FROM dwdate;