# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def iterative(self, root):
        queue = deque()
        queue.extend([root, root])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()        
            if not (node1 or node2): continue    
            if not (node1 and node2): return False
            if node1.val != node2.val: return False
            queue.extend([node1.left, node2.right, node2.right, node1.left])
        return True
    
    def recursive(self, root):
        def dfs(node1, node2):
            if not (node1 or node2): return True
            if not (node1 and node2): return False
            return (node1.val == node2.val) and dfs(node1.right, node2.left) and dfs(node2.right, node1.left)
        return dfs(root, root)
    
    isSymmetric = iterative # recursive