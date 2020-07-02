# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        queue = deque([root])
        order = deque([[root.val]])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if not child: continue
                    queue.append(child)
                    level.append(child.val)
            if level: order.appendleft(level)
        return order
            