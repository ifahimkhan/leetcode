# # f(i) the max (size) subset with nums[i] be the largest number in set
# # f(i) = max(f(j) for j in 0 .. i-1 if nums[i] % nums[j]) + 1

# 1D dp with back track, O(N^2) time O(N) space
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        dp = [0] * len(nums)
        
        max_i, max_l = 0, 0
        for i in range(len(nums)):
            dp[i] = max(dp[j] for j in range(i+1) if nums[i] % nums[j] == 0) + 1   
            if dp[i] > max_l: max_i, max_l = i, dp[i]
                
        subset = []
        l = max_l
        for i in range(max_i, -1, -1):
            if dp[i] == l and nums[max_i] % nums[i] == 0:
                subset.append(nums[i])
                max_i = i
                l -= 1
        return subset
        
