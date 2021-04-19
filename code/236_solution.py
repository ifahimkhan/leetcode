# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solution_recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node in (None, p, q): return node
            l, r = dfs(node.left), dfs(node.right)
            return node if l and r else l or r
        return dfs(root)

    def solution_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        stack = [[root, [root]]]
        while stack:
            node, path = stack.pop()
            if node == p: p_path = path.copy()
            if node == q: q_path = path.copy()
            for child in [node.left, node.right]:
                if not child: continue
                stack.append([child, path + [child]])
        
        lca = root
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]: break
            else: lca = p_path[i]
        return lca
    
    lowestCommonAncestor = solution_recursive # solution_iterative
                
