class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        curr_min = curr_max = max_prod = nums[0]
        for i, num in enumerate(nums[1:], 1):
            if num < 0: curr_min, curr_max = curr_max, curr_min
            curr_max = max(curr_max * num, num)
            curr_min = min(curr_min * num, num)
            max_prod = max(max_prod, curr_max)
        return max_prod
