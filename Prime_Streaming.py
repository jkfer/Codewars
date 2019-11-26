# https://www.codewars.com/kata/5519a584a73e70fa570005f5
# 3kyu
# Incomplete
import sys
import math


class Primes:
    def check(self, n):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    # function to generate all primes until n(inclusive):
    # works well for until 1 million numbers
    def generate(self, n):
        p = []
        L = [False] * 2 + [True] * (n-1)
        for i in range(2, n + 1):
            if L[i]:
                p += [i]
                for j in range(i, n+1, i):
                    L[j] = False
        return p
        # return iter(p) to satisfy kata


C = Primes()
print(C.generate(100000))
