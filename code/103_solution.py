# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        queue = deque([root])
        level = 0
        results = []
        
        while queue:
            level_nodes = deque()

            for _ in range(len(queue)):
                node = queue.popleft()
                if level & 1: level_nodes.appendleft(node.val)
                else: level_nodes.append(node.val)
                    
                for child in [node.left, node.right]:
                    if not child: continue
                    queue.append(child)
                    
            level += 1
            results.append(level_nodes)
        return results
    

    def dfs(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        stack = [(root, 0)]
        results = []
        
        while stack:
            node, level = stack.pop()
            if level >= len(results): results.append(deque())

            if level & 1: results[level].appendleft(node.val)
            else: results[level].append(node.val)
                
            for child in [node.right, node.left]:
                if not child: continue
                stack.append([child, level + 1])
        
        return results
            
    
    zigzagLevelOrder = dfs # bfs