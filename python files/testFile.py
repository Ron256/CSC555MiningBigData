# print('MFGR#2121'[-4:])

#!/usr/bin/python
# import sys

# fd = open('dwdate.tbl', 'r')
# lines = fd.readlines()
# fd.close()

# dDict = {}

# for line in lines:
#     vals= line.split('|')
#     if vals[12] == 'Fall':
#         dDict[vals[0]] = int(vals[4])

# for line in sys.stdin:
#    line = line.strip()
#    vals = line.split('|')

#    # lo_orderdate = d_datekey
#    if vals[6].find('-') > 0:
#        # partkey, dYear,  revenue
#        if vals[5] in dDict.keys():
#            print(vals[3] + '\t' + str(dDict[vals[5]]) + '\t' + vals[12] + '\t' + 'LO')
#    else:
#         if vals[2][:4] == 'MFGR':
#             if len(vals[4]) == 9: 
#                 if int('MFGR#2121'[-4:]) <= int(vals[4][-4:])  <= int('MFGR#2138'[-4:]):
#                     # print partKey, brandl
#                     print(vals[0] + '\t' + vals[4] + '\t' + 'Part')




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
import numpy as np

# currentKey = None
# key = ''
# pointL = []

# for line in sys.stdin:
# # for line in listOfWords:
#     vals = line.strip().split('|')
#     key = vals[0]
#     if currentKey == key:
#         pointL.append(vals[1].split(','))  # a list of strings to a list
#     else:
#         if currentKey:
#             lenPointsL = len(pointL)
#             if lenPointsL > 0:
#                 pointsArray = np.array(pointL)                      # convert the list of list of strings to an array
#                 pointsArray = pointsArray.astype(np.float)          # convert the array of strings to an array of float
#                 # print('Now printing %s'%(pointsArray))
#                 recs = pointsArray.shape[0]                         # get the number of records from the shape
#                 columns = pointsArray.shape[1]                      # get the number of columns from the shape
#                 cStr = []
#                 # loop through the columns of the numpy array to find the average of each column
#                 for col in range(columns):
#                     cStr.append(float(np.sum(pointsArray[0:recs, col])) / float(len(pointsArray[0:recs, col])))
#                 # print(str(cStr[0]))
#                 numericStr = str(cStr[0]) + '|' + str(cStr[1]) + '|' + str(cStr[2]) + '|' + str(cStr[3]) + '|' + str(cStr[4]) + '|' + str(cStr[5])
#                 print('%s\t%s' %(currentKey, numericStr))

#         # re-initialize the variables when the keys are not the same before adding.
#         pointL = []
#         currentKey = key
#         pointL.append(vals[1].split(','))  # a list of strings to a list
# if currentKey == key:
#     lenPointsL = len(pointL)
#     if lenPointsL > 0:
#         pointsArray = np.array(pointL)                      # convert the list of list of strings to an array
#         pointsArray = pointsArray.astype(np.float)          # convert the array of strings to an array of float
#         # print('Now printing %s'%(pointsArray))
#         recs = pointsArray.shape[0]                         # get the number of records from the shape
#         columns = pointsArray.shape[1]                      # get the number of columns from the shape
#         cStr = []
#         # loop through the columns of the numpy array to find the average of each column
#         for col in range(columns):
#             cStr.append(float(np.sum(pointsArray[0:recs, col])) / float(len(pointsArray[0:recs, col])))
#         numericStr = str(cStr[0]) + '|' + str(cStr[1]) + '|' + str(cStr[2]) + '|' + str(cStr[3]) + '|' + str(cStr[4]) + '|' + str(cStr[5])
#         print('%s\t%s' %(currentKey, numericStr))


currentKey = None
sumA = 0
sumB = 0
sumC = 0
sumD = 0
sumE = 0
sumF = 0
cnt = 0
centerKey = None

# for line in sys.stdin:
for line in listOfWords:
    key, a, b, c, d, e, f = line.strip().split('|')
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
    except ValueError: # if a value wasn't a number, so silently ignore/discard this line. 
        continue 
    if currentKey == key:
        sumA += a
        sumB += b
        sumC += c
        sumD += d
        sumE += e
        sumF += f
        cnt += 1
        centerKey = key

    else:
        if currentKey:
            numericStr = str(sumA/cnt) + ',' + str(sumB/cnt) + ',' + str(sumC/cnt) + ',' + str(sumD/cnt) + ',' + str(sumE/cnt) + ',' + str(sumF/cnt)    
            print('%s|%s' %(centerKey, numericStr))

        # re-initialize the variables when the keys are not the same before adding.
        sumA = 0
        sumB = 0
        sumC = 0
        sumD = 0
        sumE = 0
        sumF = 0
        cnt = 0
        centerKey = ''
        currentKey = key
        sumA = a
        sumB = b
        sumC = c
        sumD = d
        sumE = e
        sumF = f
        cnt = 1

# print the last rows
if currentKey == key:
    numericStr = str(sumA/cnt) + ',' + str(sumB/cnt) + ',' + str(sumC/cnt) + ',' + str(sumD/cnt) + ',' + str(sumE/cnt) + ',' + str(sumF/cnt)
    print('%s|%s' %(centerKey, numericStr))

    
