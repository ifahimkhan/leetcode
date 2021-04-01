# https://leetcode.com/problems/intersection-of-two-linked-lists/ ?

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        n1, n2 = p, q
        while n1 != n2:
            n1 = n1.parent if n1.parent else q
            n2 = n2.parent if n2.parent else p
        return n1
