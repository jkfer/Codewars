"""
Given a string, return a new string that has transformed based on the input:

Change case of every character, ie. lower case to upper case, upper case to lower case.
Reverse the order of words from the input.
Note: You will have to handle multiple spaces, and leading/trailing spaces.

For example:

"Example Input" ==> "iNPUT eXAMPLE"
You may assume the input only contain English alphabet and spaces.
"""

def string_transformer(s):
    # your code here
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()

    out = ""
    for i, lett in enumerate(s):
        if lett in lower:
            out += lett.upper()
        elif lett in upper:
            out += lett.lower()
        else:
            out += lett
    
    #return out

    # Now reverse the string with preserving the spaces
    final = ""
    output = ""

    for i, lett in enumerate(out):
        if lett.isspace():
            final = ' ' + output + final
            output = ""
        else:
            output += lett
    
    return output + final

# other solutions:
def string_transformer2(s):
    s = s.swapcase()
    s = s.split(" ")[::-1]
    print(s)
    s = " ".join(s)
    return s

x = string_transformer2("To    be OR not to be That is the Question")
print(x)
