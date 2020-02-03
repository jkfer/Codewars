# https://www.codewars.com/kata/5dcde0b9fcb0d100349cb5c0
# 4kyu

'''
    Write a function that returns the longest contiguous palindromic
    substring in s. In the event that there are multiple longest
    palindromic substrings, return the first to occur.
'''


def isPlain(s):
    return s == s[::-1]


# TODO: Complete in linear time xDD
def longest_palindrome(s):
    if len(s) == 1 or isPlain(s):
        return s

    ans = ""
    m = 0
    j = len(s) - 1

    for i in range(j+1):
        st = s[i]
        rem = s[i+1:]
        J = j
        while J >= i:
            if s[J] == st:
                word = s[i:J+1]
                if isPlain(word) and len(word) > m:
                    ans = word
                    m = J + 1 - i
            J -= 1

    return ans


print(longest_palindrome('ttaaftffftfaafatf'))
