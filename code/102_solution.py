# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        queue = deque([root]) if root else []
        while queue:
            results.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                results[-1].append(node.val)
                # for child in [node.left, node.right]:
                #     if not child: continue
                #     queue.append(child)
                queue.extend([child for child in [node.left, node.right] if child])
        return results