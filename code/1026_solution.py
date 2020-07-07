# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        V = 0
        stack = [(root, root.val, root.val)]
        while stack:
            node, path_min, path_max = stack.pop()
            path_min = min(path_min, node.val)
            path_max = max(path_max, node.val)
            for child in [node.left, node.right]:
                if not child: continue
                stack.append((child, path_min, path_max))
            if not (node.left or node.right):
                V = max(V, path_max - path_min)
        return V