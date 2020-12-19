class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        dp = defaultdict(lambda: -1)
        dp[(0,0,ncol-1)] = grid[0][0] + grid[0][ncol-1]
        max_val = grid[0][0] + grid[0][ncol-1]
        for r in range(1, len(grid)):
            for i in range(ncol):
                for j in range(ncol):
                    options = [
                        dp[(r-1, i-1, j-1)],
                        dp[(r-1, i-1, j)],
                        dp[(r-1, i-1, j+1)],
                        dp[(r-1, i, j-1)],
                        dp[(r-1, i, j)],
                        dp[(r-1, i, j+1)],
                        dp[(r-1, i+1, j-1)],
                        dp[(r-1, i+1, j)],
                        dp[(r-1, i+1, j+1)]
                    ]
                
                    max_option = max(options)
                    if max_option == -1: 
                        dp[(r, i, j)] = -1
                    else: 
                        if i != j:
                            dp[(r, i, j)] = max_option + grid[r][i] + grid[r][j] 
                        else:
                            dp[(r, i, j)] = max_option + grid[r][i]
                    max_val = max(max_val, dp[(r, i, j)])
        return max_val
