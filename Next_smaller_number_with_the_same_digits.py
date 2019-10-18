"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
"""
# this is incorrect - Try recursive approach for this. 


from itertools import permutations

def next_smaller(n):
    # base:
    if len(str(n)) == 1:
        return -1
    elif len(str(n)) == 2:
        N = list(map(int, str(n)))
        N.sort()
        if int("".join(list(map(str, N)))) < n:
            return "".join(list(map(str, N)))
    
    f = str(n)[0]
    rest = str(n)[1:]

    # reorder the res:
    res = list(map(int, rest))
    res.sort()
    REST = "".join(list(map(str, res)))
    if int(f + REST) < n:
        return int(f + REST)
    else:
        return -1


x = next_smaller(907)
print(x)