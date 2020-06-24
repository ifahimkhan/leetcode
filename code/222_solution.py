# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def height(node):
            h = -1
            while node:
                h += 1
                node = node.left
            return h
        
        h = height(root)
        node, num_nodes = root, 0
        while node:
            if height(node.right) == h - 1:
                num_nodes += 2 ** h
                node = node.right
            else:
                num_nodes += 2 ** (h - 1)
                node = node.left
            h -= 1
        return num_nodes