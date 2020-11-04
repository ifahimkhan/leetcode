class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: return list(range(n))
        
        adj_list = defaultdict(set)
        for (n1, n2) in edges:
            adj_list[n1].add(n2)
            adj_list[n2].add(n1)
        
        # bfs topsort
        level = deque([node for node in adj_list if len(adj_list[node]) == 1])
        while n > 2:
            nodes_this_level = len(level)
            n -= nodes_this_level
            for i in range(nodes_this_level):
                node = level.popleft()
                for next_ in adj_list[node]:
                    adj_list[next_].remove(node)
                    if len(adj_list[next_]) == 1:
                        level.append(next_)
        return level
