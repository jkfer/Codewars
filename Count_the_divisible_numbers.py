# https://www.codewars.com/kata/count-the-divisible-numbers/python


# for some reason answer was not accepted in python 3.6 online IDE. 2.7 works.
def divisible_count(x, y, k):
    if x % k == 0:
        A = x
    else:
        A = x + (k-(x % k))

    if y % k == 0:
        B = y
    else:
        B = y - (y % k)

    return (B/k) - (A/k) + 1


print(divisible_count(482019538319278661869526854438952107725709,
                      2675928442850268125308839268473209804980492, 4944))
# 443751801078274567847757365298191281808
