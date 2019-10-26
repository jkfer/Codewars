"""
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

Idea:
join all the rows of the array to have one list

"""

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def snail(array):
    new_arr = []
    n = len(array[0])
    k = n

    # base check:
    if n == 0:
        return new_arr

    for r in array:
        new_arr += r

    ans = []
    while len(new_arr) > 0:
        R = list(range(n)) + list(range((n*2 - 1), n*n, k))
        for a, i in enumerate(R):
            v = new_arr.pop(i-a)
            ans.append(v)

        new_arr = new_arr[::-1]
        n -= 1
        k -= 1

    print(ans)


snail(array)
