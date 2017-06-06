import sys, re
from collections import Counter
from adodbapi.adodbapi import counter
#get CLI arguments:
try:
    print(sys.argv[0]) #the file name itself
    print(sys.argv[1]) #the first argument
except:
    print('No Command Line Argument given')
    
# for line in open('D:/\Eclipse_Workspace/\zz1.py', 'r'):
for line in open('input_text.txt', 'r'):
    a = line.strip().split()
    sys.stdout.write(str(dict(Counter(a))))
    
