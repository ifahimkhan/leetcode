class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        dp = [[0] * n for _ in range(n)]
        for l in range(n - 2, -1, -1):
            for r in range(l + 2, n):
                dp[l][r] = max(nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r] 
                               for i in range(l + 1, r))
        return dp[0][-1]
        
