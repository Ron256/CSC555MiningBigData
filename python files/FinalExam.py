# fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\data1.txt'
fileLocation = 'C:\\Users\\rejalu1\\OneDrive - Henry Ford Health System\\CSC555MiningBigData\\data\\data2.txt'

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


# Reducer1 
#!/usr/bin/python
# import sys

# key = ''
# currentKey = None
# brandl = None
# revenueL = []
# orderdate = None
# partKey = None

# # for line in sys.stdin:
# for line in listOfWords:
#     line = line.strip()
#     vals = line.split('|')
#     key = vals[0]
#     value = '\t'.join(vals[1:])
#     # print(value)

#     if currentKey == key:
#         if value.endswith('LO'):
#             partKey = vals[0]                       # assign string partKey to the variable
#             orderdate = vals[1]                     # assign string orderdate to the variable
#             revenueL.append(int(vals[2]))            # assign string revenue to the variable

#         if value.endswith('Part'):
#             brandl = vals[1]                        # assign string brandl to the variable
#     else:
#         if currentKey:                          # when the current key is done
#             lenOrderDate = len(orderdate)       # derive the length of orderdate
#             lenRevenue = len(revenueL)           # derive the length of revenue
#             lenBrandl = len(brandl)             # derive the length of brandl

#             # this acts as a joins since rows must exist on both sides
#             if (lenOrderDate * lenRevenue * lenBrandl) > 0:
#                 sumOfRev = sum(revenueL)
#                 print(partKey + '\t' + orderdate + '\t' + str(sumOfRev) + '\t' + brandl)

#         # reset the variables
#         partKey = ''
#         brandl = ''
#         revenueL = []
#         orderdate = ''
#         currentKey = key

#         if value.endswith('LO'):
#             partKey = vals[0]
#             orderdate = vals[1]
#             revenueL.append(int(vals[2]))
#             brandl = ''

#         elif value.endswith('Part'):
#             partKey = ''
#             orderdate = ''
#             revenueL = []
#             brandl = vals[1]

# lenOrderDate = len(orderdate)
# lenRevenue = len(revenueL)
# lenBrandl = len(brandl)
# if currentKey == key:
#     # this acts as a joins since rows must exist on both sides
#     if (lenOrderDate * lenRevenue * lenBrandl) > 0:
#         sumOfRev = sum(revenueL)
#         print(partKey + '\t' + orderdate + '\t' + str(sumOfRev) + '\t' + brandl)




# #!/usr/bin/python
# import sys

# for line in sys.stdin:
#     line = line.strip()
#     vals = line.split('|')

#     if vals[2][:4] == 'MFGR':
#         if 'MFGR#2121' <= vals[4]  <= 'MFGR#2138':
#             # print partKey, brandl
#             print(vals[0] + '\t' + vals[4] + '\t' + 'Part')
#     else:
#         # search a string if contains '-'
#         if vals[6].find('-') > 0:
#             print(vals[3] + '\t' + vals[5] + '\t' + vals[12] + '\t' + 'LO')



#Pass 2
#!/usr/bin/python
import sys

fd = open('dwdate.tbl', 'r')
lines = fd.readlines()
fd.close()

dDict = {}
# cnt = 0
for line in lines:
    vals= line.split('|')
    # cnt += 1
    # print(vals)
    if vals[12] == 'Fall':
        dDict[vals[0]] = int(vals[4])

for line in sys.stdin:
   line = line.strip()
   vals = line.split('|')
   
   # lo_orderdate = d_datekey
   if vals[1] in dDict.keys():
       if vals[2][:4] == 'MFGR':
           if 'MFGR#2121' <= vals[4]  <= 'MFGR#2138':
               # print partKey, brandl
               print(vals[0] + '\t' + vals[4] + '\t' + 'Part')
        else:
            if vals[6].find('-') > 0:print(vals[3] + '\t' + vals[5] + '\t' + vals[12] + '\t' + 'LO')



# Reducer

#!/usr/bin/python
# import sys

# key = ''
# currentKey = None
# brandl = None
# dYear = None
# revenueL = []

# for line in listOfWords:
# for line in sys.stdin:
#     line = line.strip()
#     vals = line.split('|')
#     key = vals[0]+'|' + vals[1]
   
#     if currentKey == key:
#         dYear = vals[0]                        
#         brandl = vals[1]                     
#         revenueL.append(int(vals[2]))           

#     else:
#         if currentKey:                          # when the current key is done
#             lendYear = len(dYear)       # derive the lengths
#             lenBrandl= len(brandl)           
#             lenRevenueL = len(revenueL)            

#             if (lendYear * lenBrandl * lenRevenueL) > 0:
#                 sumOfRev = sum(revenueL)
#                 # print(partKey + '\t' + orderdate + '\t' + str(sumOfRev) + '\t' + brandl)
#                 print('%s\t%s\t%s' %(str(sumOfRev), dYear, brandl))

#         # reset the variables
#         brandl = ''
#         revenueL = []
#         dYear = ''
#         currentKey = key
#         dYear = vals[0]                        
#         brandl = vals[1]                     
#         revenueL.append(int(vals[2]))


# lendYear = len(dYear)       # derive the lengths
# lenBrandl= len(brandl)           
# lenRevenueL = len(revenueL) 
# if currentKey == key:
#     if (lendYear * lenBrandl * lenRevenueL) > 0:
#         sumOfRev = sum(revenueL)
#         print('%s\t%s\t%s' %(str(sumOfRev), dYear, brandl))

# Option 1
#!/usr/bin/python
# import sys

# for line in sys.stdin:
#     line = line.strip()
#     vals = line.split('|')
#     if vals[3][:5] == 'MFGR#':
#         print('%s\t%s\t%s\t%s' %(vals[1], vals[3], vals[2], 'result1'))
#     else:
#         if vals[3][:5] != 'MFGR#':
#             if vals[12] == 'Fall':
#                 print('%s\t%s\t%s' %(vals[0], vals[4], 'dwdate'))

    

# #!/usr/bin/python
# import sys

# for line in sys.stdin:
#     line = line.strip()
#     vals = line.split('|')
#     if vals[3][:5] == 'MFGR#':
#         print('%s\t%s\t%s\t%s' %(vals[1], vals[3], vals[2], 'result1'))
#     else:
#         if vals[12] == 'Fall':
#             print('%s\t%s\t%s' %(vals[0], vals[4], 'dwdate'))



# #!/usr/bin/python
# import sys

# key = ''
# currentKey = None
# brandl = None
# dYear = None
# revenueL = []

# # for line in listOfWords:
# for line in sys.stdin:
#     line = line.strip()
#     vals = line.split('\t')
#     key = vals[0]

#     value = '\t'.join(vals[1:])
#     if currentKey == key:
#         if value.endswith('result1'):
#             brandl = vals[1]
#             revenueL.append(int(vals[2]))
#         if value.endswith('dwdate'):
#             dYear = vals[0]  

#     else:
#         if currentKey:                          # when the current key is done
#             lendYear = len(dYear)       # derive the lengths
#             lenBrandl= len(brandl)
#             lenRevenueL = len(revenueL)

#             if (lendYear * lenBrandl * lenRevenueL) > 0:
#                 sumOfRev = sum(revenueL)
#                 # print(partKey + '\t' + orderdate + '\t' + str(sumOfRev) + '\t' + brandl)
#                 print('%s\t%s\t%s' %(str(sumOfRev), dYear, brandl))

#         # reset the variables
#         brandl = ''
#         revenueL = []
#         dYear = ''
#         currentKey = key

#         if value.endswith('result1'):
#             brandl = vals[1]
#             revenueL.append(int(vals[2]))
#             dYear = ''

#         elif value.endswith('dwdate'):
#             dYear = vals[0]  
#             brandl = ''
#             revenueL = []

# lendYear = len(dYear)       # derive the lengths
# lenBrandl= len(brandl)
# lenRevenueL = len(revenueL)
# if currentKey == key:
#     if (lendYear * lenBrandl * lenRevenueL) > 0:
#         sumOfRev = sum(revenueL)
#         print('%s\t%s\t%s' %(str(sumOfRev), dYear, brandl))
