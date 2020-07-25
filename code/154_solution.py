class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log(N)) when there is no duplicate, O(N) worst case, when we just have a single number repeating
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]: l = m + 1
            elif nums[m] < nums[h]: h = m
            else: h -= 1
        return nums[l] # nums[h]