# https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ
# Given the string, check if it is a palindrome.


def checkPalindrome(inputString:str = '') -> bool:
    if 1 <= len(inputString) <= 100000:
        return inputString == inputString[::-1]
    return False
