
#Ronaldlee Ejalu
#CSC 555 Big Data Mining
# lineOrder_reducer.py
#!/usr/bin/python
import sys
currentKey = None
loQuantityL = []
loDiscountL = []
for line in sys.stdin:
    line = line.strip()
    splittedLinesL = line.split('\t')                               # split the line to create a list of items  e.g lo_revenue \t  lo_quantity \t lo_dis$

    key = splittedLinesL[0]                                         # pick up the key   [lo_revenue, lo_quantity, lo_discount]

    lo_quantity = splittedLinesL[1]
    lo_discount = splittedLinesL[2]
    if currentKey == key: #same key
        loQuantityL.append(int(lo_quantity))
        loDiscountL.append(int(lo_discount))
    else:
        if currentKey: # derive the maximum quantity and discount

            lenQuantity = len(loQuantityL)
            lenDiscount = len(loDiscountL)
            if (lenQuantity * lenDiscount > 0):
                # derive the maximum quantity from a list of lo_quantities
                # derive the maximum discount from a list of lo_discount
                print('%s\t%s\t%s' %(currentKey, str(max(loQuantityL)), str(max(loDiscountL))))

        loQuantityL = []                                        # re-initialize the two lists when the keys are not the same (new key) before adding$
        loDiscountL = []

        currentKey = key
        loQuantityL.append(int(lo_quantity))
        loDiscountL.append(int(lo_discount))

# output the last key
# and computer the maximum quantity and discount of all key's values in the different list
if currentKey == key:
    lenQuantity = len(loQuantityL)
    lenDiscount = len(loDiscountL)
    if (lenQuantity * lenDiscount > 0):
        # derive the maximum quantity from a list of lo_quantities
        # derive the maximum discount from a list of lo_discount
        print('%s\t%s\t%s' %(currentKey, str(max(loQuantityL)), str(max(loDiscountL))))