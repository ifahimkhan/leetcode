# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solution_dfs_handle_missing_nodes(root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
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

    def solution_dfs_doesnot(root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        def dfs(node):
            if not node or node in nodes: return node
            lca_l, lca_r = dfs(node.left), dfs(node.right)
            return node if lca_l and lca_r else lca_r or lca_l
        return dfs(root)

    lowestCommonAncestor = solution_dfs_doesnot # solution_dfs_handle_missing_nodes
