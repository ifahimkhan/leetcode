# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recursive(self, root, p, q):
        if not root: return root
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)        
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)        
        return root

    def iterative(self, root, p, q):
        node = root
        while node:
            if p.val > node.val < q.val: node = node.right
            elif p.val < node.val > q.val: node = node.left
            else: return node

    lowestCommonAncestor = iterative # recursive
