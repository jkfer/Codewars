

def sum_of_intervals(intervals):
    L = []
    for a, b in intervals:
        L += range(a, b)

    return len(set(L))


sum_of_intervals([
   [1, 2],
   [6, 10],
   [11, 15]
])
