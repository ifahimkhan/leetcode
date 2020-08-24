# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        nodes = [(root, 0)] if root else []
        while nodes:
            node, is_left = nodes.pop()
            if is_left and not (node.left or node.right): total += node.val
            if node.left: nodes.append((node.left, 1))
            if node.right: nodes.append((node.right, 0))
        return total
                
