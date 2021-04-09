# already in adj-matrix form, apply dfs/bfs is more convinent than union find. 

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)        
        visited = set()
        
        def dfs(src):
            stack = [src]
            while stack:
                src = stack.pop()
                if src in visited: continue
                visited.add(src)
                stack.extend([i for i, c in enumerate(isConnected[src]) if i != src and c == 1])
        
        num_provinces = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                num_provinces += 1
        
        return num_provinces
        
