"""
Complete the function which converts a binary number (given as a string) to
a decimal number.
"""

from math import pow


def bin_to_decimal(inp):
    res = 0
    for i, num in enumerate(inp[::-1]):
        res += int(num) * pow(2, i)
    return int(res)


print(bin_to_decimal("100"))
