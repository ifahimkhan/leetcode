# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        to_flip, stack, i = [], [root], 0
        while stack:
            node = stack.pop()
            if not node: continue
            if node.val != voyage[i]: return [-1]

            if node.right and node.right.val == voyage[i + 1]:
                if node.left: to_flip.append(node.val)
                stack.extend([node.left, node.right])
            else:
                stack.extend([node.right, node.left])
                
            i += 1
        return to_flip
