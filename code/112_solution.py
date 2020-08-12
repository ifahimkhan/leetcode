# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if not root: return False
        stack = [(root, 0)]
        while stack:
            node, val = stack.pop()
            val += node.val
            if not (node.left or node.right) and val == total: return True
            if node.left: stack.append((node.left, val))
            if node.right: stack.append((node.right, val))
        return False