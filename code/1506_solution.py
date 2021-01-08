"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def solution_hashmap(self, tree): 
        # no assumption on uniqueness of nodes' value
        in_degrees = defaultdict(int)
        for node in tree:
            for child in node.children: 
                in_degrees[child] += 1
        
        for node in tree:
            if in_degrees[node] == 0:
                return node
        
    def solution_in_cancel_out(self, tree):
        # assume uniqueness of nodes' value
        val = 0
        for node in tree:
            val += node.val
            for child in node.children:
                val -= child.val
        
        for node in tree:
            if node.val == val:
                return node
        
    findRoot = solution_in_cancel_out # solution_hashmap
