class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        total_steps = 1 # 1->0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1: sr, sc = r, c
                if grid[r][c] == 2: er, ec = r, c
                if grid[r][c] == 0: total_steps += 1
                
        self.num_ways = 0
        def backtrack(r, c, num_steps):
            if (r, c) == (er, ec):
                if num_steps == total_steps:  
                    self.num_ways += 1
                    return 
            else:
                original = grid[r][c]
                grid[r][c] = 3
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < nrow and 0 <= nc < ncol): continue
                    if grid[nr][nc] in [-1, 1, 3]: continue
                    backtrack(nr, nc, num_steps + 1)
                grid[r][c] = original
                
        backtrack(sr, sc, 0)
        return self.num_ways
        
            
