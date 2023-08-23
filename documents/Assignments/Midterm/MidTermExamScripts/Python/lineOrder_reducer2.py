

# Ronaldlee Ejalu
# CSC 555 Big Data Mining
# lineOrder_reducer2.py

#!/usr/bin/python
import sys

loRevenueL = []
cur_id =  None
key = ''
for line in sys.stdin:

    line = line.strip()
    splittedLines = line.split('\t')
    key = splittedLines[0]
    # lo_revenue = splittedLines[1]
    # print(type(cur_id))
    if cur_id == key:
        loRevenueL.append(int(splittedLines[1]))
    else:
        if cur_id:
            print('%s\t%s'%(cur_id, str(max(loRevenueL))))

        loRevenueL = []
        cur_id = key
        # print(type(cur_id))
        loRevenueL.append(int(splittedLines[1]))
# output the last key
if cur_id == key:
    print('%s\t%s'%(cur_id, str(max(loRevenueL))))