# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self, root, val):
        node = root
        new_node = TreeNode(val)
        while node:
            if val > node.val:
                if not node.right: 
                    node.right = new_node
                    break
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = new_node
                    break
                else:
                    node = node.left
        else:
            return new_node
        return root 

    def recursive(self, root, val):
        if not root: return TreeNode(val)
        if root.val < val: root.right = self.recursive(root.right, val)
        if root.val > val: root.left = self.recursive(root.left, val)
        return root

    insertIntoBST = recursive # iterative