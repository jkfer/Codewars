'''
4kyu
----
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing: 1234
The digits are sequential, decrementing: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

So, you should expect these inputs and outputs:

# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2
Error Checking
A number is only interesting if it is greater than 99!
Input will always be an integer greater than 0, and less than 1,000,000,000.
The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
You should only ever output 0, 1, or 2.
'''
import re


def is_int1(N):
    return True if re.match(r'^[1-9]0+$', N) else False


def is_int2(N):
    return True if re.match(r'^(\d)\1+$', N) else False


def is_int3(N):
    K = "".join(map(str, range(int(N[0]), int(N[-1]) + 1)))
    K_rev = "".join(map(str, range(int(N[-1]), int(N[0])+1)))
    
    return True if N == K or N == K_rev else False


def is_int4(N):
    return True if N == N[::-1] else False

# check if the number is in a incrementing or decrementing seq
def is_incr_decr(N):
    # get end values:
    en = int(N[-1])
    # check if the numbers leading upto it are incre
    # get start and one before last dig: and turn them to a list
    if (en == 0) and (N[:-1] in "123456789"):
        return True if N[-2] == "9" else False
    # check if the numbers leading upto it are decre
    elif (en == 0) and (N[:-1] in "987654321"):
        return True if N[-2] == "1" else False
    # non-zero involved decrements
    elif (N in "123456789") or (N in "987654321"):
        return True
    else:
        return False


def check(N, num, awesome_phrases):
    if len(N) >= 3:
        if any([is_int1(N), is_int2(N), is_int3(N), is_int4(N), is_incr_decr(N)]) or int(N) in awesome_phrases:
            return num
        else:
            return 0
    else:
        return 0

def is_interesting(number, awesome_phrases):
    N = str(number)
    N_plus_1 = str(number+1)
    N_plus_2 = str(number+2)
    
    A = check(N, 2, awesome_phrases) 
    B = check(N_plus_1, 1, awesome_phrases)
    C = check(N_plus_2, 1, awesome_phrases)

    if A == 2:
        return A
    else:
        return B if B == 1 else C

x = is_interesting(3236, [1337, 256])
print(x)