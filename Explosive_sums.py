"""
How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples
Basic
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
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
write the number as a combinations of two numbes - then find the ways of making those two numbes from the DP structure:

res = [1, 2]

"""
n = 42

def exp_sum(n):
    res = [1, 2]
    for i in range(2, n + 1):
        N = i + 1
        # how many ways you can write N as a sum of two numbers:
        j = 1
        count = 0
        while j <= N // 2:
            count += res[j] + res[N-j]
            j += 1
        
        res[i] = count
        print(res)

exp_sum(3)