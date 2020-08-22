class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        nrow, ncol = len(grid), len(grid[0])
        
        def bfs_cycle(sr, sc):
            symbol = grid[sr][sc]
            queue, neighbors = deque([(sr, sc)]), set()
            
            while queue:
                next_level = set()
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    grid[r][c] = '-1'
                    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                        if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] == symbol:
                            if (nr, nc) in next_level: return True
                            next_level.add((nr, nc))
                queue = deque(next_level)
            return False
                
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == '-1': continue
                if bfs_cycle(r, c): return True
        return False