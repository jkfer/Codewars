# https://www.codewars.com/kata/reversing-fun/train/python
# 7kyu


def reverse_fun(n):
    n = list(n)
    for i in range(len(n)):
        start = i
        end = len(n) - 1
        while start <= end:
            a = n[start]
            b = n[end]
            n[start] = b
            n[end] = a
            start += 1
            end -= 1
    print("".join(n))


reverse_fun('012345')
