#!/usr/bin/python
import sys
currentKey = None
loRevenueL = []
key = ''
for line in sys.stdin:
    line = line.strip()
    splittedLines = line.split('\t')                                # lo_quantity \t  lo_revenue
    #print(splittedLines)
    key = splittedLines[0]                                          # pickup the key
    lo_revenue = splittedLines[1]                                   # pickup revenue

    if currentKey == key:
        print('currentKey %s' %currentKey)
        loRevenueL.append(int(lo_revenue))                      # add revenue values to the list
    else:
        if currentKey:                                              # when the key is done derive the maximum revenue per key
            print('%s\t%s'%(currentKey, str(max(loRevenueL))))

        loRevenueL = []                                                 # re-iitialize the list before assigning a new key
        currentkey = key
        loRevenueL.append(int(lo_revenue))
# output the last key
if currentKey == key:
    print('%s\t%s'%(currentKey, str(max(loRevenueL))))
