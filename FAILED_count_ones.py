"""
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

Example:
countOnes 4 7 should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.
WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!
"""
# get the binaary of a number

from math import pow

def give_bin(n):
    S = ""
    while n != 0:
        r = n%2
        n /= 2
        S = str(r) + S
    return S

# get the length of a binary number
def give_bin_len(n):
    l = 0
    while n != 1:
        n /= 2
        l += 1
    return l+1


def countOnes(left, right):
    # of loops
    loop = give_bin_len(right)
    #init = give_bin(left)
    arr_len = right - left + 1
    count = 0

    for i in range(1, loop+1):
        A = [1]* int(pow(2,i-1)) + [0]* int(pow(2,i-1))
        q = int(arr_len / pow(2, i))
        r = int(arr_len % pow(2, i))
        print(A, q, r)
        newA = A[r-1:]

        count += (pow(2, i-1) * q) + newA.count(1)
    
    print(count)


countOnes(3, 9)

# 1
# Take the biggest number - divide by 2 until quotient is 0.
# Use this to find the number of loops you have to loop through

# 2
# get the start point right !
# convert the first number to bin ?

# 3 for each iteration of the loop find the ith (starting from last bit and move to the 2**loop values down:

# build aray and extend it until given length to find the ones in them






"""
def countOnes(left, right):
    count = 0
    for num in range(left, right+1):
        B = ""
        while num > 0:
            rem = str(num%2)
            num /= 2
            B = rem + B
        count += B.count('1')
    return count

C = {}


def inv_countOnes(n):
    c = 0
    while n != 0:
        n = n & (n-1)
        c += 1
    return c

def countOnes2(left, right):
    count = 0
    n = left

    while n <= right:
        count += inv_countOnes(n)
        n += 1
    print(count)
"""