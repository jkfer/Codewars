
"""
Buddy pairs
You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
Task
Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n

If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil

Examples
(depending on the languages)

buddy(10, 50) returns [48, 75] 
buddy(48, 50) returns [48, 75]
or
buddy(10, 50) returns "(48 75)"
buddy(48, 50) returns "(48 75)"
Note
for C: The returned string will be free'd.
See more examples in "Sample Tests:" of your language.
"""

def sum_divisors(n):
    i = 1
    res = 0
    while i <= n/2:
        if n % i == 0:
            res += i
        i += 1
    return res

def buddy(start, limit):
    res = []
    while start <= limit:
        x = sum_divisors(start)
        if x > limit:
            x -= 1
            if sum_divisors(x) - 1 == start:
                res = [start, x]
                break
        start += 1
    return res if res else "Nothing"

x = buddy(57345, 90061)
#x = sum_divisors(62744)
print(x)