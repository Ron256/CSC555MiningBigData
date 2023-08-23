

# fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\data1.txt'
fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\testdata.txt'

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


# #!/usr/bin/python
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
#             if 'MFGR#2121' <= vals[4]  <= 'MFGR#2138':
#                 # print partKey, brandl
#                 print(vals[0] + '\t' + vals[4] + '\t' + 'Part')


#!/usr/bin/python
# import sys

# key = ''
# currentKey = None
# brandl = None
# revenueL = []
# dYear = None
# partKey = None

# for line in sys.stdin:
# #for line in listOfWords:
#     line = line.strip()
#     vals = line.split('\t')
#     key = vals[0]
#     value = '\t'.join(vals[1:])
#     # print(value)

#     if currentKey == key:
#         if value.endswith('LO'):
#             partKey = vals[0]                       # assign string partKey to the variable
#             dYear =   vals[1]                     # assign string orderdate to the variable
#             revenueL.append(int(vals[2]))            # assign string revenue to the variable

#         if value.endswith('Part'):
#             brandl = vals[1]                        # assign string brandl to the variable
#     else:
#         if currentKey:                          # when the current key is done
#             lendYear = len(dYear)       # derive the length of orderdate
#             #lenRevenue = len(revenueL)           # derive the length of revenue
#             lenBrandl = len(brandl)             # derive the length of brandl

#             # this acts as a joins since rows must exist on both sides
#             if (lendYear  * lenBrandl) > 0:
#                 sumOfRev = sum(revenueL)
#                 print(partKey + '|' + dYear + '|'  + brandl + '|' + str(sumOfRev))


#        # reset the variables
#         partKey = ''
#         brandl = ''
#         revenueL = []
#         dYear = ''
#         currentKey = key

#         if value.endswith('LO'):
#             partKey = vals[0]
#             dYear = vals[1]
#             revenueL.append(int(vals[2]))
#             brandl = ''

#         elif value.endswith('Part'):
#             partKey = ''
#             dYear = ''
#             revenueL = []
#             brandl = vals[1]

# lendYear = len(dYear)
# #lenRevenue = len(revenueL)
# lenBrandl = len(brandl)
# if currentKey == key:
#     # this acts as a joins since rows must exist on both sides
#     if (lendYear * lenBrandl) > 0:
#         sumOfRev = sum(revenueL)
#         print(partKey + '|' + dYear + '|'  + brandl + '|' + str(sumOfRev))



#!/usr/bin/python
# import sys

# for line in sys.stdin:
#    line = line.strip()
#    vals = line.split('\t')
#    dYear = vals[1]
#    brandl = vals[2]
#    revenue = vals[3]
#    print(dYear + '\t' + brandl + '\t' + revenue)



#!/usr/bin/python
import sys
key = ''
currentKey = None
revenueL = []
dYear = None
brandl = None

for line in sys.stdin:
    line = line.strip()
    vals = line.split('\t')
    
    key = vals[0] + '|' + vals[1]
    if currentKey == key:
        dYear = vals[0]
        brandl = vals[1]
        revenueL.append(int(vals[2]))
    else:
        if currentKey:
            lenRevenueL = len(revenueL)

            if (lenRevenueL > 0):
                    print('%s\t%s\t%s' %(str(sum(revenueL)), dYear, brandl))

        # re-initialize the variables when the keys are not the same (new key) before adding$
        dYear = ''
        brandl = ''                                       
        revenueL = []

        currentKey = key
        dYear = vals[0]
        brandl = vals[1]
        revenueL.append(int(vals[2]))

# output the last key
if currentKey == key:
    lenRevenueL = len(revenueL)
    if (lenRevenueL > 0):
        print('%s\t%s\t%s' %(str(sum(revenueL)), dYear, brandl))
