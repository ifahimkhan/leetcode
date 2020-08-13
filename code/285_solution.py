# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # straight up inorder traversal
        if not root: return 
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            if node.val > p.val: return node
            node = node.right
