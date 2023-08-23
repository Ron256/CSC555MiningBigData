# Author: Ronaldlee Ejalu
# CSC 555 Mining Big Data
# HomeWork Assignment 3 
import sys

# This is for testing purposes on my local laptop
# fileLocation = 'C:/Users/rejalu1/OneDrive - Henry Ford Health System/CSC555MiningBigData/data/testData.txt'
# def readFile(fileLocation):
#     """ Function that generates a list of words"""
#     wordL = []                                              # declare an empty list of words
#     with open(fileLocation) as fN:
#         lines = fN.readlines()                              # read the file and generate a list of strings

#         for item in range(len(lines)):                      # Loop through the list of strings
#             cleansedLine =lines[item].strip()               # remove any white spaces

#             # replace the '|' delimeter with 't' since Hive assumes that everything is tab separated
#             splittedLinesL = cleansedLine.split('|')         # split the string to create a list of words, in hadoof, it has to be '\t' delimeted
#             splittedPtye = splittedLinesL[6].split(' ')
#             # print(splittedPtye[0], splittedPtye[1], splittedPtye[2])
#             ptypeTransformed = splittedPtye[2] +',' + splittedPtye[1] + ' ' + splittedPtye[0]           # swampping the first and last words 
#             # print(splittedLinesL[0] + '\t' + splittedLinesL[1].replace(' ','_') + '\t' + splittedLinesL[2].replace('#','_') + '\t' + splittedLinesL[3].replace('#','_') + '\t' + splittedLinesL[4].replace('#','_') + '\t' + splittedLinesL[5].replace('#','_') + '\t' + ptypeTransformed + '\t' + splittedLinesL[7] + '\t' +  splittedLinesL[5].replace(' ','_'))
            
#             print('\t'.join([splittedLinesL[0], splittedLinesL[1].replace(' ','_'), splittedLinesL[2].replace('#','_'), splittedLinesL[3].replace('#','_'), splittedLinesL[4].replace('#','_'), splittedLinesL[5].replace('#','_'), ptypeTransformed, splittedLinesL[7], splittedLinesL[5].replace(' ','_')]))
            






#             # print(splittedLinesL)

#             # for splittedItem in range(len(splittedLinesL)): # loop through the list of words and add words to the wordL(list)
#             #     if len(splittedLinesL[splittedItem]) == 0:  # if there are empty spaces just pass
#             #         pass
#             #     else:
#             #         wordL.append(splittedLinesL[splittedItem])
#         return wordL                                        # return a list of words 

# listOfWords = readFile(fileLocation)                        # return a list of words

def transformPart():
    """
    This function swamps the first and last columns in the 7th column and replaces the space by the comma
    and the rest of the columns where applicable it, replace space(' ') and # characters by an underscore.
    Hive uses this function to perform the mentioned transformations.
    """
    for lines in sys.stdin:# Loop through the list of strings
        cleansedLine =lines.strip()               # remove any white spaces

        # replace the '|' delimeter with '\t' since Hive assumes that everything is tab separated
        splittedLinesL = cleansedLine.split('\t')         # split the string to create a list of words, in hadoof, it has to be '\t' delimeted
        splittedPtype = splittedLinesL[6].split('\t')
    
        ptypeTransformed = splittedPtype[2] +',' + splittedPtype[1] + ' ' + splittedPtype[0]           # swampping the first and last words 
        # print(splittedLinesL[0] + '\t' + splittedLinesL[1].replace(' ','_') + '\t' + splittedLinesL[2].replace('#','_') + '\t' + splittedLinesL[3].replace('#','_') + '\t' + splittedLinesL[4].replace('#','_') + '\t' + splittedLinesL[5].replace('#','_') + '\t' + ptypeTransformed + '\t' + splittedLinesL[7] + '\t' +  splittedLinesL[5].replace(' ','_'))
            
        print('\t'.join([splittedLinesL[0], splittedLinesL[1].replace(' ','_'), splittedLinesL[2].replace('#','_'), splittedLinesL[3].replace('#','_'), splittedLinesL[4].replace('#','_'), splittedLinesL[5], ptypeTransformed, splittedLinesL[7], splittedLinesL[8].replace(' ','_')]))
        return 'done'

transformPart()
            




