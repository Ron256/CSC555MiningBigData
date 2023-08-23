#!/usr/bin/python
import sys

fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\testData2.txt'

def readFile(fileLocation):
    """ Function that generates a list of words"""
    wordL = []                                              # declare an empty list of words
    with open(fileLocation) as fN:
        lines = fN.readlines()                              # read the file and generate a list of strings

        for item in range(len(lines)):                      # Loop through the list of strings
            splittedLinesL = lines[item].strip().split('\t')         # split the string to create a list of words

            for splittedItem in range(len(splittedLinesL)): # loop through the list of words and add words to the wordL(list)
                if len(splittedLinesL[splittedItem]) == 0:  # if there are empty spaces just pass
                    pass
                else:
                    wordL.append(splittedLinesL[splittedItem])
        return wordL                                        # return a list of words 

listOfWords = readFile(fileLocation)                        # return a list of words
# print('printing the list %s' %listOfWords)





loRevenueL = []
cur_id = None

# key = ''
# for line in sys.stdin:
for line in listOfWords:
    line = line.strip()
    splittedLines = line.split('|')
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

