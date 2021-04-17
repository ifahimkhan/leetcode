class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        max_average = 0
        seen = set()
        annotation = dict()
        stack = [root]
        while stack:
            node = stack.pop()
            if node in seen:
                left_sum, left_num = annotation.get(node.left, (0, 0))
                right_sum, right_num = annotation.get(node.right, (0, 0))
                subtree_sum = left_sum + right_sum + node.val
                subtree_num = left_num + right_num + 1
                annotation[node] = (subtree_sum, subtree_num)
                max_average = max(max_average, subtree_sum / subtree_num)
            else:
                seen.add(node)
                stack.extend([nd for nd in [node, node.left, node.right] if nd])
        
        return max_average            
