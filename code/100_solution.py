# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self, p: TreeNode, q: TreeNode) -> bool:
        tour_p, tour_q = deque([p]), deque([q])
        while tour_p and tour_q:
            node_p, node_q = tour_p.popleft(), tour_q.popleft()
            if not (node_p or node_q): continue
            if not (node_p and node_q): return False
            if node_p.val != node_q.val: return False
            tour_p.extend([node_p.left, node_p.right])
            tour_q.extend([node_q.left, node_q.right])
        return tour_p == tour_q
    
    def recursive(self, p, q):
        if not (p or q): return True
        if not (p and q): return False
        if p.val != q.val: return False
        return self.recursive(p.left, q.left) and self.recursive(p.right, q.right)
    
    isSameTree = recursive # iterative
