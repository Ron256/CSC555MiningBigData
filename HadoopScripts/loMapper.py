#!/usr/bin/python
""" Read the data from stdin and filter it by lo_quantity where it is between 17 and 24
Then print lo_shipmentmode and lo_tax separated by ('\t')
which will be consumed by the reducer. """
import sys
for line in sys.stdin:
        line  = line.strip()
        vals = line.split('|')
        if 17 <= int(vals[8]) <= 24:
                valsT = vals[16].strip()
                valsT = valsT.replace(' ','_')
                print('%s\t%d' %(valsT, int(vals[14])))