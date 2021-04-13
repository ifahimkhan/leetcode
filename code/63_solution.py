class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        target = (m-1, n-1)
        
        dp = [0] * n
        dp[0] = int(grid[0][0] == 0)
        for c in range(1, n):
            dp[c] = int(dp[c-1] == 1 and grid[0][c] == 0)
        
        for r in range(1, m):
            dp[0] = int(dp[0] == 1 and grid[r][0] == 0)
            for c in range(1, n):
                dp[c] = dp[c] + dp[c-1] if grid[r][c] == 0 else 0
        return dp[-1]
