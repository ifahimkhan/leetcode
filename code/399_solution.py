class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        edges = defaultdict(defaultdict)
        for (num, denum), value in zip(equations, values):
            edges[num][denum] = value
            edges[denum][num] = 1 / value

        for num in edges.keys(): edges[num][num] = 1
        
        def dfs(current, target, used):
            if current not in edges: return -1
            if target in edges[current]: return edges[current][target]
            
            used.add(current)
            for next_ in filter(lambda x: x not in used, edges[current]):
                result = dfs(next_, target, used)
                if result != -1: 
                    edges[current][target] = edges[current][next_] * result
                    return edges[current][target]
            return -1
        
        return [dfs(*query, set()) for query in queries]
