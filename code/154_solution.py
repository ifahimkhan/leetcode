class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < nums[h]:
                h = mid 
            elif nums[mid] > nums[h]:
                l = mid + 1
            else:
                h -= 1
        return nums[l]        