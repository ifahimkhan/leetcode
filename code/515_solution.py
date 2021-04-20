class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        max_values = []
        row = [root] if root else []
        while row:
            max_values.append(max(node.val for node in row))
            row = [child for node in row for child in (node.left, node.right) if child]
        return max_values
