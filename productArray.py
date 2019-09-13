

"""
Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

"""

def product_array(numbers):
    res = []
    i = 0


    while i < len(numbers):
        nums = numbers[:i] + numbers[i+1:]
        j = 0
        s = 1
        
        for num in nums:
            s *= num
        
        res.append(s) 
        i += 1
    
    return res

product_array([16,17,4,3,5,2])