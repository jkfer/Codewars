
str = "The greatest victory is that which requires no battle"

def reverseWords(str):
    output = ""
    L = str.split()
    for i, word in enumerate(L):
        if i == len(L) - 1:
            output =  word + output
        else:
            output = ' ' + word + output
        
    return output

x = reverseWords(str)
print(x)
print(list(x))