# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solution_bfs(self, root):
        if not root: return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not (node.left or node.right): return depth
            if node.left: queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))
                
    def solution_dfs(self, root):
        if not root: return 0
        min_depth = 2**32
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if not (node.left or node.right): min_depth = min(min_depth, depth)
            if node.left: stack.append((node.left, depth + 1))
            if node.right: stack.append((node.right, depth + 1))
        return min_depth
    
    minDepth = solution_dfs # solution_bfs
