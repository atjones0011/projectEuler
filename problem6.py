import sys

try:
    startNumber = int(sys.argv[1])
    endNumber = int(sys.argv[2])
except:
    sys.exit("Script execution must follow the following format: python problem6.py <startNumber> <endNumber>")

sumOfSquares = 0
for x in range(startNumber, endNumber + 1):
    sumOfSquares += x * x

squareOfSums = 0
for x in range(startNumber, endNumber + 1):
    squareOfSums += x

print squareOfSums * squareOfSums - sumOfSquares
