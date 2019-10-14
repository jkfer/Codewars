"""
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we count on you!
"""


from itertools import product


def get_possibilities(num):
    D = {0: [1, 2, 3],
         1: [4, 5, 6],
         2: [7, 8, 9],
         3: [None, 0, None]
         }
    r = None
    # find the row, that the number is in:
    for row, nums in D.items():
        if num in nums:
            r = row
    
    # Now get the index of the num:
    i = D[r].index(num)

    possib = []
    # get vert - index doesnt change: D[r][i] - r: row-1 to row+1
    row_start = r - 1 if r != 0 else r
    row_end = r + 1 if r != 3 else r
    for R in range(row_start, row_end+1):
        if D[R][i] != None and D[R][i] not in possib:
            possib.append(D[R][i])
    
    # get horiz - Row doesnt change: D[r][i]: index goes from i-1 to i+1
    i_start = i - 1 if i != 0 else i
    i_end = i + 1 if i != 2 else i
    for I in range(i_start, i_end + 1):
        if D[r][I] != None and D[r][I] not in possib:
            possib.append(D[r][I]) 
    
    return possib



def get_pins(observed):
    P = []
    res = []
    for i in observed:
        P.append(get_possibilities(int(i)))
    
    for ans in product(*P):
        res.append(("".join(map(str, ans))))

    return res

x = get_pins("1234")
print(x)





