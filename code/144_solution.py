# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        order = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            order.append(node.val)
            for child in [node.right, node.left]:
                if not child: continue
                stack.append(child)
        return order