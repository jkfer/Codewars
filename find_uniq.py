"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
Its guaranteed that array contains more than 3 numbers
The tests contain some very huge arrays so think about performance
"""


def find_uniq(arr):
    i = 0
    res = []
    while i < len(arr):
        if arr[i] not in res:
            res.append(arr[i])
        elif len(res) == 2:
            break
        i += 1

    if i == len(arr):
        return res[1]
    else:
        res.remove(arr[i])
        return res[0]


def find_uniq2(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


x = find_uniq([ 0, 0, 0.55, 0, 0 ])
print(x)