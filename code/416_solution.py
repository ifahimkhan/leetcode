class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2: return False
        s //= 2
        n = len(nums)
        dp = [[True] + [False] * s for _ in range(n)]
        if nums[0] <= s: dp[0][nums[0]] = True

        for i, num in enumerate(nums[1:], 1):
            for j in range(1, s + 1):
                if dp[i - 1][j]: 
                    dp[i][j] = True
                elif j >= num: 
                    dp[i][j] = dp[i - 1][j - num]
        return dp[-1][-1]

                                
