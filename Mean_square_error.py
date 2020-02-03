# https://www.codewars.com/kata/51edd51599a189fe7f000015
# 5kyu


def solution(array_a, array_b):
    n = 0
    ans = 0
    for a, b in list(zip(array_a, array_b)):
        ans += abs(a-b) ** 2
        n += 1

    return ans / n
