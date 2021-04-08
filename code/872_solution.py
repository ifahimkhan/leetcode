# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def array_equals(arr1, arr2):
            if len(arr1) != len(arr2): return False
            for v1, v2 in zip(arr1, arr2):
                if v1 != v2: return False
            return True
        
        def dfs(root):
            leaf_values = []
            visited = set()
            stack = [root]
            while stack:
                node = stack.pop()
                if not node.left and not node.right: leaf_values.append(node.val)
                stack.extend([child for child in [node.right, node.left] if child])
            return leaf_values
        
        return array_equals(dfs(root1), dfs(root2))
            
            
            
