
# Ronaldlee Ejalu
# CSC 555 Big Data Mining
# lineOrder_mapper2.py

#!/usr/bin/python
import sys
for line in sys.stdin:
    line = line.strip()
    lineorder = line.split('\t')
    #print(lineorder)
    lo_revenue = lineorder[0]
    lo_quantity = lineorder[1]
    lo_discount = lineorder[2]
    if 4 <= int(lo_discount) <= 8: # if lo_discount is between 4 and 8
        print('%s\t%s' %(lo_quantity, lo_revenue))