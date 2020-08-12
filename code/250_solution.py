# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node):
            is_uni = True
            for child in [node.left, node.right]:
                if not child: continue
                is_uni &= dfs(child) and child.val == node.val
            self.count += is_uni
            return is_uni
        
        if root: dfs(root)
        return self.count
