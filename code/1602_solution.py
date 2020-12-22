# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = deque([root])
        found_u = False
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if found_u: return node
                if node == u: found_u = True
                queue.extend([child for child in [node.left, node.right] if child])
            if found_u: return None
        return None
