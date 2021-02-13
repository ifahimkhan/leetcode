class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        
        n = len(grid)
        queue = deque([[0, 0, 1]])
        visited = set()
        while queue:
            r, c, l = queue.popleft()
            if (r, c) in visited: continue
            if (r, c) == (n-1, n-1): return l
            visited.add((r, c))
            
            for rr, cc in [(r-1, c), (r-1, c-1), (r, c-1), (r+1, c-1), (r+1, c), (r+1, c+1), (r, c+1), (r-1, c+1)]:
                if 0 <= rr < n and 0 <= cc < n and grid[rr][cc] == 0:
                    queue.append((rr, cc, l + 1))
        return -1
