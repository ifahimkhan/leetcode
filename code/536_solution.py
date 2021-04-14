# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s: return None

        stack = []
        node = None

        l = 0
        while l < len(s):
            if s[l] == '(':
                stack.append(node)
                node = None
                l += 1
            elif s[l] == ')':
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                node = stack.pop()
                l += 1
            else:
                r = l
                while r < len(s) and s[r] not in '()': r += 1
                node = TreeNode(val=int(s[l:r]))
                l = r
        return node 
