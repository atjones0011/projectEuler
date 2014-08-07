import sys

try:
    belowNumber = int(sys.argv[1])
    multiples =sys.argv[2:]
except:
    sys.exit("Script execution must follow the following format: python problem1.py <testBelow> <multiple1> [<multiple2>, ...]")

sum = 0

for x in range(belowNumber):
    for y in multiples:
        if x % int(y) == 0:
            sum = x + sum
            break

print sum
