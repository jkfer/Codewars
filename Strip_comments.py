"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution(text, markers):
    L = text.split('\n')
    for i, line in enumerate(L):
        for j in markers:
            if j in line:
                K = line.index(j)
                line = line[:K]
                L[i] = line.strip()
    
    return "\n".join(L)


if __name__ == "__main__":
    X = solution('cherries lemons cherries\nwatermelons lemons avocados\nbananas', ['-', '#', '?', '@', '!', '^', '=', "'", ','])
    print(X)

