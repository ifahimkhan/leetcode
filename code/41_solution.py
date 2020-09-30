class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # partition, move positive numbers before non-positive numbers
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] <= 0: 
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else: 
                l += 1
        
        # edge case - no number or no postive number at all
        if not nums or (r == 0 and nums[0] <= 0): return 1 
        
        # make sure r points to last postive number. 
        if nums[r] <= 0: r -= 1 
        
        # if there is no missing positive number nums[0, ... , r] should be 1 to r + 1 (shuffled)
        
        # 2nd pass: mark existing postive numbers that are <= num_max
        num_max = r + 1
        for i in range(r + 1):
            num = abs(nums[i])
            if num > num_max: continue
            nums[num - 1] = -abs(nums[num - 1])
        
        # 3rd pass: find the first missing positive number
        for i in range(r + 1):
            if nums[i] >= 0: 
                return i + 1
        
        return num_max + 1 
