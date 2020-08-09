class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        queue = deque()
        count_1, flipped  = 0, 0
        
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 2: queue.append((r,c))
                if grid[r][c] == 1: count_1 += 1

        if not count_1: return 0

        t = -1                    
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        flipped += 1
                        queue.append((nr, nc))
            t += 1
        
        return t if flipped == count_1 else -1
                
            
        