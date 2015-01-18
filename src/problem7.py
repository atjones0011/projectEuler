import sys
from utils import prime

try:
    whichPrime = int(sys.argv[1])
except:
    sys.exit("Script execution must follow the following format: python problem7.py <whichPrime>")

count = 0
position = 1

while count != whichPrime:
    if prime.isPrime(position):
        count += 1
    position += 1

sys.exit(str(position - 1))
