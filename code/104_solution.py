# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [(root, 1)] if root else []
        max_depth = 0
        while stack:
            node, level = stack.pop()
            max_depth = max(max_depth, level)
            for child in [node.left, node.right]:
                if not child: continue
                stack.append([child, level + 1])
        return max_depth