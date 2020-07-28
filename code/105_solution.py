# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root, stack, i = None, [], 0
        for val in preorder:
            new = TreeNode(val)
            if not root: 
                last = root = new
            else:
                if last.val == inorder[i]:
                    while stack and stack[-1].val == inorder[i]:
                        last = stack.pop()
                        i += 1
                    last.right = new
                else:
                    last.left = new
                last = new
            stack.append(new)
        return root