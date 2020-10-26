class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:       
        dp = [[0] * i for i in range(1, 102)]
        dp[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                overflow = dp[r][c] - 1
                if overflow <= 0: continue
                dp[r + 1][c] += overflow / 2
                dp[r + 1][c + 1] += overflow / 2
        return min(dp[query_row][query_glass], 1)
        
