class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # time ~O(2^N*N) # space ~O(N)
        N = len(graph)
        paths = []
        
        def backtrack(candidate):
            if candidate[-1] == N - 1: return paths.append(candidate.copy())
            
            for choice in graph[candidate[-1]]:
                candidate.append(choice)
                backtrack(candidate)
                candidate.pop()
        
        backtrack([0])
        return paths
