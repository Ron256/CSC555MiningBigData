
import numpy as np
from numpy import savetxt
import random
# from fractions import Fraction
import fractions
# np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
# #M  = np.array([[0, 1/2, 1, 0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2],[1/3, 1/2, 0, 0] ])
# M  = np.array([[0, 1/2, 0], [1/2, 0, 1], [1/2, 1/2, 0] ])
# print('Matrix M : %s' %M)

# v = np.array([[1/3], [1/3], [1/3], [1/3]])
# print(v.shape)
# y = M **2 
# print(y)
arr = np.random.randint(50, size = (360000,10))
print(arr.shape)
np.savetxt('C:/Users/rejalu1/OneDrive - Henry Ford Health System/CSC555MiningBigData/documents/Assignments/Assignment6/testnp.csv', arr, fmt= '%i', delimiter = ' ')

text_file =  sc.textFile("hdfs://ec2-3-143-227-198.us-east-2.compute.amazonaws.com/data/bioproject.xml")
word_file = text_file.flatMap(lambda line: line.split(" "))
wordCounts = word_file.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a + b)
wordCounts.saveAsTextFile("hdfs://ec2-3-143-227-198.us-east-2.compute.amazonaws.com/data/wordCntResults")
