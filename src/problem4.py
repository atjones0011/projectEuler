import sys

'''
Checks if a string is a palindrome
'''
def isPalindrome(testStr):
    return testStr == testStr[::-1]

'''
Main execution
'''
largestPalindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(str(i * j)) & (i * j > largestPalindrome):
            largestPalindrome = i * j

sys.exit(str(largestPalindrome))