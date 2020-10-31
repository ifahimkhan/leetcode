# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solution_inorder(self, root):
        """ Do not return anything, modify root in-place instead. """
        stack = []
        n1, n2, prev, node = None, None, None, root
        
        # inorder
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev and node.val < prev.val:
                n1 = node
                if n2: break
                n2 = prev
            prev = node
            node = node.right

        n1.val, n2.val = n2.val, n1.val        
        
    recoverTree = solution_inorder
