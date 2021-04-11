# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level = [root]
        while level:
            next_level = []
            for node in level:
                next_level.extend([child for child in [node.left, node.right] if child])
            
            if next_level: 
                level = next_level
            else:
                break
        
        return sum([node.val for node in level])
