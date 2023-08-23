
#Ronaldlee Ejalu
#CSC 555 Big Data Mining
# lineOrder_mapper.py
#!/usr/bin/python
import sys
for line in sys.stdin:
        line = line.strip()
        lineorder = line.split('|')
        lo_orderpriority = lineorder[6]
        lo_quantity = lineorder[8]
        lo_discount = lineorder[11]
        lo_revenue = lineorder[12]
        if 'URGENT' in lo_orderpriority:
                print('%s\t%s\t%s' %(lo_revenue, lo_quantity, lo_discount))