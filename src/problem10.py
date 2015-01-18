import sys
from utils import prime

try:
    startRange = int(sys.argv[1])
    endRange = int(sys.argv[2])
except:
    sys.exit("Script execution must follow the following format: python problem10.py <startRange> <endRange>")

sum = 0

for x in range(startRange, endRange + 1):
    if prime.isPrime(x):
        sum += x

sys.exit(str(sum))
