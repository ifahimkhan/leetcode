class Solution:
    def solution_dp(self, nums):
        n = len(nums)
        if n <= 1: return n
        
        dp = [[0, 1] for _ in range(n)] # length, count
        
        for r in range(n):
            for l in range(r):
                if nums[l] >= nums[r]: continue
                if dp[l][0] >= dp[r][0]: 
                    dp[r] = [1 + dp[l][0], dp[l][1]]
                elif dp[l][0] + 1 == dp[r][0]: 
                    dp[r][1] += dp[l][1]
        max_length = max(t[0] for t in dp)
        return sum(t[1] for t in dp if t[0] == max_length)
    
    findNumberOfLIS = solution_dp
