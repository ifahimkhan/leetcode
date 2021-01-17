class Solution:
    def solution_dp(self, n: int) -> int:
        dp = [1] * 5
        for i in range(n): 
            for j in range(1, 5):
                dp[j] += dp[j - 1]
        return dp[-1]

    def solution_combination(self, n):
        # n + 4 choose 4
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // (4 * 3 * 2 * 1)
    
    countVowelStrings = solution_combination # solution_dp
