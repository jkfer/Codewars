# https://www.codewars.com/kata/5519a584a73e70fa570005f5
# 3kyu

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
                p.append(i)
                for j in range(i * i, n+1, i):
                    L[j] = False
        return p
        # return iter(p) to satisfy kata

    # Works well for 15 mil
    def generate2(self, n):
        primes = [1] * n
        L = [False] * 2 + [True] * (n-1)
        # n = 16000000
        j = 0
        while j*j <= n:
            if L[j]:
                for q in range(j*j, n+1, j):
                    L[q] = False
            j += 1

        i, k = 2, 0
        while i < n:
            if L[i]:
                primes[k] = i
                k += 1
            i += 1

        q = n-1
        while primes[q] == 1:
            q -= 1

        return primes[:q+1]


C = Primes()
# print(C.generate(100))
print(C.generate2(15486451))
