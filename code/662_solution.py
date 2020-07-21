# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        max_width = 0
        queue = deque([(root, 1)])  # node, idx
        
        while queue:
            level_width = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, level_width)
            
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                if node.left: queue.append((node.left, 2 * idx))
                if node.right: queue.append((node.right, 2 * idx + 1))
        return max_width
    
    def dfs(self, root):
        max_width = 0
        stack = deque([(root, 1, 1)])  # node, level, idx
        level_min_max = dict() # level -> min_idx, max_idx
        
        while stack:
            node, level, idx = stack.pop()
            if level not in level_min_max: level_min_max[level] = [2 ** level, 2 ** (level -1)]
            level_min_max[level][0] = min(level_min_max[level][0], idx)
            level_min_max[level][1] = max(level_min_max[level][1], idx)
            if node.left: stack.append((node.left, level + 1, 2 * idx))
            if node.right: stack.append((node.right, level + 1, 2 * idx + 1))
        
        for min_idx, max_idx in level_min_max.values():
            max_width = max(max_width, max_idx - min_idx + 1)
        
        return max_width

    widthOfBinaryTree = dfs # bfs