class Solution:
    def solution_recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return (None, 0)
            (lca_l, n_found_l), (lca_r, n_found_r) = dfs(node.left), dfs(node.right)
            if lca_l or lca_r: return (lca_l or lca_r, 2)
            n_found = n_found_l + n_found_r + int(node in [p, q])
            lca = node if n_found == 2 else None
            return lca, n_found
        return dfs(root)[0]
    
    def solution_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
            return []

        p_path = find_path(root, p)
        q_path = find_path(root, q)
        lca = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]: 
                break
            else: 
                lca = p_path[i]
        return lca

    lowestCommonAncestor = solution_recursive # solution_iterative
