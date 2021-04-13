# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solution_recurrsive(self, root: TreeNode) -> int:
        self.max_path_sum = root.val

        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.max_path_sum = max(self.max_path_sum, l+r+node.val)
            return max(0, node.val + max(l,r))

        dfs(root)
        return self.max_path_sum

    def solution_iterative(self, root: TreeNode) -> int:
        max_path_sum = root.val
        path_sum = dict()
        visited = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            if node in visited:
                l, r = path_sum.get(node.left, 0), path_sum.get(node.right, 0)
                path_sum[node] = max(node.val, l + node.val, r + node.val, 0)
                max_path_sum = max(max_path_sum, l + r + node.val)
            else:
                visited.add(node)
                stack.extend([node, node.right, node.left])  # postorder
        return max_path_sum
        
    maxPathSum = solution_recurrsive #  solution_iterative
