class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        accum, count, l = 1, 0, 0
        for r, num in enumerate(nums):
            accum *= num
            while l <= r and accum >= k:
                accum /= nums[l]
                l += 1
            count += r - l + 1
        return count
        
