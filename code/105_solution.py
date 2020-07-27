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
            new_node = TreeNode(val)
            if not root:
                node = root = new_node
            else:
                if node.val == inorder[~i]:
                    while stack and stack[-1].val == inorder[~i]:
                        i += 1
                        node = stack.pop()
                    node.left = new_node
                    node = new_node
                else:
                    node.right = new_node
                    node = new_node
            stack.append(new_node)
        return root