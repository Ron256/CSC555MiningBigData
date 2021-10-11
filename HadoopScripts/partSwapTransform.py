
# !/usr/bin/python
# Author: Ronaldlee Ejalu
# CSC 555 Mining Big Data
# HomeWork Assignment 3
import sys


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
        #print(splittedLinesL)
        splittedPtype = splittedLinesL[6].split(' ')
        #print(splittedPtype)
        ptypeTransformed = splittedPtype[2] +',' + splittedPtype[1] + ' ' + splittedPtype[0]           # swampping the first and last words
        col0 = splittedLinesL[0]
        col1 = splittedLinesL[1].replace(' ','_')
        col2 = splittedLinesL[2].replace('#','_')
        col3 = splittedLinesL[3].replace('#','_')
        col4 = splittedLinesL[4].replace('#','_')
        col5 = splittedLinesL[5]
        col6 = ptypeTransformed
        col7 = splittedLinesL[7]
        col8 = splittedLinesL[8].replace(' ','_')
        print(col0 + '\t' + col1 + '\t' + col2 + '\t' + col3 + '\t' + col4 + '\t' + col5 + '\t' + col6 + '\t' + col7 + '\t' + col8)
transformPart()





# def transformPart():
#     """
#     This function swamps the first and last columns in the 7th column and replaces the space by the comma
#     and the rest of the columns where applicable it, replace space(' ') and # characters by an underscore.
#     Hive uses this function to perform the mentioned transformations.
#     """
#     for lines in sys.stdin:# Loop through the list of strings
#         cleansedLine =lines.strip()               # remove any white spaces

#         # replace the '|' delimeter with '\t' since Hive assumes that everything is tab separated
#         splittedLinesL = cleansedLine.split('\t')         # split the string to create a list of words, in hadoof, it has to be '\t' delimeted
#         splittedPtype = splittedLinesL[6].split(' ')
#         ptypeTransformed = splittedPtype[2] +',' + splittedPtype[1] + ' ' + splittedPtype[0]           # swampping the first and last words
#         print(splittedLinesL[0] + '\t' + splittedLinesL[1].replace(' ','_') + '\t' + splittedLinesL[2].replace('#','_') + '\t' + splittedLinesL[3].replace('#','_') + '\t' + splittedLinesL[4].replace('#','_') + '\t' + splittedLinesL[5] + '\t' + ptypeTransformed + '\t' + splittedLinesL[7] + '\t' + splittedLinesL[8].replace(' ','_'))
# transformPart()

