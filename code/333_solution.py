# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solution_recursive(self, root: TreeNode) -> int:
        
        def dfs(node):
            ''' 
            Returns:
                largest bst subtree size from this node 
                largest bst subtree size if including this node
                whether the subtree including this node is valid bst
                minimal node value in subtree from this node
                maximal node value in subtree from this node
            '''
            if not node: return 0, 0, 1, float('inf'), float('-inf')
            v = node.val
            
            l_max_size, l_size, l_valid, l_min, l_max = dfs(node.left)
            r_max_size, r_size, r_valid, r_min, r_max = dfs(node.right)
            
            this_size, this_valid = 0, 0
            if l_valid and r_valid and l_max < v < r_min: 
                this_valid = 1
                this_size = l_size + r_size + 1
                
            this_max_size = max(l_max_size, r_max_size, this_size)
            this_min = min(l_min, node.val)
            this_max = max(r_max, node.val)
            return this_max_size, this_size, this_valid, this_min, this_max
        
        return dfs(root)[0]
    
    def solution_iterative(self, root):
        stack = [root]
        base_case = (0, 0, 1, float('inf'), float('-inf'))
        annotation = dict()
        visited = set()
        while stack:
            node = stack.pop()
            if not node: continue
                
            v = node.val
            if node in visited:
                l_max_size, l_size, l_valid, l_min, l_max = annotation.get(node.left, base_case)
                r_max_size, r_size, r_valid, r_min, r_max = annotation.get(node.right, base_case)
                this_size, this_valid = 0, 0
                if l_valid and r_valid and l_max < v < r_min: 
                    this_valid = 1
                    this_size = l_size + r_size + 1

                this_max_size = max(l_max_size, r_max_size, this_size)
                this_min = min(l_min, node.val)
                this_max = max(r_max, node.val)
                annotation[node] = (this_max_size, this_size, this_valid, this_min, this_max)
            else:
                visited.add(node)
                stack.extend([node, node.right, node.left])
        return annotation.get(root, base_case)[0]
        
    largestBSTSubtree = solution_iterative # solution_recursive
            
            
