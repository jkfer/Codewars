"""
Problem Context
The Fibonacci sequence is traditionally used to explain tree recursion.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
This algorithm serves welll its educative purpose but it's tremendously inefficient, not only because of recursion, but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers already calculated by the left branch (i.e. fibonacci(n-1)).

This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much. You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it here in Code Wars you will most likely get a code timeout before any answers.

For this particular Kata we want to implement the memoization solution. This will be cool because it will let us keep using the tree recursion algorithm while still keeping it sufficiently optimized to get an answer very rapidly.

The trick of the memoized version is that we will keep a cache data structure (most likely an associative array) where we will store the Fibonacci numbers as we calculate them. When a Fibonacci number is calculated, we first look it up in the cache, if it's not there, we calculate it and put it in the cache, otherwise we returned the cached number.

Refactor the function into a recursive Fibonacci function that using a memoized data structure avoids the deficiencies of tree recursion Can you make it so the memoization cache is private to this function?
"""

cache = {0:0, 1:1}

def fib(n):
    if n not in cache.keys():
        x = list(cache.keys())
        x.sort()
        strt = x[-1] + 1
        for i in range(strt, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        
    print(cache[n])




def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        i = 2
        while i <= n:
            c = a + b
            a = b
            b = c
            i += 1
        return c

fib(70)
fib(60)

"""
High Level Solution -- Best Practices:

def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
"""
