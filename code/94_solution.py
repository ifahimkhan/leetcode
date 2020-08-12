# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorder_iterative(self, root):
        results = []
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            results.append(node.val)
            node = node.right
        return results

    def inorder_iterative_with_set(self, root):
        results = []
        stack, visited = [root], set()
        while stack:
            node = stack.pop()
            if not node: continue
            if node in visited: results.append(node.val)
            else:
                visited.add(node)
                stack.extend([node.right, node, node.left])  # inorder
                # stack.extend([node, node.right, node.left])  # postorder
                # stack.extend([node.right, node.left, node])  # preorder    
        return results
        
    def inorder_recursive(self, root):
        results = []

        def dfs(node):
            if not node: return
            if node.left: dfs(node.left)
            results.append(node.val)
            if node.right: dfs(node.right)
        
        dfs(root)
        return results
    
    inorderTraversal = inorder_recursive # inorder_iterative # inorder_iterative_with_set