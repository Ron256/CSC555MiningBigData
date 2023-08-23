# fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\data1.txt'

# def readFile(fileLocation):
#     """ Function that generates a list of words"""
#     wordL = []                                              # declare an empty list of words
#     with open(fileLocation) as fN:
#         lines = fN.readlines()                              # read the file and generate a list of strings

#         for item in range(len(lines)):                      # Loop through the list of strings
#             splittedLinesL = lines[item].strip().split(' ')         # split the string to create a list of words

#             for splittedItem in range(len(splittedLinesL)): # loop through the list of words and add words to the wordL(list)
#                 if len(splittedLinesL[splittedItem]) == 0:  # if there are empty spaces just pass
#                     pass
#                 else:
#                     wordL.append(splittedLinesL[splittedItem])
#         return wordL                                        # return a list of words 

# listOfWords = readFile(fileLocation)                        # return a list of words
# print(listOfWords)

# First Pass
# hadoop jar hadoop-streaming-2.6.4.jar -D mapred.reduce.tasks=1 -input /user/ec2-user/lineorderPart -output /data/lineorderPartRes -mapper lineorderPartMapper.py -reducer lineorderPartReducer.py -file lineorderPartMapper.py -file lineorderPartReducer.py

# second Pass

# hadoop jar hadoop-streaming-2.6.4.jar -D stream.num.map.output.key.fields=2 -input /data/lineorderPartRes -mapper resultdwdateMapper.py -reducer resultdwdateReducer.py -file resultdwdateMapper.py -file resultdwdateReducer.py -file dwdate.tbl -output /data/GroupRes


# hadoop jar hadoop-streaming-2.6.4.jar -D mapred.reduce.tasks=1 -input /data/lineorderPartRes -output /data/Result2 -mapper resultdwdateMapper.py -reducer resultdwdateReducer.py -file resultdwdateMapper.py -file resultdwdateReducer.py

# Option 2 - Mapside join
# hadoop jar hadoop-streaming-2.6.4.jar -D mapred.reduce.tasks=1 -input /user/ec2-user/lineorderPart -mapper lineorderJoinMapper.py -reducer lineorderJoinReducer.py -file lineorderJoinMapper.py -file lineorderJoinReducer.py -file dwdate.tbl -output /data/lineorderJoinRes

# hadoop jar hadoop-streaming-2.6.4.jar -D stream.num.map.output.key.fields=2 -input /data/lineorderJoinRes -mapper result2Mapper.py -reducer result2Reducer.py -file result2Mapper.py -file result2Reducer.py  -output /data/Result_out

hadoop jar hadoop-streaming-2.6.4.jar -D stream.num.map.output.key.fields=1 -input /user/ec2-user/generatedRandomFile -mapper kmeansMapper.py -reducer kmeansReducer.py -file kmeansMapper.py -file kmeansReducer.py  -file centers -output /data/KmeansInterationOne


