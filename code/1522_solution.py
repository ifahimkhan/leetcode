"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        max_diam = 0
        depths = dict() # node to maximum depth of subtree from this node
        stack = [root] if root else []
        while stack:
            node = stack[-1]
            if node not in depths:
                depths[node] = []
                stack.extend(node.children)
            else:
                stack.pop()
                d1, d2 = self.top2([depths[child] for child in node.children])
                if d1 is None:  
                    depths[node] = diam = 0
                elif d2 is None:  
                    depths[node] = diam = 1 + d1
                else: 
                    depths[node], diam = 1 + d1, 2 + d1 + d2
                max_diam = max(max_diam, diam)
        return max_diam
    
    @staticmethod        
    def top2(arr):
        t1, t2 = None, None
        for val in arr:
            if t1 is None: 
                t1 = val
            elif val >= t1:
                t2 = t1
                t1 = val
            elif t2 is None or val > t2:
                t2 = val
        return t1, t2
