# Author: Ronadlee Ejalu
# CSC 555 Assignment 1 Python file
# Part 1 Computing the different computations.
import math
import numpy as np
import random
from collections import Counter # merges two dictionaries while preserving the keys.
import urllib.request
import json
import os
import csv
import time
import pandas as pd

print('\n 2 raised to the power of 11 is %s' %(2 ** 11))
print('\n 2 raised to the poweer of 4 which is raised to the power of 4 is %s' %(math.pow(math.pow(2, 4), 4)) )
print('\n 4 raised to the power of 4 is %s' %(4 ** 4))
print('\n 8 raised to the power of 5 is %s' %(8 ** 5))
print('\n 842 MOD 100 = %s' %(842 % 100))
print('\n 837 MOD 20 = %s' %(837 % 20))
print('\n 22 MOD 111 = %s' %(22 % 111))
print('\n 111 MOD 22 = %s' %(111 % 22))
print('**'*30)

# Part b

l1 = [1, 1, 3]
l2 = [1, 2, 2]
V1 = np.array(l1)
V2 = np.array(l2)
M = np.array([[2, 1, 3], [1, 2, 1], [1, 0, 1]])

# print(V1)
# print(V2)
# print(M)

print('\n V2 - V1 = %s' %(V2 - V1))
print('\n V1 + V1 = %s' %(V1 + V1))
print('\n The Euclidean vector length of V1, |V1| = %s'%(np.linalg.norm(V1)))
print('\n The Euclidean vector length of V2, |V2| = %s'%(np.linalg.norm(V2)))
print('\n M * V2.T = \n %s'%(M * V2.T))
print('\n M * M = \n %s'%(M**2))
print('\n M raised to the power of 3 = \n %s' %(M ** 3))
print('**'*30)




# Part 2a
# helper function
def sortDict(consolidatedDict):
    """Function that returns a sorted dictionary in descending order  """

    sortedMergedDict = {key: value for (key, value) in sorted(consolidatedDict.items(), key=lambda wordCnt: wordCnt[1], reverse=True)}
    return sortedMergedDict                                 # return the sorted dictionary 


fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\HadoopBlurb.txt'

def readFile(fileLocation):
    """ Function that generates a list of words"""
    wordL = []                                              # declare an empty list of words
    with open(fileLocation) as fN:
        lines = fN.readlines()                              # read the file and generate a list of strings

        for item in range(len(lines)):                      # Loop through the list of strings
            splittedLinesL = lines[item].split(' ')         # split the string to create a list of words

            for splittedItem in range(len(splittedLinesL)): # loop through the list of words and add words to the wordL(list)
                if len(splittedLinesL[splittedItem]) == 0:  # if there are empty spaces just pass
                    pass
                else:
                    wordL.append(splittedLinesL[splittedItem])
        return wordL                                        # return a list of words 

listOfWords = readFile(fileLocation)                        # return a list of words
# print(listOfWords)
def wordCnt(listOfWords):
    wordCnt = {}                                                # define an empty dictionary
    for i in range(len(listOfWords)):                           # iterate through the list of words and count the number of words
        if listOfWords[i] in wordCnt.keys():
            wordCnt[listOfWords[i]] = wordCnt[listOfWords[i]] + 1
        else:
            wordCnt[listOfWords[i]] = 1
    return wordCnt

cntWordsDict = wordCnt(readFile(fileLocation))          # we pass the readFile method which returns a list of words and this is passed as an argument to the wordCnt function
cntWordsDict = sortDict(cntWordsDict)
# print('The contents of the dictionary in part 2a are: \n %s'%(cntWordsDict))
print('The wordCnt Dictionary has %s keys' %(len(cntWordsDict.keys())))
print('**'*30)

# Part 2b
def randomSplitOfWords(listOfWords):
    """
    Function that creates three different word count dictionaries 
    splitting the words at random between the three dicts
    """
    wordCnt1 = {}                                                # define an empty dictionary
    wordCnt2 = {}
    wordCnt3 = {}
    for i in range(len(listOfWords)):                            # iterate through the list of words and count the number of words
        randomNum = random.randint(0,2)                          # generate a random number between 0 and 2 inclusive. 
        if randomNum == 0:
            if listOfWords[i] in wordCnt1.keys():
                wordCnt1[listOfWords[i]] = wordCnt1[listOfWords[i]] + 1
            else:
                wordCnt1[listOfWords[i]] = 1
        elif randomNum == 1:
            if listOfWords[i] in wordCnt2.keys():
                wordCnt2[listOfWords[i]] = wordCnt2[listOfWords[i]] + 1
            else:
                wordCnt2[listOfWords[i]] = 1
        elif randomNum == 2:
            if listOfWords[i] in wordCnt3.keys():
                wordCnt3[listOfWords[i]] = wordCnt3[listOfWords[i]] + 1
            else:
                wordCnt3[listOfWords[i]] = 1
    return wordCnt1, wordCnt2, wordCnt3                     # return the three dictionaries of words

# Part 2c
def mergeDicts(dict1, dict2, dict3):
    """
    Function that returns a merged dictionary after using 
    Counter function from the collections package to merge 
    multiple dictionaries across a common key
    """
    tempMergedDict = {}                                     # declare empty dictionaries
    mergedDict = {}

    tempMergedDict = Counter(dict1) + Counter(dict2)        # Use the Counter function to merge dict1 and dict2 together 
    mergedDict = Counter(tempMergedDict) + Counter(dict3)   # again merge the third dictionary to the merged dict1 and dict2
    
    return mergedDict                                       # return the merged Dictionary, which contents all the contents of three dictionaries.


# Invoke the randomSplitOfWords helper function, which takes the list of words as a parameter and 
# create three different word count dictionaries splitting the words 
# at random between the three dicts
wCnt1, wCnt2, wCnt3 = randomSplitOfWords(listOfWords)
print('Dictionary 1 has %s keys' %(len(wCnt1.keys()))) 
print('Dictionary 2 has %s keys' %(len(wCnt2.keys())))
print('Dictionary 3 has %s keys\n' %(len(wCnt3.keys())))
consolidatedDict = mergeDicts(wCnt1, wCnt2, wCnt3)             # helper function which takes three dictionaries as parameters and merges them together
sortedMergedDict = sortDict(consolidatedDict)                  # helper function that returns a sorted dictionary
print('Verifying that both dictionaries in 2a and 2c match:\n')
print('The contents of the dictionary in part 2a are: \n %s\n'%(cntWordsDict))

print('The dictionary in 2a has %s keys.\n' %(len(cntWordsDict.keys())))
print('****'*30)
print('\nThe contents of the merged dictionary in part 2c are: \n %s\n' %(sortedMergedDict))
print('The dictionary in 2c has %s keys.' %(len(sortedMergedDict.keys())))
print('**'*30)

# Part 2d
# Deterministically assign each word to one of the three dictionaries
def deterministicSplitOfWords(listOfWords):
    """
    Function that creates three different word count dictionaries 
    splitting the words at random between the three dicts
    """
    dWordCnt1 = {}                                                # define an empty dictionary
    dWordCnt2 = {}
    dWordCnt3 = {}
    for i in range(len(listOfWords)):                            # iterate through the list of words and count the number of words
        detValue = hash(listOfWords[i]) % 3                      # derive the deterministic value

        if detValue == 0:
            if listOfWords[i] in dWordCnt1.keys():
                dWordCnt1[listOfWords[i]] = dWordCnt1[listOfWords[i]] + 1
            else:
                dWordCnt1[listOfWords[i]] = 1

        elif detValue == 1:
            if listOfWords[i] in dWordCnt2.keys():
                dWordCnt2[listOfWords[i]] = dWordCnt2[listOfWords[i]] + 1
            else:
                dWordCnt2[listOfWords[i]] = 1

        else: # when the deterministic value is 2
            # print('detValue: %s'%(detValue))                                              # for debugging purposes
            if listOfWords[i] in dWordCnt3.keys():
                dWordCnt3[listOfWords[i]] = dWordCnt3[listOfWords[i]] + 1
            else:
                dWordCnt3[listOfWords[i]] = 1        
        
    return dWordCnt1, dWordCnt2, dWordCnt3                                                  # return the three dictionaries of words

deterDict1, deterDict2, deterDict3 = deterministicSplitOfWords(listOfWords)

print('Dictionary 1 has %s keys.\n' %(len(deterDict1.keys())))
print('Dictionary 2 has %s keys.\n' %(len(deterDict2.keys())))
print('Dictionary 3 has %s keys.\n' %(len(deterDict3.keys())))

# Part 2e 
# Merge the three dictionaries in part 2d into one.
partEMergedDict = mergeDicts(deterDict1, deterDict2, deterDict3)             # helper function which takes three dictionaries as parameters and merges them together
sortedEMergedDict = sortDict(partEMergedDict)                                 # helper function that returns a sorted dictionary
print('Verifying that both dictionaries in 2a and 2e match:\n')
print('The contents of the dictionary in part 2a are: \n %s\n'%(cntWordsDict))

print('The dictionary in 2a has %s keys.\n' %(len(cntWordsDict.keys())))
print('****'*30)
print('\nThe contents of the merged dictionary in part 2e are: \n %s\n' %(sortedEMergedDict))
print('The dictionary in 2e has %s keys.' %(len(sortedEMergedDict.keys())))
print('**'*30)
# Part 3a
# Computing the speed of reading from disk

fileName = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/CSC555MiningBigData/data/OneDayOfTweets.csv'

def extractLine():
    """Reading the file in chunks"""
    with open(fileName, 'rb') as f:
        for item in f:
            yield item

startTime = time.time()
chunkSize = 200000
generatedLines = extractLine()                              # invoke a helper extractLine to read  the file in chunks
screenNameDict = {}
fileItemsL = [i for i, j in zip(generatedLines, range(chunkSize))]
endTime = time.time()
print('The processing of 200000 tweets data took %s seconds' %(endTime-startTime))
print('The number of operations per second is %s seconds' %(200000/(endTime-startTime)))
print('**'*30)

# Part 3b
# using urllib

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/CSC555MiningBigData/data')

tweetdata = """http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt"""
startTime = time.time()                                                     # start time of processing the file in web

webFD = urllib.request.urlopen(tweetdata)

for i in range(3300):
    if i % 1000 == 0: # Print a message every 500th tweet read
        print ("Processed " + str(i) + " tweets")
    try:
        itemResponse = webFD.readline()                                       # read one line at a time
    except Exception:
        continue
endTime = time.time()                                                        # end time of processing of writing the tweets data to a file. 
print('The processing of the tweets data took %s seconds' %(endTime-startTime))
print('The number of operations per second is %s seconds' %(3300/(endTime-startTime)))

# Part 3(c)
# Compute the speed of writing to disk
startTime = time.time()
csvf = open('C:/Users/rejalu1/OneDrive - Henry Ford Health System/CSC555MiningBigData/data/WrittenFileOfTweets.csv', 'wb')
for i in range(200000):
    if i % 10000== 0: # Print a message every 10000th tweet read
        print ("Processed " + str(i) + " tweets")
    try:
        csvf.write(fileItemsL[i])
    
    except Exception:
        continue
csvf.close()
endTime = time.time() 
print('The writing of 200000 tweets to the file system took %s seconds' %(endTime-startTime))
print('The number of operations per second is %s seconds' %(200000/(endTime-startTime)))

# Part 3(d)
# Add a final print in 3a and print
# everything you read from the file. 
def transformExtraneousValues(fileDictkey):
    """A function that takes a dictionary key and 
    checks if the value is null, an empty string or [] 
    and it replaces it with None otherwise it assigns 
    the actual value to a variable which is returned
    """
   
    valuestr = ''
    if fileDictkey =='null' or fileDictkey =='' or fileDictkey =='[]':
        valuestr = None
    else:
        valuestr = fileDictkey
    return valuestr
            
newGeoRows = [] # hold individual values of to-be-inserted row
newTweetRows = [] # hold individual values of to-be-inserted row

tweetCounter = 0
geoCounter = 0

startTime = time.time()
for i in range(200000):
    if i % 10000 == 0: # Print a message every 50th tweet read
        print ("Processed " + str(i) + " tweets")
    try:
        if fileItemsL[i]:    # check if the item is empty before hand
            # tweetLine is a byte object which needs to be decoded. 
            # the loads() function in the json object lets you convert the string into the json object which acts like a dictionary. 
            # then decode the line that come back from the web into a string. 

            fileDict = json.loads(fileItemsL[i].decode('utf-8'))    # using decode() and loads to convert each item to a dictionary
            

            geoV = fileDict['geo']
            
            NoneType=type(None)
        
            
            if geoV: # check if geoV is not null
                if (not isinstance(geoV, str) or geoV.strip()) or type(geoV) is not NoneType: # Check if the key is not None neither is it a string or blanck string
                    geoValue = fileDict['geo']['type'] + str(fileDict['geo']['coordinates'][0]) + str(fileDict['geo']['coordinates'][1])
            
                newGeoRows.append(
                    (
                        fileDict['geo']['type'] + str(fileDict['geo']['coordinates'][0]) + str(fileDict['geo']['coordinates'][1]), 
                        fileDict['geo']['type'], fileDict['geo']['coordinates'][0], fileDict['geo']['coordinates'][1])

                )

                geoCounter += 1 

                newTweetRows.append(
                    (
                        transformExtraneousValues(fileDict['created_at']), 
                        transformExtraneousValues(fileDict['id_str']), 
                        transformExtraneousValues(fileDict['text']),
                        transformExtraneousValues(fileDict['source']),
                        transformExtraneousValues(fileDict['in_reply_to_user_id']), 
                        transformExtraneousValues(fileDict['in_reply_to_screen_name']), 
                        transformExtraneousValues(fileDict['in_reply_to_status_id']), 
                        transformExtraneousValues(fileDict['retweet_count']), 
                        transformExtraneousValues(fileDict['contributors']), 
                        transformExtraneousValues(fileDict['user']['id']), 
                        geoValue
                    )
                )
                tweetCounter += 1
     
                
            else: # for the rest of the line items where the dictionary key, 'geo' is None
                newTweetRows.append(
                    (
                        transformExtraneousValues(fileDict['created_at']), 
                        transformExtraneousValues(fileDict['id_str']), 
                        transformExtraneousValues(fileDict['text']),
                        transformExtraneousValues(fileDict['source']),
                        transformExtraneousValues(fileDict['in_reply_to_user_id']), 
                        transformExtraneousValues(fileDict['in_reply_to_screen_name']), 
                        transformExtraneousValues(fileDict['in_reply_to_status_id']), 
                        transformExtraneousValues(fileDict['retweet_count']), 
                        transformExtraneousValues(fileDict['contributors']), 
                        transformExtraneousValues(fileDict['user']['id']), 
                        None
                    )
                )
                tweetCounter += 1
    
    except ValueError:
        continue

# derive the tweet and geo data frames
tweetDF = pd.DataFrame(newTweetRows, columns=['CREATED_AT','ID','TEXT','SOURCE','IN_REPLY_TO_USER_ID',
                                                'IN_REPLY_TO_SCREEN_NAME','IN_REPLY_TO_STATUS_ID',
                                                'RETWEET_COUNT','CONTRIBUTORS','User_Id','GeoId'])

geoDF = pd.DataFrame(newGeoRows, columns=['Id','Type','longitude','latitude'])

# joining the two data sets
joinedDF = pd.concat([tweetDF, geoDF], axis=1, join="inner")
print(joinedDF)
endTime = time.time()
                                                        
print('Printing 200,000 tweets took %s seconds' %(endTime-startTime))
print('The number of operations per second is %s seconds' %(200000/(endTime-startTime)))

