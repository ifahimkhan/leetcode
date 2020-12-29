# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.count = 0
        
        def palindromic(path):
            val_counts = Counter(path)
            num_odd = 0
            for v in val_counts.values():
                if v % 2 == 1: num_odd += 1
            return num_odd <= 1
        
        def dfs(path, node):
            if not (node.left or node.right):
                if palindromic(path): self.count += 1
                return 
            
            for child in [node.left, node.right]:
                if not child: continue
                dfs(path + [child.val], child)
        
        dfs([root.val], root)
        return self.count
                
                
        
