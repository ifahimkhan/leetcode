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
        path_sum = defaultdict(int)
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left and node.left not in path_sum: 
                stack.append(node.left)
            elif node.right and node.right not in path_sum: 
                stack.append(node.right)
            else:  
                stack.pop()
                l, r = path_sum[node.left], path_sum[node.right]
                path_sum[node] = max(node.val, l + node.val, r + node.val, 0)
                max_path_sum = max(max_path_sum, l + r + node.val)
        return max_path_sum
        
    maxPathSum = solution_recurrsive #  solution_iterative
