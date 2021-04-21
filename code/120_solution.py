class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nrow = len(triangle)
        
        dp = triangle[0]
        for r in range(1, nrow):
            row = triangle[r]
            n_dp = []
            for c in range(r + 1):
                if c == 0: 
                    n_dp.append(dp[0] + row[0])
                elif c == r: 
                    n_dp.append(dp[~0] + row[~0])
                else:
                    n_dp.append(min(dp[c-1], dp[c]) + row[c])
            dp = n_dp
        return min(dp)
