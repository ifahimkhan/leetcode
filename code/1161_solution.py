# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum, max_level = root.val, 1
        queue = deque([(root, 1)])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node, level = queue.popleft()
                level_sum += node.val
                queue.extend([(child, level + 1) for child in [node.left, node.right] if child])
            if level_sum > max_sum:
                max_sum, max_level = level_sum, level
        return max_level
