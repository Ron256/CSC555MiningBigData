#!/usr/bin/python
import sys
for line in sys.stdin:
        line  = line.strip()
        vals = line.split('\t')
        if 17 <= int(vals[8]) <= 24:
                valsT = vals[16].strip()
                valsT = valsT.replace(' ','_')
                print('%s\t%d' %(valsT, int(vals[14])))