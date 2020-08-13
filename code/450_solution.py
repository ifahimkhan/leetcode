# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def iterative(self, root, key):
        parent, node = None, root
        # find node to delete
        while node and node.val != key:
            parent = node
            node = node.left if node.val > key else node.right

        if not node: return root # not found do nothing
        if not parent: return self.reform(node.left, node.right) 
        if parent.left == node: parent.left = self.reform(node.left, node.right)
        if parent.right == node: parent.right = self.reform(node.left, node.right)
        return root      
    
    def recursive(self, root, key):
        if not root: return root
        if root.val == key: return self.reform(root.left, root.right)
        if root.val > key: root.left = self.recursive(root.left, key)
        if root.val < key: root.right = self.recursive(root.right, key)
        return root
    
    def reform(self, left, right):
        if not left: return right
        if not right: return left
        # promote right child as new root
        # push left subtree to be the left child of the smallest from right subtree
        node = right
        while node.left: node = node.left
        node.left = left
        return right

    deleteNode = iterative # recursive
