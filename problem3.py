import math
import sys

'''
    Function to check for a prime number.
    Quickly returns for common signatures for non-prime numbers.
'''
def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        x = math.floor(math.sqrt(n))
        y = 5
        while y <= x:
            if n % y == 0:
                return False
            elif n % (y + 2) == 0:
                return False
            y += 6
        return True

try:
    upperBound = int(sys.argv[1])
except:
    sys.exit("Script execution must follow the following format: python problem3.py <upperBound>")

if isPrime(upperBound):
    sys.exit(str(upperBound))

x = 2

while x < upperBound / 2 + 1: 
    if upperBound % x == 0:
        if isPrime(upperBound / x):
            sys.exit(str(upperBound / x))
    x += 1

sys.exit(str(1))
