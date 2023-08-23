#!/usr/bin/python
import sys

key = ''
currentKey = None
empFirstName = None  # declare variables to be used 
empLastName = None
extension = None
custAdd = None
# input comes from STDIN (standard input)
for line in sys.stdin:
#for line in listOfWords:
    line = line.strip()
    split = line.split('\t')
    key = split[0] + '|' + split[1]

    value = '\t'.join(split[2:])

    if currentKey == key: # same key
        if value.endswith('Employees'):
            empFirstName = split[0]     # assign the string first name to the variable 
            empLastName = split[1]      # assign the string last name to the variable 
            extension = split[2]        # assign the extension number to the variable

        if value.endswith('Customers'):
            custAdd = split[2]              # assign the address to the variable

    else:
        if currentKey:                     # when the current key is done
            lenExtension = len(extension)  # derive the length of the variables extension and CustAdd to be used to perform the join 
            lenCustAdd = len(custAdd)

            if (lenExtension * lenCustAdd) > 0: # for this to  act as a join   rows must exist on both sides.
                print(empFirstName + '\t' + empLastName + '\t' + extension + '\t' + custAdd)
        # reset the variables
        empFirstName = ''
        empLastName = ''
        extension = ''
        custAdd = ''
        currentKey = key

        if value.endswith('Employees'):
            empFirstName = split[0]
            empLastName = split[1]
            extension = split[2]
            custAdd = ''
        elif value.endswith('Customers'):
            empFirstName = ''
            empLastName = ''
            extension = ''
            custAdd = split[2]


lenExtension = len(extension)
lenCustAdd = len(custAdd)
if currentKey == key: # output the last key
    if (lenExtension * lenCustAdd) > 0: # for this to  act as a join   rows must exist on both sides.
        print(empFirstName + '\t' + empLastName + '\t' + extension + '\t' + custAdd)                                                                                                    [ Read 59 lines ]
 