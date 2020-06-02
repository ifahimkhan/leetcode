# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if not root: return root
        # root.right, root.left = map(self.invertTree, (root.left, root.right))
        # return root
        
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            for child in (node.left, node.right):
                if not child: continue
                stack.append(child)
        return root