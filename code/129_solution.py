# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        stack = [(root, 0)]
        while stack:
            node, partial = stack.pop()
            if not node: continue
            partial = 10 * partial + node.val
            if not (node.left or node.right): total += partial
            else: stack.extend([(node.left, partial), (node.right, partial)])
        return total