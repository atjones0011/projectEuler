import math
import sys

try:
    startNumber = int(sys.argv[1])
    endNumber = int(sys.argv[2])
except:
    sys.exit("Script execution must follow the following format: python problem6.py <startNumber> <endNumber>")

sumOfSquares = 0
for x in range(startNumber, endNumber + 1):
    sumOfSquares += pow(x, 2)

squareOfSums = pow(sum(range(startNumber, endNumber + 1)), 2)

print squareOfSums - sumOfSquares
