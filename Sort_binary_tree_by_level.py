"""
You are given a binary tree:

Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
"""

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    res = []

    def traverse(N):
        Oth = []
        for node in N:
            if node.left:
                Oth += [node.left]
            if node.right:
                Oth += [node.right]
            if node.value:
                res.append(node.value)
        
        if len(Oth) > 0:
            return traverse(Oth)
        else:
            return res
    
    return traverse([node])


Node_ex = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
x = tree_by_levels(Node_ex)
print(x)