import sys
from utils import prime

try:
    upperBound = int(sys.argv[1])
except:
    sys.exit("Script execution must follow the following format: python problem3.py <upperBound>")

if prime.isPrime(upperBound):
    sys.exit(str(upperBound))

x = 2

while x < upperBound / 2 + 1: 
    if upperBound % x == 0:
        if prime.isPrime(upperBound / x):
            sys.exit(str(upperBound / x))
    x += 1

sys.exit(str(1))
