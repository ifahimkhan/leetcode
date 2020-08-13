# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # inorder traversal of BST is non decreasing. 
        stack, prev, node = [], float('-inf'), root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev >= node.val: return False
            prev = node.val
            node = node.right
        return True
