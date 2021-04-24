class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_lists = defaultdict(list)
        for n1, n2 in connections:
            adj_lists[n1].append(n2)
            adj_lists[n2].append(n1)
        
        seen = set()
        low, high = [-1] * n, [-1] * n
        bridges = []
        
        def dfs(node, parent=None, label=0):
            seen.add(node)
            low[node] = high[node] = label
            
            for child in adj_lists[node]:
                if child == parent: continue
                
                if child in seen: 
                    high[node] = min(high[node], low[child])
                else:
                    dfs(child, node, label + 1)
                    high[node] = min(high[node], high[child])
                    
                if high[child] > low[node]: bridges.append((node, child))

        for i in range(n):
            if i in seen: continue
            dfs(i)
                
        return bridges
            
