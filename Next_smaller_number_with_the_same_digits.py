"""
https://www.codewars.com/kata/next-smaller-number-with-the-same-digits/python

Write a function that takes a positive integer and returns 
the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.

"""

def next_smaller(n):
    # base:
    if len(str(n)) == 1:
        return -1

    new_n = list(map(int, list(str(n))))

    new_n_sorted = new_n[:]
    new_n_sorted.sort()

    if new_n_sorted == new_n:
        return -1

    N = list(str(n))
    found = False

    # find the index to be swapped
    for i in range(1, len(N))[::-1]:
        if int(N[i-1]) > int(N[i]):
            found = True
            break

    if found:
        inc = N[:i]
        other = N[i:]

        # check to find if there is any digit smaller than last other:
        if len(other) > 1:
            # find the next smallest element from before
            other = list(map(int, other))
            other.sort(reverse=True)

            for j in range(len(other)):
                if other[j] < int(inc[-1]):
                    before = [str(other.pop(j))]
                    break
        elif len(other) == 1:
            before = [other.pop(0)]
        else:
            before = [""]

        if len(inc) == 0:
            start = before
        elif len(inc) == 1:
            start = before
            other = list(map(int, other + inc))
            other.sort(reverse=True, key=int)
            other = list(map(str, other))
        else:
            other = other + [inc.pop()]
            other = list(map(int, other))
            other.sort(reverse=True, key=int)
            other = list(map(str, other))
            start = inc + before

        x = int("".join(start + other))

    if x < n and len(str(n)) == len(str(x)):
        return x
    else:
        return -1


x = next_smaller(1207)
print(x)

y = next_smaller(2071)
print(y)
