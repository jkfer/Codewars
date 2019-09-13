
"""
Your task is to write a function that takes a string and return a new string with all vowels removed.

"""

def disemvowel(string):
    vowels = list('aeiouAEIOU')
    L = list(string)
    
    for i, lett in enumerate(L):
        if lett in vowels:
            L.pop(i)
        
    return ''.join(L)



def disemvowel2(string):
    vowels = list('aeiouAEIOU')
    
    for i, lett in enumerate(vowels):
        string = string.replace(lett, '')
    
    return string


x = disemvowel2("N ffns bt,\nYur wrtng s mng th wrst 'v vr rad")
print(x)