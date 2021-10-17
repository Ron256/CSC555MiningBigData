#!/usr/bin/python
import sys
import numpy as np
"""This file consumes all the data from the mapper and calculates the standard deviation for each key"""


wordL = []                                              # declare an empty list of words
curr_id = None                                          # current Id I am tracking.
id = ''                                                 # id derived from the values of the string.
for item in sys.stdin:# Loop through the list of strings
    cleansedLine =item.strip()               # remove any white spaces

    # remember to put the right delimeter.
    splittedLinesL = cleansedLine.split('\t')         # split the string to create a list of words, in hadoof, it has to be '\t' delimeted
    # print(splittedLinesL)
    id = splittedLinesL[0]                           #  pick up the key
    # print(id, type(splittedLinesL[1]))

    if curr_id == id:                               # if i see the same key, add the value to list
        bagOftax.append(float(splittedLinesL[1]))
    else:
        if curr_id: # compute the standard deviation, once the single current key is completed
            # convert the list into a numpy array
            arr = np.array(bagOftax)

            # compute the standard deviation
            computedStd = np.std(arr, dtype=np.float64)
            print('%s\t%.2f' %(curr_id, computedStd))
        curr_id = id
        bagOftax = []       # reset the list before adding  the value of the next key to the list
        bagOftax.append(float(splittedLinesL[1]))

# output the last key
# and compute the standard deviation of all the key's values in the list.
if curr_id == id:
    arr = np.array(bagOftax)
    computedStd = np.std(arr, dtype=np.float64)
    print('%s\t%.2f' %(curr_id, computedStd))
    # print('%s: %s' %(curr_id, bagOftax))