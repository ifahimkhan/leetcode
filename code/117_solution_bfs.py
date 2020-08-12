"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        queue = deque([root]) if root else []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i != n - 1: node.next = queue[0]
                for child in [node.left, node.right]:
                    if not child: continue
                    queue.append(child)
        return root
