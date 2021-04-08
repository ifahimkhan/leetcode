class Solution:
    def solution_2d_bottm_up(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # dp[l][r] is longest palindrom sub seq of s[l:r+1)
        for r in range(n):
            dp[r][r] = 1
            for l in range(r-1, -1, -1):
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l+1][r-1]
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        return dp[0][~0]

    def solution_1d_bottm_up(self, s: str) -> int:
        # compress to use two alternating rows
        n = len(s)
        prev = [0] * n
        for r in range(n):
            curr = [0] * n
            curr[r] = 1
            for l in range(r-1, -1, -1):
                if s[l] == s[r]:
                    curr[l] = 2 + prev[l+1]
                else:
                    curr[l] = max(curr[l+1], prev[l])
            prev = curr
        return curr[0]
        
        
    longestPalindromeSubseq = solution_1d_bottm_up # solution_2d_bottm_up
