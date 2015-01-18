import sys

try:
    calculateTo = int(sys.argv[1])
except:
    sys.exit("Script execution must follow the following format: python problem2.py <calculateTo>")

sum, x, y = 0, 1, 1

while y < calculateTo:
    if y % 2 == 0:
        sum = sum + y
    x, y = y, x + y

print sum
