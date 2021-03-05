# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        level_avgs = []
        level = [root]
        while level:
            total, count, next_level = 0, 0, []
            for _ in range(len(level)):
                node = level.pop()
                
                total += node.val
                count += 1
                
                next_level.extend(child for child in [node.left, node.right] if child)
                
            level_avgs.append(total / count)
            level = next_level
            
        return level_avgs
    
    
    def dfs(self, root):
        level_stats = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            
            if level == len(level_stats):
                level_stats.append([node.val, 1])
            else:
                level_stats[level][0] += node.val
                level_stats[level][1] += 1
                
            stack.extend((child, level + 1) for child in [node.left, node.right] if child)
        
        level_avgs = [level[0] / level[1] for level in level_stats]
        return level_avgs
    
    averageOfLevels = dfs # bfs
