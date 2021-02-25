class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        if len(nums) == 2: return 0 if nums[0] <= nums[1] else 2
        
        n = len(nums)
        l, r = 0, n - 1
        while l < n-1 and nums[l] <= nums[l+1]: l += 1
        while r > 0   and nums[r] >= nums[r-1]: r -= 1
            
        if l == n - 1 and r == 0: return 0
        s_min, s_max = min(nums[l:r+1]), max(nums[l:r+1])

        while l > 0   and s_min < nums[l-1]: l -= 1
        while r < n-1 and s_max > nums[r+1]: r += 1
        return r - l + 1
