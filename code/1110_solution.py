# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return 
        
        to_delete = set(to_delete)
        forest = []
        stack = [(root, True)]
        
        while stack:
            node, consider_root = stack.pop()
            if node.val not in to_delete and consider_root: forest.append(node)
            consider_root = node.val in to_delete
            
            if node.left:
                stack.append((node.left, consider_root))
                if node.left.val in to_delete: node.left = None
                    
            if node.right:
                stack.append((node.right, consider_root))
                if node.right.val in to_delete: node.right = None
                    
        return forest
            
