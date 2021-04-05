# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        left_sides = [root]
        node = root.left
        while node:
            left_sides.append(node)
            node = node.left or node.right
        
        right_sides = [root]
        node = root.right
        while node:
            right_sides.append(node)
            node = node.right or node.left
        
        leaves = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right: leaves.append(node)
            stack.extend([child for child in [node.right, node.left] if child])
        
        boundries = [node.val for node in left_sides]
        added = set(left_sides)
        for node in leaves:
            if node not in added:
                boundries.append(node.val)
                added.add(node)
        for node in reversed(right_sides):
            if node not in added:
                boundries.append(node.val)
        return boundries
            
        
        
