"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

def anagrams(word, words):
    #your code here
    res = []
    for new_word in words:
        if set(word) == set(new_word) and len(word) ==  len(new_word):
            if all(word.count(lett) == new_word.count(lett) for lett in list(word)):
                res.append(new_word)
    
    return res


x = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print(x)

def anagrams2(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]


from collections import Counter

def anagrams3(word, words):
    counts = Counter(word)
    return [w for w in words if Counter(w) == counts]