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
    whichPrime = int(sys.argv[1])
except:
    sys.exit("Script execution must follow the following format: python problem7.py <whichPrime>")

count = 0
position = 1

while count != whichPrime:
    if isPrime(position):
        count += 1
    position += 1

print position - 1
