class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for num in nums:
            if nums[abs(num) - 1] < 0: dups.append(abs(num))
            else: nums[abs(num) - 1] *= -1
        return dups
