"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# https://leetcode.com/problems/intersection-of-two-linked-lists/ ?
# p -> lca --> root -> q ----> lca
# q ----> lca --> root -> p -> lca

class Solution:
    def solution_set(self, p, q):
        p_parents = set([p])
        q_parents = set([q])

    while True:
        if p in q_parents: return p
        if q in p_parents: return q
        if p.parent:
            p = p.parent
            p_parents.add(p)
        if q.parent:
            q = q.parent
            q_parents.add(q)
   
    def solution_two_pointers(self, p: 'Node', q: 'Node') -> 'Node':
        n1, n2 = p, q
        while n1 != n2:
            n1 = n1.parent if n1.parent else q
            n2 = n2.parent if n2.parent else p
        return n1
    lowestCommonAncestor = solution_two_pointers
