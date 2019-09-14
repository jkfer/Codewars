"""
Your task is to calculate logical value of boolean array. Test arrays are one-dimensional and their size is in the range 1-50.

Links referring to logical operations: AND, OR and XOR.

You should begin at the first value, and repeatedly apply the logical operation across the remaining elements in the array sequentially.

First Example:

Input: true, true, false, operator: AND

Steps: true AND true -> true, true AND false -> false

Output: false

Second Example:

Input: true, true, false, operator: OR

Steps: true OR true -> true, true OR false -> true

Output: true

Third Example:

Input: true, true, false, operator: XOR

Steps: true XOR true -> false, false XOR false -> false

Output: false
"""
from collections import Counter

def logical_calc(array, op):
    if op == "AND":
        return False if False in array else True
    elif op == "OR":
        return True if True in array else False
    else:
        # op == "XOR"
        if len(array) == 1:
            return array[0]
        else:
            stack = []
            i = 0
            while i < len(array):
                if stack == []:
                    if array[i] != array[i+1]:
                        stack.append(True)
                    else:
                        stack.append(False)
                    i += 1
                else:
                    stack.append(True) if stack[0] != array[i] else stack.append(False)
                    stack.pop(0)
                i += 1
            return stack[0]

x = logical_calc([True, False], "XOR")
print(x)

# alternate is use operator module .and_ .or_ feature