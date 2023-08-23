#!/usr/bin/python
# Author: Ronaldlee Ejalu
# CSC 555 Mining Big Data
# MidTerm Exam
# dwdateTransform.py
import sys

for lines in sys.stdin:
        columnList = []
        strippedLines = lines.strip()         # remove any white spaces
        lines = strippedLines.split('\t')  # split the string to create a list of words
        d_datekey  = lines[0]
        d_date  = lines[1]
        d_dayofweek = lines[2]
        d_month = lines[3]
        d_year  = lines[4]
        d_yearmonthnum = lines[5]
        d_yearmonth =  lines[6]
        d_daynuminweek  = lines[7]
        d_daynuminmonth = lines[8]
        d_daynuminyear  = lines[9]
        d_daysinwkmonthyr  = d_daynuminweek  + '|' + d_daynuminmonth  + '|' + d_daynuminyear
        d_monthnuminyear = lines[10]
        d_sellingseason = lines[11]
        d_lastdayinweekfl = lines[12]
        d_holidayfl = lines[13]
        d_weekdayfl = lines[14]


        print(d_datekey + '\t' + d_date + '\t' + d_dayofweek + '\t' + d_month + '\t' + d_year + '\t' + d_yearmonthnum + '\t' + d_yearmonth + '\t' + d_daysinwkmonthyr + '\t' +  d_monthnuminyear + '\t' + d_sellingseason + '\t' + d_lastdayinweekfl + '\t' + d_holidayfl + '\t' + d_weekdayfl)


