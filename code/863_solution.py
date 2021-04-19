class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        adj_lists = defaultdict(set)

        stack = [root]
        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if not child: continue
                adj_lists[child].add(node)
                adj_lists[node].add(child)
                stack.append(child)

        queue = [target]
        seen = set([target])
        for i in range(K):
            queue = [nei for nd in queue for nei in adj_lists[nd] if nei not in seen]
            seen |= set(queue)
        return [node.val for node in queue]
