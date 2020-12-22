# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        
        def is_balance(node):
            if not(node.left or node.right): return 1, True
            hl, l_balance = is_balance(node.left) if node.left else (0, True)
            hr, r_balance = is_balance(node.right) if node.right else (0, True)
            if not l_balance or not r_balance: return 0, False
            return 1 + max(hl, hr), abs(hl - hr) <= 1
        
        _, is_balanced = is_balance(root)
        return is_balanced
                    
            
