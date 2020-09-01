class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        l = 0
        max_length = 1
        for r in range(1, len(nums)):
            if nums[r - 1] >= nums[r]: l = r
            max_length = max(max_length, r - l + 1)
        return max_length
        
