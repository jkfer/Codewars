"""
Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
No letters should return 'z'
Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
"""



def add_letters(*letters):
    D = {}
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i, lett in enumerate(alph, start=1):
        D[lett] = i

    val = 0
    for lett in letters:
        val += D[lett]
    
    # adjust for overflow
    if val > 26:
        val %= 26
    
    if val == 0:
        return 'z'
    else:
        for key, value in D.items():
            if value == val:
                return key
    print(val)

x = add_letters("x", "c", "g", "z", "n")
print(x)