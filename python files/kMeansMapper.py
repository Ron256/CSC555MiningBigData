
import sys
import math
import numpy as np
centerFileName = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\centers.txt'

fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\data1.txt'

def readFile(fileLocation):
    """ Function that generates a list of words"""
    wordL = []                                              # declare an empty list of words
    with open(fileLocation) as fN:
        lines = fN.readlines()                              # read the file and generate a list of strings
        # print(lines.strip())
        # for item in range(len(lines)):                      # Loop through the list of strings
        #     splittedLinesL = lines[item].strip()         # split the string to create a list of words

        #     for splittedItem in range(len(splittedLinesL)): # loop through the list of words and add words to the wordL(list)
        #         if len(splittedLinesL[splittedItem]) == 0:  # if there are empty spaces just pass
        #             pass
        #         else:
        #            wordL.append(splittedLinesL[splittedItem])
        return lines                                     # return a list of words 

listOfWords = readFile(fileLocation)                        # return a list of words
# print(listOfWords)

#!/usr/bin/python
import sys
import math
fd = fd = open('centers', 'r')
lines = fd.readlines()
fd.close()

centroids = []
dDict = {}

for line in lines: # loop through the lines and populate the centers list
    line = line.strip()
    vals = line.split('|')
    dDict[vals[0]] = vals[1]  

# for line in listOfWords:
for line in sys.stdin:
    line = line.strip()
    record = line.split(',')
    minDist = 200000000000000
    index = -1
    for key, value in dDict.items(): 
        try:
            cent = dDict[key]
            centEl = cent.split(',')
            record[0] = float(record[0])
            record[1] = float(record[1])
            record[2] = float(record[2])
            record[3] = float(record[3])
            record[4] = float(record[4])
            record[5] = float(record[5])
        except ValueError:
            continue
        distEuclid = math.sqrt(math.pow(record[0] - float(centEl[0]),2) + math.pow(record[1] - float(centEl[1]), 2) + math.pow(record[2] - float(centEl[2]), 2) \
             + math.pow(record[3] - float(centEl[3]), 2) + math.pow(record[4] - float(centEl[4]), 2) + math.pow(record[5] - float(centEl[5]), 2))

        # determine the point which is closer to the centroid
        if distEuclid <= minDist:
            minDist = distEuclid
            index = key
            points = str(record[0]) + ',' + str(record[1]) + ',' + str(record[2]) + ',' + str(record[3]) + ',' + str(record[4]) + ',' + str(record[5])
    print('%s\t%s' %(index, points))


