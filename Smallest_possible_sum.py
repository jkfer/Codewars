# 4kyu
# https://www.codewars.com/kata/52f677797c461daaf7000740

from collections import Counter

def divisors(n):
    res = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            res.add(i)
            res.add(n/i)
    return res

# solution timed out
def solution(a):
    if len(a) == 1:
        return a[0]
    
    while len(set(a)) > 1:
        a.sort(reverse=True, key=int)
        i = a.count(a[0]) - 1
        #while a[i] == a[i+1] and i < len(a) - 1:
        #    i += 1
        
        if a[i] % a[i+1] == 0:
            a[i] -= a[i+1]
        elif a[i] % a[i+1] > 0:
            a[i] %= a[i+1]
    
    return sum(a)

# solution timed out
def solution2(a):
    if len(a) == 1:
        return a[0]
    
    res = [None] * len(a)

    for i, num in enumerate(a):
        if i == 0:
            res[i] = divisors(num)
        else:
            res[i] = res[i-1].intersection(divisors(num))
        
        if len(res[i]) == 1:
            return res[i][0] * len(a)
    
    R = list(res[-1])
    R.sort(reverse=True, key=int)
    return R[0] * len(a)




#X = [13062222, 1647278, 6348800, 14404088, 2099072, 14463918, 863288, 2839352, 12057822, 3308382, 5542862, 187550, 2430648, 377208, 3813248, 10884782, 6309182, 4587008, 6508512, 13579488, 12499262, 13176302, 215822, 3223008, 1607102, 5035950, 513422, 11357408, 11146112, 4223502, 5767550, 1687950, 11894328, 1489550, 4722912, 3630968, 3782558, 3110912, 1898750, 3482478, 1432448, 15252992, 201438, 1250168, 1015808, 3661038, 10781118, 6309182, 15007968, 9430200, 7813550, 1321592, 9673550, 632462, 2480000, 7167200, 583358, 1791800, 5729792, 8718750, 1489550, 458552, 2191328, 10832888, 2504862, 6074078, 2786528, 5468958, 1146752, 11624318, 5617262, 1834208, 155000, 1267838, 13233528, 2554958, 11463800, 321408, 8214752, 2144952, 7041278, 607662, 13005368, 3000800, 406782, 9047288, 10473102, 6875118, 536238, 819950, 208568, 14523872, 13579488, 1708472, 1687950, 8350718, 12892032, 2580192, 9094718]
#print(solution(X))

print(solution([1,2]))