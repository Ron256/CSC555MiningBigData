# JoinMapper.py
#!/usr/bin/python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    split = line.split('|')
    #if split[0][:3]== 'EMP':
        #if split[1] == 'Brendan' and split[2] == 'Anastasio':
        #       print(split[1] + '\t' + split[2] + '\t' + split[3]  + '\t' + 'Employees')
    if split[0][:3]== 'EMP':
        if len(split[1]) > 0 or len(split[2]) > 0  or len(split[3]) > 0:
            print(split[1] + '\t' + split[2] + '\t' + split[3] + '\t' + 'Employees')
    else:
        if len(split[3]) > 0:
            print(split[1] + '\t' + split[2] + '\t' + split[3] + '\t' + 'Customers')
