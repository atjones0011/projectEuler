import sys

'''
Converts a string of ints into a list of ints and finds the product
'''
def getProd(numStr):
    return reduce(lambda x, y: x * y, [int(i) for i in numStr])

'''
Main execution
'''
try:
    inNumber = sys.argv[1]
    numAdj = int(sys.argv[2])
except:
    sys.exit("Script execution must follow the following format: python problem5.py <inNumber> <numAdj>")

result = 0

if numAdj >= len(inNumber):
    result = getProd(inNumber)
else:
    for x in range(0, len(inNumber) - numAdj + 1):
        if getProd(inNumber[x : x + numAdj]) > result:
            result = getProd(inNumber[x : x + numAdj])

sys.exit(str(result))