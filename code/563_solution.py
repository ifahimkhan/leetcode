# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(node):
            if not node: return 0
            lsum = dfs(node.left)
            rsum = dfs(node.right)
            tilt = abs(lsum - rsum)
            self.total += tilt
            return lsum + rsum + node.val
        
        dfs(root)
        return self.total
