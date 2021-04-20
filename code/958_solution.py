class Solution:
    def solution_bfs(self, root: TreeNode) -> bool:
        nodes_remain = 1 if root else 0
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if not node: return nodes_remain == 0
            nodes_remain -= 1
            queue.extend([node.left, node.right])
            if node.left: nodes_remain += 1
            if node.right: nodes_remain += 1
        
        return True
    
    def solution_dfs(self, root):
        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            if l & (l + 1) == 0 and l / 2 <= r <= l: return l + r + 1
            if r & (r + 1) == 0 and r <= l <= r * 2 + 1: return l + r + 1
            return -1
        return dfs(root) != -1
    
    isCompleteTree = solution_dfs # solution_bfs
