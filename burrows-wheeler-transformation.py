# https://www.codewars.com/kata/burrows-wheeler-transformation
"""
bananabar

b a n a n a b a r
r b a n a n a b a
a r b a n a n a b
b a r b a n a n a
a b a r b a n a n
n a b a r b a n a
a n a b a r b a n
n a n a b a r b a
a n a n a b a r b

               .-.
a b a r b a n a n
a n a b a r b a n
a n a n a b a r b
a r b a n a n a b
b a n a n a b a r <- 4
b a r b a n a n a
n a b a r b a n a
n a n a b a r b a
r b a n a n a b a
               '-'

Output: ("nnbbraaaa", 4)

a n
a n
a b
a b
b r
b a
n a
n a
r a


"""
def encode(s):
    res = []
    for _ in range(len(s)):
        res.append(s)
        s = s[-1] + s[:len(s)-1]
    res.sort()
    S = "".join([k[-1] for k in res])
    print(S, res.index(s))

def decode(s, n):
    pass

encode('bananabar')