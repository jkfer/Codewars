# https://www.codewars.com/kata/54d7660d2daf68c619000d95
# 5kyu

"""
finding the least common multiplier of 2 numbers ?
lcm - least common multiple (smallest positive int that is a miltiple of given
nums)
gcd - greatest common denominator (the largest positive int dividing the given
nums)

As far as two numbers are concerned:
lcm = a*b / gcd(a, b)
"""

import math


def get_divi(num):
    D = set()
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            D.add(int(i))
            D.add(int(num/i))
    return D


def gcd(a, b):
    L = get_divi(a).intersection(get_divi(b))
    ans = max(L)
    return ans


def lcm(a, b):
    return int((a*b) / gcd(a, b))


def convertFracts(lst):
    # base case - if len(lst) == 1:
    if len(lst) == 1:
        return lst

    G = list(zip(*lst))
    for i, l in enumerate(G):
        G[i] = list(l)

    K = lcm(G[1][0], G[1][1])
    for j in G[1][2:]:
        K = lcm(K, j)

    ans = []
    for i, k in enumerate(G[0]):
        G[0][i] = int(K / G[1][i])
        ans.append([G[0][i], K])

    return ans


# print(lcm(56, 77))
ll = convertFracts([[1, 2], [1, 3], [1, 4]])
print(ll)
