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

    def solution_iterative(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        def find_path(node, target):
            path, stack = [], [node]
            while stack:
                node = stack.pop()
                if not path or path[~0] is not node:
                    path.append(node)
                    if node is target: return path
                    stack.extend([nd for nd in [node, node.left, node.right] if nd])
                else:
                    path.pop()

        p_path = find_path(root, p)
        q_path = find_path(root, q)
        lca = root
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]: break
            else: lca = p_path[i]
        return lca
    
    lowestCommonAncestor = solution_recursive # solution_iterative
                
