"""
How many ways can you make the sum of a number?

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1

Examples
exp_sum(1) # 1
exp_sum(2) # 2 -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42
Explosive
exp_sum(50) # 204226
exp_sum(80) # 15796476
exp_sum(100) # 190569292
See here for more examples.

Idea -
Solve using DP (Dynamic Programming)
write the number as a combinations of two numbes
then find the ways of making those two numbes from the DP structure:

0 => 1 (0)
1 => 1 (1)
2 => 2 (1, 1), (2)
3 => 3 (3), (1, 1, 1), (2, 1)

The pattern here is that
for 1, you add the ways of making 0
for 2, you add the ways of making, ways(0), ways(1)
for 3, you add the ways of making, ways(1) + ways(2)
for 5, you add the ways of making, ways(1) + ways(4) (for 4, you use ways(1), ways(3)....
for 10 you add the ways of making ways(1), ways(9)
"""


def exp_sum(n):
    if n in [0, 1, 2]:
        return n

    R = [1] + [0] * n

    for i in range(1, n+1):
        for j in range(i, n+1):
            R[j] += R[j-i]

    return R[-1]


print(exp_sum(10))
