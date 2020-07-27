# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root, stack, i = None, [], 0
        for val in reversed(postorder):
            new = TreeNode(val)
            if not root:
                last = root = new
            else:
                if last.val == inorder[~i]:
                    while stack and stack[-1].val == inorder[~i]:
                        i += 1
                        last = stack.pop()
                    last.left = new
                else:
                    last.right = new
                last = new
            stack.append(new)
        return root