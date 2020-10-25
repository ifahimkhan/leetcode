class Solution:
    def solution_top_down(self, n):
        @lru_cache(None)
        def dfs(i):
            if i == 0: return False
            for k in range(1, int(i**.5) + 1):
                if not dfs(i - k**2): return True
            return False

        return dfs(n)
            
    def solution_bottom_up(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k**2] for k in range(1, int(i**.5) + 1))
        return dp[-1]
    
    winnerSquareGame = solution_top_down # solution_bottom_up
