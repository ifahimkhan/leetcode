# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        total = 0
        while stack:
            node, num = stack.pop()
            num = (num << 1) + node.val
            if not (node.left or node.right): total += num
            stack.extend([(child, num) for child in [node.left, node.right] if child])
        return total
