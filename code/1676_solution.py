# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        total = len(nodes)
        nodes = set(nodes)
        def dfs(node):
            if not node: return None, 0
            (lca_l, n_found_l), (lca_r, n_found_r) = dfs(node.left), dfs(node.right)
            if lca_l or lca_r: return (lca_l or lca_r, total)
            n_found = n_found_l + n_found_r + int(node in nodes)
            lca = node if n_found == total else None
            return lca, n_found
        return dfs(root)[0]        
