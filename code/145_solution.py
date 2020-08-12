# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder_iterative(self, root):
        if not root: return None
        results = []
        stack = [root, root]
        while stack:
            node = stack.pop()
            if stack and stack[-1] is node:
                if node.right: stack.extend([node.right] * 2)
                if node.left: stack.extend([node.left] * 2)
            else:
                results.append(node.val)
        return results

    def postorder_iterative_with_set(self, root):
        results = []
        stack, visited = [root], set()
        while stack:
            node = stack.pop()
            if not node: continue
            if node in visited: results.append(node.val)
            else:
                visited.add(node)
                # stack.extend([node.right, node, node.left])  # inorder
                stack.extend([node, node.right, node.left])  # postorder
                # stack.extend([node.right, node.left, node])  # preorder
        return results
    
    def postorder_recursive(self, root):
        results = []

        def dfs(node):
            if not node: return 
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            results.append(node.val)

        dfs(root)
        return results

    postorderTraversal = postorder_recursive # postorder_iterative_with_set # postorder_iterative