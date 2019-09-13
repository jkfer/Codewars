

# tidy number is that number where each digit is greater than or equal to the digit preseding it.

def tidyNumber(n):
    L = [int(i) for i in str(n)]
    print(L)
    i = 0
    res = True
    while i < len(L) - 1:
        if L[i] > L[i+1]:
            res = False
            break
        i += 1

    return res


tidyNumber(12)