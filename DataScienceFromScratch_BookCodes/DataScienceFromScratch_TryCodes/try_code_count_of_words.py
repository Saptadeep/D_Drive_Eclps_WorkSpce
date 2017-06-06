import sys, re

arg1 = sys.argv[0]
arg2 = sys.argv[1]

print (arg1)
print (arg2)
for line in sys.stdin:
    sys.stdout.write(line)
