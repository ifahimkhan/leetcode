class Solution:
    def solution_1(self, nums: List[int], x: int) -> int:
        accum_r, prefix_sum_r = 0, dict()            
        for i, num in enumerate(reversed(nums)):
            prefix_sum_r[accum_r] = i
            accum_r += num
            if accum_r > x: break
            
        min_steps = 2 ** 32
        
        accum_l = 0
        for i, num in enumerate(nums):
            if (x - accum_l) in prefix_sum_r and i + prefix_sum_r[x - accum_l] <= len(nums): 
                min_steps = min(min_steps, i + prefix_sum_r[x - accum_l])
            accum_l += num
        
        return min_steps if min_steps != 2 ** 32 else -1
        
    def solution_2(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        l = 0 
        accum = 0
        max_size = -1
        for r, num in enumerate(nums):
            accum += num
            while l < n and accum > target:
                accum -= nums[l]
                l += 1
            if accum == target:
                max_size = max(max_size, r - l + 1)
        return -1 if max_size == -1 else n - max_size
    
    minOperations = solution_2 # solution_1
