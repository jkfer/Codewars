# https://www.codewars.com/kata/perimeter-of-squares-in-a-rectangle/train/python

# as advised in the description the fib sequence works well enough for this.


def perimeter(n):
    a, b = 0, 1
    ans = 1
    if n in [0, 1]:
        return n*4

    for _ in range(1, n+1):
        c = a + b
        ans += c
        a, b = b, c

    return ans * 4


print(perimeter(7))
