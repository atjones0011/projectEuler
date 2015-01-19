import sys

def modulus(values, x):
    return {x % i for i in values}

try:
    lowerBound = int(sys.argv[1])
    upperBound = int(sys.argv[2])
except:
    sys.exit("Script execution must follow the following format: python problem5.py <lowerBound> <upperBound>")

if lowerBound > upperBound:
    sys.exit("lowerBound must be smaller than upperBound.")

divArray = range(lowerBound, upperBound + 1)

# Must use copy of array due to manipulation of original
for i in divArray[:]:

    # If index == 0, decrementing will cause entire array to be used.
    # Pass 1-element array, instead
    if divArray.index(i) == 0:
        position = 0
    else:
        position = divArray.index(i) - 1

    # Removing items from divArray to limit calculations
    for j in divArray[:position]:
        if i % j == 0:
            try:
                divArray.remove(j)
            except:
                continue

currPos = max(divArray)

while True:
    if sum(modulus(divArray, currPos)) == 0:
        break
    else:
        currPos += 1

sys.exit(str(currPos))