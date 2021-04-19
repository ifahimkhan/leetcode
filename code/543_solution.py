# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Bascially, the same as 124

class Solution:
    def solution_recursive(root: TreeNode) -> int:
        max_diam[0] = 0

        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            max_diam[0] = max(max_diam[0], l+r)
            return max(0, 1 + max(l,r))

        dfs(root)
        return max_diam[0]        

    def solution_iterative(root: TreeNode) -> int:
        max_dim = 0
        depths = defaultdict(int)
        stack = [root] if root else []
        while stack:
            node = stack[-1]
            if node.left and node.left not in depths:
                stack.append(node.left)
            elif node.right and node.right not in depths:
                stack.append(node.right)
            else:
                stack.pop()
                l, r = depths[node.left], depths[node.right]
                depths[node] = 1 + max(l, r)
                max_dim = max(max_dim, l + r)
        return max_dim
    
    diameterOfBinaryTree = solution_iterative
