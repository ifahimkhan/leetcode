# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1: return TreeNode(val=v,left=root)
        
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            if level == d - 1:
                node.left = TreeNode(val=v, left=node.left)
                node.right = TreeNode(val=v, right=node.right)
            else:
                stack.extend([(child, level + 1) for child in [node.left, node.right] if child])
        
        return root
                
                
        
